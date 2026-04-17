### TRDCY -- Environmental Tracer Decay Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, TRDCY, specifies the environmental tracer decay tables that specifies the tracer decay half-life, for when the MXENVTR parameter has been set to greater than zero on the TRACERS keyword in the RUNSPEC section to activate environmental tracers. The keyword can only be used with environmental tracers.

Unlike other keywords, the TRSCY keyword must be concatenated with the three character name of the tracer declared by TRACER keyword in the PROPS section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
