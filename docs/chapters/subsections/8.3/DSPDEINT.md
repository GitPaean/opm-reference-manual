### DSPDEINT -- Activate Brine Tracer Dispersion Interpolation by Water Density

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword, [DSPDEINT](#__RefHeading___Toc220511_1772380413), activates the brine tracer dispersion interpolation by water density option for when the Brine phase is activated in the model by the [BRINE](#__RefHeading___Toc162083_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section and the [DISPERSE](#__RefHeading___Toc184339_1772380413) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section is in the input file. They keyword cause the lookup and interpolation of the [DISPERSE](#__RefHeading___Toc184339_1772380413) tracer concentration to water density, that is the tracer concentration data on the [DISPERSE](#__RefHeading___Toc184339_1772380413) keyword has been replaced by the water density data.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
