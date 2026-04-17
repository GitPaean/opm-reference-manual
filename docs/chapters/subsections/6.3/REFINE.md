### REFINE -- Start the Definition of a Local Grid Refinement

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The REFINE keyword defines the start of a Cartesian or radial Local Grid Refinement ("LGR") definition that sets the properties of the selected LGR. The keyword is then followed by the property keywords associated with the section where the keyword is being invoked. For example, if the REFINE keyword is used in the GRID section then most of the keywords in that section can be used to set the grid properties for the LGR.

The ENDFIN keyword is used to terminate the LGR definition.

There is no data required for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
