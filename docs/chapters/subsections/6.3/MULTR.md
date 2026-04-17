### MULTR -- Multiply Cell Transmissibility in the +R Direction

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

MULTR multiples the transmissibility between two cell faces in the +R direction for all the cells in the model via an array, that is the keyword sets the transmissibility multiplier of block (I, J, K) between the cells (I, J, K) and (I+I, J, K). An alternative to defining the complete array is to use the BOX keyword to define an area of the grid and then use the MULTR keyword to set the multipliers just for the area defined by the BOX keyword (see the example).

The keyword should only be used with radial and spider grids, as declared by the RADIAL or SPIDER keywords in the RUNSPEC section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | MULTR+ | MULTR+ is an array of real positive numbers assigning the transmissibility multipliers in the +R direction to each cell face in the model.<br>Repeat counts may be used, for example 20\*100.0. | 1.0 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.74: MULTR Keyword Description

See also the MULTR-, MULTTHT, MULTTHT-, MULTZ and MULTZ- keywords for scaling transmissible between between grid cells in the R direction.

#### Example

\--

\-- DEFINE INPUT BOX FOR EDITING INPUT ARRAYS

\--

\-- \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

BOX

10 10 1 6 1 3 / DEFINE BOX AREA

\--

\-- SET MULTR+ TRANSMISSIBILITY MULTIPLIERS

\--

MULTR

18\*0.300 /

\--

\-- DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS

\--

ENDBOX

The above example defines a 0.3 scaling multiplier for the 18 cells defined by the preceding BOX statement. The ENDBOX keyword resets the input box to the full grid.
