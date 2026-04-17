### WLIMTOL -- Define Well Constraint Tolerance

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

WLIMTOL keyword defines the tolerance to be used for various constraints applied to connections, completions (if connections have been lumped via the COMPLUMP keyword in the SCHEDULE section), wells, and groups, including the field group. See also the GCONTOL keyword in the SCHEDULE section that sets the tolerance parameters for groups.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
