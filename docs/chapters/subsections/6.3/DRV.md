### DRV -- Define the Size of Grid Blocks in the R Direction via a Vector

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

DRV defines the size of grid blocks in the R direction via a vector as opposed to defining the property for each cell for a Radial or Spider Grid. The RADIAL or SPIDER keyword in the RUNSPEC section should be activated to indicate that radial or spider geometry is being used.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | DRV | DRV is a vector of real numbers describing the cell size for the grid blocks in the R direction in a radial grid.<br>Repeat counts may be used, for example 10\*100.0. | None |
| feet | m | cm |  |
| Notes:<br>1)  The number of entries should correspond to the NX parameter on the DIMENS keyword in the RUNSPEC section<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.23: DRV Keyword Description

Note that the SPIDER keyword activates OPM Flow's radial grid geometry option for the model. This keyword will create a spiderweb-shaped grid based on a corner-point grid using the standard radial grid keywords: INRAD, DRV, DTHETAV, DZ/DZV etc. in the GRID the section. A spider grid can be viewed in 3D in OPM ResInsight unlike radial grids that cannot be viewed in the software. To overcome this, the simulator now converts radial grids to Irregular Corner-Point Grids and adjusts the model's pore volume to reflect radial coordinates; thus, overcoming the display limitation.

See also the DR, DTHETAV, DZ and TOPS keywords in the GRID section to fully define a radial or spider grid model.

#### Example

\--

\-- INNER RADIUS OF FIRST GRID BLOCK IN THE RADIAL DIRECTION

\--

INRAD

0.25

/

\--

\-- DEFINE GRID BLOCK SIZES IN THE R DIRECTION

\--

DRV

1.75 2.32 5.01 10.84 23.39 50.55 109.21 235.92 509.68 1101.08 /

The above example defines the size of the cells in the R direction based on NX equals 10 on the DIMENS keyword in the RUNSPEC section. Note the INRAD keyword to define the inner radius of the radial grid.
