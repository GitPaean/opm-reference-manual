### TRANGL -- Define Non-Neighbor Connections Between Global and LGR Cells Manually

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[TRANGL](#__RefHeading___Toc1306682_4250154414) enables Non-Neighbor Connections ("NNC") between the global cells and the Local Grid Refinement ("LGR") cells to be manually specified, as oppose to the simulator calculating the transmissibilities. The [LGR](#__RefHeading___Toc55049_4106839650) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section should be utilized to define the presence of LGRs in the model and to define various [LGR](#__RefHeading___Toc55049_4106839650) dimension parameters.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | I1 | A positive integer that defines the [LGR](#__RefHeading___Toc55049_4106839650) grid block in the I-direction in a non-neighbor connection, must be greater than or equal to one and less than or equal to NX on the [CARFIN](#__RefHeading___Toc150726_63720426) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section. | None |
| --- | --- | --- | --- |
| 2 | J1 | A positive integer that defines the [LGR](#__RefHeading___Toc55049_4106839650) grid block in the J-direction in a non-neighbor connection, must be greater than or equal to one and less than or equal to NY on the [CARFIN](#__RefHeading___Toc150726_63720426) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section. | None |
| 3 | K1 | A positive integer that defines the [LGR](#__RefHeading___Toc55049_4106839650) grid block in the K-direction in a non-neighbor connection, must be greater than or equal to one and less than or equal to NZ on the [CARFIN](#__RefHeading___Toc150726_63720426) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section. | None |
| 4 | I2 | A positive integer that defines the GLOBAL grid block in the I-direction in a non-neighbor connection, must be greater than or equal to one and less than or equal to NX on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | None |
| 5 | J2 | A positive integer that defines the GLOBAL grid block in the J-direction in a non-neighbor connection, must be greater than or equal to one and less than or equal to NY on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | None |
| 6 | K2 | A positive integer that defines the GLOBAL grid block in the K-direction in a non-neighbor connection, must be greater than or equal to one and less than or equal to NZ on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | None |
| 7 | TRANSNNC | TRANSNNC is a positive real number greater than or equal to zero that defines the transmissibility between the GLOBAL grid block (I1, J1, K1) and the [LGR](#__RefHeading___Toc55049_4106839650) grid block (I2, J2, K2).<br>The default value of zero sets the transmissibility between the two cells to zero. | 0.0 |
| cP.rb/day/psia | cP.rm^3^/day/bars | cP.rcc/hr/atm |  |
| Notes:<br>1)  Each record must be terminated by a "/" and the keyword is terminated by a "/". |  |  |  |

Table 6.130: TRANGL Keyword Description

#### Example

\--

\-- MANUALLY DEFINE LGR-GLOBAL GRID NON-NEIGHBOR CONNECTIONS

\--

\-- \-\-\--LGR\-\-\-\-- \-\--GLOBAL\-\-\-- \-- TRANSNCC \--

\-- I1 J1 K1 I2 J2 K2

TRANGL

1 1 1 1 1 2 0.2500 /

1 1 2 1 1 3 0.2500 /

1 1 3 1 1 4 0.2500 /

/

The above example defines the transmissibility between [LGR](#__RefHeading___Toc55049_4106839650) cell (1, 1, 1) and global cell (1, 1, 2), [LGR](#__RefHeading___Toc55049_4106839650) cell (1, 1, 2) and global cell (1, 1, 3) and finally between [LGR](#__RefHeading___Toc55049_4106839650) cell (1, 1, 3) and global cell (1, 1, 4) to be 0.2500.
