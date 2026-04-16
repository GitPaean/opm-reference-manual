### VFPIDIMS -- Injection Vertical Flow Performance Table Dimensions

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[VFPIDIMS](#__RefHeading___Toc91587_327352552) keyword defines the maximum dimensions of the injection well Vertical Lift Performance ("VFP") tables defined by [VFPINJ](#__RefHeading___Toc121917_2556401936) keyword. The VFP tables for the producing wells are defined by the [VFPPDIMS](#__RefHeading___Toc95111_327352552) keyword.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | MXMFLO | A positive integer that defines the maximum number of injection rate entries for the [VFPINJ](#__RefHeading___Toc121917_2556401936) keyword. | 0 |
| 2 | MXMTHP | A positive integer that defines the maximum number of THP entries for the [VFPINJ](#__RefHeading___Toc121917_2556401936) keyword. | 0 |
| 3 | MXVFPTAB | A positive integer that defines the maximum number of [VFPINJ](#__RefHeading___Toc121917_2556401936) tables entered through the [VFPINJ](#__RefHeading___Toc121917_2556401936) keyword. | 0 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.56: VFPIDIMS Keyword Description

#### Example

\-- INJECTING VFP TABLES

\-- VFP VFP VFP

\-- MXMFLO MXMTHP NMMVFT

VFPIDIMS

10 10 12 /

The above example defines that the maximum number of injection rates and THP entries on the [VFPINJ](#__RefHeading___Toc121917_2556401936) keyword is 10, and the number of [VFPINJ](#__RefHeading___Toc121917_2556401936) tables is 12.
