### NOCASC -- Activate Linear Solver Tracer Algorithm

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

NOCASC keyword activates the linear solver tracer algorithm for single phase tracers.

OPM Flow uses a different numerical scheme which makes this keyword redundant; hence, OPM Flow ignores this keyword. It is documented here for completeness.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- TRACER SOLVER OPTION

\--

NOCASC

The above example switches on the linear solver tracer algorithm; however, this has no effect in OPM Flow input decks.
