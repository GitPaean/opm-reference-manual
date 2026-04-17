### EOSNUM -- Define the Equation of State Region Numbers

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The EOSNUM keyword defines the Equation Of State (EOS) region number for all the cells in the model via an array. The region number specifies which Equation Of State is used in each grid block. The keyword should only be used if the compositional mode has been requested using the COMPS keyword in the RUNSPEC section.

OPM Flow does not currently support the general compositional modeling formulation.

This keyword is not supported by OPM Flow but it will be parsed and its data ignored.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | EOSNUM | EOSNUM is an array of positive integers less than or equal to NMEOSR that define the EOS region number for each cell in the model.<br>The NMEOSR variable on the TABDIMS keyword in the RUNSPEC section defines the number of EOS regions in the model. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  If a cell is not assigned a region then the default value will be used.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table : EOSNUM Keyword Description

#### Examples

The example below sets two EOSNUM regions for a 4 x 5 x 2 model.

\--

\-- DEFINE EOSNUM REGIONS FOR ALL CELLS

\--

EOSNUM

20\*1

20\*2

/
