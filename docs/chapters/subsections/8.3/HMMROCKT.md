### HMMROCKT -- History Match Rock Compaction Gradient Cumulative Multipliers

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[HMMROCKT](#__RefHeading___Toc219815_373485663) defines the rock compaction gradient cumulative multipliers to be applied to the compaction data entered by the ROCTAB or [ROCKTABH](#__RefHeading___Toc266641_516898843) keywords in the PRROPS section, for when the History Match Gradient option has been activated by the [HMDIMS](#__RefHeading___Toc207753_4219267791) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section

The [ROCKTAB](#__RefHeading___Toc107256_3812137098) keyword defines the rock compaction attributes to be applied for when the rock compaction option has been invoked by the [ROCKCOMP](#__RefHeading___Toc55593_1778172979) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. [ROCKTAB](#__RefHeading___Toc107256_3812137098) defines pore volume and transmissibility multipliers versus pressure that are used in the compaction calculations. If the [RKTRMDIR](#__RefHeading___Toc111812_2939291539) has been activated in the [PROPS](#__RefHeading___Toc39329_784232322) section, then the transmissibility multiplier is directional dependent

This keyword should only be used if compaction option has been enabled.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.
