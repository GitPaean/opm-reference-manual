### SATNUM -- Define the Saturation Table Region Numbers

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SATNUM keyword defines the saturation tables (relative permeability and capillary pressure tables) region numbers for each grid block, as such there must be one entry for each cell in the model. The region number specifies which set of relative permeability tables (SGFN, SWFN, SOF2, SOF3, SOF32D, SGOF, SLGOF and SWOF) are used to calculate the relative permeability and capillary pressure in a grid block.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | SATNUM | SATNUM defines an array of positive integers assigning a grid cell to a particular saturation table region.<br>The maximum number of SATNUM regions is set by the NTSFUN variable on the TABDIMS keyword in the RUNSPEC section. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  If a cell is not assigned a SATNUM region then the default value will be used.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table : SATNUM Keyword Description

#### Examples

The example below sets three SATNUM regions for a 4 x 5 x 2 model.

\--

\-- DEFINE SATNUM REGIONS FOR ALL CELLS

\--

SATNUM

2 2 1 1 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1

3 3 1 1 3 3 1 1 1 1 1 1 1 1 1 1 1 1 1 1

/

Alternatively the EQUALS keyword could be employed to accomplish the same task, that is:

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

SATNUM 1 1\* 1\* 1\* 1\* 1\* 1\* / SET REGION 1

SATNUM 2 1 2 1 2 1 1 / SET REGION 2

SATNUM 3 1 2 1 2 2 2 / SET REGION 3

/
