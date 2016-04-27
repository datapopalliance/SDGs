# Summary of key files in this repository

- **[Goals, Target, and Indicators.xlsx](Goals, Target, and Indicators.xlsx):**  An Excel spreadsheets which contains codes and descriptions for each goal, target, and indicators of the SDGs (on separate tabs).
- **[SDG-goals.csv](SDG-goals.csv):**  A CSV file of the goals (code and description).
- **[SDG-targets.csv](SDG-targets.csv):**  A CSV file of the targets (code and description).
- **[SDG-indicators_proposed-2016-03-24.csv](SDG-indicators_proposed-2016-03-24.csv):** A CSV file of the proposed indicators, as described below.
- **[json versions](json versions)**: A folder containing a python script that reads in the information from the above CSV files, and outputs it to various json files. The script and its output files are described [here](json versions/README.md).

*Please feel free to report any errors in the [issues](https://github.com/datapopalliance/SDGs/issues) section or by emailing [research@datapopalliance.org](mailto:research@datapopalliance.org).*

# Goals and Targets

**Source:** Extracted from the Sustainable Development Goals website on March 22, 2016: https://sustainabledevelopment.un.org/?menu=1300

# Provisional Proposed Tiers for Global SDG Indicators as of March 24, 2016

**Source:** [**Provisional-Proposed-Tiers-for-SDG-Indicators-24-03-16.pdf**](http://unstats.un.org/sdgs/files/meetings/iaeg-sdgs-meeting-03/Provisional-Proposed-Tiers-for-SDG-Indicators-24-03-16.pdf), available in the `Documents` section of the summary page of the [Third meeting of the IAEG-SDGs](http://unstats.un.org/sdgs/meetings/iaeg-sdgs-meeting-03).

## Important information from the source document

This file contains a proposed classification of the SDG indicators into three tiers based on their level of methodological development and data availability. The Secretariat, in consultation with the IAEG-SDG Co-Chairs, invited international agencies, entities and organisations to submit responses to an online questionnaire that requested information on the state of methodological development of the indicator, whether an international standard exists, and data availability for the indicator.

During this consultation, more than 380 individual responses were received from these organisations (each individual response to a specific indicator is counted as one response, so a single agency could submit multiple responses), and these agencies also were asked to provisionally categorise the indicators into one of the following three tiers:

- **Tier 1:** Indicator conceptually clear, established methodology and standards available and data regularly produced by countries.
- **Tier 2:** Indicator conceptually clear, established methodology and standards available but data are not regularly produced by countries.
- **Tier 3:** Indicator for which there are no established methodology and standards or methodology/standards are being developed/tested.

The Secretariat reviewed and compiled. It also reviewed the proposed tier assignments across the different targets and goals and, in some cases, proposed a different tier for an indicator. This document contains the agency’s tier classification, a proposed tier by the Secretariat, a possible custodian agency or agencies (who would be responsible for compiling the data at the global level and for global reporting), other involved agencies, and a column that provides a summary of the detailed information provided by these agencies.

***This file is very preliminary in nature.*** It will be updated and revised as additional and new information is received from both agencies and countries. This file is intended as a discussion document for the 3rd IAEG-SDG meeting. It is planned that the discussion at the meeting will focus predominately on those indicators classified as Tier III. 

Possible custodian agencies, other interested agencies and the tier classification itself may be changed moving forward, based on discussions at the 3rd meeting of the IAEG-SDG and in the future.

## Additional variables

In the [`SDG-indicators_proposed-2016-03-24.csv`](SDG-indicators_proposed-2016-03-24.csv) file:

`tier_proposed` and `tier_revised` provide the proposed and revised tiers for each indicator. The values from from the `Proposed Tier by Agency` and `Revised Tier (by Secretariat)` columns of the source PDF file, respectively.

The contain the values `Tier I`, `Tier II`, `Tier III`, or `-` (when blank). In some cases, additional, multiple tiers are proposed, and/or comments are provided to explain the rational of the revised tier.

`tier_proposed_coded` and `tier_revised_coded` provide a numerical version of the values in `tier_proposed_coded` and `tier_revised_coded`, respectively.

They contain the tier `1`, `2`, or `3`; or `blank` if no tier was given in the source file; or `multiple` if more than one tier was given.

