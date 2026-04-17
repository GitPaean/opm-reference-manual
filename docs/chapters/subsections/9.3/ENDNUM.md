### ENDNUM -- Define the End-Point Scaling Depth Region Numbers

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The ENDNUM keyword defines the end-point scaling depth table region numbers for each grid block. The end-point scaling depth tables for various regions are defined by the ENPVTD[^1] and the ENKRVD[^2] keywords in the PROPS section. In the RUNSPEC section the NTENDP variable on the ENDSCALE keyword defines the maximum number of depth tables.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | ENDNUM | ENDNUM defines an array of positive integers assigning a grid cell to a particular end-point scaling depth table region.<br>The maximum number of ENDNUM regions is set by the NTENDP variable on the ENDSCALE keyword in the RUNSPEC section. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  If a cell is not assigned a ENDNUM region number then the default value of one will be used.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 9.2: ENDNUM Keyword Description

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Examples

The example below sets three ENDNUM regions for a 4 x 5 x 2 model.

\--

\-- DEFINE ENDNUM REGIONS FOR ALL CELLS

\--

ENDNUM

2 2 1 1 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1

3 3 1 1 3 3 1 1 1 1 1 1 1 1 1 1 1 1 1 1

/

Alternatively the EQUALS keyword could be employed to accomplish the same task, that is:

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
