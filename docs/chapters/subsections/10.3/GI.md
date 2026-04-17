### GI -- Define the Initial Equilibration Gi Values for All Grid Blocks

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The GI keyword defines the initial equilibration GI values for all grid cells in the model and should be used in conjunction with the other enumeration equilibration keywords; PBUB, PDEW, PRESSURE, RS, RV, SOIL and SWAT keywords etc., to fully describe the initial state of the model. The keyword should only be used if the GI Pseudo Compositional option has been activated in the model via the GIMODEL keyword in the RUNSPEC section.

This is the non-standard method to initialize the model via enumeration and is seldom employed in the industry. The standard methodology is for OPM Flow to initialize a model using the parameters on the EQUIL keyword combined with other keywords to fully describe the initial state of the model. The keyword can be used with all grid types.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

See also the GIALL keyword in the PROPS section that sets the GI values as a function of pressure, as well as setting the corresponding RVGI, RSGI, BGGI and BOGI values at the same time.
