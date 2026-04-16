### EDITNNC -- Scale Non-Neighbor Connections Between Cells Manually

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[EDITNNC](#__RefHeading___Toc89569_718313858) enables Non-Neighbor Connections ("NNC"), entered via the [NNC](#__RefHeading___Toc63285_718313858) keyword or calculated by the simulator, to be multiplied (re-scaled) by a constant. For example, if the existing transmissibility between non-neighbor connections is Told and the multiplier is C, then the resulting transmissibility, Tnew, will be . Only previously defined [NNC](#__RefHeading___Toc63285_718313858)'s entered via the [NNC](#__RefHeading___Toc63285_718313858) keyword or calculated by the simulator can be edited, otherwise a warning message will be printed.

| 1 | I1 | A positive integer that defines the first grid block in the I-direction in a non-neighbor connection, must be greater than or equal to one and less than or equal to NX on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | None |
| --- | --- | --- | --- |
| 2 | J1 | A positive integer that defines the first grid block in the J-direction in a non-neighbor connection, must be greater than or equal to one and less than or equal to NY on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | None |
| 3 | K1 | A positive integer that defines the first grid block in the K-direction in a non-neighbor connection, must be greater than or equal to one and less than or equal to NZ on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | None |
| 4 | I2 | A positive integer that defines the second grid block in the I-direction in a non-neighbor connection, must be greater than or equal to one and less than or equal to NX on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | None |
| 5 | J2 | A positive integer that defines the second grid block in the J-direction in a non-neighbor connection, must be greater than or equal to one and less than or equal to NY on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | None |
| 6 | K2 | A positive integer that defines the second grid block in the K-direction in a non-neighbor connection, must be greater than or equal to one and less than or equal to NZ on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | None |
| 7 | TRANSMUL | TRANSMUL is a positive real number greater than or equal to zero that defines a constant that scales the transmissibility between the first grid block (I1, J1, K1) and the second grid block (I2, J2, K2).<br>The default value of one means no scaling will be applied. | 1 |
| dimensionless | dimensionless | dimensionless |  |
| 8 | ISATNUM1 | The default value of zero means the existing saturation table allocated to the upstream cell (I1,J1,K1). | 0 |
| 9 | ISATNUM2 | ISATNUM2 is a positive integer defining which saturation table number (relative permeability table) to be used for flow from the second grid block to the first grid block.<br>The default value of zero means the existing saturation table allocated to the downstream cell (I2,J2,K2). | 0 |
| 10 | IPRSNUM1 | IPRSNUM1 is a positive integer defining which pressure table number (PVT table) to be used for flow from the first grid block to the second grid block.<br>The default value of zero means the existing PVT table allocated to the upstream cell (I1,J1,K1). | 0 |
| 11 | IPRSNUM2 | IPRSNUM2 is a positive integer defining which pressure table number (PVT table) to be used for flow from the second grid block to the first grid block.<br>The default value of zero means the existing PVT table allocated to the downstream cell (I2,J2,K2). | 0 |
| 12 | FACE1 | FACE1 is a character string that defines the face associated with flow from the first grid block to the second grid block, where FACE1 can have values of: X+, X-, Y+, Y-, Z+, or Z-.<br>FACE1 is used with the commercial simulator's Vertical Equilibrium option which is not supported by OPM Flow. | None |
| 13 | FACE2 | FACE2 is a character string that defines the face associated with flow from the second grid block to the first grid block, where FACE2 can have values of: X+, X-, Y+, Y-, Z+, or Z-.<br>FACE2 is used with the commercial simulator's Vertical Equilibrium option which is not supported by OPM Flow. | None |
| 14 | DIFFNNC | DIFFNNC is a positive real number greater than or equal to zero that scales the diffusivity between the first grid block (I1, J1, K1) and the second grid block (I2, J2, K2). | 0.0 |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  Each record must be terminated by a "/" and the keyword is terminated by a "/". |  |  |  |

Table 7.3: EDITNNC Keyword Description

Note that although items (8) to (14) for this keyword are not available in OPM Flow, even if they were, it is strongly recommended that these items are defaulted if the data is being entered manually, as opposed to being generated by pre-processing software.

Care should be taken that cells in different [PVTNUM](#__RefHeading___Toc68366_2752266063) regions (see the [PVTNUM](#__RefHeading___Toc68366_2752266063) keyword in the [REGIONS](#__RefHeading___Toc40648_784232322) section) are not connected, since the fluid properties are associated with a cell. If for example, a rbbl or a rm^3^ of oil flows from [PVTNUM](#__RefHeading___Toc68366_2752266063) region 1 to [PVTNUM](#__RefHeading___Toc68366_2752266063) region 2, then the oil properties of that oil will change from the PVT 1 data set to the PVT data set 2. This will result in material balance errors, that may or may not cause numerical issues.

If the transmissibility across a fault needs to be modified see the [FAULTS](#__RefHeading___Toc45779_719036256) and [MULTFLT](#__RefHeading___Toc90875_3218818441) keywords in the [GRID](#__RefHeading___Toc38674_784232322) section for an alternative and less complicated method to modifying fault transmissibilities. Transmissibility between reservoir regions can be modified by using [MULTREGT](#__RefHeading___Toc296621_1576177388) keyword, provided [MULTNUM](#__RefHeading___Toc61329_2752266063) has been used to define the inter-region transmissibility region numbers for each grid block. Finally, the [MULTX](#__RefHeading___Toc80283_1778172979), [MULTY](#__RefHeading___Toc80287_1778172979) and [MULTZ](#__RefHeading___Toc80291_1778172979) series of keywords can be used to modify transmissibility between various cells. All the aforementioned keywords are described in the [GRID](#__RefHeading___Toc38674_784232322) section.

See also the [EDITNNCR](#__RefHeading___Toc140002_2545341761) keyword in the [EDIT](#__RefHeading___Toc40641_784232322) section that resets an existing [NNC](#__RefHeading___Toc63285_718313858) to a user defined value.

#### Example

\--

\-- MANUALLY RESCALE NON-NEIGHBOR CONNECTIONS

\--

\-- \-\-\-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\-\-\-- \-- TRANSMUL \--

\-- I1 J1 K1 I2 J2 K2

EDITNCC

1 1 1 1 1 2 0.2000 / SET NNC FOR FAULT

1 1 2 1 1 3 0.2000 / SET NNC FOR FAULT

1 1 3 1 1 4 0.2000 / SET NNC FOR FAULT

/

The above example multiplies the transmissibility between cells (1, 1, 1) and (1, 1, 2), (1, 1, 2) and (1, 1, 3) and finally between (1, 1, 3) and (1, 1, 4) by 0.200.
