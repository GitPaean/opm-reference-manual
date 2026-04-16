### TRACTVD -- Activate Tracer Explicit Flux Limited Transport Option

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[TRACTVD](#__RefHeading___Toc1293239_4250154414) activates the Tracer Explicit Flux Limited Transport option. Basically the option is used to control numerical dispersion for tracers. Both the [TRACERS](#__RefHeading___Toc76509_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section and the [TRACER](#__RefHeading___Toc121485_83452205) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section must be declared to activate tracers and to define the tracers.

See also the [TRACITVD](#__RefHeading___Toc1279868_4250154414) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section activates the Tracer Implicit Flux Limited Transport option.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
