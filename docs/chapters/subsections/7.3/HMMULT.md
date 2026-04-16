### HMMULT -- History Match Grid Transmissibility & Pore Volume Gradient Cumulative Multipliers

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [HMMULT](#__RefHeading___Toc275609_4219267791) series of keywords defines the history match gradient cumulative permeability multipliers, for when the History Match Gradient option has been activated by the [HMDIMS](#__RefHeading___Toc207753_4219267791) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The keyword consists of the first six characters of "HMMULT" followed by a one or two character string shown in , that determines the transmissibility direction, for example, HMMULTX.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

| Grid<br>Keyword | [HMMULT](#__RefHeading___Toc275609_4219267791)<br>Keyword | Grid<br>Keyword | [HMMULT](#__RefHeading___Toc275609_4219267791) Keyword |  |
| --- | --- | --- | --- | --- |
| X/R | [MULTX](#__RefHeading___Toc80283_1778172979) | HMMULTX | [MULTR](#__RefHeading___Toc228976_1841740821) | HMMULTR |
| XY |  | HMMULTXY |  |  |
| Y/HT | [MULTY](#__RefHeading___Toc80287_1778172979) | hMMULTY | [MULTTHT](#__RefHeading___Toc270099_1841740821) | HMMULTTH |
| z | [MULTZ](#__RefHeading___Toc80291_1778172979) | HMMULTZ | [MULTZ](#__RefHeading___Toc80291_1778172979) | HMMULTZ |
| PV | [MULTPV](#__RefHeading___Toc95300_3218818441) | HMMULTPV | [MULTPV](#__RefHeading___Toc95300_3218818441) | HMMULTPV |

Table 7.5: [HMMULT](#__RefHeading___Toc275609_4219267791) Keyword List

See also the [HMMLT](#__RefHeading___Toc224680_4219267791) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section.
