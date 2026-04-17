### GSEPCOND -- Assign Group Separators

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The GSEPCOND keyword assigns previously defined separators to a group. Group separators are specified by the SEPVALS keyword in the SCHEDULE section. The facility is used in black-oil modeling to re-scale the PVT data entered via the PROPS section, based on the saturation point oil formation volume factor (Bob) and the initial saturated gas-oil ratio (Rsi) entered on the SEVPALS keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
