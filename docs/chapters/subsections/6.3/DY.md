### DY -- Define the Size of Grid Blocks in the Y Direction for All Cells

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[DY](#__RefHeading___Toc45767_719036256) defines the size of all grid blocks in the Y direction via an array for each cell in a Cartesian Regular Grid model.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [DY](#__RefHeading___Toc45767_719036256) | [DY](#__RefHeading___Toc45767_719036256) is an array of real numbers describing the cell size in the Y direction for each cell in the model.<br>Repeat counts may be used, for example 10\*100.0. | None |
| feet | m | cm |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.28: DY Keyword Description

See also the [DX](#__RefHeading___Toc92905_705534506), [DZ](#__RefHeading___Toc45769_719036256) and [TOPS](#__RefHeading___Toc55283_3701168388) keywords to fully define a Cartesian Regular Grid.

#### Example

\--

\-- DEFINE GRID BLOCK Y DIRECTION CELL SIZE (BASED ON NX x NY x NZ = 300)

\--

DY

300\*1000 /

The above example defines the size of the cells in the Y direction based on 300 cells in the model as defined by the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.
