### LTOSIGMA -- Dual Porosity Viscous Displacement Sigma Parameters

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [LTOSIGMA](#__RefHeading___Toc528401_3181922006) keyword defines parameters to calculate the sigma factor in conjunction with the data entered via the [LX](#__RefHeading___Toc499449_3181922006), [LY](#__RefHeading___Toc499451_3181922006) and [LZ](#__RefHeading___Toc499453_3181922006) keywords in the [GRID](#__RefHeading___Toc38674_784232322) section, for when the [VISCD](#__RefHeading___Toc486166_3181922006) keyword has been used in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section to activate the Dual Porosity Viscous Displacement option. In addition, either the [DUALPORO](#__RefHeading___Toc241173_1772380413) or [DUALPERM](#__RefHeading___Toc241171_1772380413) keyword should be entered in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section to activate the dual porosity or dual permeability models.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
