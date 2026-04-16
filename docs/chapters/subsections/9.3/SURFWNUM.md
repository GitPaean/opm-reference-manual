### SURFWNUM -- Define the Saturation Table Region Numbers (High Salinity and Water Wet)

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [SURFWNUM](#__RefHeading___Toc1179776_4250154414) keyword defines the saturation tables (relative permeability and capillary pressure tables) region numbers for each grid block, as such there must be one entry for each cell in the mode, for when the Surfactant Wettability option has been selected. The keyword may also be used with the Low Salt Brine option, in this case the water wet curves are calculated as a function of the low and high water wet salinity curves. The region number specifies which set of relative permeability tables are used to calculate the relative permeability and capillary pressure in a grid block. Note that the keyword is obligatory if the [SURFACTW](#__RefHeading___Toc863864_4250154414) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section has been used to invoke the Surfactant Wettability option.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | [SURFWNUM](#__RefHeading___Toc1179776_4250154414) | [SURFWNUM](#__RefHeading___Toc1179776_4250154414) defines an array of positive integers assigning a grid cell to a particular saturation table region.<br>The maximum number of [SURFWNUM](#__RefHeading___Toc1179776_4250154414) regions is set by the NTSFUN variable on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  If a cell is not assigned a [SATNUM](#__RefHeading___Toc71136_2752266063) region then the default value will be used.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 9.23: SURFWNUM Keyword Description

#### Example

The example below sets three [SURFWNUM](#__RefHeading___Toc1179776_4250154414) regions for the model.

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

SURFWNUM 1 1\* 1\* 1\* 1\* 1\* 1\* / SET REGION 1

SURFWNUM 2 1 2 1 2 1 1 / SET REGION 2

SURFWNUM 3 1 2 1 2 2 2 / SET REGION 3

/
