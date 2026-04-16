### WFRICSGL -- Convert Friction Well to Multi-Segment Well (LGR)

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[WFRICSGL](#__RefHeading___Toc1032922_487874538) converts a previously defined Local Grid Refinement ("LGR") friction well, as per the [WFRICTNL](#__RefHeading___Toc1032926_487874538) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, to a multi-segment [LGR](#__RefHeading___Toc55049_4106839650) well. The keyword thus acts as a replacement for the [WELSEGS](#__RefHeading___Toc97661_3261743917) and [COMPSEGL](#__RefHeading___Toc97659_3261743917) keywords for [LGR](#__RefHeading___Toc55049_4106839650) multi-segment wells. See also the [WFRICSEG](#__RefHeading___Toc1032920_487874538) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section that performs similar functionality for wells in the global grid.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
