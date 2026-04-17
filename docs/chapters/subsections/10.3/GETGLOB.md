### GETGLOB -- Activate Loading of Global Grid Restart Data Option

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, GETGLOB, switches on the global grid read option for when the run is restarting from a RESTART file. Only the global grid will be loaded in the subsequent RESTART keyword and any Local Grid Refinements ("LGR") on the RESTART file will be ignored.

There is no data required for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

\--

\-- ACTIVATE LOADING OF GLOBAL GRID RESTART DATA OPTION

\--

GETGLOB

The above example switches on the option to only load the global grid from the RESTART file.
