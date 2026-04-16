### WSCTAB -- Assign Well Scale Deposition and Scale Damage Tables

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[WSCTAB](#__RefHeading___Toc957314_4263943340) assigns scale deposition and scale damage tables to a well, for when the Scale Deposition option has been activated by declaring the dimensions of the scaling deposition tables using the [SCDPDIMS](#__RefHeading___Toc637730_516898843) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Scale deposits reduce the productivity of well and this relationship is defined in the [SCDPTAB](#__RefHeading___Toc644093_516898843) and [SCDATAB](#__RefHeading___Toc618634_516898843) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, and are allocated to a well by the [WSCTAB](#__RefHeading___Toc957314_4263943340) keyword.

See also the [WPIMULT](#__RefHeading___Toc121645_2412586160) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section that adjusts a well's productivity index by a constant value.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
