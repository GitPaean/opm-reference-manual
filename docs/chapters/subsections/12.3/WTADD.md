### WTADD -- Add a Constant to a Well Target or Constraint

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, WTADD, adds a constant to a previously define well's target or constraint, as stated on the WCONPROD, WCONINJE, or WELTARG keywords, but not for the history matching wells using the WCONHIST or WCONINJH keywords. All the aforementioned keywords are in the SCHEDULE section. The constant can be positive or negative.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
