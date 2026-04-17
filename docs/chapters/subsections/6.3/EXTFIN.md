### EXTFIN -- Define an External Unstructured Local Grid Refinement

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The EXTFIN keyword defines an external Unstructured Local Grid Refinement ("LGR") in a cell or a group of cells in the global grid, and for when LGRs have been activated for the model using the LGR keyword in the RUNSPEC section. Note the global grid can be either structured, see the EXTREPGL keyword in the GRID section for global structure grids, or unstructured, see the EXTHOST keyword in the GRID section for unstructured global grids.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
