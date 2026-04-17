### PINCHNUM -- Define Pinch-Out Regions for the PINCHREG Keyword

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The PINCHNUM keyword defines the pinch-out region numbers for each grid block, as such there must be one entry for each cell in the model. The array is used with the PINCHREG keyword to set the pinch-out options and threshold thickness for each region.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | PINCHNUM | PINCHNUM defines an array of positive integers assigning a grid cell to a particular PINCHNUM region.<br>The maximum number of PINCHNUM regions is set by the NRPINC variable on the GRIDOPTS keyword in the RUNSPEC section. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.109: PINCHNUM Keyword Description

#### Example

The example below sets defines three PINCHNUM regions for various layers in a model based on the model's layering.

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

MULTNUM 1 1\* 1\* 1\* 1\* 1\* 1\* / SET REGION 1

MULTNUM 2 1 2 1 2 10 50 / SET REGION 2

MULTNUM 3 1 2 1 2 51 100 / SET REGION 3

/

One can then set the pinch-out criteria for each region.

\--

\-- SET PINCH-OUT CRITERA VIA THE PINCHNUM REGION

\--

PINCHREG

\-- THRESHOLD GAP EMPTY TRANS

\-- THICKNESS NO GAP GAP CALC

0.1 1\* 1\* 1\* / PINCHNUM 01

1.0 1\* 10 1\* / PINCHNUM 02

1.0 NOGAP 20 1\* / PINCHNUM 03

The above example sets the default pinch-out criteria for grid blocks defined as region one via the PINCHNUM array and different criteria for regions two and three.
