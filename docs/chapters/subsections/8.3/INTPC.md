### INTPC -- Activate Dual Porosity Integrated Capillary Pressure Option

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [INTPC](#__RefHeading___Toc218037_2369005893) keyword activates the integrated capillary pressure option for the oil, gas or both phases, for when a Dual Porosity model has been activated by either the [DUALPORO](#__RefHeading___Toc241173_1772380413) or [DUALPERM](#__RefHeading___Toc241171_1772380413) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. In addition, the keyword can only be used if the Gravity Drainage option has been specified by either the [GRAVDR](#__RefHeading___Toc455285_1414963541) or [GRAVDRM](#__RefHeading___Toc471678_1414963541) in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Basically, activating this feature results in the simulator adjusting the capillary pressure curves by integrating the matrix capillary pressure curves over the matrix block height to calculate the average saturation.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
