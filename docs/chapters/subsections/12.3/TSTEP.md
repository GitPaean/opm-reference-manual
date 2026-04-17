### TSTEP -- Advance Simulation by Reporting Time

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword advances the simulation to a given report time after which additional keywords may be entered to instruct OPM Flow to perform additional functions via the SCHEDULE section keywords, or further TSTEP keywords may be entered to advance the simulator to the next report time.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | TSTEP | A vector of real positive numbers that define the length of the time intervals to subsequent report steps.<br>Repeat counts may be used, for example 10\*365.25. | None |
| days | days | hours |  |
| Notes:<br>1)  The keyword is followed by a vector of numbers separated by a space and the keyword is terminated by a "/". |  |  |  |

*Table 12.65: TSTEP Keyword Description*
See also the DATES and TIME keywords in the SCHEDULE section. Note that since OPM Flow uses the standard Gregorian calendar and therefore leap years are accounted for in the DATES keyword. Thus, it is more accurate to use the DATES keyword to progress the simulator through time if one is matching actual production data.

Whenever possible it is a good idea to always set the start date to be at the beginning of the year, as like most simulators, OPM Flow reports are always stated at the number of days from the start date (and sometimes at a given date). If the start date is at the beginning of the year, then calculating the actual date is relatively straight forward and simple.

#### Examples

The first example shows how to advance the simulation via the reporting time steps from the given start date of January 1, 2022 set via the START keyword in the RUNSPEC section, to the next year, without any actions or reporting taking place.

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

Again, if the simulated production targets are actual production data or the results are going to be used in economic evaluations then the DATES keyword may be more useful in advancing the simulation via the reporting time steps, as the exact dates will be honored.
