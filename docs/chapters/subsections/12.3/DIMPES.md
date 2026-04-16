### DIMPES -- Define IMPES Dynamic Solution Parameters

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword, [DIMPES](#__RefHeading___Toc173991_1772380413), defines the Implicit in Pressure Explicit Saturation ("IMPES") dynamic solution parameters and results in the simulator switching from the current solution formulation to the [IMPES](#__RefHeading___Toc53039_4106839650) formulation. OPM Flow uses a different numerical scheme which makes this keyword redundant; hence, OPM Flow ignores this keyword. It is documented here for completeness.

There is no data required for this keyword.

See section [Running OPM Flow From The Command Line](#running-opm-flow-from-the-command-line) on how to invoke various numerical schemes via the OPM Flow command line interface.

#### Example

\--

\-- ACTIVATE THE IMPES SOLUTION OPTION

\--

DIMPES

The above example switches on the [IMPES](#__RefHeading___Toc53039_4106839650) solution option; however, this has no effect in OPM Flow input decks.
