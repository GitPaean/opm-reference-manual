### HMAQUNUM -- History Match Numerical Aquifer Gradient Parameters

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [HMAQUNUM](#__RefHeading___Toc463484_2135714711) keyword defines the history match numerical aquifer gradient parameters for when the History Match Gradient option has been activated by the [HMDIMS](#__RefHeading___Toc207753_4219267791) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, and numerical aquifers have been specified in the model via the [AQUNUM](#__RefHeading___Toc4430_421927891) keyword and connected to the grid using [AQUCON](#__RefHeading___Toc115431_846947960) keyword. All keywords are in the [GRID](#__RefHeading___Toc38674_784232322) section.

See also the [HMDIMS](#__RefHeading___Toc207753_4219267791) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section that specifies the dimensions for the gradient option, including the maximum number of aquifers that can be used with the History Match Gradient option.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
