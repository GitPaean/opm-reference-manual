### HMMULTFT -- History Match Fault Transmissibility Gradient Cumulative Multipliers

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[HMMULTFT](#__RefHeading___Toc219832_373485663) defines the history match fault transmissibility gradient cumulative multipliers to be applied to the fault transmissibilities for faults declared by the FAULT keyword in the [GRID](#__RefHeading___Toc38674_784232322) section, for when the History Match Gradient option has been activated by the [HMDIMS](#__RefHeading___Toc207753_4219267791) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The keyword allows for the re-scaling of the existing fault transmissibilities calculated by OPM Flow, or if the [MULTFLT](#__RefHeading___Toc90875_3218818441) keyword has been entered, then [HMMULTFT](#__RefHeading___Toc219832_373485663) is applied to the existing [MULTFLT](#__RefHeading___Toc90875_3218818441) multipliers.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
