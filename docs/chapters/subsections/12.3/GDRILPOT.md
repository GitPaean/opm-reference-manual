### GDRILPOT -- Define Group Potential Rates for Automatic Drilling

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword, [GDRILPOT](#__RefHeading___Toc262268_156692946), defines the minimum group potential rate that will result in a well from the one of the automatic drilling queues, as defined by either the [QDRILL](#__RefHeading___Toc614222_501926209) or [WDRILPRI](#__RefHeading___Toc442117_2026549522) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, to be drilled and placed on production. The advantage of using a group's potential, as oppose to a minimum rate limit, is that setting the potential greater than the group's minimum flow rate, will result in well being drilled in time to support the desired production rate.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
