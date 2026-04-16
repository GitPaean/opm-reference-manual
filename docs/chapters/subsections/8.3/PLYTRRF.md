### PLYTRRF -- Define Polymer Rock Permeability Reduction versus Temperature

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [PLYTRRF](#__RefHeading___Toc258118_501926209) keyword defines the polymer rock permeability reduction factor to the water phase as a function of temperature, for when the Polymer option has been activated by the [POLYMER](#__RefHeading___Toc38609_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. See the PLYTRRF keyword for the options on how this data is used in the polymer model and the PERMFAC parameter on the [PLYROCK](#__RefHeading___Toc110216_2939291539) keyword for setting the property for the whole grid for a constant temperature. Both keywords are in the [PROPS](#__RefHeading___Toc39329_784232322) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
