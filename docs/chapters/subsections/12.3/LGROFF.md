### LGROFF -- Deactivate a Local Grid Refinement

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [LGROFF](#__RefHeading___Toc281548_2843394514) keyword deactivates a stated Local Grid Refinement ("LGR") and optionally sets the minimum number of wells below which the [LGR](#__RefHeading___Toc55049_4106839650) will be automatically deactivated. LGRs must have declared by the [LGR](#__RefHeading___Toc55049_4106839650) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, and defined by the [CARFIN](#__RefHeading___Toc150726_63720426) (Cartesian [LGR](#__RefHeading___Toc55049_4106839650) grid) or RADIN/RADIN4 (radial [LGR](#__RefHeading___Toc55049_4106839650) grid) keywords in the [GRID](#__RefHeading___Toc38674_784232322) section. LGRs can subsequently be activated by the [LGRON](#__RefHeading___Toc281550_2843394514) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

Currently, OPM Flow does not support the local grid refinement feature and therefore this keyword is ignored by the simulator.

| 1 | LGRNAME | A character string of up to eight characters in length that defines the [LGR](#__RefHeading___Toc55049_4106839650) name for which the [LGR](#__RefHeading___Toc55049_4106839650) is being deactivated.<br>The [LGR](#__RefHeading___Toc55049_4106839650) must have been previously defined by the [CARFIN](#__RefHeading___Toc150726_63720426) (Cartesian [LGR](#__RefHeading___Toc55049_4106839650) grid) or RADIN/RADIN4 (radial [LGR](#__RefHeading___Toc55049_4106839650) grid) keywords in the [GRID](#__RefHeading___Toc38674_784232322) section. | None |
| --- | --- | --- | --- |
| 2 | MNWELLS | A positive integer greater than or equal to zero that defines the minimum number of active wells, below which the [LGR](#__RefHeading___Toc55049_4106839650) will be automatically deactivated.<br>The default value of zero implies that there is no limit to the number of wells and results in the [LGR](#__RefHeading___Toc55049_4106839650) being unconditionally being deactivated. | 0 |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.50: LGROFF Keyword Description

#### Example

The example below unconditionally deactivates LGR-OP01, and sets the minimum number of active wells for deactivating LGR-OP02 and LGR-OP03 to one. For all the gas well LGRs (LGR-GP\*) the minimum number of wells for deactivation is set to two.

\--

\-- DEACTIVATE LOCAL GRID REFINEMENTS

\--

\-- LGRNAME MNWELLS

LGROFF

LGR-OP01 /

LGR-OP02 1 /

LGR-OP03 1 /

LGR-GP\* 2 /

/
