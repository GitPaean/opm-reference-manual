### HMMLCTAQ -- History Match Carter-Tracy Aquifer Gradient Multipliers

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [HMMLCTAQ](#__RefHeading___Toc213367_4219267791) keyword defines the history match analytical Carter-Tracy aquifer gradient multipliers for when the History Match Gradient option has been activated by the [HMDIMS](#__RefHeading___Toc207753_4219267791) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, and analytical Carter-Tracy aquifers have been specified in the model via the [AQUCT](#__RefHeading___Toc179876_3429068809) and connected to the grid using the [AQUANCON](#__RefHeading___Toc177536_3429068809) or [AQANCONL](#__RefHeading___Toc177536_342906880911111) keywords. All keywords are in the [SOLUTION](#__RefHeading___Toc43947_784232322) section.

Multipliers can be declared for the Carter-Tracy aquifer permeability, aquifer angle of influence and the aquifer depth.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
