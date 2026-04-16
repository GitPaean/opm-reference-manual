### WFRICSEG -- Convert Friction Well to Multi-Segment Well

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[WFRICSEG](#__RefHeading___Toc1032920_487874538) converts a previously defined friction well, as per the [WFRICTN](#__RefHeading___Toc1032924_487874538) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, to a multi-segment well. The keyword thus acts as a replacement for the [WELSEGS](#__RefHeading___Toc97661_3261743917) and [COMPSEGS](#__RefHeading___Toc316604_3519154785) keywords for multi-segment wells. See also the [WFRICSGL](#__RefHeading___Toc1032922_487874538) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section that performs similar functionality for wells in Local Grid Refinements.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
