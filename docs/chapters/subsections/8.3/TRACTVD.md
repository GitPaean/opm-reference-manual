### TRACTVD -- Activate Tracer Explicit Flux Limited Transport Option

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

TRACTVD activates the Tracer Explicit Flux Limited Transport option. Basically the option is used to control numerical dispersion for tracers. Both the TRACERS keyword in the RUNSPEC section and the TRACER keyword in the PROPS section must be declared to activate tracers and to define the tracers.

See also the TRACITVD keyword in the PROPS section activates the Tracer Implicit Flux Limited Transport option.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
