### SURFST -- Surfactant Water-Oil Surface Tension versus Surfactant Concentration

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SURFST keyword defines surfactant water-oil surface tension versus surfactant concentration in the water phase tables, used in adjusting the pressure independent capillary pressure vectors in the SWFN or SWOF saturation tables, entered by their respective keywords in the PROPS section. SURFST is also used to adjust the relative permeability curves on the aforementioned tables via the capillary number. The Surfactant option must have been activated by the SURFACTANT keyword in the RUNSPEC section to use this keyword and either this keyword or the SURFSTES keyword, also in the PROPS section, is obligatory in this case.

See also the SURFSTES that defines the surfactant water-oil surface tension as a function of surfactant concentration in the water phase and salt concentration or the effective salinity.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
