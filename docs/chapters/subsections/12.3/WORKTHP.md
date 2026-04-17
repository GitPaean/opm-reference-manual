### WORKTHP -- Define Well Workover Options for THP Killed Wells

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WORKTHP keyword defines workover options for when a well dies, that is unable to produce at the current operating conditions, when under Tubing Head Pressure ("THP") control. For example, if a well is producing to the high pressure separator and therefore has a high THP constraint, then the WORKTHP keyword can be used to switch the well to the lower pressure separator via re-setting the THP constraint.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
