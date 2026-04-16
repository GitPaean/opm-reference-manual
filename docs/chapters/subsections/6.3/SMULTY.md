### SMULTY -- Multiply Cell Transmissibility in the +Y Direction (Auto-Refinement)

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[SMULTY](#__RefHeading___Toc1275012_516898843) multiples the transmissibility between two cell faces in the +Y direction between cells in a host base grid and the connecting auto-refined grid cells, via an array, that is the keyword sets the transmissibility multiplier of block (Ihost, Jhost, Khost) in the host base grid, multiplies the transmissibility all the cells (Iauto, Jauto, Kauto) and (Iauto, J+1auto, Kauto) in the auto-refinement grid. The Auto Refinement option must be enabled to use this keyword via the [AUTOREF](#__RefHeading___Toc161695_1314821763) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

An alternative to defining the complete array is to use the [BOX](#__RefHeading___Toc42110_3671211675) keyword to define an area of the grid and then use the [SMULTY](#__RefHeading___Toc1275012_516898843) keyword to set the multipliers just for the area defined by the [BOX](#__RefHeading___Toc42110_3671211675) keyword (see the example).

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > No.                                                                                                                                                                                                                                                                                                                                                                                                                                                          | > Name                                            | > Description                                                                                                                                                                          | > Default |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 1                                                                                                                                                                                                                                                                                                                                                                                                                                                            | > [SMULTY](#__RefHeading___Toc1275012_516898843)+ | > [SMULTY](#__RefHeading___Toc1275012_516898843)+ is an array of real positive numbers assigning the transmissibility multipliers in the +X direction to each cell face in the model.  | > 1.0     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                   |                                                                                                                                                                                        |           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                   | > Repeat counts may be used, for example 20\*100.0.                                                                                                                                    |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Notes:                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                   |                                                                                                                                                                                        |           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                   |                                                                                                                                                                                        |           |
| 1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.   |                                                   |                                                                                                                                                                                        |           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                   |                                                                                                                                                                                        |           |
| 2)  The keyword is terminated by a "/".                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                   |                                                                                                                                                                                        |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Table 6.119: SMULTY Keyword Description

See also the [MULTX](#__RefHeading___Toc80283_1778172979), [MULTY](#__RefHeading___Toc80287_1778172979) and [MULTZ](#__RefHeading___Toc80291_1778172979) keywords for scaling transmissible between grid cells.

#### Example

\--

\-- DEFINE INPUT BOX FOR EDITING INPUT ARRAYS

\--

\-- \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

BOX

10 10 1 6 1 3 / DEFINE BOX AREA

\--

\-- SET SMULTY+ TRANSMISSIBILITY MULTIPLIERS

\--

SMULTY

18\*0.300 /

\--

\-- DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS

\--

ENDBOX

The above example defines a 0.3 scaling multiplier for the 18 cells defined by the preceding [BOX](#__RefHeading___Toc42110_3671211675) statement. The [ENDBOX](#__RefHeading___Toc88719_1778172979) keyword resets the input box to the full grid.
