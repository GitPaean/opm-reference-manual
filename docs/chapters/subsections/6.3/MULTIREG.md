### MULTIREG -- Multiply an Array by a Constant based on a Region Number

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The MULTIREG keyword multiplies an array or part of an array by a constant for cells with a specific region number. The region number array can be FLUXNUM, MULTNUM or OPERNUM and these arrays must be defined and be available before the MULTIREG keyword is read by the simulator. The constant can be an integer or real value depending on the array type; however, the arrays that can be operated on are dependent on which section the MULTIREG keyword is being applied in.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | ARRAY | A character string of up to eight characters in length that defines the keyword identifying the array to be modified. | None |
| 2 | CONSTANT | An integer or real value to multiply the ARRAY by in the same units as the ARRAY property for a given REGION. | 0 |
| 3 | REGION<br>NUMBER | REGION NUMBER is a positive integer representing the region for which the CONSTANT in (2) should be applied. | None |
| 4 | REGION<br>ARRAY | The REGION ARRAY to use for applying the CONSTANT in (2) based on the REGION NUMBER in (3). REGION ARRAY can have the following values:<br>1)  F for the FLUXNUM array<br>2)  M for the MULTNUM array<br>3)  O for the OPERNUM array | M |
| Notes:<br>1)  Where the REGION NUMBER should be less than or equal to the maximum number of regions as defined on the REGDIMS keyword for the FIPNUM and OPERNUM arrays or the GRIDOPTS keyword for the MULTNUM array in the RUNSPEC section.<br>2)  If the GRIDOPTS keyword is not present in the RUNSPEC section or if the GRIDOPTS keyword is present but the maximum number of MULTNUM regions (NRMULT) equals zero then REGION ARRAY will default to F for the FLUXNUM array.<br>3)  Each record must be terminated by a "/" and the keyword is terminated by a "/". |  |  |  |

Table 6.70: MULTIREG Keyword Description

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

Table 6.71: MULTIREG Keyword Applicable Arrays by Section

#### Example

\--

\-- FIRST DEFINE THE PROPERTY ARRAYS AND MULTNUM ARRAYS FOR 10 X 10 X 20 MODEL

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

PORO 0.2000 1\* 1\* 1\* 1\* 1\* 1\* / PORO TO 0.20 IN MODEL

PERMX 100.00 1\* 1\* 1\* 1\* 1\* 1\* / PERMX TO 0.10 IN MODEL

MULTNUM 1 1\* 1\* 1\* 1\* 1\* 1\* / MULTNUM IN MODEL

MULTNUM 2 1\* 5 1 5 6 6 / MULTNUM IN MODEL

MULTNUM 3 1\* 1\* 1\* 1\* 10 10 / MULTNUM IN MODEL

/

\--

\-- NOW RESET PORO AND PERMX BASED ON THE MULTNUM REGION NUMBER

\--

\-- MULTIPLY AN ARRAY BY A CONSTANT BASED ON A REGION NUMBER

\--

\-- ARRAY CONSTANT REGION REGION ARRAY

\-- VALUE NUMBER M / F / O

MULTIREG

PORO 1.050 1 M /

PORO 1.100 2 M /

PORO 0.950 3 M /

PERMX 1.25 1 M /

PERMX 1.30 2 M /

PERMX 0.90 3 M /

/

The example first defines the PORO and PERMX property arrays for the model and then sets the MULTNUM array to 1 for all cells in the model, after which selected areas of model are assigned various MULTNUM integer values. The MULTIREG can then be invoked to multiply the PORO and PERMX arrays by a constant for the various MULTNUM regions.
