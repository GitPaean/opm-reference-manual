### SPOLY -- Define the Initial Equilibration Polymer Concentration for All Grid Blocks

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [SPOLY](#__RefHeading___Toc124292_23127940) keyword defines the initial equilibration polymer concentration values for all grid cells in the model and should be used in conjunction with the [PBUB](#__RefHeading___Toc135619_1317547213), [PDEW](#__RefHeading___Toc135623_1317547213), [PRESSURE](#__RefHeading___Toc135627_1317547213), [RS](#__RefHeading___Toc137361_1317547213), [RV](#__RefHeading___Toc137365_1317547213), [SGAS](#__RefHeading___Toc137369_1317547213), [SGAS](#__RefHeading___Toc137369_1317547213) and [SWAT](#__RefHeading___Toc137373_1317547213) keywords etc., to fully describe the initial state of the model. The keyword should only be used if the polymer phase has been activated in the model via the [POLYMER](#__RefHeading___Toc38609_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

This is the non-standard method to initialize the model via enumeration and is seldom employed in the industry. The standard methodology is for OPM Flow to initialize a model using the parameters on the [EQUIL](#__RefHeading___Toc135617_1317547213) keyword combined with other keywords to fully describe the initial state of the model. The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [SPOLY](#__RefHeading___Toc124292_23127940) | [SPOLY](#__RefHeading___Toc124292_23127940) is an array of real positive numbers that are greater than or equal to zero assigning the initial equilibration polymer concentration values to each cell in the model.<br>Repeat counts may be used, for example 20\*25.0. | None |
| lb/stb | kg/sm^3^ | gm/scc |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 10.51: SPOLY Keyword Description

See also the [PBUB](#__RefHeading___Toc135619_1317547213), [PDEW](#__RefHeading___Toc135623_1317547213), [PRESSURE](#__RefHeading___Toc135627_1317547213), [RS](#__RefHeading___Toc137361_1317547213), [RV](#__RefHeading___Toc137365_1317547213), [SGAS](#__RefHeading___Toc137369_1317547213), [SOIL](#__RefHeading___Toc137371_1317547213) and [SWAT](#__RefHeading___Toc137373_1317547213) keywords to fully define the initial state of the model.

#### Example

\--

\-- DEFINE INITIAL EQUILIBRATION POLYMER VALUES FOR ALL CELLS IN THE MODEL

\-- BASED ON NX = 100, NY = 100 AND NZ = 3

\--

SPOLY

1000\*0.0000 1000\*0.0000 1000\*15.000 /

The above example defines the initial equilibration polymer concentration values to be 0.0000 for all the cells in the first and second layers and finally 15.000 for all the cells in the third layer.
