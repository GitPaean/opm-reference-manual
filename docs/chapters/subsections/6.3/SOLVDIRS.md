### SOLVDIRS -- Define Linear Solver Principal Directions

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [SOLVDIRS](#__RefHeading___Toc778602_4250154414) keyword defines the linear solver principal directions, which should be set to XY, XZ, YX, YZ, ZX, or ZY. The default direction is based on the direction of the highest transmissibility and [SOLVDIRS](#__RefHeading___Toc778602_4250154414) allows for over writing the default direction for when linear convergence of the equations are problematic.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

See section [Running OPM Flow From The Command Line](#running-opm-flow-from-the-command-line) on how to invoke various numerical schemes via the OPM Flow command line interface.
