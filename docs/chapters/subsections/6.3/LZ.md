### LZ -- Dual Porosity Viscous Displacement Z Direction Matrix Size for All Cells

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The LZ keyword defines the size of "representative" matrix grid blocks in the Z direction via an array in dual porosity and dual permeability runs, for when the VISCD keyword has been used in the RUNSPEC section to activate the dual porosity viscous displacement option. In addition, either the DUALPORO or DUALPERM keyword should be entered in the RUNSPEC section to activate the dual porosity or dual permeability models. The VISCD option is used to model the viscous displacement of fluids from the matrix by the fracture pressure gradient, for when the fracture system has a more moderate permeability, and flow to and from the matrix caused by the fracture pressure gradient acts as an additional production mechanism.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | LZ | LZ is an array of real numbers describing the "representative" cell size in the Z direction for each cell in the model.<br>Repeat counts may be used, for example 10\*100.0. | 0 |
| feet | m | cm |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x (NZ/2) parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.57: LZ Keyword Description

If the VISCD keyword has been used to activate the Dual Porosity Viscous Displacement option and LZ has not been specified then LZ is set to zero in the calculation of the viscous displacement term.

See also the LX, LY and LTOSIGMA keywords in the GRID section.

#### Example

\--

\-- DEFINE INPUT BOX FOR EDITING INPUT ARRAYS

\--

\-- \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

BOX

10 10 1 6 1 1 / DEFINE BOX AREA

\--

\-- DEFINE DUAL POROSITY VISCOUS DISPLACEMENT Z DIRECTION MATRIX SIZE

\--

LZ

6\*3.0 /

\--

\-- DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS

\--

ENDBOX

The example defines a subset of the grid and the size of the "representative" matrix cells in the Y direction to 15.0 ft.; after which the ENDBOX keyword resets the input to be the full grid.
