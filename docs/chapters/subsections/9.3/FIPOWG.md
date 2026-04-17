### FIPOWG -- Activate Oil, Gas, and Water FIP Zone Reporting

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The FIPOWG keyword activates automatic fluid in-place reporting based on the initial oil, gas and water zones defined by the initial equilibration. The fluid contacts on the EQUIL keyword in the SOLUTION section determine the reporting fluid category a grid cell belongs to. For example all grid cells with depths above the gas-oil contact on the EQUIL keyword will be assigned to the gas zone and reported accordingly. Similarly, grid cells with depths between the gas-oil contact and the water-oil contact will be assigned to the oil zone. And finally, grid cells with depths below the oil-water contact will be assigned to the water zone. The simulator can print out summaries of the fluid in-place in each region, the current flow rates between regions, and the cumulative flows between regions.

Note that the total number of FIP and FIPNUM regions must be defined by the NMFIPR variable on the REGDIMS keyword in the RUNSPEC section.

There is no data required for this keyword.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

#### Example

\--

\-- ACTIVATE OIL, GAS, AND WATER FIP ZONE REPORTING

\--

FIPOWG

The above example switches on automatic fluid in-place reporting based on the initial oil, gas and water zones defined by the initial equilibration.
