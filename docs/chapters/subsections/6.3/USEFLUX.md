### USEFLUX -- Activate Flux Boundary Model and Define Flux File

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The USEFLUX keyword activates the Flux Boundary model and defines the name of the FLUX file. Only grid blocks that have been declared by the FLUXREG keyword in the GRID section to be in an active flux region, are active for the run.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
