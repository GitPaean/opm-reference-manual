### SURFNUM -- Define the Surfactant Miscible Saturation Table Region Numbers

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [SURFNUM](#__RefHeading___Toc896940_4250154414) keyword defines the saturation tables (relative permeability and capillary pressure tables) region numbers for each grid block, as such there must be one entry for each cell in the model. The region number specifies which set of oil-water relative permeability tables ([SWFN](#__RefHeading___Toc106882_335817223), [SOF2](#__RefHeading___Toc106876_335817223), [SOF3](#__RefHeading___Toc106878_335817223), and [SWOF](#__RefHeading___Toc45811_7190362561)) are used to calculate the relative permeability and capillary pressure in a grid block. In this case the [SURFNUM](#__RefHeading___Toc896940_4250154414) allocated tables assume that oil and water are miscible, whereas the [SATNUM](#__RefHeading___Toc71136_2752266063) allocated tables are used to allocate the immiscible saturation tables. To use this keyword the Surfactant option must have been activated by the [SURFACT](#__RefHeading___Toc863854_4250154414) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | [SURFNUM](#__RefHeading___Toc896940_4250154414) | [SURFNUM](#__RefHeading___Toc896940_4250154414) defines an array of positive integers assigning a grid cell to a particular saturation table region.<br>The maximum number of [SURFNUM](#__RefHeading___Toc896940_4250154414) regions is set by the NTSFUN variable on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  If a cell is not assigned a [SURFNUM](#__RefHeading___Toc896940_4250154414) region then the default value will be used.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 9.22: SURFNUM Keyword Description

#### Example

The example below sets three [SURFNUM](#__RefHeading___Toc896940_4250154414) for the model.

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

SURFNUM 1 1\* 1\* 1\* 1\* 1\* 1\* / SET REGION 1

SURFNUM 2 1\* 1\* 1\* 1\* 1 1 / SET REGION 2

SURFNUM 3 1\* 1\* 1\* 1\* 2 2 / SET REGION 3

/
