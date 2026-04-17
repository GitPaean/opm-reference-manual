### NINENUM -- Define the Nine-Point Discretization Region

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The NINENUM keyword defines areas in the grid that should use the Nine-Point Discretization formulation by setting a grid block's NINENUM value to one, or zero for the conventional standard five-point discretization formulation, for when the Nine-Point Discretization formulation has been activated by the NINEPOIN keyword in the RUNSPEC section. There should be a NINENUM value for each grid block in the model. Note that if the if the NINEPOIN keyword in the RUNSPEC section has been invoked and the NINENUM keyword has not been used in the input deck, then all the grid will use the nine-point scheme.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | NINENUM | NINENUM defines an integer array of zeros and ones assigning a grid cell to a particular discretization region, a value of zero for five-point or a value of one for nine-point discretization.<br>Note that the default value of one implies a cell is included in the Nine-Point Discretization region; thus, if a cell is to use the conventional standard five-point finite difference discretization formulation, then NINENUM must be explicitly set to zero. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.88: NINENUM Keyword Description

The NINENUM keyword cannot be used in models with Local Grid Refinements ("LGR") to set different discretization regions within the model, that is if LGRs are present in the model either all the grid uses nine-point discretization, if NINEPOIN is present in the RUNSPEC section, or five-point if NINEPOIN is absent.

#### Example

The example below sets a portion of the model to us the Nine-Point Discretization formulation.

\--

\-- DEFINE NINE-POINT DISCRETIZATION REGION FOR ALL CELLS

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

NINENUM' 0 1\* 1\* 1\* 1\* 1\* 1\* / FIVE-POINT

NINENUM' 1 1\* 1\* 1\* 1\* 1 5 / NINE-POINT

/

Here the first line sets all the grid to us the five-point discretization formulation, all values set to zero, and then the second line sets all the cells in the layers one to five to use the nine-point discretization formulation.
