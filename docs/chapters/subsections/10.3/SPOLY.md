### SPOLY -- Define the Initial Equilibration Polymer Concentration for All Grid Blocks

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SPOLY keyword defines the initial equilibration polymer concentration values for all grid cells in the model and should be used in conjunction with the PBUB, PDEW, PRESSURE, RS, RV, SGAS, SGAS and SWAT keywords etc., to fully describe the initial state of the model. The keyword should only be used if the polymer phase has been activated in the model via the POLYMER keyword in the RUNSPEC section.

This is the non-standard method to initialize the model via enumeration and is seldom employed in the industry. The standard methodology is for OPM Flow to initialize a model using the parameters on the EQUIL keyword combined with other keywords to fully describe the initial state of the model. The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SPOLY | SPOLY is an array of real positive numbers that are greater than or equal to zero assigning the initial equilibration polymer concentration values to each cell in the model.<br>Repeat counts may be used, for example 20\*25.0. | None |
| lb/stb | kg/sm^3^ | gm/scc |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 10.51: SPOLY Keyword Description

See also the PBUB, PDEW, PRESSURE, RS, RV, SGAS, SOIL and SWAT keywords to fully define the initial state of the model.

#### Example

\--

\-- DEFINE INITIAL EQUILIBRATION POLYMER VALUES FOR ALL CELLS IN THE MODEL

\-- BASED ON NX = 100, NY = 100 AND NZ = 3

\--

SPOLY

1000\*0.0000 1000\*0.0000 1000\*15.000 /

The above example defines the initial equilibration polymer concentration values to be 0.0000 for all the cells in the first and second layers and finally 15.000 for all the cells in the third layer.
