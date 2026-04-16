### ENDFIN -- End the Definition of a Local Grid Refinement

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [ENDFIN](#__RefHeading___Toc111797_332691817) keyword defines the end of a Cartesian or radial local grid refinement ("LGR") definition and a [LGR](#__RefHeading___Toc55049_4106839650) property definition data set. In the [GRID](#__RefHeading___Toc38674_784232322) section the [CARFIN](#__RefHeading___Toc150726_63720426), [RADFIN](#__RefHeading___Toc76871_718313858), and [RADFIN4](#__RefHeading___Toc76873_718313858) keywords defines the start of an [LGR](#__RefHeading___Toc55049_4106839650) description section, whereas the [REFINE](#__RefHeading___Toc126224_332691817) keyword in the [EDIT](#__RefHeading___Toc40641_784232322), [PROPS](#__RefHeading___Toc39329_784232322), [REGIONS](#__RefHeading___Toc40648_784232322), [SOLUTION](#__RefHeading___Toc43947_784232322) and [SCHEDULE](#__RefHeading___Toc43945_784232322) section defines the start. The [REFINE](#__RefHeading___Toc126224_332691817) keyword can also be used in the [GRID](#__RefHeading___Toc38674_784232322) section provided the [LGR](#__RefHeading___Toc55049_4106839650) has been previously specified by the [CARFIN](#__RefHeading___Toc150726_63720426), [RADFIN](#__RefHeading___Toc76871_718313858), or [RADFIN4](#__RefHeading___Toc76873_718313858) keywords.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

The example below is based on using the [CARFIN](#__RefHeading___Toc150726_63720426) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section to define an [LGR](#__RefHeading___Toc55049_4106839650) in the global grid, named [LGR](#__RefHeading___Toc55049_4106839650)-OP01 with a maximum of one well allowed in the [LGR](#__RefHeading___Toc55049_4106839650).

\--

\-- CARFIN LGR GRID COMMANDS

\--

\-- LGR \-\-\-\-- FINE GRID \-\-\-\-\-- \-- CARFIN GRID \-- MAX HOST

\-- NAME I1 I2 J1 J2 K1 K2 NX NY NZ WELLS NAME

CARFIN

LGR-OP01 24 24 87 87 1 50 3 3 50 1 GLOBAL /

ENDFIN

Here the one global cell in the areal plane (24, 87) is divided into three [LGR](#__RefHeading___Toc55049_4106839650) cells in the x-direction and three cells in the y-direction. Since no other property data is given, then the [LGR](#__RefHeading___Toc55049_4106839650) cells take their properties from the host grid, that is the global grid.
