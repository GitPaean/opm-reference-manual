### RVW -- Define the Initial Equilibration Vaporized Water in Gas Ratio for All Grid Blocks

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [RVW](#__RefHeading___Toc537756_4287353749) keyword defines the initial equilibration vaporized water in gas ratio values for all grid cells in the model and should be used in conjunction with the [PBUB](#__RefHeading___Toc135619_1317547213), [PDEW](#__RefHeading___Toc135623_1317547213), [PRESSURE](#__RefHeading___Toc135627_1317547213), [RV](#__RefHeading___Toc137365_1317547213), [SGAS](#__RefHeading___Toc137369_1317547213), [SOIL](#__RefHeading___Toc137371_1317547213) and [SWAT](#__RefHeading___Toc137373_1317547213) keywords etc., to fully describe the initial state of the model. The keyword should only be used if both gas and water phases have been activated in the model via the [GAS](#__RefHeading___Toc38607_2267116897) and [WATER](#__RefHeading___Toc38611_2267116897) keywords, and the [VAPWAT](#__RefHeading___Toc317543_3149455253) is also present activating OPM Flow's Vaporized Water Model. All the aforementioned keywords are in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

This is the non-standard method to initialize the model via enumeration and is seldom employed in the industry. The standard methodology is for OPM Flow to initialize a model using the parameters on the [EQUIL](#__RefHeading___Toc135617_1317547213) keyword combined with other keywords to fully describe the initial state of the model. The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [RVW](#__RefHeading___Toc537756_4287353749) | [RVW](#__RefHeading___Toc537756_4287353749) is an array of real positive numbers assigning the initial equilibration gas-vaporized water ratio values to each cell in the model.<br>Repeat counts may be used, for example 20\*1.30. | None |
| stb/Mscf | sm^3^/sm^3^ | rcc/scc |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 10.34: RVW Keyword Description

See also the [PBUB](#__RefHeading___Toc135619_1317547213), [PDEW](#__RefHeading___Toc135623_1317547213), [PRESSURE](#__RefHeading___Toc135627_1317547213), [RV](#__RefHeading___Toc137365_1317547213), [SGAS](#__RefHeading___Toc137369_1317547213), [SOIL](#__RefHeading___Toc137371_1317547213) and [SWAT](#__RefHeading___Toc137373_1317547213) keywords to fully define the initial state of the model.

#### Example

\--

\-- INITIAL EQUILIBRATION WATER VAPOR IN GAS RATIO VALUES FOR ALL CELLS

\-- BASED ON NX = 100, NY = 100 AND NZ = 3

\--

RVW

1000\*0.0000 1000\* 0.0000 1000\*1.3000 /

The above example defines the initial equilibration gas-vaporized water values to be 0.000 for all the cells in the first and second layers and 1.3000 for all the cells in the third layer.
