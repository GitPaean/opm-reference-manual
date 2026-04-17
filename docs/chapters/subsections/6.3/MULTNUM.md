### MULTNUM -- Define the Multiple Transmissibility Regions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The MULTNUM keyword defines the inter-region transmissibility region numbers for each grid block, as such there must be one entry for each cell in the model. The array can be used with the EQUALREG, ADDREG, COPYREG, MULTIREG, MULTREGP and MULTREGT keywords in calculating various grid properties in the GRID section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | MULTNUM | MULTNUM defines an array of positive integers assigning a grid cell to a particular inter-region transmissibility region.<br>The maximum number of MULTNUM regions is set by the NRMULT variable on the GRIDOPTS keyword in the RUNSPEC section. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.72: MULTNUM Keyword Description

#### Examples

The example below sets three MULTNUM regions for a 4 x 5 x 2 model.

\--

\-- DEFINE MULTNUM REGIONS FOR ALL CELLS

\--

MULTNUM

2 2 1 1 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1

3 3 1 1 3 3 1 1 1 1 1 1 1 1 1 1 1 1 1 1

/

Alternatively the EQUALS keyword could be employed to accomplish the same task, that is:

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

MULTNUM 1 1\* 1\* 1\* 1\* 1\* 1\* / SET REGION 1

MULTNUM 2 1 2 1 2 1 1 / SET REGION 2

MULTNUM 3 1 2 1 2 2 2 / SET REGION 3

/

One can then increase PERMX by 25% in region three only.

\--

\-- MULTIPLY AN ARRAY BY A CONSTANT BASED ON A REGION NUMBER

\--

\-- ARRAY CONSTANT REGION REGION ARRAY

\-- VALUE NUMBER M / F / O

MULTIREG

PERMX 1.25 3 M /

/
