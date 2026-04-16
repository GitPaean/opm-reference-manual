### FILEUNIT -- Activate Unit Consistency Checking

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [FILEUNIT](#__RefHeading___Toc160788_1371377330) keyword defines the units of the data set, and is used to verify that the units in the input deck and any associated include files are consistent. The keyword does not provide for the conversion between different sets of units.

+-------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------+-----------+
| > No.                                     | > Name                                             | > Description                                                                      | > Default |
+-------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------+-----------+
| > 1                                       | > [FILEUNIT](#__RefHeading___Toc160788_1371377330) | > A character string that defines the units of the data set, and should be set to: | > None    |
|                                           |                                                    |                                                                                    |           |
|                                           |                                                    | 1)  [FIELD](#__RefHeading___Toc71850_2267116897) for field units,                  |           |
|                                           |                                                    |                                                                                    |           |
|                                           |                                                    | 2)  [METRIC](#__RefHeading___Toc70639_2267116897) for metric units, or             |           |
|                                           |                                                    |                                                                                    |           |
|                                           |                                                    | 3)  [LAB](#__RefHeading___Toc72458_2267116897) for laboratory units                |           |
+-------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------+-----------+
| > Notes:                                  |                                                    |                                                                                    |           |
|                                           |                                                    |                                                                                    |           |
| 1)  No unit conversion is performed.      |                                                    |                                                                                    |           |
|                                           |                                                    |                                                                                    |           |
| 2)  The keyword is terminated by a "/".   |                                                    |                                                                                    |           |
+-------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------+-----------+

Table 6.38: FILEUNIT Keyword Description

OPM Flow\'s behavior is controllable through the \"UNIT_SYSTEM_MISMATCH\" environment variable. The default behavior if the check fails (i.e., if one of the [INCLUDE](#__RefHeading___Toc55749_2479612490) files has a unit system different from the main run specification) is to terminate the simulation with an error.

#### Example

\--

\-- ACTIVATE UNIT CONSISTENCY CHECKING

\--

FILEUNIT

FIELD /

The above example defines the data set units to be [FIELD](#__RefHeading___Toc71850_2267116897) units.
