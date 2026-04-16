### RPTPROPS -- Define PROPS Section Reporting

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword defines the data in the [PROPS](#__RefHeading___Toc39329_784232322) section that is to be printed to the output print file in human readable format. The keyword has two distinct forms, the first of which consists of the keyword followed by a series of integers on the next line indicating the data to be printed (see the first example). This is the original formal in the commercial simulator and was subsequently superseded by the second format. The second format consists of the keyword followed by a series of character strings that indicate the data to be printed. In most cases the character string is the keyword used to load the data in the OPM Flow input deck, for example [PVDG](#__RefHeading___Toc104056_57619843) for the dry gas PVT tables. Its is anticipated that OPM Flow will eventually support the functionality of the second format only, the first format although recognized will be completely ignored.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

+-------------------------------------------+-----------------------------------------------+---------------------------------------------------------------+-----------+
| > No.                                     | > Name                                        | > Description                                                 | > Default |
+-------------------------------------------+-----------------------------------------------+---------------------------------------------------------------+-----------+
| > 1                                       | > [PVDG](#__RefHeading___Toc104056_57619843)  | > Print dry gas PVT tables                                    | > N/A     |
+-------------------------------------------+-----------------------------------------------+---------------------------------------------------------------+-----------+
| > 2                                       | > [PVTG](#__RefHeading___Toc104060_57619843)  | > Print wet gas PVT tables                                    | > N/A     |
+-------------------------------------------+-----------------------------------------------+---------------------------------------------------------------+-----------+
| > 3                                       | > [SGFN](#__RefHeading___Toc106868_335817223) | > Print gas relative permeability saturation function tables. | > N/A     |
+-------------------------------------------+-----------------------------------------------+---------------------------------------------------------------+-----------+
| > 4                                       | > [SGL](#__RefHeading___Toc22881_784232322)   | > Print connate gas saturation array.                         | > N/A     |
+-------------------------------------------+-----------------------------------------------+---------------------------------------------------------------+-----------+
| > ....                                    |                                               | > ....                                                        | > N/A     |
+-------------------------------------------+-----------------------------------------------+---------------------------------------------------------------+-----------+
| > Notes:                                  |                                               |                                                               |           |
|                                           |                                               |                                                               |           |
| 1)  The keyword is terminated by a "/".   |                                               |                                                               |           |
+-------------------------------------------+-----------------------------------------------+---------------------------------------------------------------+-----------+

Table 8.132: RPTPROPS Keyword Description

#### Examples

The first example shows the original format of this keyword; although the keyword and format are recognized by OPM Flow, the format is ignored and is unlikely to be implemented in in the simulator.

\--

\-- DEFINE PROPS SECTION REPORT OPTION (ORIGINAL FORMAT)

--

RPTPROPS

1 2\*0 1 3\*1 /

The next example shows the second format of the keyword which may be supported in a future release of OPM Flow.

\--

\-- DEFINE PROPS SECTION REPORT OPTIONS

\--

RPTPROPS

PVDO SOF2 SGFN SWFN /
