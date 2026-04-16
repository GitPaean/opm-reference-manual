### LYFIN -- Define Logarithmic LGR Grid Block Spacing in the Y-Direction

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [LYFIN](#__RefHeading___Toc516798_3181922006) keyword defines the parameters for automatically generating a Local Grid Refinement ("LGR") grid in the Y direction based on logarithmic block spacing, for when the [LGR](#__RefHeading___Toc55049_4106839650) option has been activated by the [LGR](#__RefHeading___Toc55049_4106839650) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. [LYFIN](#__RefHeading___Toc516798_3181922006) should be placed in between the [CARFIN](#__RefHeading___Toc150726_63720426) and [ENDFIN](#__RefHeading___Toc111797_332691817) keywords in the [GRID](#__RefHeading___Toc38674_784232322) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
