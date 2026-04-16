### OPTIONS -- Activate Various Program Options

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [OPTIONS](#__RefHeading___Toc51266_1640804870) keyword activates various program options in the commercial simulator. Currently, none of the options available in the commercial simulator are implemented in OPM Flow, and it is unlikely that this keyword will be supported in the future releases of OPM Flow.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

+-------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > No.                                     | > Description                                                                                                                                                                                                                                                                                                | > Default |
+-------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 1 - 273                                 | > Commercial simulator options keyword, used to to switch on or off specific features. The keyword is commonly used to revert the simulator\'s behavior to past functionality that has been depreciated in the current version of the commercial simulator, for backward compatibility with previous models. | > 0       |
+-------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Notes:                                  |                                                                                                                                                                                                                                                                                                              |           |
|                                           |                                                                                                                                                                                                                                                                                                              |           |
| 1)  The keyword is terminated by a "/".   |                                                                                                                                                                                                                                                                                                              |           |
+-------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Table 5.32: OPTIONS Keyword Description

#### Examples

\--

\-- SKIP ACTIVATE

\-- OPTIONS OPTION

OPTIONS

77\*0 1 /

The above example activates the use of scratch files for pre-processing grid geometry data for non-neighbor connections. Note if multiple options are required then one can just repeat the format of the example to activate multiple options as the keyword does not overwrite previous entries. So for example:

\--

\-- SKIP ACTIVATE

\-- OPTIONS OPTION

OPTIONS

7\*0 1 /

\--

\-- SKIP ACTIVATE

\-- OPTIONS OPTION

OPTIONS

77\*0 1 /

\--

\-- SKIP ACTIVATE

\-- OPTIONS OPTION

OPTIONS

177\*0 1 /

Could be used to activate the 8, 78 and 178 options if they were available.
