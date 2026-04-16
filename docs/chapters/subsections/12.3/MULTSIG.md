### MULTSIG -- Multiply Matrix-Fracture Coupling for All Cells

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword, [MULTSIG](#__RefHeading___Toc264217_1841740821), defines a constant multiplier to modify the matrix-fracture coupling transmissibility for dual porosity and dual permeability models, for when the matrix-fracture coupling transmissibilities have been specified via the [SIGMAGD](#__RefHeading___Toc1228903_516898843) or [SIGMAGDV](#__RefHeading___Toc1228905_516898843) keywords in the [GRID](#__RefHeading___Toc38674_784232322) section, and the dual porosity or dual permeability models have been activated by the [DUALPORO](#__RefHeading___Toc241173_1772380413) or [DUALPERM](#__RefHeading___Toc241171_1772380413) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, respectively.

This keyword applies the multiplier for all cells in model; whereas, the [MULTSIGV](#__RefHeading___Toc598414_31819220061) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section applies the multiplier to individual grid blocks.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
