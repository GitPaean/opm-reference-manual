### NOHYST -- Deactivate the Hysteresis Option

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [NOHYST](#__RefHeading___Toc268481_718033703) keyword deactivates the Hysteresis option and informs the simulator to ignore the [IMBNUM](#__RefHeading___Toc129665_83452205) array in the [REGIONS](#__RefHeading___Toc40648_784232322) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- DEACTIVATE THE HYSTERESIS OPTION

\--

NOHYST

The above example switches off the default behavior of multiplying the fracture porosity by the fracture permeability to calculate the effective fracture permeability.
