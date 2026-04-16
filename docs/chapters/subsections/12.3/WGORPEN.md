### WGORPEN -- Define Well GOR Penalty Parameters

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [WGORPEN](#__RefHeading___Toc1081798_487874538) keyword defines a well's Gas-Oil Ratio ("GOR") penalty parameters used to calculate a well's oil production target for the current month, as a function of the well's previous month's average GOR. The [WGORPEN](#__RefHeading___Toc1081798_487874538) calculated oil rate overwrites any oil targets set by the [WCONPROD](#__RefHeading___Toc146754_4203985108) and [WELTARG](#__RefHeading___Toc134888_2055188184) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. In North American, it is common practice for the regulator to enforce GOR penalties, in order to control gas production in depletion drive oil reservoirs, with the stated intention to maximize oil recovery by limiting the energy loss from the reservoir by excessive gas production.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
