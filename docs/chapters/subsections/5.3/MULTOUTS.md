### MULTOUTS -- Activate Non-Unified Multiple Summary Output File Option

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword switches on the Multiple Output Files option for SUMMARY files only, and overwrites the UNIFOUT keyword in the RUNSPEC section that activates the Unified Output Files option for all output files.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

See also [OPM FLOW OUTPUT FILE FORMATS](#anchor-2) for a more detailed description of the various file types (ASCII or binary) and file structure formats (unified or non-unified formats).

#### Example

\--

\-- ACTIVATE MULTIPLE OUTPUT SUMMARY FILES ONLY OPTION

\--

MULTOUTS

The above example switches on the multiple output file option.
