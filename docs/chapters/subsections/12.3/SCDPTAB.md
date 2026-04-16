### SCDPTAB -- Well Connection Scale Deposition Tables

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[SCDATAB](#__RefHeading___Toc618634_516898843) defines the well connection scale deposition rate as a function of sea water flow rate, for when the Scale Deposition option has been activated by declaring the dimensions of the scaling deposition tables using the [SCDPDIMS](#__RefHeading___Toc637730_516898843) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The [SCDATAB](#__RefHeading___Toc618634_516898843) tables are allocated to individual wells using the [WSCTAB](#__RefHeading___Toc957314_4263943340) keyword and the sea water fraction is based on a water tracer entered via the [SCDPTRAC](#__RefHeading___Toc644103_516898843) keyword; both keywords are in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
