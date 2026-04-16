### TEMP -- Activate the Temperature Modeling Option

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword activates the temperature modeling option.

In OPM Flow\'s thermal model ([THERMAL](#__RefHeading___Toc137276_650382403) keyword) enthalpy is conserved and the energy equations are solved fully implicitly with the black-oil equations. Whereas, in OPM Flow\'s temperature model ([TEMP](#__RefHeading___Toc146397_3544483072) keyword) internal energy is conserved (the work term is neglected and internal energy is equal to enthalpy) and the energy equations are solved sequentially after the black-oil equations. Note that the thermal model can be modified so that internal energy rather than enthalpy is conserved by setting the command line option \--conserve-inner-energy-thermal=true (the default is false). If properties like density or viscosity \"strongly\" depend on temperature, the thermal model is recommended.

There is no data required for this keyword and there is no terminating "/" for this keyword.

The temperature option ([TEMP](#__RefHeading___Toc146397_3544483072) keyword) and the thermal option ([THERMAL](#__RefHeading___Toc137276_650382403) keyword) are two separate modeling facilities in the commercial simulator, although some keywords can be used by both options, for example the [RTEMP](#__RefHeading___Toc111816_2939291539) keyword. OPM Flow's temperature model is not directly equivalent to either the commercial simulator's black-oil [TEMP](#__RefHeading___Toc146397_3544483072) or compositional [THERMAL](#__RefHeading___Toc137276_650382403) formulation.

The energy black-oil implementation in OPM Flow uses a mixture of the commercial simulators black-oil and the commercial simulators "compositional thermal" keywords, as well as some OPM Flow specific keywords.

#### Example

\--

\-- ACTIVATE THE TEMPERATURE MODELING OPTION (OPM FLOW TEMPERATURE OPTION ONLY)

\--

TEMP

The above example activates the temperature modeling option.
