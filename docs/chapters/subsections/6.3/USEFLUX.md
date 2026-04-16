### USEFLUX -- Activate Flux Boundary Model and Define Flux File

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [USEFLUX](#__RefHeading___Toc1709193_4250154414) keyword activates the Flux Boundary model and defines the name of the FLUX file. Only grid blocks that have been declared by the [FLUXREG](#__RefHeading___Toc290821_803326780) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section to be in an active flux region, are active for the run.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
