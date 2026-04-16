### GRIDFILE -- Set the Grid File Output Options

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword controls the output of a standard [GRID](#__RefHeading___Toc38674_784232322) or extended [GRID](#__RefHeading___Toc38674_784232322) file, as well as the extensible EGRID file for post-processing applications. The extended and extensible [GRID](#__RefHeading___Toc38674_784232322) formats are comparable; however, the extensible [GRID](#__RefHeading___Toc38674_784232322) format is more compact and is the only format supported by OPM Flow.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | NGRID | A positive integer that controls the output of the [GRID](#__RefHeading___Toc38674_784232322) geometry file:<br>1)  \- for no [GRID](#__RefHeading___Toc38674_784232322) file to be written out.<br>2)  \- for the standard [GRID](#__RefHeading___Toc38674_784232322) file to be written out.<br>3)  \- for the extended [GRID](#__RefHeading___Toc38674_784232322) file to be written out.<br>Only the default value of zero is supported. | 0 |
| 2 | NEGRID | A positive integer that controls the output of the EGRID geometry file:<br>1)  \- for no extensible [GRID](#__RefHeading___Toc38674_784232322) file to be written out.<br>2)  \- for the extensible [GRID](#__RefHeading___Toc38674_784232322) file to be written out.<br>Only the default value of one is supported. | 1 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 6.41: GRIDFILE Keyword Description

#### Example

\--

\-- GRID FILE OUTPUT OPTIONS

\-- GRID EGRID

\-- OPTN OPTN

GRIDFILE

0 1 /

The above example defines that no [GRID](#__RefHeading___Toc38674_784232322) file will be written out and that the extensible [GRID](#__RefHeading___Toc38674_784232322) (that is the EGRID geometry format) file will be produced. This is the only configuration that OPM Flow supports
