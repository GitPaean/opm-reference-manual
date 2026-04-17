### PERMJFUN -- Define Leverett J-Function Permeability for All Cells

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

PERMJFUN defines the permeability to be used in de-normalizing the Leverett J-Functions[^1] for when the PERM variable on the JFUNC or the JFUNCR keyword in the GRID section has been set to "U", as oppose to using PERMX, PERMY, PERMZ arrays etc.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | PERMJFUN | PERMJFUN is an array of real positive numbers assigning the permeability to be used in de-normalizing the Leverett J-Function to each cell in the model.<br>Repeat counts may be used, for example 20\*100.0. | None |
| mD | mD | mD |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.102: PERMJFUN Keyword Description

For grid blocks that have not been assigned a PERMJFUN value the default directional permeability will be used, that is the average of PERMX and PERMY.

See also the PERMX, PERMY and PERMZ keywords to fully define the permeability for the model.

#### Example

\--

\-- DEFINE GRID BLOCK PERMJFUN FOR ALL CELLS (BASED ON NX x NY x NZ = 300)

\--

PERMJFUN

100\*500.0 100\*50.0 100\*200.0 /

The above example defines the PERMJFUN to be 500.0, 50.0, and 200.0 for the first, second and third layers in the model for all 300 cells, as defined by the DIMENS keyword in the RUNSPEC section.

[^1]: Leverett, M. C.; "Capillary Behaviour in Porous Solids", Trans. AIME (1941) 142, 152-168.
