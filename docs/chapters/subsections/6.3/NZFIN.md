### NZFIN -- Define the Number of LGR Grid Blocks in the Z-Direction

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

NZFIN defines the number of Local Grid Refinement ("LGR") cells within a global or host cell in the z-direction via a vector, as opposed to defining the size for each cell for a Cartesian LGR Grid. The LGR keyword in the RUNSPEC section should be activated to indicate an LGR is being used, and the keyword NXFIN should be placed in between the CARFIN and ENDFIN keywords in the GRID section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | NZFIN | NZFIN is a vector of integer numbers describing the number of LGR cells within each defined global or host grid block in the x-direction in a Cartesian LGR grid.<br>Repeat counts may be used, for example 2\*2.0. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the NX parameter on the CARFIN keyword in the GRID section.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.93: NZFIN Keyword Description

See also the CARFIN, ENDFIN, NXFIN, and NYFIN keywords in the GRID section to fully define a Cartesian LGR grid model.

#### Example

\--

\-- CARFIN LGR GRID COMMANDS

\--

\-- LGR \-\-\-\-- HOST GRID \-\-\-\-\-- \-- CARFIN GRID \-- MAX HOST

\-- NAME I1 I2 J1 J2 K1 K2 NX NY NZ WELLS NAME

CARFIN

LGR-OP01 24 24 86 86 1 50 8 1 100 1 GLOBAL /

\--

\-- DEFINE LGR GRID BLOCKS IN THE Z-DIRECTION

\--

NZFIN

50\*2 /

ENDFIN

The above example splits the global cells (24, 86, 1-50) into two LGR grid blocks per host cell in the z-direction, and since the HZFIN keyword has not been supplied, then the host cells will split into equal proportions.
