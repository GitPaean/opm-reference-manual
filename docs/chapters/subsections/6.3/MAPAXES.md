### MAPAXES -- Define the Map Origin Input Data

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[MAPAXES](#__RefHeading___Toc39960_2479612490) specifies the origin of the map used to create the grid. It is usually output by pre-processing software when exporting the grid geometry. The data is not used by OPM Flow intrinsically, but is merely written to the output EGRID file, as specified by the [GRIDFILE](#__RefHeading___Toc45785_719036256) keyword, for the use of post-processing software like OPM ResInsight.

+-------------------------------------------+------------+---------------------------------------------------------------------------------+-----------+
| > No.                                     | > Name     | > Description                                                                   | > Default |
+-------------------------------------------+------------+---------------------------------------------------------------------------------+-----------+
| > Field                                   | > Metric   | > Laboratory                                                                    |           |
|                                           |            |                                                                                 |           |
| > (feet)                                  | > (metres) | > (metres)                                                                      |           |
+-------------------------------------------+------------+---------------------------------------------------------------------------------+-----------+
| > 1                                       | > X1       | > X1 is a real number that defines the x co-ordinate of a point on the y-axis.  | > None    |
+-------------------------------------------+------------+---------------------------------------------------------------------------------+-----------+
| > 2                                       | > Y1       | > Y1 is a real number that defines the y co-ordinate of a point on the y-axis.  | > None    |
+-------------------------------------------+------------+---------------------------------------------------------------------------------+-----------+
| > 3                                       | > X2       | > X2 is a real number that defines the x co-ordinate of the origin.             | > None    |
+-------------------------------------------+------------+---------------------------------------------------------------------------------+-----------+
| > 4                                       | > Y2       | > Y2 is a real number that defines the y co-ordinate of the origin.             | > None    |
+-------------------------------------------+------------+---------------------------------------------------------------------------------+-----------+
| > 5                                       | > X3       | > X3 is a real number that defines the x co-ordinate of a point on the x-axis.  | > None    |
+-------------------------------------------+------------+---------------------------------------------------------------------------------+-----------+
| > 6                                       | > Y3       | > Y3 is a real number that defines the y co-ordinate of a point on the x-axis.  | > None    |
+-------------------------------------------+------------+---------------------------------------------------------------------------------+-----------+
| > Notes:                                  |            |                                                                                 |           |
|                                           |            |                                                                                 |           |
| 1)  The keyword is terminated by a "/".   |            |                                                                                 |           |
+-------------------------------------------+------------+---------------------------------------------------------------------------------+-----------+

Table 6.58: MAPAXES Keyword Description

#### Example

\--

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- MAPAXES \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\-- X1 Y1 X2 Y2 X3 Y3

MAPAXES

0.0 100.0 0.0 0.0 100.0 0.0 /

The above example defines the map axes to be exported to the grid file for use by post-processing software.
