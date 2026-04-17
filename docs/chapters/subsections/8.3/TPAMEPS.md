### TPAMEPS -- Volumetric Strain versus Coal Gas Concentration Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

TPAMEPS defines the volumetric strain versus coal gas concentration tables, for when the Coal Bed Methane option has been activated via the COAL keyword, and PALM-MAN has been declared for the ROCKOPT variable on the ROCKCOMP keyword; both keywords are in the RUNSPEC section. The Palmer-Mansoorii[^1] and [^2] rock model is used to calculate the impact on pore volume and permeability due to rock compaction.

See also the ROCKPARMA keyword in the PROPS section that defines the Palmer-Mansoori parameters.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

[^1]: Palmer, I. and Mansoori, J. "How Permeability Depends on Stress and Pore Pressure in Coalbeds: A New Model," paper SPE 52607, SPE Reservoir Evaluation & Engineering (1998) 1, No. 6, 539-544.

[^2]: Clarkson, C.R., Pan, Z., Palmer, I. and Harpalani, S. \"Predicting Sorption-Induced Strain and Permeability Increase With Depletion for Coalbed-Methane Reservoirs\", SPE 114778-PA, SPE Journal (2010) 15, No. 1, 152--159.
