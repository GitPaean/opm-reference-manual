### NEXT -- Maximum Next Time Step Size (Alias for NEXTSTEP)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the maximum time step size the simulator should take for the next time step. This keyword can be used to reset the time step for when known large changes to the model are taking place that may result in time step chops. For example, if the reporting time size is using monthly reporting steps via the DATES keyword in the SCHEDULE section, then if for example, a group of wells start production at a given date, then the NEXT keyword can be used to shorten the next step in order to avoid a time step chop.

Time steps chops are computationally expensive as the simulator cannot solve the current time step at the given tolerance, and therefore has to reduce the time step size. For example, if the previous completed time step was at day 365 and the current time step ending at 396 days cannot be solved, then the simulator will reduce the current time step to perhaps end at day 370, if this still cannot solved then the time step will be chopped back again to perhaps to less then one day. Using the NEXT or NEXTSTEP keyword, the simulator is instructed to take a small time step in the anticipation that this will avoid time step chops and thus improve computational performance.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | NSTEP1 | NSTEP1 is a real positive value that defines the maximum length of the next time step. | None |
| days | days | hours |  |
| 2 | NSTEP2 | NSTEP2 is a character string that should be set to either NO or YES to state if the NSTEP1 should be applied to future reporting time steps.<br>1)  NO: Means that NSTEP1 should not be applied to subsequent reporting time steps.<br>2)  YES: Means that NSTEP1 should be applied to subsequent reporting time steps.<br>The default value of NO means that NSTEP1 will only be applied once. | NO |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 12.54: NEXT Keyword Description

See also the DATES and TSTEP keywords in the RUNSPEC section that are used to advance the simulation through time.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored. See section [Running OPM Flow From The Command Line](#running-opm-flow-from-the-command-line) on how to control time stepping for OPM Flow.

#### Example

\-- NEXT ALL

\-- STEP TIME

\-- \-\-\-- \-\-\--

NEXT

1 \'NO\' /

Here the next step size is set to one day and should only be used once.
