### WGASPROD -- Define Sale Gas Well Production Targets

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WGASPROD keyword declares wells to be Sales Gas producers and sets the incremental gas rate for a well and the maximum number of increments that this rate can be increased. Wells must have been previously been defined via the WELSPECS and WCONPROD keywords in the SCHEDULE section and are subject to any targets or constraints on WCONPROD keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
