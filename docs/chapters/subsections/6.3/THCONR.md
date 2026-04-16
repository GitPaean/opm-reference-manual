### THCONR -- Define Rock and Fluid Thermal Conductivity for All Cells

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [THCONR](#__RefHeading___Toc132284_650382403) keyword defines the reservoir rock plus fluid thermal conductivity for all cells for when the thermal calculation is activated by the [THERMAL](#__RefHeading___Toc137276_650382403) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

This keyword can only be used if the thermal option has been activated by the [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Note this is different to the commercial simulator that uses the [TEMP](#__RefHeading___Toc146397_3544483072) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section to activate the black-oil thermal model.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [THCONR](#__RefHeading___Toc132284_650382403) | [THCONR](#__RefHeading___Toc132284_650382403) is an array of real positive numbers that define the combined rock and fluid conductivity of a grid block.<br>Repeat counts may be used, for example 3000\*25.0 | None |
| Btu/ft/day/°R | kJ/m/day/K | J/cm/hr/K |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

*Table 6.124: THCONR Keyword Description*
Note that there two ways to define the rock and in situ fluids thermal conductivity:

3)  1)  1)  Either by using the [THCONR](#__RefHeading___Toc132284_650382403) keyword to define the combined rock and fluid conductivity, and optionally the [THCONSF](#__RefHeading___Toc132286_650382403) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section, or

        2)  by specifying the rock and fluid conductivities individually using the [THCROCK](#__RefHeading___Toc124825_650382403), [THCOIL](#__RefHeading___Toc119871_650382403), [THCGAS](#__RefHeading___Toc93091_718313858), and [THCWATER](#__RefHeading___Toc323954_1728001293) keywords in the [GRID](#__RefHeading___Toc38674_784232322) section.

Hence, the [THCROCK](#__RefHeading___Toc124825_650382403) and [THCONR](#__RefHeading___Toc132284_650382403) keywords are mutually exclusive.

#### Example

\--

\-- DEFINE GRID BLOCK ROCK-FLUID THERMAL CONDUCTIVITY

-- FOR ALL CELLS (BASED ON NX x NY x NZ = 300)

\--

THCONR

300\*25.0 /

The above example defines the combined rock and fluid thermal conductivity of 25.0 for each cell in the 300 grid block model, as defined by the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.
