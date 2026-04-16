### SMRYDIMS -- Define Maximum Number of Summary Vectors to be Written

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [SMRYDIMS](#__RefHeading___Toc61766_1778172979) keyword defines the maximum number of summary vectors to be written out to the [SUMMARY](#__RefHeading___Toc43949_784232322) file (\*.SUMMARY).

OPM Flow uses dynamic memory allocation and therefore the keyword has no effect and is ignored by the simulator, but is documented here for completeness.

+-------------------------------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > No.                                     | > Name   | > Description                                                                                                                                                     | > Default |
+-------------------------------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 1                                       | > NSUMMX | > A positive integer that defines the maximum number of summary vectors to be written out to the [SUMMARY](#__RefHeading___Toc43949_784232322) file (\*.SUMMARY). | > 10000   |
+-------------------------------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Notes:                                  |          |                                                                                                                                                                   |           |
|                                           |          |                                                                                                                                                                   |           |
| 1)  The keyword is terminated by a "/".   |          |                                                                                                                                                                   |           |
+-------------------------------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Table 5.42: SMRYDIMS Keyword Description

#### Example

\--

\-- SET THE MAXIMUM NUMBER OF SUMMARY VECTORS THAT CAN BE WRITTEN OUT

\--

SMRYDIMS

10000 /

The above example sets maximum number of summary vectors that can be written out to the [SUMMARY](#__RefHeading___Toc43949_784232322) file to the default value of 10,000; however, this has no effect in OPM Flow input decks.
