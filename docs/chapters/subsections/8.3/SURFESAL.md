### SURFESAL -- Define Surfactant Effective Salinity Coefficient

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, [SURFESAL](#__RefHeading___Toc890338_4250154414), defines the surfactant effective salinity coefficient as well as enabling the effective salinity calculation for surfactant adsorption. The keyword should only be used if the [BRINE](#__RefHeading___Toc162083_289573908) keyword has been declared to activate the brine phase, the [ECLMC](#__RefHeading___Toc206960_803326780) keyword to enable the Multi-Component Brine model, and the [SURFACT](#__RefHeading___Toc863854_4250154414) keyword has been used to activate the surfact phase. All three keywords are in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
