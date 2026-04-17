### COPYBOX -- Copy Array Data Defined by a Box

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The COPYBOX keyword copies an array (or part of an array) to another part of the same array. The array can be real or integer depending on the array type; however, the array that can be operated on is dependent on which section the COPYBOX keyword is being used.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | ARRAY-1 | The name of the array to be copied<br>This is the keyword name identifying the property and is up to eight characters in length and enclosed in quotes. | None |
| --- | --- | --- | --- |
| 2 | I1 | A positive integer that defines the SOURCE lower bound of the array in the I-direction to be modified must be greater than or equal 1 and less than or equal to I2 and NX. | 1 |
| 3 | I2 | A positive integer that defines the SOURCE upper bound of the array in the I-direction to be modified must be greater than or equal to II and less than or equal to NX | NX |
| 4 | J1 | A positive integer that defines the SOURCE lower bound of the array in the J-direction to be modified must be greater than or equal 1 and less than or equal to J2 and NY. | 1 |
| 5 | J2 | A positive integer that defines the SOURCE upper bound of the array in the J-direction to be modified must be greater than or equal to JI and less than or equal to NY. | NY |
| 6 | K1 | A positive integer that defines the SOURCE lower bound of the array in the K-direction to be modified must be greater than or equal to one and less than or equal to K2 and NZ. | 1 |
| 7 | K2 | A positive integer that defines the SOURCE upper bound of the array in the K-direction to be modified must be greater than or equal to KI and less than or equal to NZ. | NZ |
| 8 | I3 | A positive integer that defines the DESTINATION lower bound of the array in the I-direction to be modified must be greater than or equal 1 and less than or equal to I2 and NX. | 1 |
| 9 | I4 | A positive integer that defines the DESTINATION upper bound of the array in the I-direction to be modified must be greater than or equal to II and less than or equal to NX | NX |
| 10 | J3 | A positive integer that defines the DESTINATION lower bound of the array in the J-direction to be modified must be greater than or equal 1 and less than or equal to J2 and NY. | 1 |
| 11 | J4 | A positive integer that defines the DESTINATION upper bound of the array in the J-direction to be modified must be greater than or equal to JI and less than or equal to NY. | NY |
| 12 | K3 | A positive integer that defines the DESTINATION lower bound of the array in the K-direction to be modified must be greater than or equal to one and less than or equal to K2 and NZ. | 1 |
| 13 | K4 | A positive integer that defines the DESTINATION upper bound of the array in the K-direction to be modified must be greater than or equal to KI and less than or equal to NZ. | NZ |
| Notes:<br>1)  Where NX, NY and NZ are the dimensions of the model as defined on the DIMENS keyword in the RUNSPEC section.<br>2)  Each record must be terminated by a "/" and the keyword is terminated by a "/". |  |  |  |

Table 6.18: COPYBOX Keyword Description

Note that the SOURCE and DESTINATION arrays must be of the same size in all dimensions and the applicable arrays for each section are defined in .

| GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- |
| DX |  | SWL | ENDNUM |  |  |  |
| DY |  | SWCR | EQLNUM |  |  |  |
| DZ |  | SWU | FIPNUM |  |  |  |
| PERMX |  | SGL | IMBNUM |  |  |  |
| PERMY |  | SGCR | MISCNUM |  |  |  |
| PERMZ |  | SGU | PVTNUM |  |  |  |
| MULTX |  | KRW | ROCKNUM |  |  |  |
| MULTY |  | KRO | SATNUM |  |  |  |
| MULTZ |  | KRG | WH2NUM |  |  |  |
| DR |  | PCG |  |  |  |  |
| DTHETA |  | PCW |  |  |  |  |
| PERMR |  |  |  |  |  |  |
| PERMTHT |  |  |  |  |  |  |
| DZNET |  |  |  |  |  |  |
| PORO |  |  |  |  |  |  |
| NTG |  |  |  |  |  |  |
| FLUXNUM |  |  |  |  |  |  |
| MULTNUM |  |  |  |  |  |  |
| MPFANUM |  |  |  |  |  |  |
| DIFFX |  |  |  |  |  |  |
| DIFFY |  |  |  |  |  |  |
| DIFFZ |  |  |  |  |  |  |
| DIFFR |  |  |  |  |  |  |
| DIFFTHT |  |  |  |  |  |  |

Table 6.19: COPYBOX Keyword Applicable Arrays by Section

#### Example

\--

\-- SOURCE \-\-\-\-\-- SOURCE BOX \-\-\-\-\-- \-\-\-- DESTINATION BOX \-\-\--

\-- ARRAY I1 I2 J1 J2 K1 K2 I1 I2 J1 J2 K1 K2

COPYBOX

PORO 1\* 1\* 1\* 1\* 12 14 1\* 1\* 1\* 1\* 15 17 / PORO

PERMX 1\* 1\* 1\* 1\* 12 14 1\* 1\* 1\* 1\* 15 17 / PERMX

/

The above example copies all the PORO and PERMX values in layers 12 to 14 to layers 15 and 17.
