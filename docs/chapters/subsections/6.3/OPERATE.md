### OPERATE -- Define Mathematical Operations on Arrays

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The OPERATE keyword performs a mathematical operation on a specified array or part of an array, optionally using another specified array as input to the operation. The keyword allows for various mathematical functions and their associated variables to be defined and applied to the specified array. Input constants can be integer or real valued depending on the array type; however, the arrays that can be operated on are dependent on which section the OPERATE keyword is being applied in.

| 1 | Y | A character string of up to eight characters in length that defines the keyword identifying the array to be modified. | None |
| --- | --- | --- | --- |
| 2 | I1 | A positive integer that defines the lower bound of the array in the I-direction to be modified must be greater than or equal to one and less than or equal to I2 and NX. | 1 |
| 3 | I2 | A positive integer that defines the upper bound of the array in the I-direction to be modified must be greater than or equal to I1 and less than or equal to NX | NX |
| 4 | J1 | A positive integer that defines the lower bound of the array in the J-direction to be modified must be greater than or equal to one and less than or equal to J2 and NY. | 1 |
| 5 | J2 | A positive integer that defines the upper bound of the array in the J-direction to be modified must be greater than or equal to J1 and less than or equal to NY. | NY |
| 6 | K1 | A positive integer that defines the lower bound of the array in the K-direction to be modified must be greater than or equal to one and less than or equal to K2 and NZ. | 1 |
| 7 | K2 | A positive integer that defines the upper bound of the array in the K-direction to be modified must be greater than or equal to K1 and less than or equal to NZ. | NZ |
| 8 | EQUATION | A defined character string of up to eight characters that defines the mathematical function to be applied, using the X array and the ALPHA and BETA constants declared on this keyword. EQUATION should be set to one of the following character strings: | None |
| 'MULTA' -<br>'POLY' -<br>'SLOG' -<br>'LOG10' -<br>'LOGE' -<br>'INV' -<br>'MULTX' - | 'ADDX' -<br>'COPY' -<br>'MAXLIM' -<br>'MINLIM' -<br>'MULTP' -<br>'ABS' -<br>'MULTIPLY' - |  |  |
| 9 | X | A character string of up to eight characters in length that defines the keyword identifying the array to be used as an input parameter. | None |
| 10 | ALPHA | An integer or real value that is the α variable in the EQUATION function. | None |
| 11 | BETA | An integer or real value that is the β variable in the EQUATION function. | None |
| Notes:<br>1)  Where NX, NY and NZ are the dimensions of the model as defined on the DIMENS keyword in the RUNSPEC section.<br>2)  Each record must be terminated by a "/" and the keyword is terminated by a "/". |  |  |  |

Table 6.94: OPERATE Keyword Description

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

Table 6.95: OPERATE Keyword Applicable Arrays by Section

Double precision and integer work arrays may also be used to hold temporary values for use in more complex operations. Note that these work arrays are reset to zero at the start of each section of the data file. The names of the double precision work arrays should be of the form \'WORKn\', where n is a positive integer that defines the work array index, for example \'WORK1\', \'WORK2\', and so on. Similarly, the names of integer work arrays should be of the form \'IWORKn\', for example \'IWORK1\', \'IWORK2\', and so on. OPM Flow currently only supports double precision work arrays, and does not currently support using work arrays with \"global\" arrays (MULTZ\*). Note that the permeability arrays (PERM\*) are treated as \"global\" arrays in the GRID section only. In the commercial simulator the maximum number of double precision and integer work arrays are specified using the REGDIMS keyword. Whereas, OPM Flow does not impose a limit on the maximum number of work arrays.

Note that care should be exercised when performing operations on integer array data as all transforms are performed using floating point arithmetic operations. In addition, operations on any of the transmissibility arrays (TRANX, TRANX-, TRANY, TRANY-, TRANZ, and TRANZ-) may result in untended consequences as these arrays have zero values on the boundary of the grid. In this use OPM ResInsight to verify and visually inspect the results.

#### Example

The first example uses the MULTP function combined with the Net-to-Gross (NTG) array to re-scale the MULTX, MULTY and MULTZ arrays to reduce the transmissibility in three separate reservoirs based on the reservoir quality (NTG).

\--

\-- MATHEMATICAL OPERATIONS ON ARRAYS BY CELL

\--

\-- OUTPUT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\-- OPERATION INPUT ALPHA BETA

\-- ARRAY I1 I2 J1 J2 K1 K2 \-\-\-\-\-\-\-\-- ARRAY \-\-\-\-- \-\-\--

OPERATE

MULTX 1\* 1\* 1\* 1\* 1 32 'MULTP' NTG 1.00 0.75 / RES1

MULTY 1\* 1\* 1\* 1\* 1 32 'MULTP' NTG 1.00 0.75 / RES1

MULTZ 1\* 1\* 1\* 1\* 1 32 'MULTP' NTG 1.00 0.75 / RES1

MULTX 1\* 1\* 1\* 1\* 34 64 'MULTP' NTG 1.00 0.85 / RES2

MULTY 1\* 1\* 1\* 1\* 34 64 'MULTP' NTG 1.00 0.85 / RES2

MULTZ 1\* 1\* 1\* 1\* 34 64 'MULTP' NTG 1.00 0.85 / RES2

MULTX 1\* 1\* 1\* 1\* 67 96 'MULTP' NTG 1.00 0.50 / RES3

MULTY 1\* 1\* 1\* 1\* 67 96 'MULTP' NTG 1.00 0.50 / RES3

MULTZ 1\* 1\* 1\* 1\* 67 96 'MULTP' NTG 1.00 0.50 / RES3

/

The next example shows how to set the maximum gas saturation (SGU) based on the minimum (lowest) water saturation (SWL) when using the End-Point Scaling option.

\--

\-- MATHEMATICAL OPERATIONS ON ARRAYS

\--

\-- OUTPUT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\-- OPERATION INPUT ALPHA BETA

\-- ARRAY I1 I2 J1 J2 K1 K2 \-\-\-\-\-\-\-\-- ARRAY \-\-\-\-- \-\-\--

OPERATE

SGU 1\* 1\* 1\* 1\* 1\* 1\* \'MULTA\' SWL -1.0 1.0 /

/

The above example sets the maximum gas saturation to be one minus the minimum water saturation.
