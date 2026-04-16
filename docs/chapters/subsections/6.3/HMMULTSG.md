### HMMULTSG -- History Match Dual porosity Sigma Gradient Cumulative Multipliers

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[HMMULTSG](#__RefHeading___Toc225109_373485663) defines the history match dual porosity sigma parameter gradient cumulative multipliers applied to the dual porosity sigma value declared by the [SIGMAV](#__RefHeading___Toc162093_2895739081) and [SIGMAGDV](#__RefHeading___Toc1228905_516898843) keywords in the [PROPS](#__RefHeading___Toc39329_784232322) section, for when the History Match Gradient option has been activated by the [HMDIMS](#__RefHeading___Toc207753_4219267791) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. In addition to the [HMDIMS](#__RefHeading___Toc207753_4219267791) keyword, either the [DUALPERM](#__RefHeading___Toc241171_1772380413) keyword that activates the Dual Permeability option, or the [DUALPORO](#__RefHeading___Toc241173_1772380413) keyword that activates the Dual Porosity option for the run, must be declared in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
