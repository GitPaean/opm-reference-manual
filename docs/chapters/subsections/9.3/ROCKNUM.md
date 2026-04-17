### ROCKNUM -- Define Rock Compaction Table Region Numbers

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The ROCKNUM keyword defines the rock compaction table region numbers for each grid block, as such there must be one entry for each cell in the model. The region number specifies which set of rock compaction tables defined by the ROCKTAB keyword are used to calculate the rock compaction in a grid block.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | ROCKNUM | ROCKNUM defines an array of positive integers assigning a grid cell to a particular rock compaction table region.<br>The maximum number of ROCKNUM regions is set by the NTROCC variable on the ROCKCOMP keyword in the RUNSPEC section. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  If a cell is not assigned a ROCKNUM region then the default value will be used.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 9.19: ROCKNUM Keyword Description

#### Examples

The example below sets three ROCKNUM regions for a 4 x 5 x 2 model.

\--

\-- DEFINE ROCKNUM REGION FOR ALL CELLS

\--

ROCKNUM

2 2 1 1 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1

3 3 1 1 3 3 1 1 1 1 1 1 1 1 1 1 1 1 1 1

/

Alternatively the EQUALS keyword could be employed to accomplish the same task, that is:

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

ROCKNUM 1 1\* 1\* 1\* 1\* 1\* 1\* / SET REGION 1

ROCKNUM 2 1 2 1 2 1 1 / SET REGION 2

ROCKNUM 3 1 2 1 2 2 2 / SET REGION 3

/
