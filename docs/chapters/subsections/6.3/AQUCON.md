### AQUCON -- Define Numerical Aquifer Connections to the Grid

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

AQUCON keyword defines how numerical aquifers are connected to the simulation grid and these type of aquifers are characterized by the AQUNUM keyword in the GRID section. Analytical aquifers are connected to the simulation grid by the AQUANCON keyword in the GRID section, this includes the Carter-Tracy and Fetkovich analytical aquifers, both of which are implemented in OPM Flow. Both aquifer types dimensions are declared by the AQUDIMS keyword in the RUNSPEC section.

| 1 | AQUID | AQUID is a positive integer greater than or equal to one and less than or equal to the maximum number of numerical aquifers as defined by the MXNAQN variable on the AQUDIMS keyword in the RUNSPEC section, that defines the aquifer to be connected to the grid. | None |
| --- | --- | --- | --- |
| 2 | I1 | A positive integer that defines the lower bound of the cells in the I-direction to be connected to the aquifer and must be greater than or equal to one and less than or equal to I2 and NX. | 1 |
| 3 | I2 | A positive integer that defines the upper bound of the cells in the I-direction to be connected to the aquifer and must be greater than or equal to I1 and less than or equal to NX | NX |
| 4 | J1 | A positive integer that defines the lower bound of the cells in the J-direction to be connected to the aquifer and must be greater than or equal to one and less than or equal to J2 and NY. | 1 |
| 5 | J2 | A positive integer that defines the upper bound of the cells in the J-direction to be connected to the aquifer and must be greater than or equal to JI and less than or equal to NY. | NY |
| 6 | K1 | A positive integer that defines the lower bound of the cells in the K-direction to be to be connected to the aquifer and must be greater than or equal to one and less than or equal to K2 and NZ. | 1 |
| 7 | K2 | A positive integer that defines the upper bound of the cells in the K-direction to be connected to the aquifer and must be greater than or equal to KI and less than or equal to NZ. | NZ |
| 8 | AQUFACE | AQUFACE is a character string that sets the connection "face" of the cells declared by this record and should be set to one of the following:<br>1)  X+, Y+, or Z+ for the positive direction, or X-, Y- or Z- for the negative direction transmissibilities.<br>2)  I+, J+, or K+ for the positive direction, or I-, J- or K- for the negative direction transmissibilities. | None |
| 9 | AQUMULT | AQUMULT is a positive real number greater than or equal to zero that scales the OPM Flow calculated transmissibility between the AQUID aquifer and the grid cell connections defined by this record.<br>The default value of one sets the transmissibility between the aquifer and grid cells to the OPM Flow calculated value. | 1.0 |
| dimensionless | dimensionless | dimensionless |  |
| 10 | AQUOPT1 | AQUOPT1 is a defined integer value set to either zero or one, that defines the area to be used in calculating the connection transmissibility between the aquifer and the grid cells:<br>1)  A value of zero means the cross-sectional defined on the AQUNUM keyword will be used, whereas,<br>2)  A value of one means the cross-sectional defined by the grid cell connections defined by this record will be used. | 0 |
| dimensionless | dimensionless | dimensionless |  |
| 11 | AQUOPT2 | AQUOPT2 is a character string that sets the cell face connection and should be set to one of the following:<br>1)  YES: Aquifer connections *can adjoin* to active cells allowing for connections inside the reservoir grid. It is not recommended to use this option without thoroughly checking the connections in the model.<br>2)  NO: Aquifer connections *cannot adjoin* to active cells preventing connections inside the reservoir grid. This is the recommended and the default value. | NO |
| 12 | VEOPT1 | Vertical Equilibrium Option Number 1-- Not Used | 1 |
| 13 | VEOPT2 | Vertical Equilibrium Option Number 2-- Not Used | 1 |
| Notes:<br>1)  Where NX, NY and NZ are the dimensions of the model as defined on the DIMENS keyword in the RUNSPEC section.<br>2)  Each record must be terminated by a "/" and the keyword is terminated by a "/". |  |  |  |

Table 6.8: AQUCON Keyword Description

#### Example

The following example defines numerical aquifer number one connected to the I+ face of various cells in the model.

\--

\-- NUMERICAL AQUIFER CONNECTIONS

\--

\-- ID \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\-- CONNECT TRANS TRANS ADJOIN

\-- NUMBER I1 I2 J1 J2 K1 K2 FACE MULT OPTN CELLS

AQUCON

1 57 57 28 36 46 58 \'I+\' 1\* 1\* \'NO\' /

1 111 111 38 41 22 31 \'I+\' 1\* 1\* \'NO\' /

1 96 96 44 49 22 31 \'I+\' 1\* 1\* \'NO\' /

1 43 43 28 35 54 58 \'I+\' 1\* 1\* \'NO\' /

1 98 98 38 42 32 40 \'I+\' 1\* 1\* \'NO\' /

1 79 79 41 67 5 11 \'I+\' 1\* 1\* \'NO\' /

1 61 61 48 72 12 17 \'I+\' 1\* 1\* \'NO\' /

/

See the AQUNUM keyword in the GRID section for a complete example on defining and connecting a numerical aquifer to a simulation grid.
