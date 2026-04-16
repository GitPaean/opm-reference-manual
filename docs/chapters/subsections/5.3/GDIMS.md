### GDIMS -- Activate Instantaneous Gradient Option and Define Dimensions

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [GDIMS](#__RefHeading___Toc256824_156692946) keyword activates the Instantaneous Gradient option and defines the maximum dimensions as used by the [GWRTWCV](#__RefHeading___Toc251585_870710203) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. The Instantaneous Gradient option calculates derivatives of solution quantities at the current time step with respect to variations in the variables at the *current time step*. This is different to Gradient option that calculates the derivatives of solution quantities at the current time step with respect to variations in the variables at the initial* time step*, that is a time equal to zero. Consequently, the Instantaneous Gradient option can be switched on and off by the [GUPFREQ](#__RefHeading___Toc246071_870710203) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, whereas the Gradient option cannot.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
