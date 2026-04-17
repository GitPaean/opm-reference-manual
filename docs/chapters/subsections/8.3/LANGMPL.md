### LANGMPL -- Define Langmuir Pressure Grid Cell Multiplier

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, LANGMPL, defines the coal bed methane Langmuir Adsorption[^1] pressure multiplier for each grid block, for when the Coal Bed Methane option has been activated via the COAL keyword in the RUNSPEC section. The keyword applies the multiplier to the pressure values in a cell's allocated Langmuir table when calculating a cell's adsorption capacity. See the LANGMUIR keyword in the PROPS section for specifying the Langmuir tables for the model.

Note that if he Dual Porosity model has been activated by either the DUALPORO or the DUALPERM keywords in the RUNSPEC section, then LANGMPL applies to only the matrix grid block.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

[^1]:  Langmuir, Irving (June 1918). \"The Adsorption of Gases on Plane Surface of Glass, Mica and Platinum\". The Research Laboratory of the General Electric Company. 40 (9): 1361--1402. doi:10.1021/ja02242a004
