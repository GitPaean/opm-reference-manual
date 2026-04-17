### MONITOR -- Activate Output of the Monitoring Data and File

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The MONITOR keyword activates the writing out of the run time monitoring information used by post-processing graphics software to display run time information, for example the simulated production and injection rates and cumulative values. OPM Flow does not have this functionality.

Hence, OPM Flow ignores this keyword but it is documented here for completeness.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- ACTIVATE MONITORING OUTPUT DATA AND FILES

\--

MONITOR

The above example switches on the output required for run time monitoring required by post-processing graphics software to review the simulation results in real time as the run progresses; however, this has no effect in OPM Flow input decks.
