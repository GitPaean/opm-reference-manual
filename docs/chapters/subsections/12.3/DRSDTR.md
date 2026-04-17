### DRSDTR -- Solution Gas (Rs) Maximum Rate of Increase Parameters by Region

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

DRSDTR defines the maximum rate at which the solution gas-oil ratio (Rs) can be increased in a grid cell for various regions in the model. The keyword is similar in functionality to the DRSDT keyword, that defines the maximum rate at which Rs can be increased in a grid cell for all cells in the model. The number of DRSDTR vector data sets is defined by the NTPVT parameter on the TABDIMS keyword in the RUNSPEC section and the allocation of the DRSDTR records to different grid blocks in the model is done via the PVTNUM keyword in the REGION section. One data set consists of one record or line which is terminated by a "/".

DRSDTR should only be used if the OIL, GAS, and DISGAS keywords in the RUNSPEC section have been invoked to allow oil, gas and dissolved gas to be present in the model. The keyword only affects the behavior of an increasing Rs, for example when gas is being injected into an oil reservoir, and is subject to the availability of free gas and the ability of the undersaturated oil to adsorb this gas.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | DRSDT1 | DRSDT1 is a real positive number that defines the maximum rate at which the solution gas-oil ratio is allowed to increase in a grid cell, that is the maximum rate the gas can dissolve into the available undersaturated oil.<br>A value of zero means that Rs cannot increase and free gas cannot dissolve into the unsaturated oil in a grid cell. Alternatively a very large value of DRSDT1 allows Rs to increase rapidly until there is no free gas or the oil within the grid block is fully saturated.<br>Note if the keyword is not present in the input deck then DRSDT1 is assumed to be a very large number resulting in complete re-solution of the gas into the available undersaturated oil. | None |
| Mscf/stb/d | sm^3^/sm^3^/day | scc/scc/day |  |
| 2 | DRSDT2 | DRSDT2 is a defined character string that defines whether the DRSDT1 is applied to either all grid blocks or just those grid blocks containing free gas:<br>1)  ALL: means the DRSDT1 maximum rate at which Rs is allowed to increase in a grid cell is applied to all grid blocks.<br>2)  FREE: means the DRSDT1 maximum rate at which Rs is allowed to increase in a grid cell is applied to grid blocks only containing free gas.<br>Note if the keyword is not present in the input deck then DRSDT2 is set to the default value of ALL. | ALL |
| Notes:<br>1)  The keyword is followed by NTPVT records as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each record is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 12.22: DRSDTR Keyword Description

Note this keyword can be used in history matching field performance to control the availability of the movable gas phase.

See also the VAPPARS keyword in the SOLUTION section and the DRSDT, DRVDT and DRVDTR keywords in the SCHEDULE section that controls how vaporized oil is treated and the rate at which the dissolved phase ratio increases within a grid block.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored but is documented here for completeness, as it is expected to be available in the next release of OPM Flow.

#### Examples

The first example prevents the solution gas-oil ratio from increasing and applies this to all regions for when NTPVT on the TABDIMS keyword in the RUNSPEC section is set to three.

\--

\-- SOLUTION GAS (RS) MAXIMUM RATE OF INCREASE BY REGION \--

DRSDTR

\-- MAX RS ALL/FREE

\-- DRSDT1 DRSDT2

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.0000 ALL /

0.0000 ALL /

0.0000 ALL /

The second example below prevents the solution gas-oil ratio from increasing and applies this to all grid cells in PVTNUM region one. For PVTNUM regions one and two the keyword applies 0.0005 Mscf/stb/d as the maximum rate at which the solution gas-oil ratio is allowed to increase in a grid cell, and applies this to only cells containing free gas.

\--

\-- SOLUTION GAS (RS) MAXIMUM RATE OF INCREASE BY REGION \--

DRSDTR

\-- MAX RS ALL/FREE

\-- DRSDT1 DRSDT2

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.0000 ALL /

0.0005 FREE /

0.0005 FREE /

Again, the keyword parameters when applied are subject to the availability of free gas and the ability of the undersaturated oil to adsorb this gas.
