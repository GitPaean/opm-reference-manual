### PERMTHT -- Define the Permeability for Each Cell in the THETA Direction

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[PERMTHT](#__RefHeading___Toc114309_23127940) sets the permeability for each cell in the THETA direction in a radial geometry grid. The [RADIAL](#__RefHeading___Toc51752_2905512151) or [SPIDER](#__RefHeading___Toc439805_750232207) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) should be activated to indicate that radial or spider geometry is being used.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [PERMTHT](#__RefHeading___Toc114309_23127940) | [PERMTHT](#__RefHeading___Toc114309_23127940) is an array of real positive numbers assigning the permeability in the THETA direction to each cell in the model. This equivalent to [PERMY](#__RefHeading___Toc45793_719036256) in a Cartesian grid.<br>Repeat counts may be used, for example 20\*100.0. | None |
| mD | mD | mD |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.104: PERMTHT Keyword Description

Note that the [SPIDER](#__RefHeading___Toc439805_750232207) keyword activates OPM Flow's radial grid geometry option for the model. This keyword will create a spiderweb-shaped grid based on a corner-point grid using the standard radial grid keywords: [INRAD](#__RefHeading___Toc19324_3701168388), [DRV](#__RefHeading___Toc91991_705534506), [DTHETAV](#__RefHeading___Toc19322_3701168388), [DZ](#__RefHeading___Toc45769_719036256)/[DZV](#__RefHeading___Toc55601_3701168388) etc. in the [GRID](#__RefHeading___Toc38674_784232322) the section. A spider grid can be viewed in 3D in OPM ResInsight unlike radial grids that cannot be viewed in the software. To overcome this, the simulator now converts radial grids to Irregular Corner-Point Grids and adjusts the model's pore volume to reflect radial coordinates; thus, overcoming the display limitation.

See also the [PERMR](#__RefHeading___Toc19328_3701168388) and [PERMZ](#__RefHeading___Toc45795_719036256) keywords to fully define the permeability for a radial or spider grid model.

#### Example

\--

\-- DEFINE GRID BLOCK PERMTHT DATA FOR ALL CELLS (NX x NY x NZ = 300)

\--

PERMTHT

100\*500.0 100\*50.0 100\*200.0 /

The above example defines the [PERMTHT](#__RefHeading___Toc114309_23127940) to be 500.0, 50.0, and 200.0 for the first, second and third layers in the model for all 300 cells, as defined by the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword (10, 10, 3) in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.
