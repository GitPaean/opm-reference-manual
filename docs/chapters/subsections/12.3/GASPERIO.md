### GASPERIO -- Advance Simulation by Gas Contract Period

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword advances the simulation over one or more gas contract periods for when the Gas Field Operations option has been activated by the GASFIELD keyword in the RUNSPEC section. A contract period in this case is the period over which the Daily Contract Quantity is fixed, this can a be year or one or more months. If the contract period is a year then the GASYEAR keyword in the SCHEDULE section can be used instead of GASPERIOD.

GASPERIO is an alternative to the DATES, TIME and TSTEP keywords in the SCHEDULE section that advances the simulation to a given report time after which additional keywords may be entered to instruct OPM Flow to perform additional functions via the SCHEDULE section keywords.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
