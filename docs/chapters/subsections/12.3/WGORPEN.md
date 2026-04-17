### WGORPEN -- Define Well GOR Penalty Parameters

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WGORPEN keyword defines a well's Gas-Oil Ratio ("GOR") penalty parameters used to calculate a well's oil production target for the current month, as a function of the well's previous month's average GOR. The WGORPEN calculated oil rate overwrites any oil targets set by the WCONPROD and WELTARG keywords in the SCHEDULE section. In North American, it is common practice for the regulator to enforce GOR penalties, in order to control gas production in depletion drive oil reservoirs, with the stated intention to maximize oil recovery by limiting the energy loss from the reservoir by excessive gas production.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
