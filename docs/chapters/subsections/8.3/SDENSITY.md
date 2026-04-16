### SDENSITY -- Define the Miscible or Solvent Surface Gas Density

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [SDENSITY](#__RefHeading___Toc121471_83452205) keyword defines density at surface conditions of either the miscible injection gas for when the [MISCIBLE](#__RefHeading___Toc61978_4106839650) option has been invoked in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, or the solvent for when the [SOLVENT](#__RefHeading___Toc62787_1778172979) option has been invoked in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. This keyword must be invoked if either the [MISCIBLE](#__RefHeading___Toc61978_4106839650) or [SOLVENT](#__RefHeading___Toc62787_1778172979) options have been activated in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > No.                                                                                                                                                                                 | > Name                                           | > Description                                                                                                                                                                            | > Default |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Field                                                                                                                                                                               | > Metric                                         | > Laboratory                                                                                                                                                                             |           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 1                                                                                                                                                                                   | > [SDENSITY](#__RefHeading___Toc121471_83452205) | > [SDENSITY](#__RefHeading___Toc121471_83452205) is a real positive number defining the density at surface conditions of either:                                                         | > None    |
|                                                                                                                                                                                       |                                                  |                                                                                                                                                                                          |           |
|                                                                                                                                                                                       |                                                  | 1)  the miscible injection gas for when the [MISCIBLE](#__RefHeading___Toc61978_4106839650) option has been invoked in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, or,   |           |
|                                                                                                                                                                                       |                                                  |                                                                                                                                                                                          |           |
|                                                                                                                                                                                       |                                                  | 2)  the solvent for when the [SOLVENT](#__RefHeading___Toc62787_1778172979) option has been invoked in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.                       |           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > lb/ft^3^                                                                                                                                                                            | > kg/m^3^                                        | > gm/cc                                                                                                                                                                                  |           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Notes:                                                                                                                                                                              |                                                  |                                                                                                                                                                                          |           |
|                                                                                                                                                                                       |                                                  |                                                                                                                                                                                          |           |
| 1)  The keyword is followed by NTPVT tables as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.   |                                                  |                                                                                                                                                                                          |           |
|                                                                                                                                                                                       |                                                  |                                                                                                                                                                                          |           |
| 2)  Each table is terminated by a "/" and there is no "/" terminator for the keyword.                                                                                                 |                                                  |                                                                                                                                                                                          |           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Table 8.145: SDENSITY Keyword Description

In addition to this keyword, the surface density or gravity of the in-place natural gas must be entered using either the [DENSITY](#__RefHeading___Toc45799_719036256) or [GRAVITY](#__RefHeading___Toc45801_719036256) keywords.

#### Examples

The following shows the [SDENSITY](#__RefHeading___Toc121471_83452205) keyword for when NTPVT on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section is set to one.

\--

\-- MIS-SOL

\-- DENSITY

\-- \-\-\-\-\-\--

SDENSITY

0.04520 / MIS-SOL DENSITY

The next example shows the [SDENSITY](#__RefHeading___Toc121471_83452205) keyword for when NTPVT on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section is set to three.

\--

\-- MIS-SOL

\-- DENSITY

\-- \-\-\-\-\-\--

SDENSITY

0.04520 / MIS-SOL DENSITY 1

0.05520 / MIS-SOL DENSITY 2

0.06420 / MIS-SOL DENSITY 3

There is no terminating "/" for this keyword.
