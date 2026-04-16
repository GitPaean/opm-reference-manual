### MULTNUM -- Define the Multiple Transmissibility Regions

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [MULTNUM](#__RefHeading___Toc61329_2752266063) keyword defines the inter-region transmissibility region numbers for each grid block, as such there must be one entry for each cell in the model. The array can be used with the [EQUALREG](#__RefHeading___Toc296593_1576177388), [ADDREG](#__RefHeading___Toc4414_421927891), [COPYREG](#__RefHeading___Toc296589_1576177388), [MULTIREG](#__RefHeading___Toc296613_1576177388), [MULTREGP](#__RefHeading___Toc296617_1576177388) and [MULTREGT](#__RefHeading___Toc296621_1576177388) keywords in calculating various grid properties in the [GRID](#__RefHeading___Toc38674_784232322) section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | [MULTNUM](#__RefHeading___Toc61329_2752266063) | [MULTNUM](#__RefHeading___Toc61329_2752266063) defines an array of positive integers assigning a grid cell to a particular inter-region transmissibility region.<br>The maximum number of [MULTNUM](#__RefHeading___Toc61329_2752266063) regions is set by the NRMULT variable on the [GRIDOPTS](#__RefHeading___Toc45741_719036256) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.72: MULTNUM Keyword Description

#### Examples

The example below sets three [MULTNUM](#__RefHeading___Toc61329_2752266063) regions for a 4 x 5 x 2 model.

\--

\-- DEFINE MULTNUM REGIONS FOR ALL CELLS

\--

MULTNUM

2 2 1 1 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1

3 3 1 1 3 3 1 1 1 1 1 1 1 1 1 1 1 1 1 1

/

Alternatively the [EQUALS](#__RefHeading___Toc296597_1576177388) keyword could be employed to accomplish the same task, that is:

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

MULTNUM 1 1\* 1\* 1\* 1\* 1\* 1\* / SET REGION 1

MULTNUM 2 1 2 1 2 1 1 / SET REGION 2

MULTNUM 3 1 2 1 2 2 2 / SET REGION 3

/

One can then increase [PERMX](#__RefHeading___Toc45791_719036256) by 25% in region three only.

\--

\-- MULTIPLY AN ARRAY BY A CONSTANT BASED ON A REGION NUMBER

\--

\-- ARRAY CONSTANT REGION REGION ARRAY

\-- VALUE NUMBER M / F / O

MULTIREG

PERMX 1.25 3 M /

/
