### USENOFLO -- Activate Flux Boundary Model Without a Flux File

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The USENOFLUX keyword activates the Flux Boundary model without a FLUX file. The [USEFLUX](#__RefHeading___Toc1709193_4250154414) keyword should still be in the input deck, but in this case the FLUX filename is ignored. The option is useful when the no-flow boundary condition is a reasonable assumption and avoids the pre-cursor run used to generate the FLUX file via the [DUMPFLUX](#__RefHeading___Toc65329_3218818441) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section. Only grid blocks that have been declared by the [FLUXREG](#__RefHeading___Toc290821_803326780) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section to be in an active flux region, are active for the run.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

\--

\-- ACTIVATE FLUX BOUNDARY MODEL WITHOUT A FLUX FILE

\--

USEFLUX

/

USENOFLO

The above example activates the Flux Boundary model without a FLUX file.
