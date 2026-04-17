### MLANG -- Define Langmuir Maximum Gas Concentration for All Grid Cells

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, MLANG, defines the coal bed methane Langmuir Adsorption[^1] maximum gas concentration for each grid cell used to scale the Langmuir isotherm table allocated to the cell, for when the Coal Bed Methane option has been activated via the COAL keyword in the RUNSPEC section. See the LANGMUIR keyword in the PROPS section for specifying the Langmuir tables for the model.

Note that if he Dual Porosity model has been activated by either the DUALPORO or the DUALPERM keywords in the RUNSPEC section, then MLANG applies to only the matrix grid block.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

[^1]:  Langmuir, Irving (June 1918). \"The Adsorption of Gases on Plane Surface of Glass, Mica and Platinum\". The Research Laboratory of the General Electric Company. 40 (9): 1361--1402. doi:10.1021/ja02242a004
