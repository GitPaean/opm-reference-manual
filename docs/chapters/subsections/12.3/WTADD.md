### WTADD -- Add a Constant to a Well Target or Constraint

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword, [WTADD](#__RefHeading___Toc1120312_4263943340), adds a constant to a previously define well's target or constraint, as stated on the [WCONPROD](#__RefHeading___Toc146754_4203985108), [WCONINJE](#__RefHeading___Toc146750_4203985108), or [WELTARG](#__RefHeading___Toc134888_2055188184) keywords, but not for the history matching wells using the [WCONHIST](#__RefHeading___Toc134880_2055188184) or [WCONINJH](#__RefHeading___Toc146752_4203985108) keywords. All the aforementioned keywords are in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. The constant can be positive or negative.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
