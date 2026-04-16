### DATES -- Advance Simulation by Reporting Date

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword advances the simulation to a given report date after which additional keywords may be entered to instruct OPM Flow to perform additional functions via the [SCHEDULE](#__RefHeading___Toc43945_784232322) section keywords, or further [DATES](#__RefHeading___Toc117621_2179381650) data sets or keywords may be entered to advance the simulator to the next report date.

If the [DATES](#__RefHeading___Toc117621_2179381650) keyword is to be used during the simulation, then the [START](#__RefHeading___Toc39156_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section must be declared to set the start date for the run.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | DAY | A positive integer that defines the day of the month for the data set, the value should be greater than or equal to one and less than or equal to 31. | None |
| 2 | MONTH | Character string for the month for the data set and should be one of the following \'JAN\', \'FEB\', \'MAR\', \'APR\', \'MAY\', \'JUN\', \'JUL\' (or \'JLY\'), \'AUG\', \'SEP\', \'OCT\', \'NOV\', or \'DEC\' | None |
| 3 | YEAR | A positive four digit integer value representing the year for the data set, which must be specified fully by four digits, that is 1986. | None |
| 4 | [TIME](#__RefHeading___Toc1252966_4250154414) | A numeric character string that defines the time for the data set in the form of:<br>HH:MM:SS.SSSS<br>The default value means in most cases this parameter can be defaulted. [TIME](#__RefHeading___Toc1252966_4250154414) is normally used when detailed DST matching is performed to enable the pressures and rates to be stated at specific dates and times. | 00:00:00 |
| Notes:<br>1)  The keyword is followed by a number of data sets (or rows) representing one [DATE](#__RefHeading___Toc210146_2884651453) record per row.<br>2)  Each record (or row) is terminated by a "/" and the keyword is terminated by a "/". |  |  |  |

*Table 12.19: DATES Keyword Description*
Note that OPM Flow uses the standard Gregorian calendar and therefore leap years are accounted for in the [DATES](#__RefHeading___Toc117621_2179381650) keyword. Thus, it is more accurate to use the [DATES](#__RefHeading___Toc117621_2179381650) keyword to progress the simulator through time if one is matching actual production data.

See also the [TIME](#__RefHeading___Toc1252966_4250154414) and [TSTEP](#__RefHeading___Toc118323_1596574740) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

Whenever possible it is a good idea to always set the start date to be at the beginning of the year, as like most simulators, OPM Flow reports are always stated at the number of days from the start date (and sometimes at a given date). If the start date is at the beginning of the year, then calculating the actual date is relatively straight forward and simple.

#### Examples

Given a start date of January 1, 2020 set via the [START](#__RefHeading___Toc39156_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, the following example advances the simulator from the start date of January 1, 2020 to January 1, 2021, using quarterly reporting time steps.

\-- ==============================================================================

\--

\-- SCHEDULE SECTION

\--

\-- ==============================================================================

SCHEDULE

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\-- SCHEDULE SECTION - 2020-01-01

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

RPTSCHED

\'WELLS=2\' \'WELSPECS\' \'CPU=2\' FIP=2\' /

DATES

2 JAN 2020 /

/

RPTSCHED

\'NOTHING\' /

DATES

1 APR 2020 /

1 JLY 2020 /

1 OCT 2020 /

/

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\-- SCHEDULE SECTION - 2021-01-01

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

RPTSCHED

\'WELLS=2\' \'WELSPECS\' \'CPU=2\' FIP=2\' /

DATES

1 JAN 2021 /

/

RPTSCHED

\'NOTHING\' /

DATES

1 APR 2021 /

1 JLY 2021 /

1 OCT 2021 /

/

The above example writes out a series of report at the start of the run and then advances the simulation one day to January 2, 2020 and switches off the reporting. The simulation then advances to April 1, July 1 and October 1, 2020 with no further changes to the run. After October 1, 2020 reporting is switched on again to enable a report on January 1, 2021, which is then subsequently switched off after the January 1, 2021 report time step has been completed.

Note if one wishes to terminate the run at the end of year (as opposes to the beginning of the year and get a final report for the year, then the next example demonstrates the keyword sequence to enable this.

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\-- SCHEDULE SECTION - 2021-01-01

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

RPTSCHED

\'WELLS=2\' \'WELSPECS\' \'CPU=2\' FIP=2\' /

DATES

2 JAN 2021 /

/

RPTSCHED

\'NOTHING\' /

DATES

1 FEB 2021 /

1 MAR 2021 /

1 APR 2021 /

1 MAY 2021 /

1 JUN 2021 /

1 JLY 2021 /

1 AUG 2021 /

1 SEP 2021 /

1 OCT 2021 /

1 NOV 2021 /

1 DEC 2021 /

/

\--

\-- FINAL REPORT AND RESTART AT YEAR END

\--

RPTSCHED

\'WELLS=2\' \'WELSPECS\' \'CPU=2\' FIP=2\' /

RPTRST

\'BASIC=2\' /

DATES

31 DEC 2021 /

/

In the above example monthly reporting time steps have been used instead of quarterly and report is requested after the December 1, 2021 time step and is therefore written out on December 31, 2021.
