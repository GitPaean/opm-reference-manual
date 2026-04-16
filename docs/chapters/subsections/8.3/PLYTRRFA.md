### PLYTRRFA -- Define Polymer Rock Permeability Reduction versus Temperature Option

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [PLYTRRFA](#__RefHeading___Toc258120_501926209) keyword defines the how the polymer rock permeability reduction factor to the water phase as a function of temperature data, entered via the PLYTRRA keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section, should be used. This keyword should only be used if the Polymer option has been activated by the [POLYMER](#__RefHeading___Toc38609_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. See the PERMFAC parameter on the [PLYROCK](#__RefHeading___Toc110216_2939291539) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section for setting the property for the whole grid for a constant temperature.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
