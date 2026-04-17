### LGRON -- Activate a Local Grid Refinement

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The LGRON keyword activates a stated Local Grid Refinement ("LGR") and optionally sets the minimum number of wells above which the LGR will remain active. LGRs must have declared by the LGR keyword in the RUNSPEC section, and defined by the CARFIN (Cartesian LGR grid) or RADIN/RADIN4 (radial LGR grid) keywords in the GRID section. LGRs can subsequently be deactivated by the LGROFF keyword in the SCHEDULE section.

Currently, OPM Flow does not support the local grid refinement feature and therefore this keyword is ignored by the simulator.

| 1 | LGRNAME | A character string of up to eight characters in length that defines the LGR name for which the LGR is being activated.<br>The LGR must have been previously defined by the CARFIN (Cartesian LGR grid) or RADIN/RADIN4 (radial LGR grid) keywords in the GRID section. | None |
| --- | --- | --- | --- |
| 2 | MNWELLS | A positive integer greater than or equal to zero that defines the minimum number of active wells, below which the LGR will be automatically deactivated.<br>The default value of zero implies that there is no limit to the number of wells and results in the LGR being unconditionally being activated. | 0 |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.51: LGRON Keyword Description

#### Example

The example below unconditionally activates LGR-OP01, and sets the minimum number of active wells for activating LGR-OP02 and LGR-OP03 to one. For all the gas well LGRs (LGR-GP\*) the minimum number of wells for activating these LGRs is set to two.

\--

\-- ACTIVATE LOCAL GRID REFINEMENTS

\--

\-- LGRNAME MNWELLS

LGRON

LGR-OP01 /

LGR-OP02 1 /

LGR-OP03 1 /

LGR-GP\* 2 /

/
