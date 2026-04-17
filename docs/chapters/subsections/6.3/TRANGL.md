### TRANGL -- Define Non-Neighbor Connections Between Global and LGR Cells Manually

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

TRANGL enables Non-Neighbor Connections ("NNC") between the global cells and the Local Grid Refinement ("LGR") cells to be manually specified, as oppose to the simulator calculating the transmissibilities. The LGR keyword in the RUNSPEC section should be utilized to define the presence of LGRs in the model and to define various LGR dimension parameters.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | I1 | A positive integer that defines the LGR grid block in the I-direction in a non-neighbor connection, must be greater than or equal to one and less than or equal to NX on the CARFIN keyword in the GRID section. | None |
| --- | --- | --- | --- |
| 2 | J1 | A positive integer that defines the LGR grid block in the J-direction in a non-neighbor connection, must be greater than or equal to one and less than or equal to NY on the CARFIN keyword in the GRID section. | None |
| 3 | K1 | A positive integer that defines the LGR grid block in the K-direction in a non-neighbor connection, must be greater than or equal to one and less than or equal to NZ on the CARFIN keyword in the GRID section. | None |
| 4 | I2 | A positive integer that defines the GLOBAL grid block in the I-direction in a non-neighbor connection, must be greater than or equal to one and less than or equal to NX on the DIMENS keyword in the RUNSPEC section. | None |
| 5 | J2 | A positive integer that defines the GLOBAL grid block in the J-direction in a non-neighbor connection, must be greater than or equal to one and less than or equal to NY on the DIMENS keyword in the RUNSPEC section. | None |
| 6 | K2 | A positive integer that defines the GLOBAL grid block in the K-direction in a non-neighbor connection, must be greater than or equal to one and less than or equal to NZ on the DIMENS keyword in the RUNSPEC section. | None |
| 7 | TRANSNNC | TRANSNNC is a positive real number greater than or equal to zero that defines the transmissibility between the GLOBAL grid block (I1, J1, K1) and the LGR grid block (I2, J2, K2).<br>The default value of zero sets the transmissibility between the two cells to zero. | 0.0 |
| cP.rb/day/psia | cP.rm^3^/day/bars | cP.rcc/hr/atm |  |
| Notes:<br>1)  Each record must be terminated by a "/" and the keyword is terminated by a "/". |  |  |  |

Table 6.130: TRANGL Keyword Description

#### Example

\--

\-- MANUALLY DEFINE LGR-GLOBAL GRID NON-NEIGHBOR CONNECTIONS

\--

\-- \-\-\--LGR\-\-\-\-- \-\--GLOBAL\-\-\-- \-- TRANSNCC \--

\-- I1 J1 K1 I2 J2 K2

TRANGL

1 1 1 1 1 2 0.2500 /

1 1 2 1 1 3 0.2500 /

1 1 3 1 1 4 0.2500 /

/

The above example defines the transmissibility between LGR cell (1, 1, 1) and global cell (1, 1, 2), LGR cell (1, 1, 2) and global cell (1, 1, 3) and finally between LGR cell (1, 1, 3) and global cell (1, 1, 4) to be 0.2500.
