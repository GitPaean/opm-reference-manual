### IONXSURF -- Define Surfactant Ion Exchange Constant by Saturation Table Regions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The IONXROCK keyword activates ion exchange on surfactant micellae[^1] and defines the ion exchange constant by surfactant equivalent molecular weight for saturation table regions, for when the brine and surfactant phases has been activated by the BRINE and SURFACT keywords, and the Multi-Component Brine model, that allows for the water phase to have multiple water salinities, has been activated by the ECLMC keyword. All three keywords are in the RUNSPEC section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

[^1]: Particle of colloidal dimensions that exists in equilibrium with the molecules or ions in solution from which it is formed. A micella or micelle (plural micellae or micelles, respectively) is an aggregate (or supramolecular assembly) of surfactant molecules dispersed in a liquid colloid. A typical micella in aqueous solution forms an aggregate with the hydrophilic \"head\" regions in contact with surrounding solvent, sequestering the hydrophobic single-tail regions in the micella centre (https://en.wikipedia.org/wiki/Micelle).
