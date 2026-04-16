### WBHGLR -- Define Well Bottom-Hole GLR Constraint

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, [WBHGLR](#__RefHeading___Toc422065_2026549522), defines a well's bottom-hole Gas Liquid Ratio ("GLR") constraint, where the GLR is the is the ratio of the "free" gas rate and liquid rate at bottom-hole conditions. The reference depth for bottom-hole conditions is given by the BHPREF variable on the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

Normally this type of well control is applied to pumping wells to avoid the well "pumping off", that is when the liquid column above the pump is low, resulting in an increase in gas intake and an associated loss in pump efficiency.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
