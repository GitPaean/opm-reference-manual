### NXFIN -- Define the Number of LGR Grid Blocks in the X-Direction

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

NXFIN defines the number of Local Grid Refinement ("LGR") cells within a global or host cell in the x-direction via a vector, as opposed to defining the size for each cell for a Cartesian LGR Grid. The LGR keyword in the RUNSPEC section should be activated to indicate an LGR is being used, and the keyword NXFIN should be placed in between the CARFIN and ENDFIN keywords in the GRID section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | NXFIN | NXFIN is a vector of integer numbers describing the number of LGR cells within each defined global or host grid block in the x-direction in a Cartesian LGR grid.<br>Repeat counts may be used, for example 2\*2.0. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the NX parameter on the CARFIN keyword in the GRID section.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.91: NXFIN Keyword Description

See also the CARFIN, ENDFIN, NYFIN, and NZFIN keywords in the GRID section to fully define a Cartesian LGR grid model.

#### Example

\--

\-- CARFIN LGR GRID COMMANDS

\--

\-- LGR \-\-\-\-- HOST GRID \-\-\-\-\-- \-- CARFIN GRID \-- MAX HOST

\-- NAME I1 I2 J1 J2 K1 K2 NX NY NZ WELLS NAME

CARFIN

LGR-OP01 24 25 87 87 1 50 8 1 50 1 GLOBAL /

\--

\-- DEFINE LGR GRID BLOCKS IN THE X-DIRECTION

\--

NXFIN

4 4 /

ENDFIN

The above example splits the global cells (24-25,87, 1-50) into four and four LGR grid blocks in the x-direction, and since the HXFIN keyword has not been supplied, then the host cells will split into equal proportions.
