### ZIPPY2 -- Activate Automatic Time Step Control

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [ZIPPY2](#__RefHeading___Toc146756_4203985108) keyword activates the commercial simulator's alternative automatic time step selection algorithm that assumes no prior knowledge of the problem, as opposed to the standard time step algorithm that is controlled via the TUNNING keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, combined with posterior knowledge gained from previous time steps.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

See section [[2.2](#anchor-2)](#2.2.Running OPM Flow 2018-10 |outline)[](#2.2.Running OPM Flow 2018-10 |outline)[[Running OPM Flow 2023-04 From The Command Line](#anchor-2)](#2.2.Running OPM Flow 2018-10 |outline) on how to control time stepping for OPM Flow.
