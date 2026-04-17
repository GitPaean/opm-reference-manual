### INRAD -- Define the Inner Radius of a Radial Grid

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

INRAD defines the inner radius of the reservoir model for a radial grid geometry. The RADIAL or SPIDER keyword in the RUNSPEC should be activated to indicate that radial geometry is being used.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | INRAD | A single real positive number defining the inner radius of a radial grid. | None |
| feet | m | cm |  |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 6.51: INRAD Keyword Description

Note that the SPIDER keyword activates OPM Flow's radial grid geometry option for the model. This keyword will create a spiderweb-shaped grid based on a corner-point grid using the standard radial grid keywords: INRAD, DRV, DTHETAV, DZ/DZV etc. in the GRID the section. A spider grid can be viewed in 3D in OPM ResInsight unlike radial grids that cannot be viewed in the software. To overcome this, the simulator now converts radial grids to Irregular Corner-Point Grids and adjusts the model's pore volume to reflect radial coordinates; thus, overcoming the display limitation.

See also the DR, DRV, DTHETA, DTHETAV and TOPS keywords to fully define a radial or spider grid in the model.

#### Example

\--

\-- INNER RADIUS OF FIRST GRID BLOCK IN THE RADIAL DIRECTION

\--

INRAD

0.25 /

The above example defines the inner radius of a radial grid to be 0.25 feet.
