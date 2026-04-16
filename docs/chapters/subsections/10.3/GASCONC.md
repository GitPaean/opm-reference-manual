### GASCONC -- Define the Initial Equilibration Coal Gas Concentration for All Grid Blocks

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [GASCONC](#__RefHeading___Toc189444_2330925267) keyword defines the initial equilibration coal gas concentration values for all matrix grid cells in the model and should be used in conjunction with the [GCVD](#__RefHeading___Toc224457_156692946) keyword in the [SOLUTION](#__RefHeading___Toc43947_784232322) section, to fully describe the initial state of the model. The keyword should only be used if the coal phase has been activated in the model via the [COAL](#__RefHeading___Toc234580_3519154785) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Note both [GASCONC](#__RefHeading___Toc189444_2330925267) and [GCVD](#__RefHeading___Toc224457_156692946) are optional as the simulator will calculate the coal gas concentration based on the equilibrium concentration and the block pressure.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

This is the non-standard method to initialize the model via enumeration and is seldom employed in the industry. The standard methodology is for OPM Flow to initialize a model using the parameters on the [EQUIL](#__RefHeading___Toc135617_1317547213) keyword combined with other keywords to fully describe the initial state of the model. The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [GASCONC](#__RefHeading___Toc189444_2330925267) | [GASCONC](#__RefHeading___Toc189444_2330925267) is an array of real positive numbers that define the initial equilibration coal gas concentration values to each matrix cell in the model.<br>Repeat counts may be used, for example 20\*75.0. | None |
| Mscf/ft3 | sm^3^/m^3^ | scc/cc |  |
| Notes:<br>1)  The number of entries should correspond to number of matrix cells in the model, that is (NX x NY x NZ) divided by two, as per the parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 10.15: GASCONC Keyword Description

See also the [GCVD](#__RefHeading___Toc224457_156692946) keyword in the [SOLUTION](#__RefHeading___Toc43947_784232322) section to fully define the initial state of the model.

#### Example

\--

\-- DEFINE INITIAL EQUILIBRATION COAL GAS CONCENTRATION FOR ALL CELLS

\-- BASED ON NX = 100, NY = 100 AND NZ = 6

\--

GASCONC

1000\*75.500 1000\*65.500 1000\*60.000 /

The above example defines the initial equilibration coal gas concentration values to be 75.500 for all the matrix cells in the first layer, 65.500 for all the cells in the second layer, and finally 60.000 for all the cells in the third layer.
