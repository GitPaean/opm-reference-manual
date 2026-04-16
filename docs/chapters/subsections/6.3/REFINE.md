### REFINE -- Start the Definition of a Local Grid Refinement

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [REFINE](#__RefHeading___Toc126224_332691817) keyword defines the start of a Cartesian or radial Local Grid Refinement ("LGR") definition that sets the properties of the selected [LGR](#__RefHeading___Toc55049_4106839650). The keyword is then followed by the property keywords associated with the section where the keyword is being invoked. For example, if the [REFINE](#__RefHeading___Toc126224_332691817) keyword is used in the [GRID](#__RefHeading___Toc38674_784232322) section then most of the keywords in that section can be used to set the grid properties for the [LGR](#__RefHeading___Toc55049_4106839650).

The [ENDFIN](#__RefHeading___Toc111797_332691817) keyword is used to terminate the [LGR](#__RefHeading___Toc55049_4106839650) definition.

There is no data required for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
