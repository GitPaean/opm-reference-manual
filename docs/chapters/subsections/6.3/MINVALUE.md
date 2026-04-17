### MINVALUE -- Set a Minimum Value for an Array Element

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The MINVALUE keyword sets a minimum value for the specified array or part of an array. The constant can be an integer or real value depending on the array type; however, the arrays that can be operated on are dependent on which section the MINVALUE keyword is being applied in.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | ARRAY | A character string of up to eight characters in length that defines the keyword identifying the array to be modified. | None |
| 2 | CONSTANT | CONSTANT is a positive integer or positive real value that an ARRAY element will be reset to if an element in the defined input BOX, as defined by items (3) to (8), is less than CONSTANT.<br>CONSTANT has in the same units as the ARRAY property. | None |
| 3 | I1 | A positive integer that defines the lower bound of the array in the I-direction to be modified must be greater than or equal to one and less than or equal to I2 and NX. | 1 |
| 4 | I2 | A positive integer that defines the upper bound of the array in the I-direction to be modified must be greater than or equal to I1 and less than or equal to NX | NX |
| 5 | J1 | A positive integer that defines the lower bound of the array in the J-direction to be modified must be greater than or equal to one and less than or equal to J2 and NY. | 1 |
| 6 | J2 | A positive integer that defines the upper bound of the array in the J-direction to be modified must be greater than or equal to J1 and less than or equal to NY. | NY |
| 7 | K1 | A positive integer that defines the lower bound of the array in the K-direction to be modified must be greater than or equal to one and less than or equal to K2 and NZ. | 1 |
| 8 | K2 | A positive integer that defines the upper bound of the array in the K-direction to be modified must be greater than or equal to K1 and less than or equal to NZ. | NZ |
| Notes:<br>1)  Where NX, NY and NZ are the dimensions of the model as defined on the DIMENS keyword in the RUNSPEC section.<br>2)  Each record must be terminated by a "/" and the keyword is terminated by a "/". |  |  |  |

Table 6.65: MINVALUE Keyword Description

Examples of the arrays most commonly operated on in each section are given in . Cells colored red indicate arrays that are not supported by OPM Flow operations.

| GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- |
| DX | DEPTH | SWL |  |  |  |  |
| DY | PORV | SWCR |  |  |  |  |
| DZ | TRANX | SWU |  |  |  |  |
| PERMX | TRANY | SGL |  |  |  |  |
| PERMY | TRANZ | SGCR |  |  |  |  |
| PERMZ | DIFFX | SGU |  |  |  |  |
| MULTX | DIFFY | KRW |  |  |  |  |
| MULTY | DIFFZ | KRO |  |  |  |  |
| MULTZ | TRANR | KRG |  |  |  |  |
| DR | TRANTHT | PCG |  |  |  |  |
| DTHETA | DIFFR | PCW |  |  |  |  |
| PERMR | DIFFTHT |  |  |  |  |  |
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

Table 6.66: MINVALUE Keyword Applicable Arrays by Section

#### Example

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

MINVALUE

PERMX 1.0E0 1\* 1\* 1\* 1\* 1\* 1\* / MINIMUM PERMX

PERMY 1.0E0 1\* 1\* 1\* 1\* 1\* 1\* / MINIMUM PERMY

PERMZ 1.0E-1 1\* 1\* 1\* 1\* 1\* 1\* / MINIMUM PERMZ

/

The above example resets the minimum values for the PERMX, PERMY and PERMZ, arrays to 1.0, 1.0 and 0.1, respectively, for all cells.
