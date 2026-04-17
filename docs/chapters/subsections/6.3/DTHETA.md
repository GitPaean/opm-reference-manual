### DTHETA -- Define the Size of Grid Blocks in the THETA Direction for All Cells

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

DTHETA defines the size of all grid blocks in the Theta direction via an array for each cell in model. The RADIAL or SPIDER keyword in the RUNSPEC section should be activated to indicate that radial or spider geometry is being used.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | DTHETA | DTHETA is an array of real numbers describing the cell size in the THETA direction in radial grids for each cell in the model.<br>Repeat counts may be used, for example 10\*25.0 | None |
| degrees | degrees | degrees |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.24: DTHETA Keyword Description

Note that the SPIDER keyword activates OPM Flow's radial grid geometry option for the model. This keyword will create a spiderweb-shaped grid based on a corner-point grid using the standard radial grid keywords: INRAD, DRV, DTHETAV, DZ/DZV etc. in the GRID the section. A spider grid can be viewed in 3D in OPM ResInsight unlike radial grids that cannot be viewed in the software. To overcome this, the simulator now converts radial grids to Irregular Corner-Point Grids and adjusts the model's pore volume to reflect radial coordinates; thus, overcoming the display limitation. See also the DRV, DTHETAV, DZ and TOPS keywords in the GRID section to fully define a radial or spider grid model.

#### Example

Given the dimensions of the grid in the RUNSPEC section to be 10, 6, 1 for NX, NY and NZ respectively, then DTHETA should be defined as:

\--

\-- DEFINE GRID BLOCK SIZES IN THE THETA DIRECTION

\--

DTHETA

10\*60.0

10\*60.0

10\*60.0

10\*60.0

10\*60.0

10\*60.0

/

The above example defines the size of the cells in the R direction based on 60 cells in the model as defined by the DIMENS keyword in the RUNSPEC section.
