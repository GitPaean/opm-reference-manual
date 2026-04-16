### TRPLPORO -- Activate the Triple Porosity Model Option

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [TRPLPORO](#__RefHeading___Toc1613912_4250154414) keyword activates the Triple Porosity Model option that models matrix, fractures and vuggy porosity for carbonate reservoirs, and specifies the number of matrix porosity systems

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

+-------------------------------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > No.                                     | > Name     | > Description                                                                                                                                                       | > Default |
+-------------------------------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 1                                       | > TRPLPORO | > A positive integer value that specifies the number of matrix porosity systems in the model. TRPLPORO should be set to either:                                     | > 1       |
|                                           |            |                                                                                                                                                                     |           |
|                                           |            | 1)  TRPLPORO set equal to 2, if the vugs are only connected to the fractures, so that the porosity system is matrix and connected vugs, or,                         |           |
|                                           |            |                                                                                                                                                                     |           |
|                                           |            | 2)  TRPLPORO set equal to 3, if the vugs are connected to the fractures and the matrix, so that the porosity system is matrix, connected vugs, and isolated vugs.   |           |
+-------------------------------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Notes:                                  |            |                                                                                                                                                                     |           |
|                                           |            |                                                                                                                                                                     |           |
| 1)  The keyword is terminated by a "/".   |            |                                                                                                                                                                     |           |
+-------------------------------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Table 5.49: TRPLPORO Keyword Description

Note the keyword cannot be used in conjunction with the [NMATRIX](#__RefHeading___Toc244469_718033703) keyword, which is also in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

#### Example

\--

\-- TRPLPORO

\-- OPTION

TRPLPORO

3 /

The above example activates the Triple Porosity Model option and specifies the porosity system is matrix, connected vugs, and isolated vugs.
