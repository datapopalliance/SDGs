# Built under Python 2.7.10 .

import io
import csv
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


SDG = {}


# Read goals from csv file
with io.open('../SDG-goals.csv', 'r', encoding='cp1252') as csvfile:          # encoding:  use cp1252 if the data comes from Excel
	reader = csv.reader(csvfile)
	headers = reader.next() # Skip header row
	for row in reader:
		this_entry = {
			"type"      : "goal",
			"number"   : row[headers.index('goal')],
			"description" : row[headers.index('description')]
		}
		this_entry["slug"]  = "goal_"+this_entry["number"].replace(".","_").replace(' ','')
		this_entry["parent"] = ""
		this_entry["children"] = []
		SDG[ this_entry["slug"] ] = this_entry


# Read targets from csv file
with io.open('../SDG-targets.csv', 'r', encoding='cp1252') as csvfile:          # encoding:  use cp1252 if the data comes from Excel
	reader = csv.reader(csvfile)
	headers = reader.next() # Skip header row
	for row in reader:
		this_entry = {
			"type" : "target",
			"number"      : row[headers.index('target')],
			"description" : row[headers.index('description')]
		}
		this_entry["slug"]  = "target_"+this_entry["number"].replace(".","_").replace(' ','')
		this_entry["parent"] = "goal_"+row[headers.index('goal')].replace(".","_").replace(' ','')
		this_entry["children"] = []
		SDG[ this_entry["slug"] ] = this_entry


# Read indicators from csv file
with io.open('../SDG-indicators_proposed-2016-03-24.csv', 'r', encoding='cp1252') as csvfile:          # encoding:  use cp1252 if the data comes from Excel
	reader = csv.reader(csvfile)
	headers = reader.next() # Skip header row
	num  = headers.index('Indicator')
	desc = headers.index('Description')
	for row in reader:
		this_entry = {
			"type" : "indicator",
			"number" : row[headers.index('Indicator')],
			"description" : row[headers.index('Description')]
		}
		this_entry["slug"]  = "indicator_"+this_entry["number"].replace(".","_").replace(' ','')
		this_entry["parent"] = "target_"+row[headers.index('Target')].replace(".","_").replace(' ','')
		this_entry["children"] = []
		SDG[ this_entry["slug"] ] = this_entry

# Add children
slugs = sorted(SDG)
for i in slugs:
	for j in slugs:
		if SDG[i]["slug"]==SDG[j]["parent"]:
			SDG[i]["children"].append(SDG[j]["slug"])

# Create a flat representation of the SDGs
SDG_flat = SDG

# Output the data as JSON files
with open('SDG-flat.json', 'w') as f:
	f.write( json.dumps(SDG_flat, indent=4, encoding='utf-8',sort_keys=True) )
	f.close()

# Create a hierarchical representation of the SDGs
SDG_hierarchical = {}
slugs = sorted(SDG)
for i in slugs:
	if SDG[i]["type"]=="goal":
		SDG_hierarchical[i] = SDG[i]

for i in sorted(SDG_hierarchical):
	SDG_hierarchical[i]["targets"] = {}
	for j in SDG_hierarchical[i]["children"]:
		SDG_hierarchical[i]["targets"][j] = SDG[j]
		SDG_hierarchical[i]["targets"][j]["indicators"] = {}
		for k in SDG_hierarchical[i]["targets"][j]["children"]:
			SDG_hierarchical[i]["targets"][j]["indicators"][k] = SDG[k]

# Output the data as JSON files
with open('SDG-hierarchical.json', 'w') as f:
	f.write( json.dumps(SDG_hierarchical, indent=4, encoding='utf-8',sort_keys=True) )
	f.close()



