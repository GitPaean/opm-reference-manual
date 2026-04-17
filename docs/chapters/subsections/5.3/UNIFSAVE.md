### UNIFSAVE -- Activate The Unified Output Save File Option

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The UNIFSAVE keyword causes the SAVE file output file to be a unified file, as opposed to non-unified multiple files. A unified file is a single file containing output for each reporting time step. Here a single SAVE file will be generated, as opposed to one file per report time step. See also the MULTOUT keyword in the RUNSPEC section that sets both the SUMMARY and RESTART files to be non-unified multiple files, as opposed to unified files.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

#### Example

\--

\-- ACTIVATE THE UNIFIED OUTPUT SAVE FILE OPTION

\--

UNIFSAVE

The above example switches on writing of unified SAVE output files.
