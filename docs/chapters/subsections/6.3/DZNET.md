### DZNET -- Define Grid Block Net Thickness for All Cells

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

DZNET defines the net thickness of all grid blocks in the Z direction via an array for each cell in a Cartesian Regular Grid model.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | DZNET | DZNET is an array of real numbers describing the net thickness in the Z direction for each cell in the model.<br>Repeat counts may be used, for example 10\*100.0.<br>If the value for a grid block is not defined then the grid block size (DZ) is assigned to the missing values. | DZ |
| feet | m | cm |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.31: DZNET Keyword Description

See also the DX, DY, DZ, NTG and TOPS keywords to fully define a Cartesian Regular Grid.

#### Example

\--

\-- DEFINE GRID BLOCK Z DIRECTION NET THICKNESS(BASED ON NX x NY x NZ = 300)

\--

DZNET

100\*15.0 100\*25.0 00\*45.0 /

The above example defines the net thickness of the cells in the Z direction based on 300 cells in the model as defined by the DIMENS keyword in the RUNSPEC section.
