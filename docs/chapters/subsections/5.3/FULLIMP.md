### FULLIMP -- Activate Fully Implicit Solution Option

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [FULLIMP](#__RefHeading___Toc51445_4106839650) keyword activates the Fully Implicit Solution formulation and solution options. OPM Flow uses a different numerical scheme which makes this keyword redundant; hence, OPM Flow ignores this keyword. It is documented here for completeness. The keyword as the same function as the [IMPLICIT](#__RefHeading___Toc534216_2135714711) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

There is no data required for this keyword and there is no terminating "/" for this keyword.

See section [Running OPM Flow From The Command Line](#running-opm-flow-from-the-command-line) on how to invoke various numerical schemes via the OPM Flow command line interface.

#### Example

\--

\-- ACTIVATES THE FULLY IMPLICIT SOLUTION OPTION

\--

FULLIMP

The above example switches on the fully implicit solution option; however, this has no effect in OPM Flow input decks.
