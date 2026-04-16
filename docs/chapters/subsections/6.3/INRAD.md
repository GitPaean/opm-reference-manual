### INRAD -- Define the Inner Radius of a Radial Grid

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[INRAD](#__RefHeading___Toc19324_3701168388) defines the inner radius of the reservoir model for a radial grid geometry. The [RADIAL](#__RefHeading___Toc51752_2905512151) or [SPIDER](#__RefHeading___Toc439805_750232207) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) should be activated to indicate that radial geometry is being used.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [INRAD](#__RefHeading___Toc19324_3701168388) | A single real positive number defining the inner radius of a radial grid. | None |
| feet | m | cm |  |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 6.51: INRAD Keyword Description

Note that the [SPIDER](#__RefHeading___Toc439805_750232207) keyword activates OPM Flow's radial grid geometry option for the model. This keyword will create a spiderweb-shaped grid based on a corner-point grid using the standard radial grid keywords: [INRAD](#__RefHeading___Toc19324_3701168388), [DRV](#__RefHeading___Toc91991_705534506), [DTHETAV](#__RefHeading___Toc19322_3701168388), [DZ](#__RefHeading___Toc45769_719036256)/[DZV](#__RefHeading___Toc55601_3701168388) etc. in the [GRID](#__RefHeading___Toc38674_784232322) the section. A spider grid can be viewed in 3D in OPM ResInsight unlike radial grids that cannot be viewed in the software. To overcome this, the simulator now converts radial grids to Irregular Corner-Point Grids and adjusts the model's pore volume to reflect radial coordinates; thus, overcoming the display limitation.

See also the [DR](#__RefHeading___Toc113051_2066951158), [DRV](#__RefHeading___Toc91991_705534506), [DTHETA](#__RefHeading___Toc120096_2066951158), [DTHETAV](#__RefHeading___Toc19322_3701168388) and [TOPS](#__RefHeading___Toc55283_3701168388) keywords to fully define a radial or spider grid in the model.

#### Example

\--

\-- INNER RADIUS OF FIRST GRID BLOCK IN THE RADIAL DIRECTION

\--

INRAD

0.25 /

The above example defines the inner radius of a radial grid to be 0.25 feet.
