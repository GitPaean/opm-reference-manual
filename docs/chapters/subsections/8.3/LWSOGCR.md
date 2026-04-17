### LWSOGCR -- End-Point Scaling Grid Cell SOGCR (Low Salinity and Water Wet)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

LWSOGCR defines the critical oil saturation with respect to gas ("SOGCR"), for all the cells in the model via an array, for when the Low Salt and Surfactant Wettability options have been selected. The data is used to scale the oil saturation in the low salinity water wet oil-gas relative permeability saturation tables. The ENDSCALE keyword in the RUNSPEC section should be activated to enable end-point scaling and the use of this keyword. In addition, the Low Salt option should be activated by the LOWSALT keyword in the RUNSPEC section and the Surfactant Wettability option activated by the SURFACT or SURFACTW keywords, which are also in the RUNSPEC section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
