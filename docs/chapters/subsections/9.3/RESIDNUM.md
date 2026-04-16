### RESIDNUM -- Define Vertical Equilibrium Residual Flow Region Numbers

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [RESIDNUM](#__RefHeading___Toc655956_501926209) keyword defines the Vertical Equilibrium ("VE") residual flow calculation saturation tables (relative permeability and capillary pressure tables) region numbers for each grid block, as such there must be one entry for each cell in the model. The region number specifies which set of relative permeability tables ([SGFN](#__RefHeading___Toc106868_335817223), [SWFN](#__RefHeading___Toc106882_335817223), [SOF2](#__RefHeading___Toc106876_335817223), [SOF3](#__RefHeading___Toc106878_335817223), [SOF32D](#__RefHeading___Toc765497_4250154414), [SGOF](#__RefHeading___Toc106870_335817223), [SLGOF](#__RefHeading___Toc106874_335817223) and [SWOF](#__RefHeading___Toc45811_7190362561)) are used to calculate the relative permeability and capillary pressure in a grid block. The keyword should only be used if the Vertical Equilibrium option has been invoked via the [VE](#__RefHeading___Toc557797_487874538) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | [RESIDNUM](#__RefHeading___Toc655956_501926209) | [RESIDNUM](#__RefHeading___Toc655956_501926209) defines an array of positive integers assigning a grid cell to a particular saturation table region.<br>The maximum number of [RESIDNUM](#__RefHeading___Toc655956_501926209) regions is set by the NTSFUN variable on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  If a cell is not assigned a [RESIDNUM](#__RefHeading___Toc655956_501926209) region then the default value will be used.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 9.18: RESIDNUM Keyword Description

Note that any capillary pressure data on the relative permeability tables ([SGFN](#__RefHeading___Toc106868_335817223), [SWFN](#__RefHeading___Toc106882_335817223), [SOF2](#__RefHeading___Toc106876_335817223), [SOF3](#__RefHeading___Toc106878_335817223), [SOF32D](#__RefHeading___Toc765497_4250154414), [SGOF](#__RefHeading___Toc106870_335817223), [SLGOF](#__RefHeading___Toc106874_335817223) and [SWOF](#__RefHeading___Toc45811_7190362561)) will be ignored by the [VE](#__RefHeading___Toc557797_487874538) option.

#### Example

The example below sets three [RESIDNUM](#__RefHeading___Toc655956_501926209) regions for the model, by first setting all values to one, then setting layers 2 to 10 to two, and finally setting layers 30 to 50 to three.

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

SATNUM 1 1\* 1\* 1\* 1\* 1\* 1\* / SET REGION 1

SATNUM 2 1 2 1 2 2 10 / SET REGION 2

SATNUM 3 1 2 1 2 30 50 / SET REGION 3

/
