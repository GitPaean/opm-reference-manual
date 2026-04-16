### VISCD -- Activate Dual Porosity Viscous Displacement Option

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [VISCD](#__RefHeading___Toc486166_3181922006) keyword activates the Dual Porosity Viscous Displacement option for dual porosity and dual permeability models, and therefore requires either the [DUALPORO](#__RefHeading___Toc241173_1772380413) or [DUALPERM](#__RefHeading___Toc241171_1772380413) keyword to be entered in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section to activate either one of these options. The [VISCD](#__RefHeading___Toc486166_3181922006) option is used to model the viscous displacement of fluids from the matrix by the fracture pressure gradient, for when the fracture system has a more moderate permeability, and flow to and from the matrix caused by the fracture pressure gradient acts as an additional production mechanism[^1]. Normally this mechanism is ignored as the pressure gradient in the fracture system is small due to the very high permeability of the fracture system. See the [LX](#__RefHeading___Toc499449_3181922006), [LY](#__RefHeading___Toc499451_3181922006) and [LZ](#__RefHeading___Toc499453_3181922006) keywords in the [GRID](#__RefHeading___Toc38674_784232322) section that define representative matrix grid block sizes.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

\--

\-- ACTIVATE DUAL POROSITY VISCOUS DISPLACEMENT OPTION

\--

VISCD

The above example activates the dual porosity viscous displacement option.

[^1]: Gilman, J. R. and Kazemi, H. "Improved Calculation for Viscous and Gravity Displacement in Matrix Blocks in Dual-Porosity Simulators," paper SPE 16010 (includes a number of associated papers), Journal of Petroleum Technology (1988) 40, No. 1, 60-70.
