### PLYVISCS -- Define Polymer-Salt Viscosity Scaling Factors

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

PLYSVISCS defines the polymer-salt viscosity scaling factor tables applied to pure water that are used to determine the viscosity of a polymer-salt mixture with respect to increasing polymer concentration within a grid block. The polymer option must be activated by the [POLYMER](#__RefHeading___Toc38609_2267116897) keyword, as well as the brine phase declared by the [BRINE](#__RefHeading___Toc162083_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section in order to use this keyword. However the ECLM keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) must not be used with this keyword.

See also the [PLYVSCST](#__RefHeading___Toc270351_501926209) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section to enter polymer viscosity scaling factor data that is dependent on both salt and reservoir temperature.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
