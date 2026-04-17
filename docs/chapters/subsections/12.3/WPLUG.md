### WPLUG -- Define Well Plug Back Length

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

Various keywords in the SCHEDULE section (WECON, GECON etc.) allow for a well to be automatically plugged back if the well violates a constraint, that is to close existing perforations (well connections). For example if the water cut exceeds 90%, then plug back the well. The WPLUG keyword defines for automatic plug backs the length of the perforations (length of connections) to be closed each time an automatic plug back is performed, together with various options on how the workover should be performed, top down, bottom up, etc.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
