### HMRREF -- History Match Rock Table Reference Pressure Values

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [HMRREF](#__RefHeading___Toc251590_373485663) keyword defines the history match rock compaction reference pressure gradient values to be used in conjunction with [HMMROCKT](#__RefHeading___Toc219815_373485663), [ROCKTAB](#__RefHeading___Toc107256_3812137098) and [ROCKTABH](#__RefHeading___Toc266641_516898843) keywords in the [PROPS](#__RefHeading___Toc39329_784232322) section, for when the History Match Gradient option has been activated by the [HMDIMS](#__RefHeading___Toc207753_4219267791) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The history match rock compaction data is entered via the [HMMROCKT](#__RefHeading___Toc219815_373485663), [ROCKTAB](#__RefHeading___Toc107256_3812137098) and [ROCKTABH](#__RefHeading___Toc266641_516898843) keywords in the [PROPS](#__RefHeading___Toc39329_784232322) section.

See also the [HMDIMS](#__RefHeading___Toc207753_4219267791) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section that specifies the dimensions for the gradient option, including the maximum number of rock gradient parameters that can be used with the History Match Gradient option.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
