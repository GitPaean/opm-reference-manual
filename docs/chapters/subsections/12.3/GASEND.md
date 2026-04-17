### GASEND -- Define End of Annual Scheduling Section

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, GASEND, defines the end of an Annual Scheduling section set of keywords used when the Gas Field Operations option has been activated by the GASFIELD keyword in the RUNSPEC section. An Annual Scheduling section starts with the GASBEGIN keyword and is terminated by the GASEND keyword, with keywords in between used to control and write reports at selected times between the start and end of a contract period. Only one Annual Scheduling section is activate at a time, that is, a subsequent Annual Scheduling section overwrites the previous set of entries. To clear the current Annual Schedule section enter the GASBEGIN keyword followed by the GASEND keyword word with no other keywords in between.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
