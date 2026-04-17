### HA -- History Match End-Point Gradient Additive Modifier

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The HA series of keywords defines the history match end-point gradient parameters used to set the additive cumulative end point data, for when the History Match Gradient option has been activated by the HMDIMS keyword in the RUNSPEC section. In addition, the End-Point Scaling option must also be activated by the ENDSCALE keyword which is also in the RUNSPEC section. The keyword consists of the first two characters of "HA" followed by the end-point keyword shown in , for example, HASWL.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

| Saturation | SWL | Connate water saturation, that is the smallest water saturation in a water saturation function table. |
| --- | --- | --- |
| SWCR | Critical water saturation, that is the largest water saturation for which the water relative permeability is zero. |  |
| SOWCR | Critical oil-in-water saturation, that is the largest oil saturation for which the oil relative permeability is zero in an oil-water system. |  |
| Relative<br>Permeability | KRW | Relative permeability of water at the maximum water saturation (normally the maximum water saturation is one). |
| KRO | Relative permeability of oil at the maximum oil saturation. |  |
| KRWR | Relative permeability of water at the residual oil saturation or the residual gas saturation in a gas-water run. |  |
| KRORW | Relative permeability of oil at the critical water saturation. |  |
| Capillary<br>Pressure | SWLPC | Capillary pressure connate water saturation, that is the smallest water saturation in a water saturation function table. |
| Type | End-Point<br>Keyword | Gas-Oil End-Point Definitions |
| Saturation | SGL | Connate gas saturation, that is the smallest gas saturation in a gas saturation function table. |
| SGCR | Critical gas saturation, that is the largest gas saturation for which the gas relative permeability is zero. |  |
| SOGCR | Critical oil-in-gas saturation, that is the largest oil saturation for which the oil relative permeability is zero in an oil-gas-connate water system. |  |
| Relative<br>Permeability | KRG | Relative permeability of gas at the maximum gas saturation. |
| KRGR | Relative permeability of gas at the residual oil saturation or the critical water saturation in a gas-water run. |  |
| KRORG | Relative permeability of oil at the critical gas saturation. |  |
| Capillary<br>Pressure | SGLPC | Capillary pressure connate gas saturation, that is the smallest gas saturation in a gas saturation function table. |

Table 8.45: HA Keyword List

See also the HMPROPS keyword in the PROPS section that allows the use of the ADD, BOX, EQUALS, COPY, MINVALUE, and MAXVALUE keywords to be used with the HA and HM series of keywords.
