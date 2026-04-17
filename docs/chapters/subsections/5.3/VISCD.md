### VISCD -- Activate Dual Porosity Viscous Displacement Option

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The VISCD keyword activates the Dual Porosity Viscous Displacement option for dual porosity and dual permeability models, and therefore requires either the DUALPORO or DUALPERM keyword to be entered in the RUNSPEC section to activate either one of these options. The VISCD option is used to model the viscous displacement of fluids from the matrix by the fracture pressure gradient, for when the fracture system has a more moderate permeability, and flow to and from the matrix caused by the fracture pressure gradient acts as an additional production mechanism[^1]. Normally this mechanism is ignored as the pressure gradient in the fracture system is small due to the very high permeability of the fracture system. See the LX, LY and LZ keywords in the GRID section that define representative matrix grid block sizes.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

\--

\-- ACTIVATE DUAL POROSITY VISCOUS DISPLACEMENT OPTION

\--

VISCD

The above example activates the dual porosity viscous displacement option.

[^1]: Gilman, J. R. and Kazemi, H. "Improved Calculation for Viscous and Gravity Displacement in Matrix Blocks in Dual-Porosity Simulators," paper SPE 16010 (includes a number of associated papers), Journal of Petroleum Technology (1988) 40, No. 1, 60-70.
