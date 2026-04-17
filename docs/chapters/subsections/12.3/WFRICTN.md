### WFRICTN -- Define Well as a Friction Well

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WFRICTN keyword is used to declare a previously defined well as a friction well and to set the characteristics for this type of well including: tubing size, pipe roughness, and the connections to the grid. Wellbore friction is important in horizontal and multi-lateral wells where the pressure loss along the pipe can effect a well's performance. Note that unlike other SCHEDULE section well keywords, multiple wells cannot be entered with one WFRICTN keyword, that is, the keyword must be repeated for each well.

See also the WFRICTNL keyword in the SCHEDULE section that performs similar functionality for wells in Local Grid Refinements.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
