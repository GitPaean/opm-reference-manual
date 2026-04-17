### OPERATER -- Define Mathematical Operations on Arrays by Region

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The OPERATER keyword is similar to the OPERATE keyword, except it applies the mathematical operation on specific regions, whereas, OPERATE applies the operations on a cell by cell basis. Here the OPERATER keyword performs a mathematical operation on a specified property array, optionally using another property array as input to the function. The keyword allows for various mathematical functions and their associated variables to be defined and applied to the specified region data. Input constants can be integer or real valued depending on the array type; however, the arrays that can be operated on are dependent on which section the OPERATER keyword is being applied in.

| 1 | Y | A character string of up to eight characters in length that defines the keyword identifying the array to be modified. | None |
| --- | --- | --- | --- |
| 2 | REGION | REGION is a positive integer representing the region for which the EQUATION should be applied. The default is to use the region number from the OPERNUM keyword; however this can be reset to another region array via the ARRAY item on this keyword, provided the array exists at the time the keyword is declared in the input deck.<br>Note also the OPERNUM keyword must precede the use of the OPERATER keyword. | 0 |
| 3 | EQUATION | A defined character string of up to eight characters that defines the mathematical function to be applied, using the X array and the ALPHA and BETA constants declared on this keyword. EQUATION should be set to one of the following character strings: | None |
| 'MULTA' -<br>'POLY' -<br>'SLOG' -<br>'LOG10' -<br>'LOGE' -<br>'INV' -<br>'MULTX' - | 'ADDX' -<br>'COPY' -<br>'MAXLIM' -<br>'MINLIM' -<br>'MULTP' -<br>'ABS' -<br>'MULTIPLY' - |  |  |
| 4 | X | A character string of up to eight characters in length that defines the keyword identifying the array to be used as an input parameter. | None |
| 5 | ALPHA | An integer or real value that is the α variable in the EQUATION function. | None |
| 6 | BETA | An integer or real value that is the β variable in the EQUATION function. | None |
| 7 | ARRAY | The name of the array for which the REGION variable references. This can be any standard region array as declared in the REGION section (FIPNUM, PVTNUM, etc.), provided the array exists at the time the OPERATER keyword is invoked. In addition, the MULTNUM, FLUXNUM and OPERNUM may be used.<br>Only the default value of OPERNUM is supported by OPM Flow. | OPERNUM |
| Notes:<br>1)  Where the REGION should be less than or equal to the maximum number of regions as defined on the REGDIMS keyword for the FIPNUM and OPERNUM arrays or the GRIDOPTS keyword for the MULTNUM array in the RUNSPEC section..<br>2)  Each record must be terminated by a "/" and the keyword is terminated by a "/". |  |  |  |

Table 6.96: OPERATER Keyword Description

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

Table 6.97: OPERATER Keyword Applicable Arrays by Section

Double precision and integer work arrays may also be used to hold temporary values for use in more complex operations. Note that these work arrays are reset to zero at the start of each section of the data file. The names of the double precision work arrays should be of the form \'WORKn\', where n is a positive integer that defines the work array index, for example \'WORK1\', \'WORK2\', and so on. Similarly, the names of integer work arrays should be of the form \'IWORKn\', for example \'IWORK1\', \'IWORK2\', and so on. OPM Flow currently only supports double precision work arrays, and does not currently support using work arrays with \"global\" arrays (MULTZ\*). Note that the permeability arrays (PERM\*) are treated as \"global\" arrays in the GRID section only. In the commercial simulator the maximum number of double precision and integer work arrays are specified using the REGDIMS keyword. Whereas, OPM Flow does not impose a limit on the maximum number of work arrays.

Note that care should be exercised when performing operations on integer array data as all transforms are performed using floating point arithmetic operations. In addition, operations on any of the transmissibility arrays (TRANX, TRANX-, TRANY, TRANY-, TRANZ, and TRANZ-) may result in unintended consequences as these arrays have zero values on the boundary of the grid. In this use OPM ResInsight to verify and visually inspect the results.

#### Example

The first example uses the MULTP function combined with the Net-to-Gross (NTG) array to re-scale the MULTX, MULTY and MULTZ arrays to reduce the transmissibility in three separate reservoirs based on the reservoir quality (NTG). This keyword sequence should be in the GRID section.

\--

\-- MATHEMATICAL OPERATIONS ON ARRAYS BY REGION

\--

\-- OUTPUT REGN OPERATION SOURCE ALPHA BETA REGN

\-- ARRAY NUM TYPE ARRAY CONST CONST ARRAY

OPERATER

MULTX 1 \'MULTP\' NTG 1.00 0.75 / RES1

MULTY 1 \'MULTP\' NTG 1.00 0.75 / RES1

MULTZ 1 \'MULTP\' NTG 1.00 0.75 / RES1

