### TRADS -- Environmental Tracer Adsorption Tables

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword, [TRADS](#__RefHeading___Toc1299985_4250154414), specifies the environmental tracer adsorption tables that describe how a tracer is absorbed by the surrounding rock, for when the MXENVTR parameter has been set to greater than zero on the [TRACERS](#__RefHeading___Toc76509_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section to activate environmental tracers. The keyword can only be used with environmental tracers.

Unlike other keywords, the [TRADS](#__RefHeading___Toc1299985_4250154414) keyword must be concatenated with the three character name of the tracer declared by [TRACER](#__RefHeading___Toc121485_83452205) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
