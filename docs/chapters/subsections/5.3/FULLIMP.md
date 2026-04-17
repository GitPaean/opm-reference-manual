### FULLIMP -- Activate Fully Implicit Solution Option

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The FULLIMP keyword activates the Fully Implicit Solution formulation and solution options. OPM Flow uses a different numerical scheme which makes this keyword redundant; hence, OPM Flow ignores this keyword. It is documented here for completeness. The keyword as the same function as the IMPLICIT keyword in the RUNSPEC section.

There is no data required for this keyword and there is no terminating "/" for this keyword.

See section [Running OPM Flow From The Command Line](#running-opm-flow-from-the-command-line) on how to invoke various numerical schemes via the OPM Flow command line interface.

#### Example

\--

\-- ACTIVATES THE FULLY IMPLICIT SOLUTION OPTION

\--

FULLIMP

The above example switches on the fully implicit solution option; however, this has no effect in OPM Flow input decks.
