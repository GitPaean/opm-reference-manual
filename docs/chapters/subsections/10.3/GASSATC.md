### GASSATC -- Define the Initial Equilibration Saturated Coal Gas Concentration for All Grid Blocks

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [GASSATC](#__RefHeading___Toc216737_1190369742) keyword defines the initial equilibration saturated coal gas concentration values for all grid cells in the model. The keyword should only be used if the coal phase has been activated in the model via the [COAL](#__RefHeading___Toc234580_3519154785) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The keyword is used to re-scale the Langmuir isotherms entered via the [LANGMUIR](#__RefHeading___Toc214338_2843394514) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section, in conjunction with a matrix grid blocks initial reservoir pressure. The keyword is optional, and if absent from the input file, the matrix grid block Langmuir isotherm is left unscaled.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

This is the non-standard method to initialize the model via enumeration and is seldom employed in the industry. The standard methodology is for OPM Flow to initialize a model using the parameters on the [EQUIL](#__RefHeading___Toc135617_1317547213) keyword combined with other keywords to fully describe the initial state of the model. The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [GASSATC](#__RefHeading___Toc216737_1190369742) | [GASSATC](#__RefHeading___Toc216737_1190369742) is an array of real positive numbers that define the initial equilibration saturated coal gas concentration values to each cell in the model.<br>Repeat counts may be used, for example 20\*75.0. | None |
| Mscf/ft3 | sm^3^/m^3^ | scc/cc |  |
| Notes:<br>1)  The number of entries should correspond to number of matrix cells in the model, that is (NX x NY x NZ) divided by two, as per the parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 10.16: GASSATC Keyword Description

See also the [GASCONC](#__RefHeading___Toc189444_2330925267) and the [GCVD](#__RefHeading___Toc224457_156692946) keywords in the [SOLUTION](#__RefHeading___Toc43947_784232322) section to fully define the initial state of the model.

#### Example

\--

\-- DEFINE INITIAL EQUILIBRATION SAT COAL GAS CONCENTRATION ALL CELLS MODEL

\-- BASED ON NX = 100, NY = 100 AND NZ = 6

\--

GASSATC

1000\*75.500 1000\*65.500 1000\*60.000 /

The above example defines the initial equilibration saturated coal gas concentration values to be 75.500 for all the matrix cells in the first layer, 65.500 for all the cells in the second layer, and finally 60.000 for all the cells in the third layer.