MULTX 2 \'MULTP\' NTG 1.00 0.85 / RES2

MULTY 2 \'MULTP\' NTG 1.00 0.85 / RES2

MULTZ 2 \'MULTP\' NTG 1.00 0.85 / RES2

MULTX 3 \'MULTP\' NTG 1.00 0.50 / RES3

MULTY 3 \'MULTP\' NTG 1.00 0.50 / RES3

MULTZ 3 \'MULTP\' NTG 1.00 0.50 / RES3

/

Notice that the ARRAY variable has been defaulted, resulting in OPERNUM being the regional array for the REGION variable.

The next example shows how to set the maximum gas saturation (SGU) based on the minimum (lowest) water saturation (SWL) when using the End-Point Scaling option, in the PROPS section.

\--

\-- MATHEMATICAL OPERATIONS ON ARRAYS

\--

\-- OUTPUT REGN OPERATION SOURCE ALPHA BETA REGN

\-- ARRAY NUM TYPE ARRAY CONST CONST ARRAY

OPERATER

SGU 1 \'MULTA\' SWL -1.0 1.0 /

SGU 2 \'MULTA\' SWL -1.0 1.0 /

SGU 3 \'MULTA\' SWL -1.0 1.0 /

/

The above example sets the maximum gas saturation to be one minus the minimum water saturation for regions one to three.

The final example shows how to reset the FIPNUM array when the exported array from the earth model does not correspond to the simulator's desired numbering scheme.

\--

\-- MATHEMATICAL OPERATIONS ON ARRAYS BY REGION

\--

\-- RESET FIPNUM BASED ON MULTNUM AND OPERNUM

\--

\-- DESTIN REGN OPERATION SOURCE ALPHA BETA INPUT SEGNUM EQUIL

\-- ARRAY NUM TYPE ARRAY CONST CONST ARRAY NUMBER NUMBER

OPERATER

FIPNUM 26 \'MULTA\' \'MULTNUM\' 0.00 1 / 26 1

FIPNUM 44 \'MULTA\' \'MULTNUM\' 0.00 2 / 44 2

FIPNUM 62 \'MULTA\' \'MULTNUM\' 0.00 3 / 62 3

FIPNUM 98 \'MULTA\' \'MULTNUM\' 0.00 4 / 98 4

FIPNUM 116 \'MULTA\' \'MULTNUM\' 0.00 5 / 116 5

FIPNUM 134 \'MULTA\' \'MULTNUM\' 0.00 6 / 134 6

FIPNUM 46 \'MULTA\' \'MULTNUM\' 0.00 7 / 46 7

FIPNUM 64 \'MULTA\' \'MULTNUM\' 0.00 8 / 64 8

FIPNUM 82 \'MULTA\' \'MULTNUM\' 0.00 9 / 82 9

FIPNUM 226 \'MULTA\' \'MULTNUM\' 0.00 10 / 226 10

FIPNUM 262 \'MULTA\' \'MULTNUM\' 0.00 11 / 262 11

FIPNUM 280 \'MULTA\' \'MULTNUM\' 0.00 12 / 280 12

FIPNUM 298 \'MULTA\' \'MULTNUM\' 0.00 13 / 298 13

FIPNUM 33 \'MULTA\' \'MULTNUM\' 0.00 14 / 33 14

FIPNUM 51 \'MULTA\' \'MULTNUM\' 0.00 15 / 51 15

FIPNUM 105 \'MULTA\' \'MULTNUM\' 0.00 16 / 105 16

FIPNUM 159 \'MULTA\' \'MULTNUM\' 0.00 17 / 159 17

FIPNUM 195 \'MULTA\' \'MULTNUM\' 0.00 18 / 195 18

FIPNUM 267 \'MULTA\' \'MULTNUM\' 0.00 19 / 267 19

FIPNUM 303 \'MULTA\' \'MULTNUM\' 0.00 20 / 303 20

FIPNUM 321 \'MULTA\' \'MULTNUM\' 0.00 21 / 321 21

FIPNUM 339 \'MULTA\' \'MULTNUM\' 0.00 22 / 339 22

FIPNUM 54 \'MULTA\' \'MULTNUM\' 0.00 23 / 54 23

FIPNUM 72 \'MULTA\' \'MULTNUM\' 0.00 24 / 72 24

FIPNUM 108 \'MULTA\' \'MULTNUM\' 0.00 25 / 108 25

FIPNUM 144 \'MULTA\' \'MULTNUM\' 0.00 26 / 144 26

FIPNUM 270 \'MULTA\' \'MULTNUM\' 0.00 27 / 270 27

/

Note that operation can only be done in the REGION section as FIPNUM is only available for use in this section and that the ARRAY variable has been defaulted, resulting in OPERNUM being the regional array for the REGION variable.
