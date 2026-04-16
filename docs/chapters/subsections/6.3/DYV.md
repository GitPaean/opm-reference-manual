### DYV -- Define the Size of Grid Blocks in the Y Direction via a Vector

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[DYV](#__RefHeading___Toc55933_3701168388) defines the size of grid blocks in the Y direction via a vector as opposed to defining the Y direction cell size for each cell for a Cartesian Regular Grid.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [DYV](#__RefHeading___Toc55933_3701168388) | [DYV](#__RefHeading___Toc55933_3701168388) is a vector of real numbers describing the cell size for the grid blocks in the Y direction.<br>Repeat counts may be used, for example 10\*100.0. | None |
| feet | m | cm |  |
| Notes:<br>1)  The number of entries should correspond to the NY parameter on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.29: DYV Keyword Description

See also the [DXV](#__RefHeading___Toc55931_3701168388), [DZV](#__RefHeading___Toc55601_3701168388) and [TOPS](#__RefHeading___Toc55283_3701168388) keywords to fully define a Cartesian Regular Grid.

#### Example

\--

\-- DEFINE GRID BLOCK Y DIRECTION CELL SIZE (BASED ON NY = 5)

\--

DYV

5\*100 /

The above example defines the size of the cells in the Y direction based on NY equals 5 on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.
