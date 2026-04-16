### LGRLOCK -- Deactivate Local Grid Refinement Independent Time Steps

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [LGRLOCK](#__RefHeading___Toc264711_2843394514) keyword deactivates the Local Grid Refinement ("LGR") Independent Time Step option that allows the [LGR](#__RefHeading___Toc55049_4106839650) to have solution time steps independent of the host grid for the stated [LGR](#__RefHeading___Toc55049_4106839650), that is the [LGR](#__RefHeading___Toc55049_4106839650) will now follow the global grid solution time steps. LGRs must have declared by the [LGR](#__RefHeading___Toc55049_4106839650) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, and defined by the [CARFIN](#__RefHeading___Toc150726_63720426) (Cartesian [LGR](#__RefHeading___Toc55049_4106839650) grid) or RADIN/RADIN4 (radial [LGR](#__RefHeading___Toc55049_4106839650) grid) keywords in the [GRID](#__RefHeading___Toc38674_784232322) section. [LGR](#__RefHeading___Toc55049_4106839650) independent solution time stepping can be activated by the [LGRFREE](#__RefHeading___Toc259100_2843394514) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

Currently, OPM Flow does not support the local grid refinement feature and therefore this keyword is ignored by the simulator.

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 1                                                                                                                                        | > LGRNAME | > A character string of up to eight characters in length that defines the [LGR](#__RefHeading___Toc55049_4106839650) name for which independent solution time stepping is to be deactivated.                                                                                                                                                    | > None |
|                                                                                                                                            |           |                                                                                                                                                                                                                                                                                                                                                 |        |
|                                                                                                                                            |           | > The [LGR](#__RefHeading___Toc55049_4106839650) must have been previously defined by the [CARFIN](#__RefHeading___Toc150726_63720426) (Cartesian [LGR](#__RefHeading___Toc55049_4106839650) grid) or RADIN/RADIN4 (radial [LGR](#__RefHeading___Toc55049_4106839650) grid) keywords in the [GRID](#__RefHeading___Toc38674_784232322) section. |        |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > Notes:                                                                                                                                   |           |                                                                                                                                                                                                                                                                                                                                                 |        |
|                                                                                                                                            |           |                                                                                                                                                                                                                                                                                                                                                 |        |
| 1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/".   |           |                                                                                                                                                                                                                                                                                                                                                 |        |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+

Table 12.49: LGRLOCK Keyword Description

#### Example

The example below defines three oil LGRs(LGR-OP01,-OP02, and -OP03) and all the gas well LGRs (LGR-GP\*) that should have their independent solution time steps deactivated.

\--

\-- DEACTIVATE LOCAL GRID REFINEMENT INDEPENDENT TIME STEPS

\--

\-- LGRNAME

LGRLOCK

LGR-OP01 /

LGR-OP02 /

LGR-OP03 /

LGR-GP\* /

/
