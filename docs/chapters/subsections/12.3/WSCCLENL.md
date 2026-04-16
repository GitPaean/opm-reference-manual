### WSCCLENL -- Well Deposited Scale Adjustment (LGR)

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WSCCLENL](#__RefHeading___Toc950266_4263943340) keyword adjusts the amount of scale currently accumulated around a well's well connections for wells located in a Local Grid Refinement (\"LGR\"). For example, if a workover has been performed on a well to remove (or reduce) the deposited scale over the perforations, then this keyword can be used to implement the effects of the workover. Scale deposits reduce the productivity of well and this relationship is defined in the [SCDPTAB](#__RefHeading___Toc644093_516898843) and [SCDATAB](#__RefHeading___Toc618634_516898843) keywords in [SCHEDULE](#__RefHeading___Toc43945_784232322) section. The tables are allocated to a well via the [WSCTAB](#__RefHeading___Toc957314_4263943340) keyword, which is also in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. Note that the Scale Deposition option must have been activated by declaring the dimensions of the scaling deposition tables using the [SCDPDIMS](#__RefHeading___Toc637730_516898843) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

See also the [WSCCLEAN](#__RefHeading___Toc950264_4263943340) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section that performs similar functionality for wells located in the global grid.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
