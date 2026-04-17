### HM -- History Match Region Gradient Parameters

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The HM series of keywords in the REGION section defines the history match gradient regions and sub-regions, for when the History Match Gradient option has been activated by the HMDIMS keyword in the RUNSPEC section.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

For grid properties, the region name (or region property array) is based on the property arrays defined in .

| PERMX | HMPERMX | Permeability multipliers in the x-direction. |
| --- | --- | --- |
| PERMXY | HMPRMXY | Permeability multipliers in the x-direction and y-direction |
| pERMY | HMPERMY | Permeability multipliers in the y-direction. |
| PERMZ | HMPERMZ | Permeability multipliers in the z-direction. |
| PORV | HMPORV | Pore volume multiplier |
| SIGMA | HMSIGMA | Dual porosity and/or dual permeability SIGMA multiplier |
| TRANX | HMTRANX | Transmissibility multipliers in the x-direction. |
| TRANXY | HMTRNXY | Transmissibility multipliers in the x-direction and y-direction |
| TRANY | HMTRANY | Transmissibility multipliers in the y-direction. |
| TRANZ | HMTRANZ | Transmissibility multipliers in the z-direction. |

Table 9.6: HM Region Grid Gradient Parameter Keyword List

In addition, if the End-Point Scaling option has been activated by the ENDSCALE keyword in the RUNSPEC section, then the history match gradient regions and sub-regions for the end-point data can be specified. In this the keyword consists of the first two characters of "HM" followed by the end-point keyword (), for example, HMSWL.

| Saturation | HMSWL | Connate water saturation, that is the smallest water saturation in a water saturation function table. |
| --- | --- | --- |
| HMSWCR | Critical water saturation, that is the largest water saturation for which the water relative permeability is zero. |  |
| HMSOWCR | Critical oil-in-water saturation, that is the largest oil saturation for which the oil relative permeability is zero in an oil-water system. |  |
| Relative<br>Permeability | HMKRW | Relative permeability of water at the maximum water saturation (normally the maximum water saturation is one). |
| HMKRO | Relative permeability of oil at the maximum oil saturation. |  |
| HMKRWR | Relative permeability of water at the residual oil saturation or the residual gas saturation in a gas-water run. |  |
| HMKRORW | Relative permeability of oil at the critical water saturation. |  |
| Capillary<br>Pressure | HMSWLPC | Capillary pressure connate water saturation, that is the smallest water saturation in a water saturation function table. |
| Type | End-Point<br>Keyword | Gas-Oil End-Point Definitions |
| Saturation | HMSGL | Connate gas saturation, that is the smallest gas saturation in a gas saturation function table. |
| HMSGCR | Critical gas saturation, that is the largest gas saturation for which the gas relative permeability is zero. |  |
| HMSOGCR | Critical oil-in-gas saturation, that is the largest oil saturation for which the oil relative permeability is zero in an oil-gas-connate water system. |  |
| Relative<br>Permeability | HMKRG | Relative permeability of gas at the maximum gas saturation. |
| HMKRGR | Relative permeability of gas at the residual oil saturation or the critical water saturation in a gas-water run. |  |
| HMKRORG | Relative permeability of oil at the critical gas saturation. |  |
| Capillary<br>Pressure | HMSGLPC | Capillary pressure connate gas saturation, that is the smallest gas saturation in a gas saturation function table. |

Table 9.7: HM Region End-Point Gradient Parameter Keyword List
