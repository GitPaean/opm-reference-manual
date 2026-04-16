### OPERNUM -- Define Regions for Mathematical Operations on Arrays

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the [OPERATER](#__RefHeading___Toc155507_332691817) region numbers for each grid block. The [OPERNUM](#__RefHeading___Toc67857_718313858) keyword defines the region numbers for each grid block, as such there must be one entry for each cell in the model. The array can also be used with the [EQUALREG](#__RefHeading___Toc296593_1576177388), [ADDREG](#__RefHeading___Toc4414_421927891), [COPYREG](#__RefHeading___Toc296589_1576177388), [MULTIREG](#__RefHeading___Toc296613_1576177388), [MULTREGP](#__RefHeading___Toc296617_1576177388) and [MULTREGT](#__RefHeading___Toc296621_1576177388) keywords, as well as the [OPERATER](#__RefHeading___Toc155507_332691817) keyword in calculating various grid properties in the [GRID](#__RefHeading___Toc38674_784232322) and REGION section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | [OPERNUM](#__RefHeading___Toc67857_718313858) | [OPERNUM](#__RefHeading___Toc67857_718313858) defines an array of positive integers greater than or equal to one that assigns a grid cell to a particular [OPERNUM](#__RefHeading___Toc67857_718313858) region.<br>The maximum number of [OPERNUM](#__RefHeading___Toc67857_718313858) regions is set by the NOPREG variable on the [REGDIMS](#__RefHeading___Toc70161_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>Note that the default value of zero implies that the calculations requested by the [OPERATER](#__RefHeading___Toc155507_332691817) keyword will not be performed. | 0 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.98: OPERNUM Keyword Description

#### Examples

The example below sets three [OPERNUM](#__RefHeading___Toc67857_718313858) regions for a 4 x 5 x 2 model.

\--

\-- DEFINE OPERNUM REGIONS FOR ALL CELLS

\--

OPERNUM

2 2 1 1 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1

3 3 1 1 3 3 1 1 1 1 1 1 1 1 1 1 1 1 1 1

/

Alternatively the [EQUALS](#__RefHeading___Toc296597_1576177388) keyword could be employed to accomplish the same task, that is:

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

OPERNUM 1 1\* 1\* 1\* 1\* 1\* 1\* / SET REGION 1

OPERNUM 2 1 2 1 2 1 1 / SET REGION 2

OPERNUM 3 1 2 1 2 2 2 / SET REGION 3

/

One can then increase [PERMX](#__RefHeading___Toc45791_719036256) by 25% in region three only.

\--

\-- MULTIPLY AN ARRAY BY A CONSTANT BASED ON A REGION NUMBER

\--

\-- ARRAY CONSTANT REGION REGION ARRAY

\-- VALUE NUMBER M / F / O

MULTIREG

PERMX 1.25 3 O /

/
