### PERMR -- Define the Permeability for Each Cell in the R Direction

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

PERMR sets the permeability for each cell in the R direction in a radial geometry grid. The RADIAL or SPIDER keywords in the RUNSPEC should be activated to indicate that radial or spider geometry is being used.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | PERMR | PERMR is an array of real positive numbers assigning the permeability in the R direction to each cell in the model. This equivalent to PERMX in a Cartesian grid.<br>Repeat counts may be used, for example 20\*100.0. | None |
| mD | mD | mD |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.103: PERMR Keyword Description

Note that the SPIDER keyword activates OPM Flow's radial grid geometry option for the model. This keyword will create a spiderweb-shaped grid based on a corner-point grid using the standard radial grid keywords: INRAD, DRV, DTHETAV, DZ/DZV etc. in the GRID the section. A spider grid can be viewed in 3D in OPM ResInsight unlike radial grids that cannot be viewed in the software. To overcome this, the simulator now converts radial grids to Irregular Corner-Point Grids and adjusts the model's pore volume to reflect radial coordinates; thus, overcoming the display limitation.

See also the PERMTHT and PERMZ keywords to fully define the permeability for a radial or spider grid model.

#### Example

\--

\-- DEFINE GRID BLOCK PERMR DATA FOR ALL CELLS (BASED ON NR x NY x NZ = 300)

\--

PERMR

100\*500.0 100\*50.0 100\*200.0 /

The above example defines the PERMR to be 500.0, 50.0, and 200.0 for the first, second and third layers in the model for all 300 cells, as defined by the DIMENS keyword (10, 10, 3) in the RUNSPEC section.
