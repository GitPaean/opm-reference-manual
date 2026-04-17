### TRANX -- Define the Transmissibility in the X Direction for All the Cells

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

TRANX defines the transmissibility in the X direction for all the cells in the model via an array. The keyword can be used for all grid types, except for the Radial Grid geometry. The keyword effectively overwrites previously entered and calculated data. The transmissibility overwritten is the +X face transmissibility of each grid block, that is for cell (I, J, K) the transmissibility between cells (I, J, K) and (I+1, J, K).

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | TRANX | TRANX is an array of real positive numbers assigning the transmissibility in the X direction to each cell in the model.<br>Repeat counts may be used, for example 20\*100.0. | None |
| cP.rb/day/psia | cP.rm^3^/day/bars | cP.rcc/hr/atm |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  Values not reset by this keyword remain unaltered.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 7.9: TRANX Keyword Description

See also the TRANY and TRANYZ keywords to modify the transmissibilities in the other directions.

#### Example

\--

\-- DEFINE INPUT BOX FOR EDITING INPUT ARRAYS

\--

\-- \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

BOX

1 1 10 10 1 120 / DEFINE BOX AREA

\--

\-- SET TRANX+ TRANSMISSIBILITY

\--

TRANX

120\*0.00 /

\--

\-- DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS

\--

ENDBOX

Here the BOX statement is used to define the input grid for the TRANX keyword, which overwrites the transmissibility previously calculated with transmissibility values of zero, resulting in a no-flow boundary in that part of the field. The ENDBOX keyword resets the input box to the full grid.
