### DSPDEINT -- Activate Brine Tracer Dispersion Interpolation by Water Density

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, DSPDEINT, activates the brine tracer dispersion interpolation by water density option for when the Brine phase is activated in the model by the BRINE keyword in the RUNSPEC section and the DISPERSE keyword in the PROPS section is in the input file. They keyword cause the lookup and interpolation of the DISPERSE tracer concentration to water density, that is the tracer concentration data on the DISPERSE keyword has been replaced by the water density data.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
