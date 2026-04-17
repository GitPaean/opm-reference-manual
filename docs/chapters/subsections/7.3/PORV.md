### PORV -- Define the Pore Volumes for All the Cells

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

PORV defines the pore volumes for all the cells in the model via an array. The keyword can be used for all grid types, except for the Radial Grid geometry. The keyword effectively overwrites previously entered and calculated data. The area to be modified can be defined via the various grid selection keywords, ADD, BOX, EQUALS, etc., and areas that are not selected remain unchanged.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | PORV | PORV is an array of real positive numbers assigning a pore volume to each cell in the model. Only the values in the currently defined input BOX needed be entered.<br>Repeat counts may be used, for example 20\*100.0. | None |
| rb | rm^3^ | rcc |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  Values not reset by this keyword remain unaltered.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 7.6: PORV Keyword Description

#### Example

\--

\-- DEFINE INPUT BOX FOR EDITING INPUT ARRAYS

\--

\-- \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

BOX

1\* 100 1\* 100 20 20 / DEFINE BOX AREA

\--

\-- SET PORV FOR THE GRID BLOCKS

\--

PORV

1000\*0.00 /

\--

\-- DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS

\--

ENDBOX

Here the BOX statement is used to define the input grid for the PORV keyword, which overwrites the pore volume previously calculated with pore volume values of zero, resulting in a no-flow boundary in that part of the field between layers 19 and 21, since layer 20 is deactivated. The ENDBOX keyword resets the input box to the full grid.
