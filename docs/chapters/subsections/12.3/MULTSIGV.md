### MULTSIGV -- Multiply Matrix-Fracture Coupling for Individual Cells

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, MULTSIGV, defines a constant multiplier to modify the matrix-fracture coupling transmissibility for dual porosity and dual permeability models, for when the matrix-fracture coupling transmissibilities have been specified via the SIGMAGD or SIGMAGDV keywords in the GRID section, and the dual porosity or dual permeability models have activated by the DUALPORO or DUALPERM keywords in the RUNSPEC section, respectively.

This keyword applies the multiplier for individual cells in model; whereas, the MULTSIG keyword in the SCHEDULE section applies the multiplier to all grid blocks.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
