### STOW -- Define Capillary Pressure Oil-Water Surface Tension versus Pressure

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The STOW keyword defines capillary pressure oil-water surface tension versus pressure tables used in adjusting the pressure independent capillary pressure vectors in the SWFN or SWOF saturation tables, entered by their respective keywords in the PROPS section. The SATOPTS keyword in the RUNSPEC section should state the SURFTENS character string to activate the Capillary Pressure Surface Tension Pressure Dependency option. If the STOW keyword is not supplied then no capillary pressure surface tension pressure scaling will occur and the capillary pressure values on the SWFN or SWOF saturation tables will be used directly.

Capillary pressure surface tension pressure scaling can also be used with multi-segment wells, but this facility has not been incorporated in OPM Flow's multi-segment well implementation.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
