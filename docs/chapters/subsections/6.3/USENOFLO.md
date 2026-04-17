### USENOFLO -- Activate Flux Boundary Model Without a Flux File

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The USENOFLUX keyword activates the Flux Boundary model without a FLUX file. The USEFLUX keyword should still be in the input deck, but in this case the FLUX filename is ignored. The option is useful when the no-flow boundary condition is a reasonable assumption and avoids the pre-cursor run used to generate the FLUX file via the DUMPFLUX keyword in the GRID section. Only grid blocks that have been declared by the FLUXREG keyword in the GRID section to be in an active flux region, are active for the run.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

\--

\-- ACTIVATE FLUX BOUNDARY MODEL WITHOUT A FLUX FILE

\--

USEFLUX

/

USENOFLO

The above example activates the Flux Boundary model without a FLUX file.
