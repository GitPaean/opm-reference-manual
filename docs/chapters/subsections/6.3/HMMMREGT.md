### HMMMREGT -- History Match Region Transmissibility Gradient Cumulative Multipliers

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [HMMMREGT](#__RefHeading___Toc214542_373485663) keyword multiplies the transmissibility between two regions by a constant, for when the History Match Gradient option has been activated by the [HMDIMS](#__RefHeading___Toc207753_4219267791) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The constant should be a real number. Unlike the [MULTREGT](#__RefHeading___Toc296621_1576177388) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section, the [HMMMREGT](#__RefHeading___Toc214542_373485663) keyword modifications are cumulative.

Note that the [HMMMREGT](#__RefHeading___Toc214542_373485663) keyword only declares the two regions and the multiplier between those regions, the transmissibility direction (DIR on the [MULTREGT](#__RefHeading___Toc296621_1576177388) keyword), type of transmissibility multiplier (TYPE on the [MULTREGT](#__RefHeading___Toc296621_1576177388) keyword), and the region number array to use (ARRAY on the [MULTREGT](#__RefHeading___Toc296621_1576177388) keyword), are all taken from the MULTREGY keyword. For example, the region number array can be [FLUXNUM](#__RefHeading___Toc45781_719036256), [MULTNUM](#__RefHeading___Toc61329_2752266063) or [OPERNUM](#__RefHeading___Toc67857_718313858) and these arrays must be defined and be available before the [MULTREGT](#__RefHeading___Toc296621_1576177388) keyword is read by the simulator, and before the [HMMMREGT](#__RefHeading___Toc214542_373485663) keyword is used.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.
