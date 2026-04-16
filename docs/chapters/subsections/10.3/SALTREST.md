### SALTREST -- Define the Restart Salt Concentration for All Grid Blocks

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [SALTREST](#__RefHeading___Toc599543_516898843) keyword defines restart salt concentration values for all grid cells in the model and should be used in runs that are using the [RESTART](#__RefHeading___Toc135629_1317547213) facility, where the initial run has not used the Low Salt or Brine options. This allows for initial runs that have used the standard water PVT properties via the [PVTW](#__RefHeading___Toc2086106_3315222525) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section, to be restarted with salt dependent water properties. The keyword should only be used if the salt (brine) phase has been activated in the current restart run (not the initial run) via the [BRINE](#__RefHeading___Toc162083_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [SALTREST](#__RefHeading___Toc599543_516898843) | [SALTREST](#__RefHeading___Toc599543_516898843) is an array of real positive numbers that are greater than or equal to zero assigning the restart salt concentration values to each cell in the model.<br>Repeat counts may be used, for example 20\*15.0. | None |
| lb/stb | kg/sm^3^ | gm/scc |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 10.39: SALTREST Keyword Description

See also the [PVTWSALT](#__RefHeading___Toc331848_501926209) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section and the [RESTART](#__RefHeading___Toc135629_1317547213) keyword in the [SOLUTION](#__RefHeading___Toc43947_784232322) section.

#### Example

\--

\-- DEFINE RESTART SALTREST VALUES FOR ALL CELLS IN THE MODEL

\-- BASED ON NX = 100, NY = 100 AND NZ = 3

\--

SALTREST

1000\*0.0000 1000\*0.0000 1000\*15.000 /

The above example defines the restart salt concentration values to be 0.0000 for all the cells in the first and second layers and finally 15.000 for all the cells in the third layer.
