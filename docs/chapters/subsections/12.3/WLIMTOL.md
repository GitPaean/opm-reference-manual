### WLIMTOL -- Define Well Constraint Tolerance

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[WLIMTOL](#__RefHeading___Toc123805_332691817) keyword defines the tolerance to be used for various constraints applied to connections, completions (if connections have been lumped via the [COMPLUMP](#__RefHeading___Toc97655_3261743917) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section), wells, and groups, including the field group. See also the [GCONTOL](#__RefHeading___Toc202994_156692946) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section that sets the tolerance parameters for groups.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
