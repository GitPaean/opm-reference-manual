### NODPPM -- Deactivate Fracture Porosity-Permeability Calculation

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [NODPPM](#__RefHeading___Toc256454_718033703) keyword deactivates the default behavior of multiplying the fracture porosity by the fracture permeability to calculate the effective fracture permeability in dual porosity and dual permeability runs. Either the [DUALPORO](#__RefHeading___Toc241173_1772380413) or [DUALPERM](#__RefHeading___Toc241171_1772380413) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section must be declared in the input file in order to use this keyword. If the default calculation is switched off by this keyword, then the effective fracture permeability is taken to be those entered for the fracture using the [PERMX](#__RefHeading___Toc45791_719036256), [PERMY](#__RefHeading___Toc45793_719036256) and [PERMZ](#__RefHeading___Toc45795_719036256) keywords in the [GRID](#__RefHeading___Toc38674_784232322) section. If the keyword is absent from the input deck, then the entered [PERMX](#__RefHeading___Toc45791_719036256), [PERMY](#__RefHeading___Toc45793_719036256) and [PERMZ](#__RefHeading___Toc45795_719036256) arrays for the fractures are multiplied by fracture [PORO](#__RefHeading___Toc45797_719036256) array values in order to obtain the effective fracture permeability.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- DEACTIVATE FRACTURE POROSITY-PERMEABILITY CALCULATION

\--

NODPPM

The above example switches off the default behavior of multiplying the fracture porosity by the fracture permeability to calculate the effective fracture permeability.
