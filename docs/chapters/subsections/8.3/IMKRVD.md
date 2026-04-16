### IMKRVD -- Imbibition Relative Permeability End-Points versus Depth Functions

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the maximum imbibition oil, gas, and water relative permeability versus depth for the three phases. The [ENDSCALE](#__RefHeading___Toc68146_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section should be activated to enable end-point scaling and the use of this keyword. In addition, the HYSTER option on the [SATOPTS](#__RefHeading___Toc37029_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section has to be activated to invoke the Hysteresis option.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
