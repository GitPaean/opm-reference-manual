### OUTRAD -- Define the Outer Radius of a Radial Grid

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[OUTRAD](#__RefHeading___Toc19326_3701168388) defines the OUTER radius of the reservoir model for a radial or spider grid geometry. The [RADIAL](#__RefHeading___Toc51752_2905512151) or [SPIDER](#__RefHeading___Toc439805_750232207) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) should be activated to indicate that radial or spider geometry is being used.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

+-------------------------------------------+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > No.                                     | > Name                                          | > Description                                                                                                                         | > Default |
+-------------------------------------------+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Field                                   | > Metric                                        | > Laboratory                                                                                                                          |           |
+-------------------------------------------+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 1                                       | > [OUTRAD](#__RefHeading___Toc19326_3701168388) | > A single real positive number greater than [INRAD](#__RefHeading___Toc19324_3701168388) defining the outer radius of a radial grid. | > None    |
+-------------------------------------------+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > feet                                    | > m                                             | > cm                                                                                                                                  |           |
+-------------------------------------------+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Notes:                                  |                                                 |                                                                                                                                       |           |
|                                           |                                                 |                                                                                                                                       |           |
| 1)  The keyword is terminated by a "/".   |                                                 |                                                                                                                                       |           |
+-------------------------------------------+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-----------+

Table 6.99: OUTRAD Keyword Description

Note that the [SPIDER](#__RefHeading___Toc439805_750232207) keyword activates OPM Flow's radial grid geometry option for the model. This keyword will create a spiderweb-shaped grid based on a corner-point grid using the standard radial grid keywords: [INRAD](#__RefHeading___Toc19324_3701168388), [DRV](#__RefHeading___Toc91991_705534506), [DTHETAV](#__RefHeading___Toc19322_3701168388), [DZ](#__RefHeading___Toc45769_719036256)/[DZV](#__RefHeading___Toc55601_3701168388) etc. in the [GRID](#__RefHeading___Toc38674_784232322) the section. A spider grid can be viewed in 3D in OPM ResInsight unlike radial grids that cannot be viewed in the software. To overcome this, the simulator now converts radial grids to Irregular Corner-Point Grids and adjusts the model's pore volume to reflect radial coordinates; thus, overcoming the display limitation.

The keyword allows for an alternative method of entering the size of the R direction grid cells instead of entering the data using the [DR](#__RefHeading___Toc113051_2066951158) or [DRV](#__RefHeading___Toc91991_705534506) keywords in the [GRID](#__RefHeading___Toc38674_784232322) section. Given the internal radius set by the [INRAD](#__RefHeading___Toc19324_3701168388) keyword, the external radius set by the [OUTRAD](#__RefHeading___Toc19326_3701168388) keyword and the number of grid cells in the R direction set by the NX variable on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, the R direction cells sizes are computed automatically on a geometric spacing, as defined by:

or

and the [DR](#__RefHeading___Toc113051_2066951158) value for the i^th^ cell, that is the value that can also be manually entered on the [DR](#__RefHeading___Toc113051_2066951158) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section, is given by:

Where:

[DR](#__RefHeading___Toc113051_2066951158)~i~ = [DR](#__RefHeading___Toc113051_2066951158) value for the i^th^ cell

R~i~ = current total radius for the i radii.

Ri-1 = total radius for the i -- 1 radii.

NX (NR) = number of radial grid cells excluding the inner radius

[OUTRAD](#__RefHeading___Toc19326_3701168388) = the outer radius of the radial grid, the value includes the inner radius.

For example, given an inner radius set to 0.25, an outer radius of 2,050 and the number of cells in the R direction set to ten, then shows the grid size calculations.

+-------------------------------------------------+------------+----------------------------------------------+---------+
| > [INRAD](#__RefHeading___Toc19324_3701168388)  | > 0.25     |                                              |         |
+-------------------------------------------------+------------+----------------------------------------------+---------+
| > [OUTRAD](#__RefHeading___Toc19326_3701168388) | > 2050.0   |                                              |         |
+-------------------------------------------------+------------+----------------------------------------------+---------+
| > NX                                            | > 10       |                                              |         |
+-------------------------------------------------+------------+----------------------------------------------+---------+
| > NX                                            | > Ri       | > [DR](#__RefHeading___Toc113051_2066951158) | > Ratio |
+-------------------------------------------------+------------+----------------------------------------------+---------+
| > 0                                             | > 0.250    | > 0.250                                      |         |
+-------------------------------------------------+------------+----------------------------------------------+---------+
| > 1                                             | > 0.616    | > 0.366                                      | > 1.463 |
+-------------------------------------------------+------------+----------------------------------------------+---------+
| > 2                                             | > 1.516    | > 0.900                                      | > 2.463 |
+-------------------------------------------------+------------+----------------------------------------------+---------+
| > 3                                             | > 3.733    | > 2.217                                      | > 2.463 |
+-------------------------------------------------+------------+----------------------------------------------+---------+
| > 4                                             | > 9.193    | > 5.460                                      | > 2.463 |
+-------------------------------------------------+------------+----------------------------------------------+---------+
| > 5                                             | > 22.638   | > 13.445                                     | > 2.463 |
+-------------------------------------------------+------------+----------------------------------------------+---------+
| > 6                                             | > 55.748   | > 33.109                                     | > 2.463 |
+-------------------------------------------------+------------+----------------------------------------------+---------+
| > 7                                             | > 137.281  | > 81.533                                     | > 2.463 |
+-------------------------------------------------+------------+----------------------------------------------+---------+
| > 8                                             | > 338.058  | > 200.777                                    | > 2.463 |
+-------------------------------------------------+------------+----------------------------------------------+---------+
| > 9                                             | > 832.477  | > 494.420                                    | > 2.463 |
+-------------------------------------------------+------------+----------------------------------------------+---------+
| > 10                                            | > 2050.000 | > 1217.523                                   | > 2.463 |
+-------------------------------------------------+------------+----------------------------------------------+---------+
| > Total                                         |            | > 2050.000                                   |         |
+-------------------------------------------------+------------+----------------------------------------------+---------+

Table 6.100: [OUTRAD](#__RefHeading___Toc19326_3701168388) Radial Grid Example

See also the [DR](#__RefHeading___Toc113051_2066951158), [DRV](#__RefHeading___Toc91991_705534506), [DTHETA](#__RefHeading___Toc120096_2066951158), [DTHETAV](#__RefHeading___Toc19322_3701168388) and [TOPS](#__RefHeading___Toc55283_3701168388) keywords to fully define a Radial or Spider Grid.

#### Example

\--

\-- INNER RADIUS OF FIRST GRID BLOCK IN THE RADIAL DIRECTION

\--

INRAD

0.25 /

\--

\-- OUTER RADIUS OF FIRST GRID BLOCK IN THE RADIAL DIRECTION

\--

OUTRAD

2050.0 /

The above example defines the inner radius to be 0.25 and the outer radius to be 2,050 feet. Note that the outer radius includes the inner radius.
