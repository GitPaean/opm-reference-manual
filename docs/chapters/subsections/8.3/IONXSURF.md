### IONXSURF -- Define Surfactant Ion Exchange Constant by Saturation Table Regions

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [IONXROCK](#__RefHeading___Toc223663_2369005893) keyword activates ion exchange on surfactant micellae[^1] and defines the ion exchange constant by surfactant equivalent molecular weight for saturation table regions, for when the brine and surfactant phases has been activated by the [BRINE](#__RefHeading___Toc162083_289573908) and [SURFACT](#__RefHeading___Toc863854_4250154414) keywords, and the Multi-Component Brine model, that allows for the water phase to have multiple water salinities, has been activated by the [ECLMC](#__RefHeading___Toc206960_803326780) keyword. All three keywords are in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

[^1]: Particle of colloidal dimensions that exists in equilibrium with the molecules or ions in solution from which it is formed. A micella or micelle (plural micellae or micelles, respectively) is an aggregate (or supramolecular assembly) of surfactant molecules dispersed in a liquid colloid. A typical micella in aqueous solution forms an aggregate with the hydrophilic \"head\" regions in contact with surrounding solvent, sequestering the hydrophobic single-tail regions in the micella centre (https://en.wikipedia.org/wiki/Micelle).
