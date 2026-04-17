### TRDIS -- Tracer Dispersion Table Number Allocation

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, TRDIS, specifies the tracer diffusion tables that should be allocated to a tracer, the actual dispersion tables are specified by the DISPERSE keyword in the PROPS section. The keyword can be used with Environmental Tracers if the MXENVTR parameter has been set greater than zero on the TRACERS keyword in the RUNSPEC section. The option does not work with two-phase Standard Partitioned Tracers and Multi-Partitioned Tracers. Unlike other keywords, the TRADS keyword must be concatenated with the three character name of the tracer declared by TRACER keyword in the PROPS section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
