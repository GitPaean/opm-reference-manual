### DYV -- Define the Size of Grid Blocks in the Y Direction via a Vector

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

DYV defines the size of grid blocks in the Y direction via a vector as opposed to defining the Y direction cell size for each cell for a Cartesian Regular Grid.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | DYV | DYV is a vector of real numbers describing the cell size for the grid blocks in the Y direction.<br>Repeat counts may be used, for example 10\*100.0. | None |
| feet | m | cm |  |
| Notes:<br>1)  The number of entries should correspond to the NY parameter on the DIMENS keyword in the RUNSPEC section.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.29: DYV Keyword Description

See also the DXV, DZV and TOPS keywords to fully define a Cartesian Regular Grid.

#### Example

\--

\-- DEFINE GRID BLOCK Y DIRECTION CELL SIZE (BASED ON NY = 5)

\--

DYV

5\*100 /

The above example defines the size of the cells in the Y direction based on NY equals 5 on the DIMENS keyword in the RUNSPEC section.
