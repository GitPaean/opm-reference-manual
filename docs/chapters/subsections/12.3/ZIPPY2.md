### ZIPPY2 -- Activate Automatic Time Step Control

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The ZIPPY2 keyword activates the commercial simulator's alternative automatic time step selection algorithm that assumes no prior knowledge of the problem, as opposed to the standard time step algorithm that is controlled via the TUNNING keyword in the SCHEDULE section, combined with posterior knowledge gained from previous time steps.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

See section [Running OPM Flow From The Command Line](#running-opm-flow-from-the-command-line) on how to control time stepping for OPM Flow.
