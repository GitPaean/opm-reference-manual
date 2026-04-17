### QMOBIL -- Activate or Deactivate LGR End-Point Mobility Correction

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The QMOBIL keyword activates or deactivates the end-point mobility correction for Local Grid Refinements ("LGR"), for when LGRs have been activated for the input deck using the LGR keyword in the RUNSPEC section. QMOBIL should be placed in between the LGR definition keywords CARFIN, or RADIN (or RAFDIN4) and the ENDFIN keyword in the GRID section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
