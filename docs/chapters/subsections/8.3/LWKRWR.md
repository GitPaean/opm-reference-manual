### LWKRWR -- End-Point Scaling of Grid Cell KRWR(Sw=1.0) (Low Salinity and Water Wet)

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[LWKRWR](#__RefHeading___Toc258549_42192677911) defines the scaling parameter at the critical oil to water saturation value ([SOWCR](#__RefHeading___Toc30436_784232322)), for the water relative permeability curve, for all the cells in the model via an array, and for when the Low Salt and Surfactant Wettability options have been selected. The data is used to scale the water relative permeability in the low salinity water wet water relative permeability saturation tables. The [ENDSCALE](#__RefHeading___Toc68146_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section should be activated to enable end-point scaling and the use of this keyword. In addition the Low Salt option should be activated by the [LOWSALT](#__RefHeading___Toc331072_2843394514) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section and the Surfactant Wettability option activated by the [SURFACT](#__RefHeading___Toc863854_4250154414) or [SURFACTW](#__RefHeading___Toc863864_4250154414) keywords, which are also in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
