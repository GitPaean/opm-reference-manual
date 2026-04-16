### TIME -- Advance Simulation by Cumulative Reporting Time

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword advances the simulation to a given cumulative report time after which additional keywords may be entered to instruct OPM Flow to perform additional functions via the [SCHEDULE](#__RefHeading___Toc43945_784232322) section keywords, or further [TIME](#__RefHeading___Toc1252966_4250154414) keywords may be entered to advance the simulator to the next report time.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
| > No.                                                                                                             | > Name                                          | > Description                                                                                 | > Default |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
| > Field                                                                                                           | > Metric                                        | > Laboratory                                                                                  |           |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
| > 1                                                                                                               | > [TIME](#__RefHeading___Toc1252966_4250154414) | > A vector of real positive numbers that define the cumulative length of the of report times. | > None    |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
| > days                                                                                                            | > days                                          | > hours                                                                                       |           |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
| > Notes:                                                                                                          |                                                 |                                                                                               |           |
|                                                                                                                   |                                                 |                                                                                               |           |
| 1)  The keyword is followed by a vector of numbers separated by a space and the keyword is terminated by a "/".   |                                                 |                                                                                               |           |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+

::: caption
Table 12.64: TIME Keyword Description
:::

See also the [DATES](#__RefHeading___Toc117621_2179381650) and [TSTEP](#__RefHeading___Toc118323_1596574740) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. Note that since OPM Flow uses the standard Gregorian calendar and therefore leap years are accounted for in the [DATES](#__RefHeading___Toc117621_2179381650) keyword. Thus, it is more accurate to use the [DATES](#__RefHeading___Toc117621_2179381650) keyword to progress the simulator through time if one is matching actual production data.

Whenever possible it is a good idea to always set the start date to be at the beginning of the year, as like most simulators, OPM Flow reports are always stated at the number of days from the start date (and sometimes at a given date). If the start date is at the beginning of the year, then calculating the actual date is relatively straight forward and simple.

#### Examples

The fist example shows how to advance the simulation three years using the [TIME](#__RefHeading___Toc1252966_4250154414) keyword, from the given start date of January 1, 2022 set via the [START](#__RefHeading___Toc39156_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

\-- ==============================================================================

\--

\-- SCHEDULE SECTION

\--

\-- ==============================================================================

SCHEDULE

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\-- SCHEDULE SECTION - 2022-01-01

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\--

\-- ADVANCE SIMULATION BY REPORTING TIME

\--

TIME

365.25 730.50 1095.75

/

The second example shows the same advance but using the [TSTEP](#__RefHeading___Toc118323_1596574740) keyword instead.

\-- ==============================================================================

\--

\-- SCHEDULE SECTION

\--

\-- ==============================================================================

SCHEDULE

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\-- SCHEDULE SECTION - 2022-01-01

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

RPTSCHED

\'WELLS=2\' \'WELSPECS\' \'CPU=2\' FIP=2\' /

\--

\-- ADVANCE SIMULATION BY REPORTING TIME

\--

TSTEP

3\*365.25

/

Again, if the simulated production targets are actual production data or the results are going to be used in economic evaluations then the [DATES](#__RefHeading___Toc117621_2179381650) keyword may be more useful in advancing the simulation via the reporting time steps, as the exact dates will be honored.
