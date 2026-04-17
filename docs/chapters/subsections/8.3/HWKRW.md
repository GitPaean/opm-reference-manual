### HWKRW -- End-Point Scaling of Grid Cell Krw(Sw =1.0) (High Salinity and Water Wet)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

HWKRW defines the scaling parameter at the maximum oil relative permeability value (SWU), that is for Sw = 1.0, for all the cells in the model via an array, for when the Low Salt and Surfactant Wettability options have been selected. The data is used to scale the water relative permeability in the high salinity water wet water relative permeability saturation tables. The ENDSCALE keyword in the RUNSPEC section should be activated to enable end-point scaling and the use of this keyword. In addition the Low Salt option should be activated by the LOWSALT keyword in the RUNSPEC section and the Surfactant Wettability option activated by the SURFACT or SURFACTW keywords, which are also in the RUNSPEC section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
