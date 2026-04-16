### DRSDT -- Solution Gas (Rs) Maximum Rate of Increase Parameters

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[DRSDT](#__RefHeading___Toc117623_2179381650) defines the maximum rate at which the solution gas-oil ratio (Rs) can be increased in a grid cell. The keyword is similar in functionality to the [DRSDTR](#__RefHeading___Toc135414_4268459800) keyword, that defines the maximum rate at which Rs can be increased in a grid cell by region. Both keywords should only be used if the [OIL](#__RefHeading___Toc97439_1778172979), [GAS](#__RefHeading___Toc38607_2267116897), and [DISGAS](#__RefHeading___Toc39767_2267116897) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section have been invoked to allow oil, gas and dissolved gas to be present in the model. The keyword only affects the behavior of an increasing Rs, for example when gas is being injected into an oil reservoir, and is subject to the availability of free gas and the ability of the undersaturated oil to adsorb this gas.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | DRSDT1 | DRSDT1 is a real positive number that defines the maximum rate at which the solution gas-oil ratio is allowed to increase in a grid cell, that is the maximum rate the gas can dissolve into the available undersaturated oil.<br>A value of zero means that Rs cannot increase and free gas cannot dissolve into the unsaturated oil in a grid cell. Alternatively a very large value of DRSDT1 allows Rs to increase rapidly until there is no free gas or the oil within the grid block is fully saturated.<br>Note if the keyword is not present in the input deck then DRSDT1 is assumed to be a very large number resulting in complete re-solution of the gas into the available undersaturated oil. | None |
| Mscf/stb/d | sm^3^/sm^3^/day | scc/scc/day |  |
| 2 | DRSDT2 | DRSDT2 is a defined character string that defines whether the DRSDT1 is applied to either all grid blocks or just those grid blocks containing free gas:<br>1)  [ALL](#__RefHeading___Toc4420_421927891): means the DRSDT1 maximum rate at which Rs is allowed to increase in a grid cell is applied to all grid blocks.<br>2)  FREE: means the DRSDT1 maximum rate at which Rs is allowed to increase in a grid cell is applied to grid blocks only containing free gas.<br>Note if the keyword is not present in the input deck then DRSDT2 is set to the default value of [ALL](#__RefHeading___Toc4420_421927891). | [ALL](#__RefHeading___Toc4420_421927891) |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 12.20: DRSDT Keyword Description

Note this keyword can be used in history matching field performance to control the availability of the movable gas phase.

See also the [VAPPARS](#__RefHeading___Toc210172_2884651453) keyword in the [SOLUTION](#__RefHeading___Toc43947_784232322) section and the [DRSDTR](#__RefHeading___Toc135414_4268459800), [DRVDT](#__RefHeading___Toc117625_2179381650) and [DRVDTR](#__RefHeading___Toc135416_4268459800) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section that controls how vaporized oil is treated and the rate at which the dissolved phase ratio increases within a grid block.

#### Examples

The first example prevents the solution gas-oil ratio from increasing and applies this to all grid cells.

\--

\-- SOLUTION GAS (RS) MAXIMUM RATE OF INCREASE FOR MODEL \--

DRSDT

\-- MAX RS ALL/FREE

\-- DRSDT1 DRSDT2

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.000 ALL /

And the second example below applies 0.0005 Mscf/stb/d as the maximum rate at which the solution gas-oil ratio is allowed to increase in a grid cell, and applies this to only cells containing free gas.

\--

\-- SOLUTION GAS (RS) MAXIMUM RATE OF INCREASE FOR MODEL \--

DRSDT

\-- MAX RS ALL/FREE

\-- DRSDT1 DRSDT2

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.0005 FREE /

Again, the keyword parameters when applied are subject to the availability of free gas and the ability of the undersaturated oil to adsorb this gas.
