### HRFIN -- Define the Ratio of LGR Grid Blocks in the R-Direction

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

HRFIN[^1] defines the ratio of grid blocks for the DRV keyword in the r-direction via a vector within a Local Grid Refinement ("LGR") as opposed to defining the size for each cell for a Radial LGR Grid. The LGR keyword in the RUNSPEC section should be activated to indicate an LGR is being used, and the keyword HRFIN should be placed in between the RADIN (or RAFDIN4) and ENDFIN keywords in the GRID section. The DRV keyword in the GRID section defines the radial grid size in terms of the length, that is feet for field units, this keyword defines the length as the ratio of the previous cell size, staring with the inner radius (INRAD).

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | HRFIN | HRFIN is a vector of real numbers describing the ratio of cell size for the grid blocks in the r-direction in a radial LGR for the DRV keyword.<br>Repeat counts may be used, for example 2\*1.5. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the *N*R* parameter *minus one on the RADFIN or RADFIN4 keywords in the GRID section<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.46: HRFIN Keyword Description

See also the DR, DRV, DTHETAV, and DZ keywords in the GRID section to fully define a radial LGR model.

#### Example

\--

\-- INNER RADIUS OF FIRST GRID BLOCK IN THE RADIAL DIRECTION

\--

INRAD 0.25 /

\--

\-- DEFINE GRID BLOCK DRV RATIOS IN THE R DIRECTION

\--

HRFIN

1.50 2.00 3.00 5.00 7.00 10.00 /

The above example defines the size of the cells in the R direction based on NR equals 7, resulting in NR-1 values on the RADFIN keyword in the GRID section. Note the INRAD keyword to define the inner radius of the radial grid.

[^1]: Radial grids are not currently implemented in this version of OPM Flow, but is expected to be incorporated in a future release.
