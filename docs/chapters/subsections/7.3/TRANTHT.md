### TRANTHT -- Define the Transmissibility in the +Theta Direction for All the Cells

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[TRANTHT](#__RefHeading___Toc1306690_4250154414) defines the transmissibility in the +Theta direction for all the cells in the model via an array. The keyword can only be used with Radial Grid geometry grids. The keyword effectively overwrites previously entered and calculated data. The transmissibility overwritten is the +Theta face transmissibility of each grid block, that is for cell (I, J, K) the transmissibility between cells (I, J, K) and (I, J+1, K).

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [TRANTHT](#__RefHeading___Toc1306690_4250154414) | [TRANTHT](#__RefHeading___Toc1306690_4250154414) is an array of real positive numbers assigning the transmissibility in the +Theta direction to each cell in the model.<br>Repeat counts may be used, for example 20\*100.0. | None |
| cP.rb/day/psia | cP.rm^3^/day/bars | cP.rcc/hr/atm |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  Values not reset by this keyword remain unaltered.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 7.8: [TRANR](#__RefHeading___Toc1306688_4250154414) Keyword Description

See also the [TRANR](#__RefHeading___Toc1306688_4250154414) and TRANYZ keywords to modify the transmissibilities in the other directions.

#### Example

\--

\-- DEFINE INPUT BOX FOR EDITING INPUT ARRAYS

\--

\-- \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

BOX

10 10 1 6 1 3 / DEFINE BOX AREA

\--

\-- SET TRANTHT TRANSMISSIBILITY

\--

TRANTHT

18\*0.00 /

\--

\-- DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS

\--

ENDBOX

Here the [BOX](#__RefHeading___Toc42110_3671211675) statement is used to define the input grid for the [TRANTHT](#__RefHeading___Toc1306690_4250154414) keyword, which overwrites the transmissibility previously calculated with transmissibility values of zero, resulting in a no-flow boundary in that part of the grid. The [ENDBOX](#__RefHeading___Toc88719_1778172979) keyword resets the input box to the full grid.
