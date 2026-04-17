### GASSATC -- Define the Initial Equilibration Saturated Coal Gas Concentration for All Grid Blocks

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The GASSATC keyword defines the initial equilibration saturated coal gas concentration values for all grid cells in the model. The keyword should only be used if the coal phase has been activated in the model via the COAL keyword in the RUNSPEC section. The keyword is used to re-scale the Langmuir isotherms entered via the LANGMUIR keyword in the PROPS section, in conjunction with a matrix grid blocks initial reservoir pressure. The keyword is optional, and if absent from the input file, the matrix grid block Langmuir isotherm is left unscaled.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

This is the non-standard method to initialize the model via enumeration and is seldom employed in the industry. The standard methodology is for OPM Flow to initialize a model using the parameters on the EQUIL keyword combined with other keywords to fully describe the initial state of the model. The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | GASSATC | GASSATC is an array of real positive numbers that define the initial equilibration saturated coal gas concentration values to each cell in the model.<br>Repeat counts may be used, for example 20\*75.0. | None |
| Mscf/ft3 | sm^3^/m^3^ | scc/cc |  |
| Notes:<br>1)  The number of entries should correspond to number of matrix cells in the model, that is (NX x NY x NZ) divided by two, as per the parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 10.16: GASSATC Keyword Description

See also the GASCONC and the GCVD keywords in the SOLUTION section to fully define the initial state of the model.

#### Example

\--

\-- DEFINE INITIAL EQUILIBRATION SAT COAL GAS CONCENTRATION ALL CELLS MODEL

\-- BASED ON NX = 100, NY = 100 AND NZ = 6

\--

GASSATC

1000\*75.500 1000\*65.500 1000\*60.000 /

The above example defines the initial equilibration saturated coal gas concentration values to be 75.500 for all the matrix cells in the first layer, 65.500 for all the cells in the second layer, and finally 60.000 for all the cells in the third layer.
