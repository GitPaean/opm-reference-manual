### COPY -- Copy Array Data to Another Array

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The COPY keyword copies an array (or part of an array) to another array or part of an array. The arrays can be integer or real valued; however, the arrays that can be operated on are dependent on which section the COPY keyword is being applied in.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | ARRAY-1 | A character string of up to eight characters in length that defines the keyword identifying the array to be copied from. | None |
| 2 | ARRAY-2 | A character string of up to eight characters in length that defines the keyword identifying the array to be copied to. | None |
| 3 | I1 | A positive integer that defines the lower bound of the array in the I-direction to be modified must be greater than or equal 1 and less than or equal to I2 and NX. | 1 |
| 4 | I2 | A positive integer that defines the upper bound of the array in the I-direction to be modified must be greater than or equal to II and less than or equal to NX | NX |
| 5 | J1 | A positive integer that defines the lower bound of the array in the J-direction to be modified must be greater than or equal 1 and less than or equal to J2 and NY. | 1 |
| 6 | J2 | A positive integer that defines the upper bound of the array in the J-direction to be modified must be greater than or equal to JI and less than or equal to NY. | NY |
| 7 | K1 | A positive integer that defines the lower bound of the array in the K-direction to be modified must be greater than or equal to one and less than or equal to K2 and NZ. | 1 |
| 8 | K2 | A positive integer that defines the upper bound of the array in the K-direction to be modified must be greater than or equal to KI and less than or equal to NZ. | NZ |
| Notes:<br>1)  Where NX, NY and NZ are the dimensions of the model as defined on the DIMENS keyword in the RUNSPEC section.<br>2)  Each record must be terminated by a "/" and the keyword is terminated by a "/". |  |  |  |

Table 6.16: COPY Keyword Description

Examples of the arrays most commonly operated on in each section are given in . Cells colored red indicate arrays that are not supported by OPM Flow operations.

| GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- |
| DX | DEPTH | SWL | ENDNUM | PRESSURE |  |  |
| DY | PORV | SWCR | EQLNUM | SWAT |  |  |
| DZ | TRANX | SWU | FIPNUM | SGAS |  |  |
| PERMX | TRANY | SGL | IMBNUM | RV |  |  |
| PERMY | TRANZ | SGCR | MISCNUM | RS |  |  |
| PERMZ | DIFFX | SGU | PVTNUM | TBLK |  |  |
| MULTX | DIFFY | KRW | ROCKNUM | GI |  |  |
| MULTY | DIFFZ | KRO | SATNUM | OILAPI |  |  |
| MULTZ | TRANR | KRG | WH2NUM | SALT |  |  |
| DR | TRANTHT | PCG |  | GASCONC |  |  |
| DTHETA | DIFFR | PCW |  | SOLVCONC |  |  |
| PERMR | DIFFTHT |  |  | SOLVFRAC |  |  |
| PERMTHT |  |  |  | SFOAM |  |  |
| DZNET |  |  |  | SPOLY |  |  |
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

Table 6.17: COPY Keyword Applicable Arrays by Section

#### Example

\--

\-- SOURCE DESTIN. \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

COPY

PERMX PERMY 1\* 1\* 1\* 1\* 1\* 1\* / CREATE PERMY

PERMX PERMZ 1\* 1\* 1\* 1\* 1\* 1\* / CREATE PERMZ

/

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

MULTIPLY

PERMZ 0.50000 1\* 1\* 1\* 1\* 1\* 1\* / PERMZ \* 0.5

/

The above example copies PERMX array to the PERMY and PERMZ arrays in the GRID section for all grid blocks in the model. The PERMZ array is then multiplied by 0.5 for all grid blocks in the model.
