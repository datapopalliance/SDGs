# Built under Python 2.7.10 .

import io
import csv
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# Create empty lists
goals = {}
targets = {}
indicators = {}


# Read goals from csv file
with io.open('../SDG-goals.csv', 'r', encoding='cp1252') as csvfile:          # encoding:  use cp1252 if the data comes from Excel
	reader = csv.reader(csvfile)
	headers = reader.next() # Skip header row
	for row in reader:
		this_entry = {
			"type"      : "goal",
			"goal" : {
				"number"   : row[headers.index('goal')],
				"description" : row[headers.index('description')]
			}
		}
		this_entry["goal"]["slug"]  = "goal_"+this_entry["goal"]["number"].replace(".","_").replace(' ','')
		this_entry["slug"]          = this_entry["goal"]["slug"]
		goals[ this_entry["slug"] ] = this_entry


# Read targets from csv file
with io.open('../SDG-targets.csv', 'r', encoding='cp1252') as csvfile:          # encoding:  use cp1252 if the data comes from Excel
	reader = csv.reader(csvfile)
	headers = reader.next() # Skip header row
	for row in reader:
		this_entry = {
			"type" : "target",
			"goal" : {
				"number"   : row[headers.index('goal')]
			},
			"target" : {
				"number"   : row[headers.index('target')],
				"description" : row[headers.index('description')]
			}
		}
		this_entry["goal"]["slug"]    = "goal_"  +this_entry["goal"]["number"].replace(".","_").replace(' ','')
		this_entry["target"]["slug"]  = "target_"+this_entry["target"]["number"].replace(".","_").replace(' ','')
		this_entry["slug"]            = this_entry["target"]["slug"]
		targets[ this_entry["slug"] ] = this_entry


# Read indicators from csv file
with io.open('../SDG-indicators_proposed-2016-03-24.csv', 'r', encoding='cp1252') as csvfile:          # encoding:  use cp1252 if the data comes from Excel
	reader = csv.reader(csvfile)
	headers = reader.next() # Skip header row
	num  = headers.index('Indicator')
	desc = headers.index('Description')
	for row in reader:
		this_entry = {
			"type"           : "indicator",
			"goal" : {
				"number"   : row[headers.index('Goal')]
			},
			"target" : {
				"number"   : row[headers.index('Target')]
			},
			"indicator" : {
				"number"   : row[headers.index('Indicator')],
				"description"   : row[headers.index('Description')],
			}
		}
		this_entry["goal"]["slug"]       = "goal_"     +this_entry["goal"]["number"].replace(".","_").replace(' ','')
		this_entry["target"]["slug"]     = "target_"   +this_entry["target"]["number"].replace(".","_").replace(' ','')
		this_entry["indicator"]["slug"]  = "indicator_"+this_entry["indicator"]["number"].replace(".","_").replace(' ','')
		this_entry["slug"]               = this_entry["indicator"]["slug"]
		indicators[ this_entry["slug"] ] = this_entry


# Complete description information
for slug in targets:
	goal_k = targets[slug]["goal"]["slug"]
	goal_v = goals[goal_k]["goal"]["description"]
	targets[slug]["goal"]["description"] = goal_v

for slug in indicators:
	goal_k = indicators[slug]["goal"]["slug"]
	goal_v = goals[goal_k]["goal"]["description"]
	indicators[slug]["goal"]["description"] = goal_v
	target_k = indicators[slug]["target"]["slug"]
	target_v = targets[target_k]["target"]["description"]
	indicators[slug]["target"]["description"] = target_v

# Combine the lists into a dictionary
SDG_dict = {}

for slug in goals:
	n = goals[slug]["slug"]#.replace("goal_","")
	SDG_dict[n] = goals[slug]

for slug in targets:
	n = targets[slug]["slug"]#.replace("target_","")
	SDG_dict[n] = targets[slug]

for slug in indicators:
	n = indicators[slug]["slug"]#.replace("indicator_","")
	SDG_dict[n] = indicators[slug]

SDG_list = {}
SDG_list["goals"] = goals
SDG_list["targets"] = targets
SDG_list["indicators"] = indicators


# Output the data as JSON files
with open('SDG-dict.json', 'w') as f:
	f.write( json.dumps(SDG_dict, indent=4, encoding='utf-8',sort_keys=True) )
	f.close()

# Output the data as JSON files
with open('SDG-list.json', 'w') as f:
	f.write( json.dumps(SDG_list, indent=4, encoding='utf-8',sort_keys=True) )
	f.close()