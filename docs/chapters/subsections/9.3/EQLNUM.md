### EQLNUM -- Define the Equilibration Region Numbers

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The EQLNUM keyword defines the equilibration region numbers for each grid block. The equilibration data for various regions are defined in the SOLUTION section. For example, the EQUIL keyword in the SOLUTION section defines the initial pressures and fluid contacts for each equilibration region identified by the EQLNUM region array.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | EQLNUM | EQLNUM defines an array of positive integers assigning a grid cell to a particular equilibration region.<br>The maximum number of EQLNUM regions is set by the NTEQUL variable on the EQLDIMS keyword in the RUNSPEC section. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The EQLNUM and PVTNUM arrays need to be consistent, that is the all cells with the same EQLNUM can only belong to one PVTNUM region.<br>3)  If a cell is not assigned a EQLNUM region number then the default value will be used.<br>4)  The keyword is terminated by a "/". |  |  |  |

Table 9.3: EQLNUM Keyword Description

#### Examples

The example below sets three EQLNUM regions for a 4 x 5 x 2 model.

\--

\-- DEFINE EQLNUM REGIONS FOR ALL CELLS

\--

EQLNUM

2 2 1 1 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1

3 3 1 1 3 3 1 1 1 1 1 1 1 1 1 1 1 1 1 1

/

Alternatively the EQUALS keyword could be employed to accomplish the same task, that is:

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

EQLNUM' 1 1\* 1\* 1\* 1\* 1\* 1\* / SET REGION 1

EQLNUM' 2 1 2 1 2 1 1 / SET REGION 2

EQLNUM' 3 1 2 1 2 2 2 / SET REGION 3

/
