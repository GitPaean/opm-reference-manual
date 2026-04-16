### MAPUNITS -- Define the Map Axes Units

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [MAPUNITS](#__RefHeading___Toc39962_2479612490) keyword defines the units of the coordinates stated on the [MAPAXES](#__RefHeading___Toc39960_2479612490) keyword. It is usually output by pre-processing software when exporting the grid geometry. The data is not used by OPM Flow intrinsically, but is merely written to the output EGRID file, as specified by the [GRIDFILE](#__RefHeading___Toc45785_719036256) keyword, for the use of post-processing software like OPM ResInsight.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

+----------------------------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > No.                                                                            | > Name                                            | > Description                                                                                                                                              | > Default |
+----------------------------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 1                                                                              | > [MAPUNITS](#__RefHeading___Toc39962_2479612490) | > A character string that defines the units of the coordinates stated on the [MAPAXES](#__RefHeading___Toc39960_2479612490) keyword, and should be set to: | > METRES  |
|                                                                                  |                                                   |                                                                                                                                                            |           |
|                                                                                  |                                                   | 1)  FEET for field units                                                                                                                                   |           |
|                                                                                  |                                                   |                                                                                                                                                            |           |
|                                                                                  |                                                   | 2)  METRES for metric units, or                                                                                                                            |           |
|                                                                                  |                                                   |                                                                                                                                                            |           |
|                                                                                  |                                                   | 3)  CM for laboratory units                                                                                                                                |           |
+----------------------------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Notes:                                                                         |                                                   |                                                                                                                                                            |           |
|                                                                                  |                                                   |                                                                                                                                                            |           |
| 1)  Note the alternative spelling of METRES, that is METERS is not recognized.   |                                                   |                                                                                                                                                            |           |
|                                                                                  |                                                   |                                                                                                                                                            |           |
| 2)  The keyword is terminated by a "/".                                          |                                                   |                                                                                                                                                            |           |
+----------------------------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Table 6.59: MAPUNITS Keyword Description

#### Example

\--

\-- SET THE MAP UNITS FOR THE MAPAXES KEYWORD

MAPUNITS

METRES /

The above example specifies the units on the [MAPAXES](#__RefHeading___Toc39960_2479612490) to be the default METRES.
