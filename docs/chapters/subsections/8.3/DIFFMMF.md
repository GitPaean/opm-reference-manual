### DIFFMMF -- Define Diffusivity Multipliers for Matrix-Fractures

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, [DIFFMMF](#__RefHeading___Toc324273_1539708736), defines the diffusivity multipliers for matrix-fractures for when the Dual Porosity option has be activated by either the [DUALPORO](#__RefHeading___Toc241173_1772380413) or [DUALPERM](#__RefHeading___Toc241171_1772380413) keywords, or the Coal Bed Methane option is selected by the [COAL](#__RefHeading___Toc234580_3519154785) keyword, and the Diffusivity option has been activated by the [DIFFUSE](#__RefHeading___Toc349951_1539708736) keywords; all four keywords are in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
