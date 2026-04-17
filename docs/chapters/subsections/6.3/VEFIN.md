### VEFIN -- Activate Vertical Equilibrium Model (LGR)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

If the VE keyword in the RUNSPEC section has been used to activate the Vertical Equilibrium ("VE") model for the global grid, then the VEFIN keyword may used to set various options for the Local Grid Refinements ("LGR"). The LGR keyword in the RUNSPEC section should be activated to indicate the presence of LGRs and the keyword VEFIN should be placed in between the CARFIN and ENDFIN keywords in the GRID section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
