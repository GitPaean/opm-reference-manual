### EQUALREG -- Sets an Array to a Constant by Region Number

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The EQUALREG keyword sets a specified array to a constant for cells with a specific region number. The region number array can be FLUXNUM, MULTNUM or OPERNUM and these arrays must be defined and be available before the EQUALREG keyword is read by the simulator. The constant can be an integer or real value depending on the array type; however, the arrays that can be operated on are dependent on which section the EQUALREG keyword is being applied in.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | ARRAY | A character string of up to eight characters in length that defines the keyword identifying the array to be modified. | None |
| 2 | CONSTANT | An integer or real value to be assigned to the ARRAY in the same units as the ARRAY property for a given REGION | 0 |
| 3 | REGION<br>NUMBER | REGION NUMBER is a positive integer representing the region for which the CONSTANT in (2) should be applied | None |
| 4 | REGION<br>ARRAY | The REGION ARRAY to use for applying the CONSTANT in (2) based on the REGION NUMBER in (3). REGION ARRAY can have the following values:<br>1)  F for the FLUXNUM array<br>2)  M for the MULTNUM array<br>3)  O for the OPERNUM array | M |
| Notes:<br>1)  Where the REGION NUMBER should be less than or equal to the maximum number of regions as defined on the REGDIMS keyword for the FIPNUM and OPERNUM arrays or the GRIDOPTS keyword for the MULTNUM array in the RUNSPEC section.<br>2)  If the GRIDOPTS keyword is not present in the RUNSPEC section or if the GRIDOPTS keyword is present but the maximum number of MULTNUM regions (NRMULT) equals zero then REGION ARRAY will default to F for the FLUXNUM array.<br>3)  Each record must be terminated by a "/" and the keyword is terminated by a "/". |  |  |  |

Table 6.33: EQUALREG Keyword Description

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

Table 6.34: EQUALREG Keyword Applicable Arrays by Section

#### Example

\-- FIRST DEFINE MULTNUM ARRAYS FOR 10 X 10 X 20 MODEL

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

MULTNUM 1 1\* 1\* 1\* 1\* 1\* 1\* / MULTNUM IN MODEL

MULTNUM 2 1\* 1\* 1\* 1\* 6 6 / MULTNUM IN MODEL

MULTNUM 3 1\* 1\* 1\* 1\* 10 10 / MULTNUM IN MODEL

/

\-- NOW SET PORO AND PERMX BASED ON THE MULTNUM REGION NUMBER

\--

\-- SETS A CONSTANT TO AN ARRAY BASED ON A REGION NUMBER

\--

\-- ARRAY CONSTANT REGION REGION ARRAY

\-- VALUE NUMBER M / F / O EQUALREG

PORO 0.200 1 M /

PORO 0.150 2 M /

PORO 0.120 3 M /

PERMX 100.00 1 M /

PERMX 75.00 2 M /

PERMX 50.00 3 M /

/

The example first defines the MULTNUM array to 1 for all cells in the model, after which selected areas of model are assigned various MULTNUM integer values. The EQUALREG can then be invoked to set constant values for the PORO and PERMX arrays for the various MULTNUM regions.
