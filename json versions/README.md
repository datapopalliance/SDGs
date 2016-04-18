# Source

Please see the [main README](../README.md) file for information on source of the goals, targets, and indicators.

# Script

The [build.py] script was built under Python `2.7.10`. It reads in the lists of [goals](../SDG-goals.csv), [targets](../SDG-targets.csv), and [indicators](../SDG-indicators_proposed-2016-03-24.csv), and combines them into various structured JSON files.

# Output

## `SDG-flat.json`

Goals, targets, and indicators are all listed at the same level. Each has a slug (`string`) of the form `goal_1`, `target_1_1`, or `indicator_1_1_1`; and pointers to its parent (as a `string`) and children (as a `list` of `string`s).

## `SDG-hierchical.json`

The object contains a list of goals, each of which contains a list of targets, each of which contains a list of indicators.