### MULTPV -- Multiply Cell Pore Volumes by a Constant

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[MULTPV](#__RefHeading___Toc95300_3218818441) multiples the pore volumes of a cell by a real positive constant for all the cells in the model via an array. An alternative to defining the complete array is to use the [BOX](#__RefHeading___Toc42110_3671211675) keyword to define an area of the grid and then use the [MULTPV](#__RefHeading___Toc95300_3218818441) keyword to set the multipliers just for the area defined by the [BOX](#__RefHeading___Toc42110_3671211675) keyword (see the example).

The keyword can be used for all grid types, except for the Radial Grid geometry.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | [MULTPV](#__RefHeading___Toc95300_3218818441) | [MULTPV](#__RefHeading___Toc95300_3218818441) is an array of real positive numbers assigning the pore volume multipliers for each cell in the model.<br>Repeat counts may be used, for example 20\*100.0. | 1.0 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.73: MULTPV Keyword Description

See also the [MULTREGP](#__RefHeading___Toc296617_1576177388) keyword for scaling the cell pore volumes by region numbers.

#### Example

\--

\-- DEFINE INPUT BOX FOR EDITING INPUT ARRAYS

\--

\-- \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

BOX

10 10 1 6 1 3 / DEFINE BOX AREA

\--

\-- SET PORE VOLUME MULTIPLIERS

\--

MULTPV

18\*0.0500 /

\--

\-- DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS

\--

ENDBOX

The above example defines a 0.05 scaling multiplier for the 18 cells defined by the preceding [BOX](#__RefHeading___Toc42110_3671211675) statement. The [ENDBOX](#__RefHeading___Toc88719_1778172979) keyword resets the input box to the full grid.
