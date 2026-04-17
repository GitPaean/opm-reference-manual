### SEPVALS -- Define Separator Oil Formation Volume Factor and GOR

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SEPVALS keyword defines the initial and subsequent separator oil formation volume factor (Bo) and Gas Oil Ratio ("GOR" or Rs). The facility is used in black-oil modeling to re-scale the PVT data entered via the PROPS section, based on the saturation point oil formation volume factor (Bob) and the initial saturated gas-oil ratio (Rsi) entered on the SEPVALS keyword. The first occurrence of this keyword sets the initial conditions and must be followed by the GSEPCOND keyword that assigns previously defined separators to a group.

Note that the keyword can only be used in runs with oil and dissolve gas only, with no vaporized oil (condensate) in the gas phase.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
