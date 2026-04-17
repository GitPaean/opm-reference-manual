### TRDIF -- Tracer Diffusion Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, TRDIF, specifies the tracer diffusion tables that specify the diffusion coefficient for a tracer. The keyword can be used with Environmental Tracers if the MXENVTR parameter has been set greater than zero on the TRACERS keyword in the RUNSPEC section. When used with a Standard Partitioned Tracer the diffusion coefficient applies to the solution phase, whereas as for a Multi-Partitioned Tracer the diffusion coefficient can be entered for each defined tracer phase. Unlike other keywords, the TRADS keyword must be concatenated with the three character name of the tracer declared by TRACER keyword in the PROPS section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
