### HRFIN -- Define the Ratio of LGR Grid Blocks in the R-Direction

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[HRFIN](#__RefHeading___Toc235947_4219267791)[^1] defines the ratio of grid blocks for the [DRV](#__RefHeading___Toc91991_705534506) keyword in the r-direction via a vector within a Local Grid Refinement ("LGR") as opposed to defining the size for each cell for a Radial [LGR](#__RefHeading___Toc55049_4106839650) Grid. The [LGR](#__RefHeading___Toc55049_4106839650) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section should be activated to indicate an [LGR](#__RefHeading___Toc55049_4106839650) is being used, and the keyword [HRFIN](#__RefHeading___Toc235947_4219267791) should be placed in between the RADIN (or RAFDIN4) and [ENDFIN](#__RefHeading___Toc111797_332691817) keywords in the [GRID](#__RefHeading___Toc38674_784232322) section. The [DRV](#__RefHeading___Toc91991_705534506) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section defines the radial grid size in terms of the length, that is feet for field units, this keyword defines the length as the ratio of the previous cell size, staring with the inner radius ([INRAD](#__RefHeading___Toc19324_3701168388)).

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [HRFIN](#__RefHeading___Toc235947_4219267791) | [HRFIN](#__RefHeading___Toc235947_4219267791) is a vector of real numbers describing the ratio of cell size for the grid blocks in the r-direction in a radial [LGR](#__RefHeading___Toc55049_4106839650) for the [DRV](#__RefHeading___Toc91991_705534506) keyword.<br>Repeat counts may be used, for example 2\*1.5. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the *N*R* parameter *minus one on the [RADFIN](#__RefHeading___Toc76871_718313858) or [RADFIN4](#__RefHeading___Toc76873_718313858) keywords in the [GRID](#__RefHeading___Toc38674_784232322) section<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.46: HRFIN Keyword Description

See also the [DR](#__RefHeading___Toc113051_2066951158), [DRV](#__RefHeading___Toc91991_705534506), [DTHETAV](#__RefHeading___Toc19322_3701168388), and [DZ](#__RefHeading___Toc45769_719036256) keywords in the [GRID](#__RefHeading___Toc38674_784232322) section to fully define a radial [LGR](#__RefHeading___Toc55049_4106839650) model.

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

The above example defines the size of the cells in the R direction based on NR equals 7, resulting in NR-1 values on the [RADFIN](#__RefHeading___Toc76871_718313858) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section. Note the [INRAD](#__RefHeading___Toc19324_3701168388) keyword to define the inner radius of the radial grid.

[^1]: Radial grids are not currently implemented in this version of OPM Flow, but is expected to be incorporated in a future release.
