### MULTR -- Multiply Cell Transmissibility in the +R Direction

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[MULTR](#__RefHeading___Toc228976_1841740821) multiples the transmissibility between two cell faces in the +R direction for all the cells in the model via an array, that is the keyword sets the transmissibility multiplier of block (I, J, K) between the cells (I, J, K) and (I+I, J, K). An alternative to defining the complete array is to use the [BOX](#__RefHeading___Toc42110_3671211675) keyword to define an area of the grid and then use the [MULTR](#__RefHeading___Toc228976_1841740821) keyword to set the multipliers just for the area defined by the [BOX](#__RefHeading___Toc42110_3671211675) keyword (see the example).

The keyword should only be used with radial and spider grids, as declared by the [RADIAL](#__RefHeading___Toc51752_2905512151) or [SPIDER](#__RefHeading___Toc439805_750232207) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | [MULTR](#__RefHeading___Toc228976_1841740821)+ | [MULTR](#__RefHeading___Toc228976_1841740821)+ is an array of real positive numbers assigning the transmissibility multipliers in the +R direction to each cell face in the model.<br>Repeat counts may be used, for example 20\*100.0. | 1.0 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.74: MULTR Keyword Description

See also the [MULTR-](#__RefHeading___Toc80285_17781729792), [MULTTHT](#__RefHeading___Toc270099_1841740821), [MULTTHT-](#__RefHeading___Toc80285_177817297921), [MULTZ](#__RefHeading___Toc80291_1778172979) and [MULTZ-](#__RefHeading___Toc80293_1778172979) keywords for scaling transmissible between between grid cells in the R direction.

#### Example

\--

\-- DEFINE INPUT BOX FOR EDITING INPUT ARRAYS

\--

\-- \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

BOX

10 10 1 6 1 3 / DEFINE BOX AREA

\--

\-- SET MULTR+ TRANSMISSIBILITY MULTIPLIERS

\--

MULTR

18\*0.300 /

\--

\-- DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS

\--

ENDBOX

The above example defines a 0.3 scaling multiplier for the 18 cells defined by the preceding [BOX](#__RefHeading___Toc42110_3671211675) statement. The [ENDBOX](#__RefHeading___Toc88719_1778172979) keyword resets the input box to the full grid.
