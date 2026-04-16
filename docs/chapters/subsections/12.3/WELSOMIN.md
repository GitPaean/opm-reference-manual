### WELSOMIN -- Define Well Connection Minimum Oil Saturation for Opening

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[WELSOMIN](#__RefHeading___Toc1005090_487874538) defines a minimum oil saturation for a well connection above which the connection will be opened automatically. If the grid block connection is below [WELSOMIN](#__RefHeading___Toc1005090_487874538) then connection will not be automatically opened. Automatic opening of connection is controlled by the STATUS parameter on the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. Note that if the [COMPLUMP](#__RefHeading___Toc97655_3261743917) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section has been used to lump connections into completions then [WELSOMIN](#__RefHeading___Toc1005090_487874538) is compared to the average oil saturation of the completion.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
