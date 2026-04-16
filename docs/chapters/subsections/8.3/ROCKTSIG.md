### ROCKTSIG -- Rock Compaction Tables (Dual Porosity)

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [ROCKTSIG](#__RefHeading___Toc272927_516898843) keyword defines the rock compaction attributes to be applied for when the rock compaction option has been invoked by the [ROCKCOMP](#__RefHeading___Toc55593_1778172979) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, and the either the Dual Permeability or Dual Porosity models are activated by the [DUALPERM](#__RefHeading___Toc241171_1772380413) and [DUALPORO](#__RefHeading___Toc241173_1772380413) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. [ROCKTSIG](#__RefHeading___Toc272927_516898843) specifies sigma multipliers versus pressure that are used in the dual porosity rock compaction calculations. The keyword should only be used if the Rock Compaction Hysteresis option has been activated by either setting the ROCKOPT parameter on the [ROCKCOMP](#__RefHeading___Toc55593_1778172979) keyword to one of the available options.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
