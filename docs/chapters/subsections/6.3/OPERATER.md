### OPERATER -- Define Mathematical Operations on Arrays by Region

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [OPERATER](#__RefHeading___Toc155507_332691817) keyword is similar to the [OPERATE](#__RefHeading___Toc64455_718313858) keyword, except it applies the mathematical operation on specific regions, whereas, [OPERATE](#__RefHeading___Toc64455_718313858) applies the operations on a cell by cell basis. Here the [OPERATER](#__RefHeading___Toc155507_332691817) keyword performs a mathematical operation on a specified property array, optionally using another property array as input to the function. The keyword allows for various mathematical functions and their associated variables to be defined and applied to the specified region data. Input constants can be integer or real valued depending on the array type; however, the arrays that can be operated on are dependent on which section the [OPERATER](#__RefHeading___Toc155507_332691817) keyword is being applied in.

| 1 | Y | A character string of up to eight characters in length that defines the keyword identifying the array to be modified. | None |
| --- | --- | --- | --- |
| 2 | REGION | REGION is a positive integer representing the region for which the EQUATION should be applied. The default is to use the region number from the [OPERNUM](#__RefHeading___Toc67857_718313858) keyword; however this can be reset to another region array via the ARRAY item on this keyword, provided the array exists at the time the keyword is declared in the input deck.<br>Note also the [OPERNUM](#__RefHeading___Toc67857_718313858) keyword must precede the use of the [OPERATER](#__RefHeading___Toc155507_332691817) keyword. | 0 |
| 3 | EQUATION | A defined character string of up to eight characters that defines the mathematical function to be applied, using the X array and the ALPHA and BETA constants declared on this keyword. EQUATION should be set to one of the following character strings: | None |
| 'MULTA' -<br>'POLY' -<br>'SLOG' -<br>'LOG10' -<br>'LOGE' -<br>'INV' -<br>'MULTX' - | 'ADDX' -<br>'COPY' -<br>'MAXLIM' -<br>'MINLIM' -<br>'MULTP' -<br>'ABS' -<br>'MULTIPLY' - |  |  |
| 4 | X | A character string of up to eight characters in length that defines the keyword identifying the array to be used as an input parameter. | None |
| 5 | ALPHA | An integer or real value that is the α variable in the EQUATION function. | None |
| 6 | BETA | An integer or real value that is the β variable in the EQUATION function. | None |
| 7 | ARRAY | The name of the array for which the REGION variable references. This can be any standard region array as declared in the REGION section ([FIPNUM](#__RefHeading___Toc77229_2752266063), [PVTNUM](#__RefHeading___Toc68366_2752266063), etc.), provided the array exists at the time the [OPERATER](#__RefHeading___Toc155507_332691817) keyword is invoked. In addition, the [MULTNUM](#__RefHeading___Toc61329_2752266063), [FLUXNUM](#__RefHeading___Toc45781_719036256) and [OPERNUM](#__RefHeading___Toc67857_718313858) may be used.<br>Only the default value of [OPERNUM](#__RefHeading___Toc67857_718313858) is supported by OPM Flow. | [OPERNUM](#__RefHeading___Toc67857_718313858) |
| Notes:<br>1)  Where the REGION should be less than or equal to the maximum number of regions as defined on the [REGDIMS](#__RefHeading___Toc70161_327352552) keyword for the [FIPNUM](#__RefHeading___Toc77229_2752266063) and [OPERNUM](#__RefHeading___Toc67857_718313858) arrays or the [GRIDOPTS](#__RefHeading___Toc45741_719036256) keyword for the [MULTNUM](#__RefHeading___Toc61329_2752266063) array in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section..<br>2)  Each record must be terminated by a "/" and the keyword is terminated by a "/". |  |  |  |

Table 6.96: OPERATER Keyword Description

Examples of the arrays most commonly operated on in each section are given in . Cells colored red indicate arrays that are not supported by OPM Flow operations.

| [GRID](#__RefHeading___Toc38674_784232322) | [EDIT](#__RefHeading___Toc40641_784232322) | [PROPS](#__RefHeading___Toc39329_784232322) | [REGIONS](#__RefHeading___Toc40648_784232322) | [SOLUTION](#__RefHeading___Toc43947_784232322) | [SUMMARY](#__RefHeading___Toc43949_784232322) | [SCHEDULE](#__RefHeading___Toc43945_784232322) |
| --- | --- | --- | --- | --- | --- | --- |
| [DX](#__RefHeading___Toc92905_705534506) | [DEPTH](#__RefHeading___Toc58139_3701168388) | [SWL](#__RefHeading___Toc22881_7842323221) | [ENDNUM](#__RefHeading___Toc123125_83452205) | [PRESSURE](#__RefHeading___Toc135627_1317547213) |  |  |
| [DY](#__RefHeading___Toc45767_719036256) | [PORV](#__RefHeading___Toc96547_718313858) | [SWCR](#__RefHeading___Toc27248_784232322) | [EQLNUM](#__RefHeading___Toc73734_2752266063) | [SWAT](#__RefHeading___Toc137373_1317547213) |  |  |
| [DZ](#__RefHeading___Toc45769_719036256) | [TRANX](#__RefHeading___Toc93085_718313858) | [SWU](#__RefHeading___Toc22883_7842323221) | [FIPNUM](#__RefHeading___Toc77229_2752266063) | [SGAS](#__RefHeading___Toc137369_1317547213) |  |  |
| [PERMX](#__RefHeading___Toc45791_719036256) | [TRANY](#__RefHeading___Toc93087_718313858) | [SGL](#__RefHeading___Toc22881_784232322) | [IMBNUM](#__RefHeading___Toc129665_83452205) | [RV](#__RefHeading___Toc137365_1317547213) |  |  |
| [PERMY](#__RefHeading___Toc45793_719036256) | [TRANZ](#__RefHeading___Toc93089_718313858) | [SGCR](#__RefHeading___Toc20428_784232322) | [MISCNUM](#__RefHeading___Toc129667_83452205) | [RS](#__RefHeading___Toc137361_1317547213) |  |  |
| [PERMZ](#__RefHeading___Toc45795_719036256) | [DIFFX](#__RefHeading___Toc355041_1539708736) | [SGU](#__RefHeading___Toc22883_784232322) | [PVTNUM](#__RefHeading___Toc68366_2752266063) | [TBLK](#__RefHeading___Toc198434_3325167686) |  |  |
| [MULTX](#__RefHeading___Toc80283_1778172979) | [DIFFY](#__RefHeading___Toc355043_1539708736) | [KRW](#__RefHeading___Toc97397_621662414) | [ROCKNUM](#__RefHeading___Toc118210_2939291539) | [GI](#__RefHeading___Toc372466_1414963541) |  |  |
| [MULTY](#__RefHeading___Toc80287_1778172979) | [DIFFZ](#__RefHeading___Toc355045_1539708736) | [KRO](#__RefHeading___Toc97395_621662414) | [SATNUM](#__RefHeading___Toc71136_2752266063) | [OILAPI](#__RefHeading___Toc240796_2928331029) |  |  |
| [MULTZ](#__RefHeading___Toc80291_1778172979) | [TRANR](#__RefHeading___Toc1306688_4250154414) | [KRG](#__RefHeading___Toc97393_621662414) | [WH2NUM](#__RefHeading___Toc1046874_487874538) | [SALT](#__RefHeading___Toc593214_516898843) |  |  |
| [DR](#__RefHeading___Toc113051_2066951158) | [TRANTHT](#__RefHeading___Toc1306690_4250154414) | [PCG](#__RefHeading___Toc77040_621662414) |  | [GASCONC](#__RefHeading___Toc189444_2330925267) |  |  |
| [DTHETA](#__RefHeading___Toc120096_2066951158) | [DIFFR](#__RefHeading___Toc344610_1539708736) | [PCW](#__RefHeading___Toc84164_621662414) |  | [SOLVCONC](#__RefHeading___Toc771984_4250154414) |  |  |
| [PERMR](#__RefHeading___Toc19328_3701168388) | [DIFFTHT](#__RefHeading___Toc349891_1539708736) |  |  | [SOLVFRAC](#__RefHeading___Toc785112_4250154414) |  |  |
| [PERMTHT](#__RefHeading___Toc114309_23127940) |  |  |  | [SFOAM](#__RefHeading___Toc669649_516898843) |  |  |
| [DZNET](#__RefHeading___Toc272339_1772380413) |  |  |  | [SPOLY](#__RefHeading___Toc124292_23127940) |  |  |
| [PORO](#__RefHeading___Toc45797_719036256) |  |  |  |  |  |  |
| [NTG](#__RefHeading___Toc33334_784232322) |  |  |  |  |  |  |
| [FLUXNUM](#__RefHeading___Toc45781_719036256) |  |  |  |  |  |  |
| [MULTNUM](#__RefHeading___Toc61329_2752266063) |  |  |  |  |  |  |
| [MPFANUM](#__RefHeading___Toc586676_3181922006) |  |  |  |  |  |  |
| [DIFFX](#__RefHeading___Toc355041_1539708736) |  |  |  |  |  |  |
| [DIFFY](#__RefHeading___Toc355043_1539708736) |  |  |  |  |  |  |
| [DIFFZ](#__RefHeading___Toc355045_1539708736) |  |  |  |  |  |  |
| [DIFFR](#__RefHeading___Toc344610_1539708736) |  |  |  |  |  |  |
| [DIFFTHT](#__RefHeading___Toc349891_1539708736) |  |  |  |  |  |  |

Table 6.97: [OPERATER](#__RefHeading___Toc155507_332691817) Keyword Applicable Arrays by Section

Double precision and integer work arrays may also be used to hold temporary values for use in more complex operations. Note that these work arrays are reset to zero at the start of each section of the data file. The names of the double precision work arrays should be of the form \'WORKn\', where n is a positive integer that defines the work array index, for example \'WORK1\', \'WORK2\', and so on. Similarly, the names of integer work arrays should be of the form \'IWORKn\', for example \'IWORK1\', \'IWORK2\', and so on. OPM Flow currently only supports double precision work arrays, and does not currently support using work arrays with \"global\" arrays ([MULTZ](#__RefHeading___Toc80291_1778172979)\*). Note that the permeability arrays (PERM\*) are treated as \"global\" arrays in the [GRID](#__RefHeading___Toc38674_784232322) section only. In the commercial simulator the maximum number of double precision and integer work arrays are specified using the [REGDIMS](#__RefHeading___Toc70161_327352552) keyword. Whereas, OPM Flow does not impose a limit on the maximum number of work arrays.

Note that care should be exercised when performing operations on integer array data as all transforms are performed using floating point arithmetic operations. In addition, operations on any of the transmissibility arrays ([TRANX](#__RefHeading___Toc93085_718313858), [TRANX](#__RefHeading___Toc93085_718313858)-, [TRANY](#__RefHeading___Toc93087_718313858), [TRANY](#__RefHeading___Toc93087_718313858)-, [TRANZ](#__RefHeading___Toc93089_718313858), and [TRANZ](#__RefHeading___Toc93089_718313858)-) may result in unintended consequences as these arrays have zero values on the boundary of the grid. In this use OPM ResInsight to verify and visually inspect the results.

#### Example

The first example uses the MULTP function combined with the Net-to-Gross ([NTG](#__RefHeading___Toc33334_784232322)) array to re-scale the [MULTX](#__RefHeading___Toc80283_1778172979), [MULTY](#__RefHeading___Toc80287_1778172979) and [MULTZ](#__RefHeading___Toc80291_1778172979) arrays to reduce the transmissibility in three separate reservoirs based on the reservoir quality ([NTG](#__RefHeading___Toc33334_784232322)). This keyword sequence should be in the [GRID](#__RefHeading___Toc38674_784232322) section.

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

Notice that the ARRAY variable has been defaulted, resulting in [OPERNUM](#__RefHeading___Toc67857_718313858) being the regional array for the REGION variable.

The next example shows how to set the maximum gas saturation ([SGU](#__RefHeading___Toc22883_784232322)) based on the minimum (lowest) water saturation ([SWL](#__RefHeading___Toc22881_7842323221)) when using the End-Point Scaling option, in the [PROPS](#__RefHeading___Toc39329_784232322) section.

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

The final example shows how to reset the [FIPNUM](#__RefHeading___Toc77229_2752266063) array when the exported array from the earth model does not correspond to the simulator's desired numbering scheme.

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

Note that operation can only be done in the REGION section as [FIPNUM](#__RefHeading___Toc77229_2752266063) is only available for use in this section and that the ARRAY variable has been defaulted, resulting in [OPERNUM](#__RefHeading___Toc67857_718313858) being the regional array for the REGION variable.
