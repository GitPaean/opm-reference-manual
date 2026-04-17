### SPOLYMW -- Define The Initial Equilibration Polymer Molecular Weights For All Grid Blocks

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SPOLYMW keyword defines the initial equilibration polymer molecular weights for all grid cells in the model and should only be be used with OPM Flow\'s Polymer Molecular Weight Transport option, together with the other standard equilibration keywords, in order to fully describe the initial state of the model.

This keyword should only be used if the POLYMER and POLYMW keywords in the RUNSPEC section are also activated.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SPOLYMW | SPOLYMW is an array of real positive numbers that are greater than or equal to zero assigning the initial equilibration polymer molecular weights to each cell in the model. Repeat counts may be used, for example 20\*5.0 | 0,0 |
| lb/lb-M | kg/kg-M | gm/gm-M |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 10.52: SPOLYMW Keyword Description

See also the PBUB, PDEW, PRESSURE, RS, RV, SGAS, SOIL and SWAT keywords to fully define the initial state of the model.

#### Example

\--

\-- INITIAL EQUILIBRATION POLYMER MOLECULAR WEIGHTS FOR ALL CELLS

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

SPOLYMW 0.0000 1\* 1\* 1\* 1\* 1 5 / LAYERS 1 TO 5

SPOLYMW 5.0000 1\* 1\* 1\* 1\* 6 7 / LAYERS 6 TO 7

SPOLYMW 0.0000 1\* 1\* 1\* 1\* 8 20 / LAYERS 8 TO 20

/

The above example defines the initial equilibration polymer molecular weights to be 0.0000 for all the cells, except for layers six to seven, where the polymer molecular weight is set to five for these cells.
