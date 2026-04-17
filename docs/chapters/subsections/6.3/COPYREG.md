### COPYREG -- Copy an Array to Another Array based on a Region Number

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The COPYREG keyword copies a specified array or part of an array based on cells with a specific region number to another array. The region number array can be FLUXNUM, MULTNUM or OPERNUM and these arrays must be defined and be available before the COPYREG keyword is read by the simulator. The property arrays can be real or integer valued depending on the property array type; however, the property arrays that can be operated on are dependent on which section the COPYREG keyword is being applied in.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | ARRAY-1 | A character string of up to eight characters in length that defines the keyword identifying the array to be copied from. | None |
| 2 | ARRAY-2 | A character string of up to eight characters in length that defines the keyword identifying the array to be copied to. | None |
| 3 | REGION<br>NUMBER | Integer REGION NUMBER is the region for which the array data in (1) should be copied to array data in (2). | None |
| 4 | REGION<br>ARRAY | The REGION ARRAY to use for selecting the REGION NUMBER in (3) for selecting the data to be copied. REGION ARRAY can have the following values:<br>1)  F for the FLUXNUM array<br>2)  M for the MULTNUM array<br>3)  O for the OPERNUM array | M |
| Notes:<br>1)  Where the REGION NUMBER should be less than or equal to the maximum number of regions as defined on the REGDIMS keyword for the FIPNUM and OPERNUM arrays or the GRIDOPTS keyword for the MULTNUM array in the RUNSPEC section.<br>2)  If the GRIDOPTS keyword is not present in the RUNSPEC section or if the GRIDOPTS keyword is present but the maximum number of MULTNUM regions (NRMULT) equals zero then REGION ARRAY will default to F for the FLUXNUM array.<br>3)  Each record must be terminated by a "/" and the keyword is terminated by a "/". |  |  |  |

Table 6.20: COPYREG Keyword Description

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

Table 6.21: COPYREG Keyword Applicable Arrays by Section

#### Example

\--

\-- COPY AN ARRAY TO ANOTHER ARRAY BASED ON A REGION NUMBER

\--

\-- ARRAY ARRAY REGION REGION ARRAY

\-- FROM TO NUMBER M / F / O

COPYREG

PERMX PERMY 1 M / COPY PERMX TO PERMY

PERMX PERMZ 1 M / COPY PERMX TO PERMZ

/

\--

\-- NOW RESET PERMZ BASED ON THE MULTNUM REGION NUMBER

\--

\--

\-- MULTIPLY AN ARRAY BY A CONSTANT BASED ON A REGION NUMBER

\--

\-- ARRAY CONSTANT REGION REGION ARRAY

\-- VALUE NUMBER M / F / O

MULTIREG

PERMX 0.95 1 M /

/

The above example first copies the PERMX property array for region number one to the PERMY and PERMZ property arrays for region one using the MULTNUM array to define the region numbers. After which PERMZ property array for region one is multiplied by 0.5 using the MULTIREG keyword.
