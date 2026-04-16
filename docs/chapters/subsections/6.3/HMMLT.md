### HMMLT -- History Match Grid Permeability Gradient Cumulative Multipliers

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [HMMLT](#__RefHeading___Toc224680_4219267791) series of keywords defines the history match gradient cumulative permeability multipliers, for when the History Match Gradient option has been activated by the [HMDIMS](#__RefHeading___Toc207753_4219267791) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The keyword consists of the first five characters of "HMMLT" followed by a two or three character string shown in , that determines the permeability direction, for example, HMMLTPX.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

+-----------+---------------------------------------------------+------------+----------------------------------------------------------+-----------+
| > Grid    | > [HMMULT](#__RefHeading___Toc275609_4219267791)  | > Grid     | > [HMMULT](#__RefHeading___Toc275609_4219267791) Keyword |           |
|           |                                                   |            |                                                          |           |
| > Keyword | > Keyword                                         | > Keyword  |                                                          |           |
+-----------+---------------------------------------------------+------------+----------------------------------------------------------+-----------+
| > PX/PR   | > [PERMX](#__RefHeading___Toc45791_719036256)     | > HMMLTPX  | > [PERMR](#__RefHeading___Toc19328_3701168388)           | > HMMLTPR |
+-----------+---------------------------------------------------+------------+----------------------------------------------------------+-----------+
| > PXY     | > PERMXY                                          | > HMMLTPXY |                                                          |           |
+-----------+---------------------------------------------------+------------+----------------------------------------------------------+-----------+
| > PY/THT  | > [PERMY](#__RefHeading___Toc45793_719036256)     | > hMMLTPY  | > [PERMTHT](#__RefHeading___Toc114309_23127940)          | > HMMLTTH |
+-----------+---------------------------------------------------+------------+----------------------------------------------------------+-----------+
| > PZ      | > [PERMZ](#__RefHeading___Toc45795_719036256)     | > HMMLTPZ  | > [PERMZ](#__RefHeading___Toc45795_719036256)            | > HMMLTPZ |
+-----------+---------------------------------------------------+------------+----------------------------------------------------------+-----------+

Table 6.45: [HMMLT](#__RefHeading___Toc224680_4219267791) Keyword List

See also the [HMMULT](#__RefHeading___Toc275609_4219267791) keyword in the [EDIT](#__RefHeading___Toc40641_784232322) section
