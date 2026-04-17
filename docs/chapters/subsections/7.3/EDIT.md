### EDIT -- Define the Start of the EDIT Section of Keywords

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The EDIT activation keyword marks the end of the GRID section and the start of the EDIT section that enables modifications to the OPM Flow calculated properties derived from the data entered in the GRID section, for example grid block pore volumes via the PORV array and the transmissibilities via the TRANX, TRANY and TRANZ family of keywords.

There is no data required for this keyword.

#### Example

\-- ==============================================================================

\--

\-- EDIT SECTION

\--

\-- ==============================================================================

EDIT

The above example marks the end of the GRID section and the start of the EDIT section in the OPM Flow data input file.
