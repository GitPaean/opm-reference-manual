### DTHETAV -- Sets the Size of Grid Blocks in THETA Direction via a Vector

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

DTHETAV defines the size of grid blocks in the THETA direction via a vector as opposed to defining the property for each cell for a Radial Grid. The RADIAL or SPIDER keyword in the RUNSPEC should be activated to indicate that radial geometry is being used.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | DTHETAV | DTHETAV is a vector of real numbers describing the cell size for the grid blocks in the THETA direction in a radial grid.<br>Repeat counts may be used, for example 10\*100.0. | None |
| degrees | degrees | degrees |  |
| Notes:<br>1)  The number of entries should correspond to the NY parameter of the DIMENS keyword in the RUNSPEC section.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.25: DTHETA Keyword Description

Note that the SPIDER keyword activates OPM Flow's radial grid geometry option for the model. This keyword will create a spiderweb-shaped grid based on a corner-point grid using the standard radial grid keywords: INRAD, DRV, DTHETAV, DZ/DZV etc. in the GRID the section. A spider grid can be viewed in 3D in OPM ResInsight unlike radial grids that cannot be viewed in the software. To overcome this, the simulator now converts radial grids to Irregular Corner-Point Grids and adjusts the model's pore volume to reflect radial coordinates; thus, overcoming the display limitation.

See also the DRV, DZV and TOPS keywords to fully define a radial or spider grid model.

#### Example

\--

\-- DEFINE GRID BLOCK SIZES IN THE THETA DIRECTION (BASED ON NY = 6)

\--

DTHETAV

60.0 60.0 60.0 60.0 60.0 60.0 /

The above example defines the size of the cells in the THETA direction based on NY equals six in the DIMENS keyword in the RUNSPEC section.
