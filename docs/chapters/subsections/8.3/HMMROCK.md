### HMMROCK -- History Match Rock Compressibility Gradient Cumulative Multipliers

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[HMMROCK](#__RefHeading___Toc219806_373485663) defines the rock compressibility gradient cumulative multipliers to be applied to the rock compressibility as defined by the [ROCK](#__RefHeading___Toc45809_719036256) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section, for when the History Match Gradient option has been activated by the [HMDIMS](#__RefHeading___Toc207753_4219267791) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The constant should be a real number.

The allocation of the [ROCK](#__RefHeading___Toc45809_719036256) tables to different grid blocks in the model is done via the [PVTNUM](#__RefHeading___Toc68366_2752266063) or the [SATNUM](#__RefHeading___Toc71136_2752266063) keywords in the REGION section.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.
