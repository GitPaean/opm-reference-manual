### DRVDT -- Vaporized Oil (Rv) Maximum Rate of Increase Parameters

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[DRVDT](#__RefHeading___Toc117625_2179381650) defines the maximum rate at which the vaporized oil-gas ratio or condensate-gas ratio (Rv) can be increased in a grid cell. The keyword is similar in functionality to the [DRVDTR](#__RefHeading___Toc135416_4268459800) keyword, that defines the maximum rate at which Rv can be increased in a grid cell by region. Both keywords should only be used if the [OIL](#__RefHeading___Toc97439_1778172979), [GAS](#__RefHeading___Toc38607_2267116897), and [VAPOIL](#__RefHeading___Toc56610_2267116897) (condensate) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section have been invoked to allow oil, gas and condensate to be present in the model. The keyword only affects the behavior of an increasing Rv, for example when gas is being injected into a gas condensate reservoir as part of as gas re-cycling scheme, and is subject to the availability of free oil (condensate) and the ability of the undersaturated gas to adsorb this condensate.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | DRVDT1 | DRVDT1 is a real positive number that defines the maximum rate at which the vaporized oil-gas ratio is allowed to increase in a grid cell, that is the maximum rate at which the oil can dissolve into the available undersaturated gas.<br>A value of zero means that Rv cannot increase and free oil cannot vaporize into the unsaturated gas in a grid cell. Alternatively a very large value of DRVDT1 allows Rv to increase rapidly until there is no free oil or the gas within the grid block is fully saturated.<br>Note if the keyword is not present in the input deck then DRVDT1 is assumed to be a very large number resulting in complete re-vaporization of the oil into the available undersaturated gas. | None |
| stb/Mscf/d | sm^3^/sm^3^/day | scc/scc/day |  |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 12.23: DRVDT Keyword Description

Note this keyword can be used in history matching field performance to control the availability of the movable gas phase. See also the [VAPPARS](#__RefHeading___Toc210172_2884651453) keyword in the [SOLUTION](#__RefHeading___Toc43947_784232322) section and the [DRVDTR](#__RefHeading___Toc135416_4268459800), [DRSDT](#__RefHeading___Toc117623_2179381650) and [DRSDTR](#__RefHeading___Toc135414_4268459800) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section that controls how solution gas is treated and the rate at which the vaporized phase ratio increases within a grid block.

#### Example

The example prevents the solution oil-gas ratio from increasing.

\--

\-- VAPORIZED OIL (RV) MAXIMUM RATE OF INCREASE FOR MODEL \--

DRVDT

\-- MAX RV

\-- DRVDT1

\-- \-\-\-\-\-\--

0.000 /

Again, the keyword parameters when applied are subject to the availability of free oil and the ability of the undersaturated gas to adsorb this oil.
