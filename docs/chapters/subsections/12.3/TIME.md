### TIME -- Advance Simulation by Cumulative Reporting Time

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword advances the simulation to a given cumulative report time after which additional keywords may be entered to instruct OPM Flow to perform additional functions via the SCHEDULE section keywords, or further TIME keywords may be entered to advance the simulator to the next report time.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | TIME | A vector of real positive numbers that define the cumulative length of the of report times. | None |
| days | days | hours |  |
| Notes:<br>1)  The keyword is followed by a vector of numbers separated by a space and the keyword is terminated by a "/". |  |  |  |

*Table 12.64: TIME Keyword Description*
See also the DATES and TSTEP keyword in the SCHEDULE section. Note that since OPM Flow uses the standard Gregorian calendar and therefore leap years are accounted for in the DATES keyword. Thus, it is more accurate to use the DATES keyword to progress the simulator through time if one is matching actual production data.

Whenever possible it is a good idea to always set the start date to be at the beginning of the year, as like most simulators, OPM Flow reports are always stated at the number of days from the start date (and sometimes at a given date). If the start date is at the beginning of the year, then calculating the actual date is relatively straight forward and simple.

#### Examples

The fist example shows how to advance the simulation three years using the TIME keyword, from the given start date of January 1, 2022 set via the START keyword in the RUNSPEC section.

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

The second example shows the same advance but using the TSTEP keyword instead.

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

Again, if the simulated production targets are actual production data or the results are going to be used in economic evaluations then the DATES keyword may be more useful in advancing the simulation via the reporting time steps, as the exact dates will be honored.
