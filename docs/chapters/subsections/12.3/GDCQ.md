### GDCQ -- Define Group Multiple Daily Contract Quantities

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [GDCQ](#__RefHeading___Toc229883_156692946) keyword defines the Daily Contract Quantities ("DCQ") for when multiple group contracts are required when the Gas Field Operations model has been activated by the [GASFIELD](#__RefHeading___Toc195426_1190369742) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, or the GWSINGF has been invoked to define multiple group contracts in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. The group contracts must first be defined by the [GSWINGF](#__RefHeading___Toc224004_870710203) keyword, followed by the GCDQ keyword, and then the [GASYEAR](#__RefHeading___Toc493664_1414963541) or [GASPERIO](#__RefHeading___Toc206080_1190369742) keywords. GCDQ may be repeated in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section to reset group DCQs.

See also the [SWINGFAC](#__RefHeading___Toc1193036_4250154414) keyword that set a single group DCQ at the field level, as opposed to having multiple DCQ group contracts using the [GDCQ](#__RefHeading___Toc229883_156692946) keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
