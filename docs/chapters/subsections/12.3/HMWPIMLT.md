### HMWPIMLT -- History Match Well Productivity Index Parameters

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword, [HMWPIMLT](#__RefHeading___Toc256892_373485663), defines the history match gradient parameters for well productiviity indices, for when the History Match Gradient option has been activated by the [HMDIMS](#__RefHeading___Toc207753_4219267791) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Wells must be specified using the WELPSECS keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section and their connections defined by the [COMPDAT](#__RefHeading___Toc97651_3261743917) and/or [COMPDATL](#__RefHeading___Toc153110_63720426) keywords, also in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section

See also the [HMDIMS](#__RefHeading___Toc207753_4219267791) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section that specifies the dimensions for the gradient option, including the maximum number of gradient wellss that can be used with the History Match Gradient option.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
