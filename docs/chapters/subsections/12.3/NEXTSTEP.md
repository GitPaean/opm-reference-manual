### NEXTSTEP -- Maximum Next Time Step Size

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the maximum time step size the simulator should take for the next time step. This keyword can be used to limit the time step size when known large changes to the model are taking place that may otherwise result in time step chops. For example, if the simulator is using monthly reporting steps defined by the DATES keyword in the SCHEDULE section, then if a group of wells start production at a given date, then the NEXTSTEP keyword can be used to limit the next time step in order to avoid a time step chop.

Time steps chops are computationally expensive as the simulator cannot solve the current time step at the given tolerance, and therefore has to reduce the time step size. For example, if the previous completed time step was at day 365 and the current time step ending at 396 days cannot be solved, then the simulator will reduce the current time step to perhaps end at day 370, if this still cannot solved then the time step will be chopped back again and so on, possibly reducing the time step to less then one day. Using the NEXT or NEXTSTEP keyword, the simulator is instructed to take a small time step in the anticipation that this will avoid time step chops and thus improve computational performance.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | NSTEP1 | A real positive value that defines the maximum length of the next time step. | None |
| days | days | hours |  |
| 2 | NSTEP2 | A defined character string that should be set to either NO or YES to state if the NSTEP1 should be applied to future reporting time steps.<br>1)  NO: Means that NSTEP1 should not be applied to subsequent reporting time steps.<br>2)  YES: Means that NSTEP1 should be applied to subsequent reporting time steps.<br>The default value of NO means that NSTEP1 will only be applied once. | NO |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 12.55: NEXTSTEP Keyword Description

See also the DATES and TSTEP keywords in the RUNSPEC section that are used to advance the simulation through time.

See section [Running OPM Flow From The Command Line](#running-opm-flow-from-the-command-line) on how to control time stepping for OPM Flow that allows for greater flexibility.

#### Examples

The first example shows the direct use of the NEXTSTEP keyword. Here the next time step size is limited to one day for the first time step following the next report time only.

\-- NEXT ALL

\-- STEP TIME

\-- \-\-\-- \-\-\--

NEXTSTEP

1 \'NO\' /

The next example shows a more complete use of the keyword for when the field oil production has increased dramatically from 10,000 stb/d to 50,000 stb/d as indicated by the two GCONPROD keywords.

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\-- SCHEDULE SECTION - 2021-01-01

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\--

\-- GROUP PRODUCTION CONTROLS

\--

\-- GRUP CNTL OIL WAT GAS LIQ CNTL GRUP GUIDE GUIDE CNTL

\-- NAME MODE RATE RATE RATE RATE OPT CNTL RATE DEF WAT

GCONPROD

\'FIELD\' \'ORAT\' 10E3 60E3 300E3 60E3 1\* 1\* 1\* 1\* 1\* /

/

RPTSCHED

\'WELLS=2\' \'WELSPECS\' \'CPU=2\' \'FIP=2\' /

DATES

2 JAN 2021 /

/

RPTSCHED

\'NOTHING\' /

DATES

1 FEB 2021 /

1 MAR 2021 /

/

\-- GROUP PRODUCTION CONTROLS

\--

\-- GRUP CNTL OIL WAT GAS LIQ CNTL GRUP GUIDE GUIDE CNTL

\-- NAME MODE RATE RATE RATE RATE OPT CNTL RATE DEF WAT

GCONPROD

\'FIELD\' \'ORAT\' 50E3 90E3 300E3 90E3 1\* 1\* 1\* 1\* 1\* /

/

\--

\-- NEXT ALL

\-- STEP TIME

\-- \-\-\-- \-\-\--

NEXTSTEP

1 \'NO\' /

DATES

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

Given a start date of January 1, 2020 set via the START keyword in the RUNSPEC section, the above example shows the initial oil production of 10,000 stb/d starting in January 1, 2020, and continuing up to March 1, 2021. At the March 1, 2021 report time the field oil production rate is increased to 50,000 stb/d and the maximum next time step is set to one day. After the one day time step is completed (March 2, 2012), the simulator will progressively in increase the time step size until a maximum of 31 days is reached. The 31 day maximum is a result of requesting monthly time steps via the DATES keyword. The intent of using the NEXTSTEP keyword in this case is to prevent time step chops occurring due to the "shock" to the system caused by the large increase in oil production.
