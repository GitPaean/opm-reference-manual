### MULTX- -- Multiply Cell Transmissibility in the -X Direction

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[MULTX-](#__RefHeading___Toc80285_1778172979) multiples the transmissibility between two cell faces in the -X direction for all the cells in the model via an array, that is the keyword sets the transmissibility multiplier of block (I, J, K) between the cells (I-1, J, K) and (I, J, K). An alternative to defining the complete array is to use the [BOX](#__RefHeading___Toc42110_3671211675) keyword to define an area of the grid and then use the [MULTX-](#__RefHeading___Toc80285_1778172979) keyword to set the multipliers just for the area defined by the [BOX](#__RefHeading___Toc42110_3671211675) keyword (see the example).

The keyword can be used for all grid types, except for the Radial Grid geometry.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > No.                                                                                                                                                                                                                                                                                                                                                                                                                                                          | > Name                                          | > Description                                                                                                                                                                        | > Default |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 1                                                                                                                                                                                                                                                                                                                                                                                                                                                            | > [MULTX-](#__RefHeading___Toc80285_1778172979) | > [MULTX-](#__RefHeading___Toc80285_1778172979) is an array of real positive numbers assigning the transmissibility multipliers in the -X direction to each cell face in the model.  | > 1.0     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                 |                                                                                                                                                                                      |           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                 | > Repeat counts may be used, for example 20\*100.0.                                                                                                                                  |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Notes:                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                 |                                                                                                                                                                                      |           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                 |                                                                                                                                                                                      |           |
| 1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.   |                                                 |                                                                                                                                                                                      |           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                 |                                                                                                                                                                                      |           |
| 2)  The keyword is terminated by a "/".                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                 |                                                                                                                                                                                      |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Table 6.83: MULTX- Keyword Description

Note that OPM Flow does not require the [GRIDOPTS](#__RefHeading___Toc45741_719036256)(TRANMULT) parameter in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section to be set to YES, in order to use this and other negative directional dependent multiplier keywords in the input deck. Whereas, the commercial simulator will terminate with an error if the keyword is present, and the [GRIDOPTS](#__RefHeading___Toc45741_719036256)(TRANMULT) parameter has not been set to YES.

See also the [MULTX](#__RefHeading___Toc80283_1778172979), [MULTY](#__RefHeading___Toc80287_1778172979), [MULTY-](#__RefHeading___Toc80289_1778172979), [MULTZ](#__RefHeading___Toc80291_1778172979) and [MULTZ-](#__RefHeading___Toc80293_1778172979) keywords for scaling transmissible between grid cells.

#### Example

\--

\-- DEFINE INPUT BOX FOR EDITING INPUT ARRAYS

\--

\-- \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

BOX

10 10 1 6 1 1 / DEFINE BOX AREA

\--

\-- SET MULTX- TRANSMISSIBILITY MULTIPLIERS

\--

MULTX-

6\*0.500 /

\--

\-- DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS

\--

ENDBOX

The above example defines a 0.5 scaling multiplier for the six cells defined by the preceding [BOX](#__RefHeading___Toc42110_3671211675) statement. The [ENDBOX](#__RefHeading___Toc88719_1778172979) keyword resets the input box to the full grid.
