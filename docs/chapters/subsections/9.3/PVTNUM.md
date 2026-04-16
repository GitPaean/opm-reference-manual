### PVTNUM -- Define the PVT Regions

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [PVTNUM](#__RefHeading___Toc68366_2752266063) keyword defines the PVT region numbers for each grid block, as such there must be one entry for each cell in the model. The region number specifies which set of PVT tables ([DENSITY](#__RefHeading___Toc45799_719036256), [PVDG](#__RefHeading___Toc104056_57619843), [PVDO](#__RefHeading___Toc45803_719036256), [PVTG](#__RefHeading___Toc104060_57619843), [PVTO](#__RefHeading___Toc104062_57619843), [PVCO](#__RefHeading___Toc325700_501926209), [PVTW](#__RefHeading___Toc2086106_3315222525) and [ROCK](#__RefHeading___Toc45809_719036256)) are used to calculate the PVT properties in a grid block.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | [PVTNUM](#__RefHeading___Toc68366_2752266063) | [PVTNUM](#__RefHeading___Toc68366_2752266063) defines an array of positive integers assigning a grid cell to a particular PVT region.<br>The maximum number of [PVTNUM](#__RefHeading___Toc68366_2752266063) regions is set by the NTPVT variable on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  The EQULNUM and [PVTNUM](#__RefHeading___Toc68366_2752266063) arrays need to be consistent, that is the all cells with the same PVTNUM can only belong to one EQLNUM region.<br>3)  If a cell is not assigned a [PVTNUM](#__RefHeading___Toc68366_2752266063) region then the default value will be used.<br>4)  The keyword is terminated by a "/". |  |  |  |

Table 9.17: PVTNUM Keyword Description

#### Examples

The example below sets three [PVTNUM](#__RefHeading___Toc68366_2752266063) regions for a 4 x 5 x 2 model.

\--

\-- DEFINE PVTNUM REGION FOR ALL CELLS

\--

PVTNUM

2 2 1 1 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1

3 3 1 1 3 3 1 1 1 1 1 1 1 1 1 1 1 1 1 1

/

Alternatively the [EQUALS](#__RefHeading___Toc296597_1576177388) keyword could be employed to accomplish the same task, that is:

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

PVTNUM 1 1\* 1\* 1\* 1\* 1\* 1\* / SET REGION 1

PVTNUM 2 1 2 1 2 1 1 / SET REGION 2

PVTNUM 3 1 2 1 2 2 2 / SET REGION 3

/

There third example shows how to ensure the various PVT regions are isolated. First of all define the [MULTNUM](#__RefHeading___Toc61329_2752266063) array in the [GRID](#__RefHeading___Toc38674_784232322) section and ensure all the regions are isolated.

\-- ==============================================================================

\--

\-- GRID SECTION

\--

\-- ==============================================================================

GRID

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

MULTNUM 1 1\* 1\* 1\* 1\* 1\* 1\* / SET REGION 1

MULTNUM 2 1 2 1 2 1 1 / SET REGION 2

MULTNUM 3 1 2 1 2 2 2 / SET REGION 3

/

\--

\-- SET TRANSMISSIBILITES ACROSS DIFFERENT RESERVOIRS TO ZERO TO ISOLATE

\-- RESERVOIRS

\--

\-- REGION REGION TRANS DIREC NNC REGION ARRAY

\-- FROM TO MULT OPT OPTS M / F / O

MULTREGT

1\* 1\* 0.0 1\* \'ALL\' M / ALL REGIONS SEALED

/

Then in the [REGIONS](#__RefHeading___Toc40648_784232322) section copy the [MULTNUM](#__RefHeading___Toc61329_2752266063) array to the [PVTNUM](#__RefHeading___Toc68366_2752266063) array.

\-- ==============================================================================

\--

\-- REGIONS SECTION

\--

\-- ==============================================================================

REGIONS

\--

\-- COPY AN ARRAY TO ANOTHER ARRAY BASED ON A REGION NUMBER

\--

\-- ARRAY ARRAY REGION REGION ARRAY

\-- FROM TO NUMBER M / F / O

COPYREG

MULTNUM PVTNUM 1 M / COPY MULT TO PVT 1

MULTNUM PVTNUM 2 M / COPY MULT TO PVT 2

MULTNUM PVTNUM 3 M / COPY MULT TO PVT 3

/

All the separate PVT regions are now isolated.
