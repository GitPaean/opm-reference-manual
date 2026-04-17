### OPERNUM -- Define Regions for Mathematical Operations on Arrays

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the OPERATER region numbers for each grid block. The OPERNUM keyword defines the region numbers for each grid block, as such there must be one entry for each cell in the model. The array can also be used with the EQUALREG, ADDREG, COPYREG, MULTIREG, MULTREGP and MULTREGT keywords, as well as the OPERATER keyword in calculating various grid properties in the GRID and REGION section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | OPERNUM | OPERNUM defines an array of positive integers greater than or equal to one that assigns a grid cell to a particular OPERNUM region.<br>The maximum number of OPERNUM regions is set by the NOPREG variable on the REGDIMS keyword in the RUNSPEC section.<br>Note that the default value of zero implies that the calculations requested by the OPERATER keyword will not be performed. | 0 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.98: OPERNUM Keyword Description

#### Examples

The example below sets three OPERNUM regions for a 4 x 5 x 2 model.

\--

\-- DEFINE OPERNUM REGIONS FOR ALL CELLS

\--

OPERNUM

2 2 1 1 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1

3 3 1 1 3 3 1 1 1 1 1 1 1 1 1 1 1 1 1 1

/

Alternatively the EQUALS keyword could be employed to accomplish the same task, that is:

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

OPERNUM 1 1\* 1\* 1\* 1\* 1\* 1\* / SET REGION 1

OPERNUM 2 1 2 1 2 1 1 / SET REGION 2

OPERNUM 3 1 2 1 2 2 2 / SET REGION 3

/

One can then increase PERMX by 25% in region three only.

\--

\-- MULTIPLY AN ARRAY BY A CONSTANT BASED ON A REGION NUMBER

\--

\-- ARRAY CONSTANT REGION REGION ARRAY

\-- VALUE NUMBER M / F / O

MULTIREG

PERMX 1.25 3 O /

/
