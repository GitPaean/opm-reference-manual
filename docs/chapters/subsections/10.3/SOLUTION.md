### SOLUTION -- Define the Start of the SOLUTION Section of Keywords

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SOLUTION activation keyword marks the end of the REGIONS section and the start of the SOLUTION section that defines the parameters used to initialize the model, by:

1)  defining fluid contacts and pressures, or

2)  defining pressures and fluid saturations for all cells in the model, or

3)  by restarting from a previously OPM Flow completed run.

There is no data required for this keyword.

#### Example

\-- ==============================================================================

\--

\-- SOLUTION SECTION

\--

\-- ==============================================================================

SOLUTION

The above example marks the end of the REGIONS section and the start of the SOLUTION section in the OPM Flow data input file.
