### PLYVISCT -- Define Polymer-Temperature Viscosity Scaling Factors

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

PLYSVISCT defines the polymer-temperature viscosity scaling factor tables applied to pure water that are used to determine the viscosity of the polymer at a given temperature with respect to increasing polymer concentration within a grid block. Both the polymer option must be activated by the [POLYMER](#__RefHeading___Toc38609_2267116897) keyword and the temperature option invoked by the [TEMP](#__RefHeading___Toc146397_3544483072) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section in order to use this keyword. However the [BRINE](#__RefHeading___Toc162083_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) must not be used with this keyword, that is the salt sensitivity options should be deactivated.

See also the [PLYVSCST](#__RefHeading___Toc270351_501926209) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section to enter polymer viscosity scaling factor data that is dependent on both salt and reservoir temperature.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
