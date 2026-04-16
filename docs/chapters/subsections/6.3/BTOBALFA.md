### BTOBALFA -- Dual Porosity Matrix to Fracture Multiplier (All Cells)

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [BTOBALFA](#__RefHeading___Toc162091_289573908) keyword defines a dual porosity matrix to fracture multiplier that is applied to all cells, for when the Dual Porosity model has been activated by either the [DUALPORO](#__RefHeading___Toc241173_1772380413) or the [DUALPERM](#__RefHeading___Toc241171_1772380413) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

See also the [BTOBALFV](#__RefHeading___Toc162093_289573908) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section that applies a multipliers to individual cells.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
