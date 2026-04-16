### NUMRES -- Define the Number of Reservoir Grids

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [NUMRES](#__RefHeading___Toc81021_4106839650) keyword defines the number of reservoir grids ([COORD](#__RefHeading___Toc45757_719036256) data sets) that the simulator should process. OPM Flow currently only supports a single reservoir grid.

+-------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > No.                                     | > Name   | > Description                                                                                                                      | > Default |
+-------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 1                                       | > NUMRES | > A positive integer that defines the number of [COORD](#__RefHeading___Toc45757_719036256) data sets to be processed by OPM Flow. | > 1       |
|                                           |          |                                                                                                                                    |           |
|                                           |          | > OPM Flow currently only supports a single reservoir grid and so this item should be defaulted (1\*) or set to one.               |           |
+-------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Notes:                                  |          |                                                                                                                                    |           |
|                                           |          |                                                                                                                                    |           |
| 1)  The keyword is terminated by a "/".   |          |                                                                                                                                    |           |
+-------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------+-----------+

Table 5.30: NUMRES Keyword Description

#### Example

\--

\-- DEFINE THE NUMBER OF RESERVOIR GRIDS (COORD DATA SETS)

\--

NUMRES

1 /

The above example sets the maximum number of [COORD](#__RefHeading___Toc45757_719036256) data sets to be processed to one.
