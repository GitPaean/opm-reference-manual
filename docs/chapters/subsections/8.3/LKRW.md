### LKRW -- End-Point Scaling of Grid Cell Krw(Sw =1.0) (Low Salinity and Oil Wet)

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[LKRW](#__RefHeading___Toc258547_42192677911) defines the scaling parameter at the maximum oil relative permeability value ([SWU](#__RefHeading___Toc22883_7842323221)), that is for Sw = 1.0, for all the cells in the model via an array, for when the Low Salt option and the End-point Scaling options has been activated by the [LOWSALT](#__RefHeading___Toc331072_2843394514) and the [ENDSCALE](#__RefHeading___Toc68146_2267116897) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The data is used to scale the water relative permeability in the low salinity oil wet water relative permeability saturation tables.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
