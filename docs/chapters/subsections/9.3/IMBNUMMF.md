### IMBNUMMF -- Define the Imbibition Saturation Table Region Numbers (Matrix-Fracture)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The IMBNUMMF keyword defines the imbibition saturation tables (relative permeability and capillary pressure tables) region numbers for flow between the matrix and fracture blocks, for when the HYSTER option on the SATOPTS keyword has been invoked to activate the Hysteresis option, and the Dual Porosity or Dual Permeability models have been activated via the DUALPORO or DUALPERM keywords. All keywords are in the RUNSPEC section.

The region number specifies which set of relative permeability tables (SGFN, SWFN, SOF2, SOF3, SOF32D, SGOF, SLGOF and SWOF) are used to calculate the relative permeability and capillary pressure between the matrix and fracture blocks. The keyword is optional and any cell not assigned a value will use the assignment from the IMBNUM array.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
