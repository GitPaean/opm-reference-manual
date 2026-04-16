### ENDNUM -- Define the End-Point Scaling Depth Region Numbers

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [ENDNUM](#__RefHeading___Toc123125_83452205) keyword defines the end-point scaling depth table region numbers for each grid block. The end-point scaling depth tables for various regions are defined by the ENPVTD[^1] and the [ENKRVD](#__RefHeading___Toc69787_621662414)[^2] keywords in the [PROPS](#__RefHeading___Toc39329_784232322) section. In the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section the NTENDP variable on the [ENDSCALE](#__RefHeading___Toc68146_2267116897) keyword defines the maximum number of depth tables.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | [ENDNUM](#__RefHeading___Toc123125_83452205) | [ENDNUM](#__RefHeading___Toc123125_83452205) defines an array of positive integers assigning a grid cell to a particular end-point scaling depth table region.<br>The maximum number of [ENDNUM](#__RefHeading___Toc123125_83452205) regions is set by the NTENDP variable on the [ENDSCALE](#__RefHeading___Toc68146_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  If a cell is not assigned a [ENDNUM](#__RefHeading___Toc123125_83452205) region number then the default value of one will be used.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 9.2: ENDNUM Keyword Description

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Examples

The example below sets three [ENDNUM](#__RefHeading___Toc123125_83452205) regions for a 4 x 5 x 2 model.

\--

\-- DEFINE ENDNUM REGIONS FOR ALL CELLS

\--

ENDNUM

2 2 1 1 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1

3 3 1 1 3 3 1 1 1 1 1 1 1 1 1 1 1 1 1 1

/

Alternatively the [EQUALS](#__RefHeading___Toc296597_1576177388) keyword could be employed to accomplish the same task, that is:

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

ENDNUM 1 1\* 1\* 1\* 1\* 1\* 1\* / SET REGION 1

ENDNUM 2 1 2 1 2 1 1 / SET REGION 2

ENDNUM 3 1 2 1 2 2 2 / SET REGION 3

/

[^1]: This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

[^2]: This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
