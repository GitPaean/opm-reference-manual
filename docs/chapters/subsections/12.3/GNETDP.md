### GNETDP -- Group Network Pressure and Rate Controls

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [GNETDP](#__RefHeading___Toc416323_1414963541) keyword sets a group's minimum and maximum network pressure and rate controls for when the either the Standard Network or the Extended Network options have been activated, and the group is part of a network. The keywords allows for the pressure of the group to vary in order to satisfy the rate conditions declared by this keyword. The Standard Network option is invoked if the [GRUPTREE](#__RefHeading___Toc118321_1596574740), [GRUPNET](#__RefHeading___Toc118319_1596574740), [GNETINJE](#__RefHeading___Toc114199_332691817), [GNETPUMP](#__RefHeading___Toc421755_1414963541), etc. series of keywords have been used in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. Whereas, the Extended Network option is activated by the [NETWORK](#__RefHeading___Toc311583_1841740821) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Several keywords, including, [GNETDP](#__RefHeading___Toc416323_1414963541), can be used by both network options.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
