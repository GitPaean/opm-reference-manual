### RCMASTS -- Reservoir Coupling Group Minimum Time Step for Flow Restriction

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

RCMASTS is used when reservoir coupling is invoked by the GRUPMAST and SLAVES keywords in the SCHEDULE section. The keyword should be placed within the master file and it sets the minimum time step size for groups for when a group is being restricted by a group's limiting flow rate fractional change (see the GRUPMAST keyword in the SCHEDULE section).

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
