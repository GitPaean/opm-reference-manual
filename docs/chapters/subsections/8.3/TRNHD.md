### TRNHD -- Activate Dispersion Non-Homogeneous Diffusion Option

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [TRNHD](#__RefHeading___Toc1607159_4250154414) keyword activates the Dispersion Non-Homogeneous Diffusion option for when tracer dispersion is independent of velocity or tracer concentration. Unlike other keywords, the [TRNHD](#__RefHeading___Toc1607159_4250154414) keyword must be concatenated with the name of the tracer declared by [TRACER](#__RefHeading___Toc121485_83452205) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
