### HEATCRT -- Define Reservoir Rock Heat Capacity Temperature Dependence for All Cells

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [HEATCRT](#__RefHeading___Toc138899_2509125675) keyword defines the reservoir rock volumetric heat capacity temperature dependence for all cells for when OPM Flow's thermal calculation is activated by the [THERMAL](#__RefHeading___Toc137276_650382403) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

This keyword can only be used if OPM Flow's thermal option has been activated by the [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Note this is different to the commercial simulator that uses the [TEMP](#__RefHeading___Toc146397_3544483072) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section to activate the black-oil thermal model.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [HEATCRT](#__RefHeading___Toc138899_2509125675) | [HEATCRT](#__RefHeading___Toc138899_2509125675) is an array of real positive numbers that define reservoir rock volumetric heat capacity temperature dependence of a grid block.<br>Repeat counts may be used, for example 3000\*0.05 | None |
| Btu/ft3/°R2 | kJ/m3/K2 | J/cm3/K2 |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

*Table 6.44: HEATCRT Keyword Description*
Note this keyword is incompatible with [SPECROCK](#__RefHeading___Toc121481_83452205) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section.

The data for this keyword and the [HEATCR](#__RefHeading___Toc128353_2509125675) keyword are used to calculate the reservoir rock volumetric heat capacity temperature dependence using the following relationship:

#### Example

\--

\-- DEFINE RESERVOIR ROCK HEAT CAPACITY TEMPERATURE DEPENDENCE

\-- FOR ALL CELLS (BASED ON NX x NY x NZ = 300)

\-- KEYWORD IS INCOMPATIBLE WITH THE SPECROCK KEYWORD

\-- (OPM FLOW THERMAL OPTION ONLY)

\--

HEATCRT

300\*0.05 /

The above example defines the reservoir rock volumetric heat capacity temperature dependence of 0.05 for each cell in the 300 grid block model.
