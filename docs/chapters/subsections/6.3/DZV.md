### DZV -- Define the Size of Grid Blocks in the Z Direction via a Vector

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

DZV defines the size of grid blocks in the Z direction via a vector as opposed to defining the thickness property for each cell. The keyword is used for both Cartesian Regular Grids and Radial Grids.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | DZV | DZV is a vector of real numbers describing the cell size for the grid blocks in the Z direction.<br>Repeat counts may be used, for example 10\*20.0. | None |
| feet | m | cm |  |
| Notes:<br>1)  The number of entries should correspond to the NZ parameter on the DIMENS keyword in the RUNSPEC section..<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.32: DZV Keyword Description

See also the DXV, DYV and TOPS keywords for a Cartesian Regular Grid and DRV, DTHETAV and TOPS keywords to fully define a Radial Grid model.

#### Example

\--

\-- DEFINE GRID BLOCK SIZES IN THE Z DIRECTION (BASED ON NZ = 20)

\--

DZV

3.0 5.0 3.0 2.0 5.0 15\*3.0 /

The above example defines the size of the cells in the Z direction based on NZ equals 20 on the DIMENS keyword in the RUNSPEC section.
