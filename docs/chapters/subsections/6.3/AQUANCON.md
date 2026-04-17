### AQUANCON -- Define Analytical Connections to the Grid

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The AQUANCON keyword defines how analytical aquifers are connected to the simulation grid, this includes the Carter-Tracy, Fetkovich and Constant Flux analytical aquifers, all of which are implemented in OPM Flow. Carter-Tracy analytical aquifers are characterized by the AQUCT keyword in the GRID section and Fetkovich analytical aquifers are defined by the AQUFETP keyword in the SOLUTION section. Finally, the Constant Flux aquifer is defined by the AQUFLUX keyword in SOLUTION section.

Note that numerical aquifers are connected to the grid using the AQUCON keyword in the GRID section and that both aquifer types dimensions are declared by the AQUDIMS keyword in the RUNSPEC section.

| 1 | AQUID | AQUID is a positive integer greater than or equal to one and less than the maximum number of analytical aquifers as defined by the NANAQU variable on the AQUDIMS keyword in the RUNSPEC section, that defines the aquifer to be connected to the grid. | None |
| --- | --- | --- | --- |
| 2 | I1 | A positive integer that defines the lower bound of the cells in the I-direction to be connected to the aquifer and must be greater than or equal to one and less than or equal to I2 and NX. | 1 |
| 3 | I2 | A positive integer that defines the upper bound of the cells in the I-direction to be connected to the aquifer and must be greater than or equal to I1 and less than or equal to NX | NX |
| 4 | J1 | A positive integer that defines the lower bound of the cells in the J-direction to be connected to the aquifer and must be greater than or equal to one and less than or equal to J2 and NY. | 1 |
| 5 | J2 | A positive integer that defines the upper bound of the cells in the J-direction to be connected to the aquifer and must be greater than or equal to JI and less than or equal to NY. | NY |
| 6 | K1 | A positive integer that defines the lower bound of the cells in the K-direction to be to be connected to the aquifer and must be greater than or equal to one and less than or equal to K2 and NZ. | 1 |
| 7 | K2 | A positive integer that defines the upper bound of the cells in the K-direction to be connected to the aquifer and must be greater than or equal to KI and less than or equal to NZ. | NZ |
| 8 | AQUFACE | AQUFACE is a character string that sets the connection "face" of the cells declared by this record and should be set to one of the following:<br>1)  X+, Y+, or Z+ for the positive direction, or X-, Y- or Z- for the negative direction transmissibilities.<br>2)  I+, J+, or K+ for the positive direction, or I-, J- or K- for the negative direction transmissibilities. | None |
| 9 | AQUFLUX | AQUFLUX is a positive real value that sets the fraction of the total influx between the aquifer and the defined cells declared on this keyword. If defaulted the cell face area for each cell is applied and if a value is declared then this value is applied to all cells declared by this record. | 1\* |
| ft^2^ | m^2^ | cm^2^ |  |
| 10 | AQUCOEF | AQUCOEF is a real positive values that scales the calculated connection between the aquifer and the cells declared on this record. | 1.0 |
| dimensionless | dimensionless | dimensionless |  |
| 11 | AQUOPT | AQUOPT is a character string that sets the cell face connection and should be set to one of the following:<br>1)  YES: Aquifer connections *can adjoin* to active cells allowing for connections inside the reservoir grid. It is not recommended to use this option without thoroughly checking the connections in the model.<br>2)  NO: Aquifer connections *cannot adjoin* to active cells preventing connections inside the reservoir grid. This is the recommended and the default value. | NO |
| Notes:<br>1)  Where NX, NY and NZ are the dimensions of the model as defined on the DIMENS keyword in the RUNSPEC section.<br>2)  Each record must be terminated by a "/" and the keyword is terminated by a "/". |  |  |  |

Table 6.7: AQUANCON Keyword Description

#### Example

The following example defines aquifer number one connected to the I+ face of various cells in the model.

\--

\-- ANALYTIC AQUIFER CONNECTION

\--

\-- ID \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\-- CONNECT AQF AQF ADJOIN

\-- NUMBER I1 I2 J1 J2 K1 K2 FACE INFLX MULTI CELLS

AQUANCON

1 57 57 28 36 46 58 \'I+\' 1\* 1\* \'NO\' /

1 111 111 38 41 22 31 \'I+\' 1\* 1\* \'NO\' /

1 96 96 44 49 22 31 \'I+\' 1\* 1\* \'NO\' /

1 43 43 28 35 54 58 \'I+\' 1\* 1\* \'NO\' /

1 98 98 38 42 32 40 \'I+\' 1\* 1\* \'NO\' /

1 79 79 41 67 5 11 \'I+\' 1\* 1\* \'NO\' /

1 61 61 48 72 12 17 \'I+\' 1\* 1\* \'NO\' /

/

See the AQUCT keyword in the GRID section for a complete example on defining and connecting a Carter-Tracy aquifer to a simulation grid.
