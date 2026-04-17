### PERMY -- Define the Permeability in the Y Direction for All the Cells

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

PERMY defines the permeability in the Y direction for all the cells in the model via an array. The keyword can be used for all grid types, except for the Radial Grid geometry.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | PERMY | PERMY is an array of real positive numbers assigning the permeability in the Y direction to each cell in the model.<br>Repeat counts may be used, for example 20\*100.0. | None |
| mD | mD | mD |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.106: PERMY Keyword Description

See also the PERMX and PERMZ keywords to fully define the permeability for the model.

#### Example

\--

\-- DEFINE GRID BLOCK PERMY DATA FOR ALL CELLS (BASED ON NX x NY x NZ = 300)

\--

PERMY

100\*500.0 100\*50.0 100\*200.0 /

The above example defines the PERMY to be 500.0, 50.0, and 200.0 for the first, second and third layers in the model for all 300 cells, as defined by the DIMENS keyword in the RUNSPEC section.
