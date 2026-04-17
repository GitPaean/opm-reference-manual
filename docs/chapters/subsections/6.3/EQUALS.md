### EQUALS -- Sets a Specified Array to a Constant

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The EQUALS keyword sets a specified array or part of an array to a constant. The constant can be an integer or real value depending on the array type; however, the arrays that can be operated on are dependent on which section the EQUALS keyword is being applied in.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | ARRAY | A character string of up to eight characters in length that defines the keyword identifying the property to be modified. | None |
| 2 | CONSTANT | An integer or real value that the ARRAY will be set to in the same units as the ARRAY property. | None |
| 3 | I1 | A positive integer that defines the lower bound of the array in the I-direction to be modified must be greater than or equal to one and less than or equal to I2 and NX. | 1 |
| 4 | I2 | A positive integer that defines the upper bound of the array in the I-direction to be modified must be greater than or equal to II and less than or equal to NX | NX |
| 5 | J1 | A positive integer that defines the lower bound of the array in the J-direction to be modified must be greater than or equal to one and less than or equal to J2 and NY. | 1 |
| 6 | J2 | A positive integer that defines the upper bound of the array in the J-direction to be modified must be greater than or equal to JI and less than or equal to NY. | NY |
| 7 | K1 | A positive integer that defines the lower bound of the array in the K-direction to be modified must be greater than or equal to one and less than or equal to K2 and NZ. | 1 |
| 8 | K2 | A positive integer that defines the upper bound of the array in the K-direction to be modified must be greater than or equal to KI and less than or equal to NZ. | NZ |
| Notes:<br>1)  Where NX, NY and NZ are the dimensions of the model as defined on the DIMENS keyword in the RUNSPEC section.<br>2)  Each record must be terminated by a "/" and the keyword is terminated by a "/". |  |  |  |

Table 6.35: EQUALS Keyword Description

Examples of the arrays most commonly operated on in each section are given in . Cells colored red indicate arrays that are not supported by OPM Flow operations.

| DX | DEPTH | SWL | ENDNUM | PRESSURE |  |  |
| --- | --- | --- | --- | --- | --- | --- |
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

Table 6.36: EQUALS Keyword Applicable Arrays by Section

#### Examples

The first example resets the PERMX, PERMY and PERMZ, arrays to 0.10, 0.10, and 0.01 for all cells in layer five, respectively.

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\- I1 I2 J1 J2 K1 K2

EQUALS

PERMX 0.1000 1\* 1\* 1\* 1\* 5 5 / PERMX TO 0.10 IN LAYER 5

PERMY 0.1000 1\* 1\* 1\* 1\* 5 5 / PERMY TO 0.10 IN LAYER 5

PERMZ 0.0100 1\* 1\* 1\* 1\* 5 5 / PERMZ TO 0.01 IN LAYER 5

/

The second example illustrates how to correctly setup a Cartesian Regular Grid in OPM Flow, given the DIMENS keyword in the RUNSPEC section is set to:

\--

\-- MAX MAX MAX

\-- NDIVIX NDIVIY NDIVIZ

DIMENS

10 10 3 /

and the following keywords in the GRID section:

\--

\-- ACTIVATE IRREGULAR CORNER-POINT GRID TRANSMISSIBILITIES

\--

OLDTRAN

\--

\-- DEFINE GRID BLOCK X DIRECTION CELL SIZE (BASED ON NX = 5)

\--

DX

300\*1000 /

\--

\-- DEFINE GRID BLOCK Y DIRECTION CELL SIZE (BASED ON NY = 5)

\--

DY

300\*1000 /

\--

\-- DEFINE GRID BLOCK SIZES IN THE Z DIRECTION

\--

DZ

100\*20 100\*30 100\*50 /

\--

\-- DEFINE GRID BLOCK TOPS FOR THE TOP LAYER

\--

TOPS

100\*8325 /

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

PERMX 500.000 1\* 1\* 1\* 1\* 1 1 / Layer #01 Properties

PERMY 500.000 /

PERMZ 20.000 /

PORO 0.300 /

NTG 1.000 /

PERMX 50.000 1\* 1\* 1\* 1\* 2 2 / Layer #02 Properties

PERMY 50.000 /

PERMZ 50.000 /

PORO 0.300 /

NTG 1.000 /

PERMX 200.000 1\* 1\* 1\* 1\* 3 3 / Layer #03 Properties

PERMY 200.000 /

PERMZ 200.000 /

PORO 0.300 /

NTG 1.000 /

/

Notice that the DX, DY, DZ and TOPS keywords are defined separately, that is they are not included in the EQUALS keyword.
