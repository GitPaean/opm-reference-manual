### TSTEP -- Advance Simulation by Reporting Time

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword advances the simulation to a given report time after which additional keywords may be entered to instruct OPM Flow to perform additional functions via the [SCHEDULE](#__RefHeading___Toc43945_784232322) section keywords, or further [TSTEP](#__RefHeading___Toc118323_1596574740) keywords may be entered to advance the simulator to the next report time.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [TSTEP](#__RefHeading___Toc118323_1596574740) | A vector of real positive numbers that define the length of the time intervals to subsequent report steps.<br>Repeat counts may be used, for example 10\*365.25. | None |
| days | days | hours |  |
| Notes:<br>1)  The keyword is followed by a vector of numbers separated by a space and the keyword is terminated by a "/". |  |  |  |

*Table 12.65: TSTEP Keyword Description*
See also the [DATES](#__RefHeading___Toc117621_2179381650) and [TIME](#__RefHeading___Toc1252966_4250154414) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. Note that since OPM Flow uses the standard Gregorian calendar and therefore leap years are accounted for in the [DATES](#__RefHeading___Toc117621_2179381650) keyword. Thus, it is more accurate to use the [DATES](#__RefHeading___Toc117621_2179381650) keyword to progress the simulator through time if one is matching actual production data.

Whenever possible it is a good idea to always set the start date to be at the beginning of the year, as like most simulators, OPM Flow reports are always stated at the number of days from the start date (and sometimes at a given date). If the start date is at the beginning of the year, then calculating the actual date is relatively straight forward and simple.

#### Examples

The first example shows how to advance the simulation via the reporting time steps from the given start date of January 1, 2022 set via the [START](#__RefHeading___Toc39156_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, to the next year, without any actions or reporting taking place.

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

\-- JAN FEB MAR APR MAY JUN JLY AUG SEP OCT NOV DEC

TSTEP

31 28 31 30 31 30 31 31 30 31 30 31

/

The second example is similar to the previous example but with quarterly reporting time steps used instead based on days per quarter

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

\-- QUARTERLY

TSTEP

4\*91.3125

/

Again, if the simulated production targets are actual production data or the results are going to be used in economic evaluations then the [DATES](#__RefHeading___Toc117621_2179381650) keyword may be more useful in advancing the simulation via the reporting time steps, as the exact dates will be honored.
