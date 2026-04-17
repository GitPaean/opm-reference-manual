### FLUXNUM -- Define the Flux Regions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The FLUXNUM keyword defines the flux region numbers for each grid block, as such there must be one entry for each cell in the model. The array is used with the Flux Boundary option to define the various flux regions; however, the Flux Boundary option has not been implemented in OPM Flow. In addition, the array can be used with the EQUALREG, ADDREG, COPYREG, MULTIREG, MULTREGP and MULTREGT keywords in calculating various grid properties in the GRID section. This facility has been implemented in OPM Flow.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | FLUXNUM | FLUXNUM defines an array of positive integers assigning a grid cell to a particular flux region.<br>The maximum number of flux regions is set by the MXNFLX variable on the REGDIMS keyword in the RUNSPEC section. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.39: FLUXNUM Keyword Description

#### Examples

The example below sets three FLUXNUM regions for a 4 x 5 x 2 model.

\--

\-- DEFINE FLUXNUM REGIONS FOR ALL CELLS

\--

FLUXNUM

2 2 1 1 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1

3 3 1 1 3 3 1 1 1 1 1 1 1 1 1 1 1 1 1 1

/

Alternatively the EQUALS keyword could be employed to accomplish the same task, that is:

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

FLUXNUM 1 1\* 1\* 1\* 1\* 1\* 1\* / SET REGION 1

FLUXNUM 2 1 2 1 2 1 1 / SET REGION 2

FLUXNUM 3 1 2 1 2 2 2 / SET REGION 3

/
