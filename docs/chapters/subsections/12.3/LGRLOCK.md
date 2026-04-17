### LGRLOCK -- Deactivate Local Grid Refinement Independent Time Steps

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The LGRLOCK keyword deactivates the Local Grid Refinement ("LGR") Independent Time Step option that allows the LGR to have solution time steps independent of the host grid for the stated LGR, that is the LGR will now follow the global grid solution time steps. LGRs must have declared by the LGR keyword in the RUNSPEC section, and defined by the CARFIN (Cartesian LGR grid) or RADIN/RADIN4 (radial LGR grid) keywords in the GRID section. LGR independent solution time stepping can be activated by the LGRFREE keyword in the SCHEDULE section.

Currently, OPM Flow does not support the local grid refinement feature and therefore this keyword is ignored by the simulator.

| 1 | LGRNAME | A character string of up to eight characters in length that defines the LGR name for which independent solution time stepping is to be deactivated.<br>The LGR must have been previously defined by the CARFIN (Cartesian LGR grid) or RADIN/RADIN4 (radial LGR grid) keywords in the GRID section. | None |
| --- | --- | --- | --- |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

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
