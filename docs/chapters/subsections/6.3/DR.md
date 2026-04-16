### DR -- Define the Size of Grid Blocks in the R Direction for All Cells

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[DR](#__RefHeading___Toc113051_2066951158) defines the size of all grid blocks in the R direction via an array for each cell in the model. The [RADIAL](#__RefHeading___Toc51752_2905512151) or [SPIDER](#__RefHeading___Toc439805_750232207) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section should be activated to indicate that radial or spider geometry is being used.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [DR](#__RefHeading___Toc113051_2066951158) | [DR](#__RefHeading___Toc113051_2066951158) is an array of real numbers describing the cell size in the R direction for each cell in the model in a radial grid.<br>Repeat counts may be used, for example 10\*100.0. | None |
| feet | m | cm |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  The first layer (K=1) must always be fully defined; however, subsequent layers may be default and if defaulted they will take the values from the layer above.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 6.22: DR Keyword Description

Note that the [SPIDER](#__RefHeading___Toc439805_750232207) keyword activates OPM Flow's radial grid geometry option for the model. This keyword will create a spiderweb-shaped grid based on a corner-point grid using the standard radial grid keywords: [INRAD](#__RefHeading___Toc19324_3701168388), [DRV](#__RefHeading___Toc91991_705534506), [DTHETAV](#__RefHeading___Toc19322_3701168388), [DZ](#__RefHeading___Toc45769_719036256)/[DZV](#__RefHeading___Toc55601_3701168388) etc. in the [GRID](#__RefHeading___Toc38674_784232322) the section. A spider grid can be viewed in 3D in OPM ResInsight unlike radial grids that cannot be viewed in the software. To overcome this, the simulator now converts radial grids to Irregular Corner-Point Grids and adjusts the model's pore volume to reflect radial coordinates; thus, overcoming the display limitation.

See also the [DRV](#__RefHeading___Toc91991_705534506), [DTHETAV](#__RefHeading___Toc19322_3701168388), [DZ](#__RefHeading___Toc45769_719036256) and [TOPS](#__RefHeading___Toc55283_3701168388) keywords in the [GRID](#__RefHeading___Toc38674_784232322) section to fully define a radial or spider grid model.

#### Example

Given the dimensions of the grid in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section to be 10,1, 8 for NX, NY and NZ respectively, we first define the inner radius of the radial model,

\--

\-- INNER RADIUS OF FIRST GRID BLOCK IN THE RADIAL DIRECTION

\--

INRAD

0.25

/

and then [DR](#__RefHeading___Toc113051_2066951158) should be defined as:

\--

\-- DEFINE GRID BLOCK R DIRECTION CELL SIZE

\--

DR

1.75 2.32 5.01 10.84 23.39 50.55 109.21 235.92 509.68 1101.0

1.75 2.32 5.01 10.84 23.39 50.55 109.21 235.92 509.68 1101.0

1.75 2.32 5.01 10.84 23.39 50.55 109.21 235.92 509.68 1101.0

1.75 2.32 5.01 10.84 23.39 50.55 109.21 235.92 509.68 1101.0

1.75 2.32 5.01 10.84 23.39 50.55 109.21 235.92 509.68 1101.0

1.75 2.32 5.01 10.84 23.39 50.55 109.21 235.92 509.68 1101.0

1.75 2.32 5.01 10.84 23.39 50.55 109.21 235.92 509.68 1101.0

1.75 2.32 5.01 10.84 23.39 50.55 109.21 235.92 509.68 1101.0

/

The above example defines the size of the cells in the R direction based on 80 cells in the model as defined by the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

Note that since the first layer (K=1) must be defined and subsequent layers default to the layer above then:

\--

\-- INNER RADIUS OF FIRST GRID BLOCK IN THE RADIAL DIRECTION

\--

INRAD

0.25

/

\--

\-- DEFINE GRID BLOCK R DIRECTION CELL SIZE

\--

DR

1.75 2.32 5.01 10.84 23.39 50.55 109.21 235.92 509.68 1101.0

/

is equivalent to previous example.
