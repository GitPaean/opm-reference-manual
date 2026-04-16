### HZFIN -- Define the Ratio of LGR Grid Blocks in the Z-Direction

+-----------------------------------------+-----------------------------------+----------------------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#__RefHeading___Toc40641_784232322) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+----------------------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[HZFIN](#__RefHeading___Toc227697_2135714711) defines the split ratio of grid blocks for the [DZV](#__RefHeading___Toc55601_3701168388) keyword in the z-direction via a vector within a Local Grid Refinement ("LGR") as opposed to defining the size for each cell for a Cartesian [LGR](#__RefHeading___Toc55049_4106839650) Grid. The [LGR](#__RefHeading___Toc55049_4106839650) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section should be activated to indicate an [LGR](#__RefHeading___Toc55049_4106839650) is being used, and the keyword [HYFIN](#__RefHeading___Toc200810_2135714711) should be placed in between the [CARFIN](#__RefHeading___Toc150726_63720426) and [ENDFIN](#__RefHeading___Toc111797_332691817) keywords in the [GRID](#__RefHeading___Toc38674_784232322) section. The [DZV](#__RefHeading___Toc55601_3701168388) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section defines the grid size in terms of the length, that is feet for field units, this keyword defines the length as the ratio of the coarse cells.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > No.                                                                                                                                                                                    | > Name          | > Description                                                                                                                                                                                                        | > Default |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Field                                                                                                                                                                                  | > Metric        | > Laboratory                                                                                                                                                                                                         |           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 1                                                                                                                                                                                      | > HYZIN         | > [HZFIN](#__RefHeading___Toc227697_2135714711) is a vector of real numbers describing the ratio of cell size for the grid blocks in the z-direction in a Cartesian [LGR](#__RefHeading___Toc55049_4106839650) grid. | > None    |
|                                                                                                                                                                                          |                 |                                                                                                                                                                                                                      |           |
|                                                                                                                                                                                          |                 | > Repeat counts may be used, for example 2\*2.0.                                                                                                                                                                     |           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > dimensionless                                                                                                                                                                          | > dimensionless | > dimensionless                                                                                                                                                                                                      |           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Notes:                                                                                                                                                                                 |                 |                                                                                                                                                                                                                      |           |
|                                                                                                                                                                                          |                 |                                                                                                                                                                                                                      |           |
| 1)  The number of entries should correspond to the NZ parameter on the [CARFIN](#__RefHeading___Toc150726_63720426) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section.   |                 |                                                                                                                                                                                                                      |           |
|                                                                                                                                                                                          |                 |                                                                                                                                                                                                                      |           |
| 2)  The keyword is terminated by a "/".                                                                                                                                                  |                 |                                                                                                                                                                                                                      |           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Table 6.49: HZFIN Keyword Description

See also the [CARFIN](#__RefHeading___Toc150726_63720426), [ENDFIN](#__RefHeading___Toc111797_332691817), [HXFIN](#__RefHeading___Toc326256_373485663), and [HYFIN](#__RefHeading___Toc200810_2135714711) keywords in the [GRID](#__RefHeading___Toc38674_784232322) section to fully define a Cartesian [LGR](#__RefHeading___Toc55049_4106839650) grid model.

#### Example

\--

\-- CARFIN LGR GRID COMMANDS

\--

\-- LGR \-\-\-\-- HOST GRID \-\-\-\-\-- \-- CARFIN GRID \-- MAX HOST

\-- NAME I1 I2 J1 J2 K1 K2 NX NY NZ WELLS NAME

CARFIN

LGR-OP01 24 25 86 87 1 50 5 3 100 1 GLOBAL /

\--

\-- DEFINE LGR GRID BLOCK IN THE Z-DIRECTION

NZFIN

50\*2 /

\--

\-- DEFINE GRID BLOCK LGR RATIOS IN THE Z-DIRECTION

\--

HZFIN

50\*2.0 /

ENDFIN

The above example defines the size of the cells in the z-direction based on NZ equals 100 on the [CARFIN](#__RefHeading___Toc150726_63720426) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section.
