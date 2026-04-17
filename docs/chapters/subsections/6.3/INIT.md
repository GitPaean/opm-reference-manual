### INIT -- Activate the INIT File Option

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword switches on the writing of the INIT file that contains the static data specified in the GRID, PROPS and REGIONS sections. For example, the PORO, PERM and NTG arrays from the GRID section. The data is used in post-processing software, for example OPM ResInsight, to visualize the static grid properties.

The INIT file can either be written out in formatted form as ASCII i.e. text files, if the FMTOUT keyword has been activated, or binary format if the FMTOUT keyword has not been activated. Normally, this option is always activated by the user and when activated the binary form of the file is used.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- ACTIVATE WRITING THE INIT FILE FOR POST-PROCESSING

INIT

The above example switches on the writing of the INIT file for post-processing in ResInsight.
