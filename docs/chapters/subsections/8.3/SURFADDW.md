### SURFADDW -- Defined Surfactant Adsorbed Concentration versus Wettability Fraction

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[SURFADDW](#__RefHeading___Toc877085_4250154414) defines tables of surfactant adsorbed concentration versus wettability fraction for when the [SURFACTW](#__RefHeading___Toc863864_4250154414) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section as been declared to activate the surfactant phase with changing wettability. The tables consists of columnar vectors of adsorbed surfactant concentration versus a wettability fraction that indicates the fraction of phase wettability. Here, a wettability fraction of zero indicates a 100% water wet rock resulting in the [SURFWNUM](#__RefHeading___Toc1179776_4250154414) allocated saturation tables being used, and a value of one meaning 100% oil wet rock, with the [SATNUM](#__RefHeading___Toc71136_2752266063) allocated saturations tables being employed. Both the [SURFWNUM](#__RefHeading___Toc1179776_4250154414) and [SATNUM](#__RefHeading___Toc71136_2752266063) keywords are in the [REGIONS](#__RefHeading___Toc40648_784232322) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
