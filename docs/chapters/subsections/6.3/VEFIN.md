### VEFIN -- Activate Vertical Equilibrium Model (LGR)

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

If the [VE](#__RefHeading___Toc557797_487874538) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section has been used to activate the Vertical Equilibrium ("VE") model for the global grid, then the [VEFIN](#__RefHeading___Toc557801_487874538) keyword may used to set various options for the Local Grid Refinements ("LGR"). The [LGR](#__RefHeading___Toc55049_4106839650) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section should be activated to indicate the presence of LGRs and the keyword [VEFIN](#__RefHeading___Toc557801_487874538) should be placed in between the [CARFIN](#__RefHeading___Toc150726_63720426) and [ENDFIN](#__RefHeading___Toc111797_332691817) keywords in the [GRID](#__RefHeading___Toc38674_784232322) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
