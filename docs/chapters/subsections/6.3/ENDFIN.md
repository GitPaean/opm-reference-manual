### ENDFIN -- End the Definition of a Local Grid Refinement

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The ENDFIN keyword defines the end of a Cartesian or radial local grid refinement ("LGR") definition and a LGR property definition data set. In the GRID section the CARFIN, RADFIN, and RADFIN4 keywords defines the start of an LGR description section, whereas the REFINE keyword in the EDIT, PROPS, REGIONS, SOLUTION and SCHEDULE section defines the start. The REFINE keyword can also be used in the GRID section provided the LGR has been previously specified by the CARFIN, RADFIN, or RADFIN4 keywords.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

The example below is based on using the CARFIN keyword in the GRID section to define an LGR in the global grid, named LGR-OP01 with a maximum of one well allowed in the LGR.

\--

\-- CARFIN LGR GRID COMMANDS

\--

\-- LGR \-\-\-\-- FINE GRID \-\-\-\-\-- \-- CARFIN GRID \-- MAX HOST

\-- NAME I1 I2 J1 J2 K1 K2 NX NY NZ WELLS NAME

CARFIN

LGR-OP01 24 24 87 87 1 50 3 3 50 1 GLOBAL /

ENDFIN

Here the one global cell in the areal plane (24, 87) is divided into three LGR cells in the x-direction and three cells in the y-direction. Since no other property data is given, then the LGR cells take their properties from the host grid, that is the global grid.
