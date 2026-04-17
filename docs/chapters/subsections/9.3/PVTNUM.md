### PVTNUM -- Define the PVT Regions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The PVTNUM keyword defines the PVT region numbers for each grid block, as such there must be one entry for each cell in the model. The region number specifies which set of PVT tables (DENSITY, PVDG, PVDO, PVTG, PVTO, PVCO, PVTW and ROCK) are used to calculate the PVT properties in a grid block.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | PVTNUM | PVTNUM defines an array of positive integers assigning a grid cell to a particular PVT region.<br>The maximum number of PVTNUM regions is set by the NTPVT variable on the TABDIMS keyword in the RUNSPEC section. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The EQULNUM and PVTNUM arrays need to be consistent, that is the all cells with the same PVTNUM can only belong to one EQLNUM region.<br>3)  If a cell is not assigned a PVTNUM region then the default value will be used.<br>4)  The keyword is terminated by a "/". |  |  |  |

Table 9.17: PVTNUM Keyword Description

#### Examples

The example below sets three PVTNUM regions for a 4 x 5 x 2 model.

\--

\-- DEFINE PVTNUM REGION FOR ALL CELLS

\--

PVTNUM

2 2 1 1 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1

3 3 1 1 3 3 1 1 1 1 1 1 1 1 1 1 1 1 1 1

/

Alternatively the EQUALS keyword could be employed to accomplish the same task, that is:

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

PVTNUM 1 1\* 1\* 1\* 1\* 1\* 1\* / SET REGION 1

PVTNUM 2 1 2 1 2 1 1 / SET REGION 2

PVTNUM 3 1 2 1 2 2 2 / SET REGION 3

/

There third example shows how to ensure the various PVT regions are isolated. First of all define the MULTNUM array in the GRID section and ensure all the regions are isolated.

\-- ==============================================================================

\--

\-- GRID SECTION

\--

\-- ==============================================================================

GRID

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

MULTNUM 1 1\* 1\* 1\* 1\* 1\* 1\* / SET REGION 1

MULTNUM 2 1 2 1 2 1 1 / SET REGION 2

MULTNUM 3 1 2 1 2 2 2 / SET REGION 3

/

\--

\-- SET TRANSMISSIBILITES ACROSS DIFFERENT RESERVOIRS TO ZERO TO ISOLATE

\-- RESERVOIRS

\--

\-- REGION REGION TRANS DIREC NNC REGION ARRAY

\-- FROM TO MULT OPT OPTS M / F / O

MULTREGT

1\* 1\* 0.0 1\* \'ALL\' M / ALL REGIONS SEALED

/

Then in the REGIONS section copy the MULTNUM array to the PVTNUM array.

\-- ==============================================================================

\--

\-- REGIONS SECTION

\--

\-- ==============================================================================

REGIONS

\--

\-- COPY AN ARRAY TO ANOTHER ARRAY BASED ON A REGION NUMBER

\--

\-- ARRAY ARRAY REGION REGION ARRAY

\-- FROM TO NUMBER M / F / O

COPYREG

MULTNUM PVTNUM 1 M / COPY MULT TO PVT 1

MULTNUM PVTNUM 2 M / COPY MULT TO PVT 2

MULTNUM PVTNUM 3 M / COPY MULT TO PVT 3

/

All the separate PVT regions are now isolated.
