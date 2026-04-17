### PSTEADY -- Activate Pseudo Steady State Flow Calculation Option

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The PSTEADY keyword activates Pseudo Steady State Flow Calculation option by advancing the simulator until it reaches a pseudo steady state flow and then sets the date to the date defined on this keyword, that is written to the RESTART file. Keyword also includes parameters defining the conditions for pseudo steady flow state.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
