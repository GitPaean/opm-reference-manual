### WSEGMULT -- Define Multi-Segment Well Frictional Pressure Loss Multipliers

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

WSEGMULT supplies a set of constants used to modify (or scale) a multi-segment well's segment frictional pressure drop between connecting segments The constants enable either a constant pressure to be applied, or for the pressure drop to vary as a function of the Gas-Oil Ratio ("GOR") or the Water-Oil Ratio ("WOR"). The simulator calculated pressure drop is multiplied by the following resulting value:

Where the constants x~1~ to x~5~ are defined by the values on this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
