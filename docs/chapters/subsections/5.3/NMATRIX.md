### NMATRIX -- Activate the Discretized Matrix Dual Porosity Option

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [NMATRIX](#__RefHeading___Toc244469_718033703) keyword activates the Discretized Matrix Dual Porosity option and specifies the number of sub-grid blocks in the actual matrix grid blocks. See also the NMATOPS keyword in the [GRID](#__RefHeading___Toc38674_784232322) section that defines various parameters for this option.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

+-------------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------+
| > No.                                     | > Name                                           | > Description                                                                                             | > Default |
+-------------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------+
| > 1                                       | > [NMATRIX](#__RefHeading___Toc244469_718033703) | > A positive integer value that specifies the number of sub-grid blocks in the actual matrix grid blocks. | > 1       |
+-------------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------+
| > Notes:                                  |                                                  |                                                                                                           |           |
|                                           |                                                  |                                                                                                           |           |
| 1)  The keyword is terminated by a "/".   |                                                  |                                                                                                           |           |
+-------------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------+

Table 5.26: NMATRIX Keyword Description

Note the keyword cannot be used in conjunction with the [TRPLPORO](#__RefHeading___Toc1613912_4250154414) keyword, which is also in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

#### Example

\--

\-- SUB-GRIDS

\-- NMATRIX

NMATRIX

4 /

The above example activates the Discretized Matrix Dual Porosity option and specifies the number of sub-grid blocks in the actual matrix grid block to be four.
