### MULSGGDV -- Multiply Matrix-Fracture Coupling for Oil-Gas Gravity Drainage for Individual Cells

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, MULSGGDV, defines a constant multiplier to modify the matrix-fracture coupling transmissibility for dual porosity and dual permeability models, for when the alternative matrix-fracture coupling transmissibilities for oil-gas gravity drainage has been selected. The alternative matrix-fracture coupling transmissibilities for oil-gas gravity drainage option is activated via the SIGMAGD or SIGMAGDV keywords in the GRID section, and the dual porosity or dual permeability models are activated by the DUALPORO or DUALPERM keywords in the RUNSPEC section, respectively.

This keyword applies the multiplier for individual cells in model; whereas, the MULSGGD keyword in the SCHEDULE section applies the multiplier to all grid blocks.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
