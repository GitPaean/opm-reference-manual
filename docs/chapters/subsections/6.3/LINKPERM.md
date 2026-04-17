### LINKPERM -- Assign Cell Permeabilities to Cell Faces

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The LINKPERM keyword assigns the grid cell permeabilities entered via the PERMX, PERMY and PERMZ keywords to a cell face (I±, J±, or K±) and results in the simulator using these values directly in the calculating the transmissibility between grid blocks. This is different to the conventional way of entering permeability data that consists of entering the cell centered permeability and the simulator calculating a weighted average transmissibility based on the cell centered permeability of the up-stream and down-stream grid blocks.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
