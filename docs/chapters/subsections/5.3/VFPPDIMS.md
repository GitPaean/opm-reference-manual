### VFPPDIMS -- Production Vertical Flow Performance Table Dimensions

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[VFPPDIMS](#__RefHeading___Toc95111_327352552) keyword defines the maximum dimensions of the production well Vertical Lift Performance ("VFP") tables defined by [VFPPROD](#__RefHeading___Toc121919_2556401936) keyword. The VFP tables for the injection wells are defined by the [VFPIDIMS](#__RefHeading___Toc91587_327352552) keyword.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | MXMFLO | A positive integer that defines the maximum number of production flow rate entries for the [VFPPROD](#__RefHeading___Toc121919_2556401936) keyword. | 0 |
| 2 | MXMTHP | A positive integer that defines the maximum number of THP entries for the [VFPPROD](#__RefHeading___Toc121919_2556401936) keyword. | 0 |
| 3 | MXMWFR | A positive integer that defines the maximum number of water fraction entries (WOR, WCUT, GWR etc.) for the [VFPPROD](#__RefHeading___Toc121919_2556401936) keyword. | 0 |
| 4 | MXMGFR | A positive integer that defines the maximum number of gas fraction entries (GOR, GLR, OGR etc.) for the [VFPPROD](#__RefHeading___Toc121919_2556401936) keyword. | 0 |
| 5 | MXMALQ | A positive integer that defines the maximum number of artificial lift quantity entries for the [VFPPROD](#__RefHeading___Toc121919_2556401936) keyword. | 0 |
| 6 | MXVFPTAB | A positive integer that defines the maximum number of [VFPPROD](#__RefHeading___Toc121919_2556401936) tables entered through the [VFPPROD](#__RefHeading___Toc121919_2556401936) keyword. | 0 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.57: VFPPDIMS Keyword Description

#### Example

\-- PRODUCING VFP TABLES

\-- VFP VFP VFP VFP VFP VFP

\-- MXMFLO MXMTHP MXMWFR MXMGFR MXMALQ NMMVFT

VFPPDIMS

20 10 10 10 6 9 /

Here the example shows that there are a maximum of 20 flow rates, 10 THP entries, 10 water and gas fraction entries, and six artificial lift entries for the nine [VFPPROD](#__RefHeading___Toc121919_2556401936) VFP production tables.
