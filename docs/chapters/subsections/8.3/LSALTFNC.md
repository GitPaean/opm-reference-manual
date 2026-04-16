### LSALTFNC -- Define Low Salt Weighting Factors versus Salt Concentration Functions

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [LSALTFNC](#__RefHeading___Toc338141_2843394514) keyword defines the low salt weighting factors versus salt concentration functions for when the Low Salt option has been activated by the [LOWSALT](#__RefHeading___Toc331072_2843394514) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The tables are used to modify the oil and water relative permeability saturation end-points, as well as the water-oil capillary pressure end-points, for different salt concentrations within a grid cell.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
