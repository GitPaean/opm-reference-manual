### SURFSTES -- Surfactant Water-Oil Surface Tension versus Surfactant and Salt Concentrations

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SURFSTES keyword defines surfactant water-oil surface tension versus surfactant concentration in the water phase tables, used in adjusting the pressure independent capillary pressure vectors in the SWFN or SWOF saturation tables, entered by their respective keywords in the PROPS section. SURFSTES is also used to adjust the relative permeability curves on the aforementioned tables via the capillary number. The Surfactant option must have been activated by the SURFACTANT keyword in the RUNSPEC section to use this keyword and either this keyword or the SURFST keyword, also in the PROPS section, is obligatory in this case. In addition, the BRINE keyword in the RUNSPEC section must be activated and the ESSNODE keyword in the PROPS section must be used to define the salt concentration or the effective salinity.

See also the SURFSTS that defines the surfactant water-oil surface tension as a function of surfactant concentration in the water phase only.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
