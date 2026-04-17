### RVW -- Define the Initial Equilibration Vaporized Water in Gas Ratio for All Grid Blocks

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The RVW keyword defines the initial equilibration vaporized water in gas ratio values for all grid cells in the model and should be used in conjunction with the PBUB, PDEW, PRESSURE, RV, SGAS, SOIL and SWAT keywords etc., to fully describe the initial state of the model. The keyword should only be used if both gas and water phases have been activated in the model via the GAS and WATER keywords, and the VAPWAT is also present activating OPM Flow's Vaporized Water Model. All the aforementioned keywords are in the RUNSPEC section.

This is the non-standard method to initialize the model via enumeration and is seldom employed in the industry. The standard methodology is for OPM Flow to initialize a model using the parameters on the EQUIL keyword combined with other keywords to fully describe the initial state of the model. The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | RVW | RVW is an array of real positive numbers assigning the initial equilibration gas-vaporized water ratio values to each cell in the model.<br>Repeat counts may be used, for example 20\*1.30. | None |
| stb/Mscf | sm^3^/sm^3^ | rcc/scc |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 10.34: RVW Keyword Description

See also the PBUB, PDEW, PRESSURE, RV, SGAS, SOIL and SWAT keywords to fully define the initial state of the model.

#### Example

\--

\-- INITIAL EQUILIBRATION WATER VAPOR IN GAS RATIO VALUES FOR ALL CELLS

\-- BASED ON NX = 100, NY = 100 AND NZ = 3

\--

RVW

1000\*0.0000 1000\* 0.0000 1000\*1.3000 /

The above example defines the initial equilibration gas-vaporized water values to be 0.000 for all the cells in the first and second layers and 1.3000 for all the cells in the third layer.
