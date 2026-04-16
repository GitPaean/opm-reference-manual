### GTMULT -- Multiply Group Target or Constraint by a Constant

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, [GTMULT](#__RefHeading___Toc235061_870710203), multiplies a group's target or constraint value by a numerical constant. The group must have been initially fully defined using the [GCONPROD](#__RefHeading___Toc146746_4203985108) or [GCONPRI](#__RefHeading___Toc659214_1190369742) keywords for producers or [GCONINJE](#__RefHeading___Toc134874_2055188184) for injectors. Variables not changed by the [GTMULT](#__RefHeading___Toc235061_870710203) keyword remain the same as those previously entered via the group control keywords or previously entered [GTMULT](#__RefHeading___Toc235061_870710203) keywords. See also the [GRUPTARG](#__RefHeading___Toc196552_870710203) keyword that sets the values for a group's target and constraints, and the [GTADD](#__RefHeading___Toc235059_870710203) keyword that adds a constant to a group's target or constraint. All the aforementioned keywords are described in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
