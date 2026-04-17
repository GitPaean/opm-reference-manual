### LANGSOLV -- Langmuir Adsorption Isotherm Solvent Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The LANGMUIR keyword defines the coal bed methane Langmuir Adsorption Isotherms[^1] Solvent tables, for when the Coal Bed Methane option has been activated via the COAL keyword and the Solvent phase has been declared by the SOLVENT keyword in the RUNSPEC section. See the COALNUM keyword in the GRID section for allocating the Langmuir solvent tables to the grid blocks, and also the LANGMUIR keyword in the PROPS section for defining the Langmuir Adsorption Isotherm tables. Keywords COALADS and COALPP, also in the PROPS section, are used to specify the relative adsorption data in runs containing the solvent phase.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

[^1]:  Langmuir, Irving (June 1918). \"The Adsorption of Gases on Plane Surface of Glass, Mica and Platinum\". The Research Laboratory of the General Electric Company. 40 (9): 1361--1402. doi:10.1021/ja02242a004
