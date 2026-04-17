### MULTX- -- Multiply Cell Transmissibility in the -X Direction

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

MULTX- multiples the transmissibility between two cell faces in the -X direction for all the cells in the model via an array, that is the keyword sets the transmissibility multiplier of block (I, J, K) between the cells (I-1, J, K) and (I, J, K). An alternative to defining the complete array is to use the BOX keyword to define an area of the grid and then use the MULTX- keyword to set the multipliers just for the area defined by the BOX keyword (see the example).

The keyword can be used for all grid types, except for the Radial Grid geometry.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | MULTX- | MULTX- is an array of real positive numbers assigning the transmissibility multipliers in the -X direction to each cell face in the model.<br>Repeat counts may be used, for example 20\*100.0. | 1.0 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.83: MULTX- Keyword Description

Note that OPM Flow does not require the GRIDOPTS(TRANMULT) parameter in the RUNSPEC section to be set to YES, in order to use this and other negative directional dependent multiplier keywords in the input deck. Whereas, the commercial simulator will terminate with an error if the keyword is present, and the GRIDOPTS(TRANMULT) parameter has not been set to YES.

See also the MULTX, MULTY, MULTY-, MULTZ and MULTZ- keywords for scaling transmissible between grid cells.

#### Example

\--

\-- DEFINE INPUT BOX FOR EDITING INPUT ARRAYS

\--

\-- \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

BOX

10 10 1 6 1 1 / DEFINE BOX AREA

\--

\-- SET MULTX- TRANSMISSIBILITY MULTIPLIERS

\--

MULTX-

6\*0.500 /

\--

\-- DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS

\--

ENDBOX

The above example defines a 0.5 scaling multiplier for the six cells defined by the preceding BOX statement. The ENDBOX keyword resets the input box to the full grid.
