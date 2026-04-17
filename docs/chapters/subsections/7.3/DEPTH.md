### DEPTH -- Edits the Depth at the Center of Each Cell

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The DEPTH keywords modifies the depth at the center of selected cells in the model. The cells DEPTH are calculated by OPM Flow at the end of the GRID section and this keyword allows the user to adjust the calculated depths in the EDIT section. The area to be modified can be defined via the various grid selection keywords, ADD, BOX, EQUALS, etc., and areas that are not selected remain unchanged.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | DEPTH | DEPTH is an array of real numbers defining the depth at the center of each cell in the model. Only the values in the currently defined input BOX needed be entered.<br>Repeat counts may be used, for example 30\*5201.0. | None |
| feet | m | cm |  |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 7.2: Depth Keyword Description

See also the TOPS keyword to define the top structural depth for the cells.

#### Examples

The example below modifies the DEPTH of the cells for a selection of 10 cells from an NX = 10, NY = 11 and NZ = 20 model.

\--

\-- DEFINE INPUT BOX FOR EDITING INPUT ARRAYS

\--

\-- \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

BOX

1 10 11 11 20 20 / SET BOX AREA TO BE MODIFIED

/

\--

\-- SET GRID BLOCK CENTER DEPTH FOR THE GRID BLOCKS

\--

DEPTH 10\*3500.0 /

\--

\-- DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS

\--

ENDBOX

Alternatively the EQUALS keyword can be used to perform the same edit.

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

DEPTH 3500.0 1 10 11 11 20 20 / RESET DEPTH

/
