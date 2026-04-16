### RIVSALT -- Define River Upstream Flow Salt Concentrations

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [RIVSALT](#__RefHeading___Toc687458_501926209) keyword defines the injected salt concentration in individual river branches in a previously characterized river system using the [RIVERSYS](#__RefHeading___Toc674955_501926209) and the [REACHES](#__RefHeading___Toc643464_501926209) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. The River option must be activated via the [RIVRDIMS](#__RefHeading___Toc681201_501926209) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section in order to use this keyword. In addition, the Brine option must also be enabled via the [BRINE](#__RefHeading___Toc162083_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
