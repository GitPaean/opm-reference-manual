### SURFESAL -- Define Surfactant Effective Salinity Coefficient

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, SURFESAL, defines the surfactant effective salinity coefficient as well as enabling the effective salinity calculation for surfactant adsorption. The keyword should only be used if the BRINE keyword has been declared to activate the brine phase, the ECLMC keyword to enable the Multi-Component Brine model, and the SURFACT keyword has been used to activate the surfact phase. All three keywords are in the RUNSPEC section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
