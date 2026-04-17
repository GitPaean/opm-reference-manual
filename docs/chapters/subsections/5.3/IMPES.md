### IMPES -- Activate Implicit Pressure Explicit Saturation Solution Option

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The IMPES keyword activates the Implicit Pressure Explicit Saturation formulation and solution options, commonly know as IMPES. OPM Flow uses a different numerical scheme which makes this keyword redundant; hence, OPM Flow ignores this keyword. It is documented here for completeness.

There is no data required for this keyword and there is no terminating "/" for this keyword.

See section [Running OPM Flow From The Command Line](#running-opm-flow-from-the-command-line) on how to invoke various numerical schemes via the OPM Flow command line interface.

#### Example

\--

\-- ACTIVATE THE IMPES SOLUTION OPTION

\--

IMPES

The above example switches on the IMPES solution option; however, this has no effect in OPM Flow input decks.
