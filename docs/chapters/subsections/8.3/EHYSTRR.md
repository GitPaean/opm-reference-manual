### EHYSTRR -- Define Hysteresis Model and Parameters via SATNUM

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The EHYSTRR keyword defines the hysteresis model and associated parameters via the drainage SATNUM allocation region array, for when the hysteresis option has been activated by the HYSTER variable on the SATOPTS keyword in the RUNSPEC section. Only the Killough[^1] model is available for this keyword and the keyword is optional.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped. See also the EHYSTR keyword in the RUNSPEC for an alternative keyword to enter the hysteresis model and associated parameters that is supported by OPM Flow

| 1 | HYSTRCP | HYSTRCP is a positive real value that defines the Killough curvature parameter for capillary pressure hysteresis model.<br>The value should range from 0.05 to 0.10. | 0.1 |
| --- | --- | --- | --- |
| 2 | HYSTREL | HYSTREL is a positive real number that defines the Killough's wetting phase relative permeability curvature parameter. This parameter is ignored if HYSMOD on the EHYSTR keyword is not set to 4. | 1.0 |
| 3 | HYSTSGR | HYSTSGR is a positive real number that sets a scaling parameter for the trapped non-wetting phase saturation in the Killough model. | 0.1 |
| Notes:<br>1)  The keyword is followed by NTSFUN rows as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)   There is no "/" terminator for the keyword. |  |  |  |

Table 8.33: EHYSTRR Keyword Description

#### Example

\--

\-- HYSTERESIS MODEL AND PARAMETERS VIA SATNUM

\--

\-- PC-CUR RELPERM TRAPPED

\-- HYSTRCP HYSTREL HYSTSGR

EHYSTRR

0.04 1.0 1\* / SATNUM REGION 1

0.06 1.0 1\* / SATNUM REGION 2

0.08 1.0 1\* / SATNUM REGION 3

0.10 1.0 1\* / SATNUM REGION 4

0.10 1.0 1\* / SATNUM REGION 5

The above example defines the hysteresis model and parameters for when NTSFUN equals five on the TABDIMS keyword in the RUNSPEC section, that is for five SATNUM regions.

[^1]: Killough, J. E. "Reservoir Simulation with History-dependent Saturation Functions," paper SPE 5106, Society of Petroleum Engineers Journal (1976) 16, No. 1, 37-48.
