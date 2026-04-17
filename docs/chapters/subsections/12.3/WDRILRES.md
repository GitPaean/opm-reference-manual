### WDRILRES -- Activate Prevention of Multi-Completions in the Same Cell for Queued Wells

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WDRILRES keyword activates the prevention of multi-completions being completed in the same cell for wells in a drilling queue. Setting this option stops any well defined as a queued well via the QDRILL and WDRILLPRI keywords in the SCHEDULE section, or any wells set to automatic opening by setting the STATUS variable to AUTO on the WCONPROD keyword in the RUNSPEC section, from opening if there is an already existing active well connection to a cell.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
