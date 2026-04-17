### TRNHD -- Activate Dispersion Non-Homogeneous Diffusion Option

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The TRNHD keyword activates the Dispersion Non-Homogeneous Diffusion option for when tracer dispersion is independent of velocity or tracer concentration. Unlike other keywords, the TRNHD keyword must be concatenated with the name of the tracer declared by TRACER keyword in the PROPS section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
