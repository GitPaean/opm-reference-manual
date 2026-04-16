### WPOTCALC -- Well Potential Calculation Options

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[WPOTCALC](#__RefHeading___Toc649219_4263943340) defines how shut-in and stopped wells should have their well potentials calculated. Well potentials for wells under these conditions need to have their potentials calculated if they are in a Priority Drilling Queue via the [WDRILPRI](#__RefHeading___Toc442117_2026549522) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, or the Prioritization option has been enabled by the [PRIORITY](#__RefHeading___Toc46726_327352552) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.
