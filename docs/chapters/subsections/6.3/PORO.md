### PORO -- Define the Porosity Values for All the Cells

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[PORO](#__RefHeading___Toc45797_719036256) defines the porosity for all the cells in the model via an array. The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [PORO](#__RefHeading___Toc45797_719036256) | [PORO](#__RefHeading___Toc45797_719036256) is an array of real positive numbers that are greater than or equal to zero and less than or equal to one that are the porosity values for each cell in the model.<br>Repeat counts may be used, for example 3000\*0.15 | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.112: PORO Keyword Description

See also the [NTG](#__RefHeading___Toc33334_784232322), [PERMX](#__RefHeading___Toc45791_719036256), [PERMY](#__RefHeading___Toc45793_719036256) and [PERMX](#__RefHeading___Toc45791_719036256) keywords to fully define a grid's properties

#### Example

\--

\-- DEFINE GRID BLOCK POROSITY DATA FOR ALL CELLS (BASED ON NX x NY x NZ = 300)

\--

PORO

300\*0.300 /

The above example defines a constant porosity of 0.300 to all 300 cells in the model as defined by the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.
