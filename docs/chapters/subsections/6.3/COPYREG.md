### COPYREG -- Copy an Array to Another Array based on a Region Number

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [COPYREG](#__RefHeading___Toc296589_1576177388) keyword copies a specified array or part of an array based on cells with a specific region number to another array. The region number array can be [FLUXNUM](#__RefHeading___Toc45781_719036256), [MULTNUM](#__RefHeading___Toc61329_2752266063) or [OPERNUM](#__RefHeading___Toc67857_718313858) and these arrays must be defined and be available before the [COPYREG](#__RefHeading___Toc296589_1576177388) keyword is read by the simulator. The property arrays can be real or integer valued depending on the property array type; however, the property arrays that can be operated on are dependent on which section the [COPYREG](#__RefHeading___Toc296589_1576177388) keyword is being applied in.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | ARRAY-1 | A character string of up to eight characters in length that defines the keyword identifying the array to be copied from. | None |
| 2 | ARRAY-2 | A character string of up to eight characters in length that defines the keyword identifying the array to be copied to. | None |
| 3 | REGION<br>NUMBER | Integer REGION NUMBER is the region for which the array data in (1) should be copied to array data in (2). | None |
| 4 | REGION<br>ARRAY | The REGION ARRAY to use for selecting the REGION NUMBER in (3) for selecting the data to be copied. REGION ARRAY can have the following values:<br>1)  F for the [FLUXNUM](#__RefHeading___Toc45781_719036256) array<br>2)  M for the [MULTNUM](#__RefHeading___Toc61329_2752266063) array<br>3)  O for the [OPERNUM](#__RefHeading___Toc67857_718313858) array | M |
| Notes:<br>1)  Where the REGION NUMBER should be less than or equal to the maximum number of regions as defined on the [REGDIMS](#__RefHeading___Toc70161_327352552) keyword for the [FIPNUM](#__RefHeading___Toc77229_2752266063) and [OPERNUM](#__RefHeading___Toc67857_718313858) arrays or the [GRIDOPTS](#__RefHeading___Toc45741_719036256) keyword for the [MULTNUM](#__RefHeading___Toc61329_2752266063) array in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  If the [GRIDOPTS](#__RefHeading___Toc45741_719036256) keyword is not present in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section or if the [GRIDOPTS](#__RefHeading___Toc45741_719036256) keyword is present but the maximum number of [MULTNUM](#__RefHeading___Toc61329_2752266063) regions (NRMULT) equals zero then REGION ARRAY will default to F for the [FLUXNUM](#__RefHeading___Toc45781_719036256) array.<br>3)  Each record must be terminated by a "/" and the keyword is terminated by a "/". |  |  |  |

Table 6.20: COPYREG Keyword Description

Examples of the arrays most commonly operated on in each section are given in . Cells colored red indicate arrays that are not supported by OPM Flow operations.

| [DX](#__RefHeading___Toc92905_705534506) | [DEPTH](#__RefHeading___Toc58139_3701168388) | [SWL](#__RefHeading___Toc22881_7842323221) | [ENDNUM](#__RefHeading___Toc123125_83452205) | [PRESSURE](#__RefHeading___Toc135627_1317547213) |  |  |
| --- | --- | --- | --- | --- | --- | --- |
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

Table 6.21: [COPYREG](#__RefHeading___Toc296589_1576177388) Keyword Applicable Arrays by Section

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

The above example first copies the [PERMX](#__RefHeading___Toc45791_719036256) property array for region number one to the [PERMY](#__RefHeading___Toc45793_719036256) and [PERMZ](#__RefHeading___Toc45795_719036256) property arrays for region one using the [MULTNUM](#__RefHeading___Toc61329_2752266063) array to define the region numbers. After which [PERMZ](#__RefHeading___Toc45795_719036256) property array for region one is multiplied by 0.5 using the [MULTIREG](#__RefHeading___Toc296613_1576177388) keyword.
