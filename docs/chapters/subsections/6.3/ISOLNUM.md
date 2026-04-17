### ISOLNUM -- Define the Independent Reservoir Regions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The ISOLNUM keyword defines areas of the grid that consists of isolated reservoirs where the only form of communication between the reservoirs is via wellbore connections This enables the reservoir flow equations to be solved independently for greater computational efficiency.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | ISOLNUM | ISOLNUM defines an array of positive integers assigning a grid cell to a particular isolated reservoir region.<br>The maximum number of ISOLNUM regions is set by the NRFREG variable on the REGDIMS keyword in the RUNSPEC section. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  Setting ISOLNUM for a cell to zero makes the cell inactive.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 6.52: ISOLNUM Keyword Description

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

The example below defines three separate independent reservoirs; the first reservoir covers the whole grid and layers 1 to 50, reservoir two cover the whole grid and layers 52 to 150, and finally the third reservoir again covers the whole grid but with layers 152 to 300. The layers 51 and 151 are shale layers made inactive by setting ISOLNUM to zero.

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
