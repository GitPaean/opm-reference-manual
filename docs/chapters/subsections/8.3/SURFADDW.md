### SURFADDW -- Defined Surfactant Adsorbed Concentration versus Wettability Fraction

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

SURFADDW defines tables of surfactant adsorbed concentration versus wettability fraction for when the SURFACTW keyword in the RUNSPEC section as been declared to activate the surfactant phase with changing wettability. The tables consists of columnar vectors of adsorbed surfactant concentration versus a wettability fraction that indicates the fraction of phase wettability. Here, a wettability fraction of zero indicates a 100% water wet rock resulting in the SURFWNUM allocated saturation tables being used, and a value of one meaning 100% oil wet rock, with the SATNUM allocated saturations tables being employed. Both the SURFWNUM and SATNUM keywords are in the REGIONS section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
