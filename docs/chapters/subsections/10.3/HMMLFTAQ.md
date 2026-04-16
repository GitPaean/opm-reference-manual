### HMMLFTAQ -- History Match Fetkovich Aquifer Gradient Multipliers

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [HMAQUFET](#__RefHeading___Toc202094_4219267791) keyword defines the history match analytical Fetkovich aquifer gradient multipliers for when the History Match Gradient option has been activated by the [HMDIMS](#__RefHeading___Toc207753_4219267791) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, and analytical Fetkovich aquifers have been specified in the model via the [AQUFET](#__RefHeading___Toc197384_1310555686) and/or the [AQUFETP](#__RefHeading___Toc4428_421927891) keywords and connected to the grid using [AQUANCON](#__RefHeading___Toc177536_3429068809) or [AQANCONL](#__RefHeading___Toc177536_342906880911111) keywords. All keywords are in the [SOLUTION](#__RefHeading___Toc43947_784232322) section.

Multipliers can be declared for the Fetkovich aquifer water volume, aquifer permeability, and the aquifer depth.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
