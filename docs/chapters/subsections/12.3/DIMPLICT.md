### DIMPLICT -- Activate Fully Implicit Dynamic Solution Formulation

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, DIMPLICT, activates the Fully Implicit Formulation and results in the simulator switching from the current solution formulation to the fully implicit formulation. OPM Flow uses a different numerical scheme which makes this keyword redundant; hence, OPM Flow ignores this keyword. It is documented here for completeness.

There is no data required for this keyword.

See section [Running OPM Flow From The Command Line](#running-opm-flow-from-the-command-line) on how to invoke various numerical schemes via the OPM Flow command line interface.

#### Example

\--

\-- ACTIVATES THE FULLY IMPLICIT SOLUTION OPTION

\--

DIMPLICT

The above example switches on the fully implicit solution option; however, this has no effect in OPM Flow input decks.
