### SURFACTW -- Activate the Surfactant Phase with Wettability Changes in the Model

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword indicates that the surfactant phase is present in the model and to activate the surfactant flooding mode with Changes to Wettability option activated as well. The keyword will also invoke data input file checking to ensure that all the required surfactant phase input parameters are defined in the input deck. See also the [SURFACT](#__RefHeading___Toc863854_4250154414) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section that actives the surfactant phase only, that is without the Changes to the Wettability option.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

\--

\-- ACTIVATE THE SURFACTANT PHASE WITH WETTABILITY CHANGES IN THE MODEL

\--

SURFACTW

The above example declares that the surfactant phase is active in the model together with the wettability changes.
