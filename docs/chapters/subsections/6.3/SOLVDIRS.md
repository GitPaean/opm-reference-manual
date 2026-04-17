### SOLVDIRS -- Define Linear Solver Principal Directions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SOLVDIRS keyword defines the linear solver principal directions, which should be set to XY, XZ, YX, YZ, ZX, or ZY. The default direction is based on the direction of the highest transmissibility and SOLVDIRS allows for over writing the default direction for when linear convergence of the equations are problematic.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

See section [Running OPM Flow From The Command Line](#running-opm-flow-from-the-command-line) on how to invoke various numerical schemes via the OPM Flow command line interface.
