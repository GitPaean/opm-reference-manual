### ISOLNUM -- Define the Independent Reservoir Regions

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [ISOLNUM](#__RefHeading___Toc69656_3218818441) keyword defines areas of the grid that consists of isolated reservoirs where the only form of communication between the reservoirs is via wellbore connections This enables the reservoir flow equations to be solved independently for greater computational efficiency.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | [ISOLNUM](#__RefHeading___Toc69656_3218818441) | [ISOLNUM](#__RefHeading___Toc69656_3218818441) defines an array of positive integers assigning a grid cell to a particular isolated reservoir region.<br>The maximum number of [ISOLNUM](#__RefHeading___Toc69656_3218818441) regions is set by the NRFREG variable on the [REGDIMS](#__RefHeading___Toc70161_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  Setting [ISOLNUM](#__RefHeading___Toc69656_3218818441) for a cell to zero makes the cell inactive.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 6.52: ISOLNUM Keyword Description

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

The example below defines three separate independent reservoirs; the first reservoir covers the whole grid and layers 1 to 50, reservoir two cover the whole grid and layers 52 to 150, and finally the third reservoir again covers the whole grid but with layers 152 to 300. The layers 51 and 151 are shale layers made inactive by setting [ISOLNUM](#__RefHeading___Toc69656_3218818441) to zero.

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

ISOLNUM 1 1\* 1\* 1\* 1\* 1 50 / DEFINED RESERVOIR 1

ISOLNUM 0 1\* 1\* 1\* 1\* 51 51 / DEFINED A SHALE

ISOLNUM 2 1\* 1\* 1\* 1\* 52 150 / DEFINED RESERVOIR 2

ISOLNUM 0 1\* 1\* 1\* 1\* 151 151 / DEFINED A SHALE

ISOLNUM 3 1\* 1\* 1\* 1\* 152 300 / DEFINED RESERVOIR 3

/

Note the above example has no effect as the keyword is ignored by the simulator.
