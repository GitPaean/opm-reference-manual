### LOAD -- Load a SAVE File for a Fast Restart

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The LOAD keyword loads a previously generated SAVE file to enable a fast restart. A SAVE file contains all the data from a previous run's RUNSPEC, GRID, EDIT, PROPS and REGIONS sections, and thus there is no need for the simulator to calculate various parameters, including grid block transmissibilities etc. This allows for the current run to restart quicker than a conventional restart run using the RESTART keyword in the SOLUTION section via a RESTART file (\*.UNRST or \*.FUNRST etc.). The keyword should be the first keyword in the input deck and the RUNSPEC, GRID, EDIT, PROPS and REGIONS sections should be deleted from the input deck.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
