### MLANGSLV -- Define Langmuir Maximum Solvent Concentration for All Grid Cells

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, MLANGSLV, defines the coal bed methane Langmuir Adsorption[^1] maximum solvent concentration for each grid cell used to scale the Langmuir isotherm solvent table allocated to the cell, for when the Coal Bed Methane option has been activated via the COAL keyword in the RUNSPEC section. In addition, the Solvent phase must have been declared by the SOLVENT keyword in the RUNSPEC section. See the COALNUM keyword in the GRID section for allocating the Langmuir solvent tables to the grid blocks, and also the LANGMUIR keyword in the PROPS section for defining the Langmuir Adsorption Isotherm tables. Keywords COALADS and COALPP, also in the PROPS section, are used to specify the relative adsorption data in runs containing the solvent phase.

Note that if he Dual Porosity model has been activated by either the DUALPORO or the DUALPERM keywords in the RUNSPEC section, then MLANGSLV applies to only the matrix grid block.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

[^1]:  Langmuir, Irving (June 1918). \"The Adsorption of Gases on Plane Surface of Glass, Mica and Platinum\". The Research Laboratory of the General Electric Company. 40 (9): 1361--1402. doi:10.1021/ja02242a004
