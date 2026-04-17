### DRVDTR -- Vaporized Oil (Rv) Maximum Rate of Increase Parameters by Region

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

DRVDTR defines the maximum rate at which the vaporized oil-gas ratio or condensate-gas ratio (Rv) can be increased in a grid cell for various regions in the model. The keyword is similar in functionality to the DRVDT keyword, that defines the maximum rate at which Rv can be increased in a grid cell for all cells in the model. The number of DRVDTR vector data sets is defined by the NTPVT parameter on the TABDIMS keyword in the RUNSPEC section and the allocation of the DRVDTR records to different grid blocks in the model is done via the PVTNUM keyword in the REGION section. One data set consists of one record or line which is terminated by a "/".

This keyword should only be used if the OIL, GAS, and VAPOIL (condensate) keywords in the RUNSPEC section have been invoked to allow oil, gas and condensate to be present in the model. The keyword only affects the behavior of an increasing Rv, for example when gas is being injected into a gas condensate reservoir as part of as gas re-cycling scheme, and is subject to the availability of free oil (condensate) and the ability of the undersaturated gas to adsorb this condensate.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | DRVDT1 | DRVDT1 is a real positive number that defines the maximum rate at which the vaporized oil-gas ratio is allowed to increase in a grid cell, that is the maximum rate at which the oil can vaporize into the available undersaturated gas.<br>A value of zero means that Rv cannot increase and free oil cannot vaporize into the unsaturated gas in a grid cell. Alternatively a very large value of DRVDT1 allows Rv to increase rapidly until there is no free oil or the gas within the grid block is fully saturated.<br>Note if the keyword is not present in the input deck then DRVDT1 is assumed to be a very large number resulting in complete re-vaporization of the oil into the available undersaturated gas. | None |
| stb/Mscf/d | sm^3^/sm^3^/day | scc/scc/day |  |
| Notes:<br>1)  The keyword is followed by NTPVT records as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each record is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 12.24: DRVDTR Keyword Description

Note this keyword can be used in history matching field performance to control the availability of the movable gas phase.

See also the VAPPARS keyword in the SOLUTION section and DRVDT, DRSDT, and DRSDTR keywords in the SCHEDULE section that controls how dissolved gas is treated and the rate at which the vaporized phase ratio increases within a grid block.

#### Examples

The first example prevents the vaporized oil-gas ratio from increasing and applies this to all regions for when NTPVT on the TABDIMS keyword in the RUNSPEC section is set to three.

\--

\-- VAPORIZED OIL (RV) MAXIMUM RATE OF INCREASE PARAMETERS BY REGION

\--

DRVDTR

\-- MAX RV

\-- DRVDT1

\-- \-\-\-\-\-\--  -

0.000 /

0.000 /

0.000 /

The second example below prevents the vaporized oil-gas ratio from increasing and applies this to all grid cells in PVTNUM region one. For PVTNUM regions one and two the keyword applies 0.005 stb//Mscf/d as the maximum rate at which the vaporized oil-gas ratio is allowed to increase in a grid cell,

\--

\-- VAPORIZED OIL (RV) MAXIMUM RATE OF INCREASE PARAMETERS BY REGION

\--

DRVDTR

\-- MAX RV

\-- DRVDT1

\-- \-\-\-\-\-\--

0.0000 /

0.0005 /

0.0005 /

Again, the keyword parameters when applied are subject to the availability of free oil and the ability of the undersaturated gas to adsorb this oil.
