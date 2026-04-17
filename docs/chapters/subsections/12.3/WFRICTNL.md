### WFRICTNL -- Define Well as a Friction Well (LGR)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WFRICTNL keyword is used to declare a previously defined Local Grid Refinement ("LGR") well as a LGR friction well and to set the characteristics for this type of well including: tubing size, pipe roughness, and the connections to the grid. Wellbore friction is important in horizontal and multi-lateral wells where the pressure loss along the pipe can effect a well's performance. Note that unlike other SCHEDULE section well keywords, multiple wells cannot be entered with one WFRICTNL keyword, that is, the keyword must be repeated for each well.

See also the WFRICTN keyword in the SCHEDULE section that performs similar functionality for wells in the global grid.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
