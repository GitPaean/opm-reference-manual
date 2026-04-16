### WPLUG -- Define Well Plug Back Length

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

Various keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section ([WECON](#__RefHeading___Toc134884_2055188184), [GECON](#__RefHeading___Toc134876_2055188184) etc.) allow for a well to be automatically plugged back if the well violates a constraint, that is to close existing perforations (well connections). For example if the water cut exceeds 90%, then plug back the well. The [WPLUG](#__RefHeading___Toc628135_4263943340) keyword defines for automatic plug backs the length of the perforations (length of connections) to be closed each time an automatic plug back is performed, together with various options on how the workover should be performed, top down, bottom up, etc.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
