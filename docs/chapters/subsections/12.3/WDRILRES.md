### WDRILRES -- Activate Prevention of Multi-Completions in the Same Cell for Queued Wells

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [WDRILRES](#__RefHeading___Toc447101_2026549522) keyword activates the prevention of multi-completions being completed in the same cell for wells in a drilling queue. Setting this option stops any well defined as a queued well via the [QDRILL](#__RefHeading___Toc614222_501926209) and WDRILLPRI keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, or any wells set to automatic opening by setting the STATUS variable to AUTO on the [WCONPROD](#__RefHeading___Toc146754_4203985108) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, from opening if there is an already existing active well connection to a cell.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
