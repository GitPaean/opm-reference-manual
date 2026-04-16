### SUMTHIN -- Define SUMMARY Data Reporting Time Steps

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword defines a time interval for writing out the [SUMMARY](#__RefHeading___Toc43949_784232322) data to the [SUMMARY](#__RefHeading___Toc43949_784232322) file and the RSM file, if the [RUNSUM](#__RefHeading___Toc210156_2884651453) keyword has also been activated in the [SUMMARY](#__RefHeading___Toc43949_784232322) section. Only the data for the first time step in the time interval is written out and the other time steps are skipped until the next time interval, except for report time steps. Note that report time steps data are always written out regardless of the setting on this keyword. This enables the size of the [SUMMARY](#__RefHeading___Toc43949_784232322) files to be reduced depending on the size of the time interval. However, the keyword will produce irregular time steps reports of the [SUMMARY](#__RefHeading___Toc43949_784232322) data.

+-------------------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > No.                                     | > Name    | > Description                                                                                                                                                                                                                                         | > Default |
+-------------------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Field                                   | > Metric  | > Laboratory                                                                                                                                                                                                                                          |           |
+-------------------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 1                                       | > SUMSTEP | > SUMSTEP is a real positive number that defines the time interval for which the first time step of data will be written to the [SUMMARY](#__RefHeading___Toc43949_784232322) file (and the RSM file if RSM output has been activated).               | > None    |
|                                           |           |                                                                                                                                                                                                                                                       |           |
|                                           |           | > For example, if SUMSTEP is set to 30 days, and if the simulator takes time steps of 0, 5, 10, 16, 24, 30, 40, 45, 60, 90 days. Then the [SUMMARY](#__RefHeading___Toc43949_784232322) data will be written out at time steps 0, 30, 40 and 60 days. |           |
+-------------------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > days                                    | > days    | > hours                                                                                                                                                                                                                                               |           |
+-------------------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Notes:                                  |           |                                                                                                                                                                                                                                                       |           |
|                                           |           |                                                                                                                                                                                                                                                       |           |
| 1)  The keyword is terminated by a "/".   |           |                                                                                                                                                                                                                                                       |           |
+-------------------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Table 11.33: SUMTHIN Keyword Description

See also the [RPTONLY](#__RefHeading___Toc210150_2884651453) keyword in the [SUMMARY](#__RefHeading___Toc43949_784232322) section that forces the [SUMMARY](#__RefHeading___Toc43949_784232322) data to be only written out at report time steps, as oppose to all time steps or SUMSTEP time intervals.

#### Example

\--

\-- DEFINE SUMMARY DATA REPORTING TIME STEP INTERVAL

\--

\-- SUMSTEP

SUMTHIN

30.0 / /

The above example defines the [SUMMARY](#__RefHeading___Toc43949_784232322) file time step interval to be 30 days for both field and metric units.
