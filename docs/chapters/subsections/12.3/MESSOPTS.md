### MESSOPTS -- Reset Severity Level for Forced Time Steps

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, MESSOPTS, resets the severity level for time steps that are forced to be accepted by the simulator. The normal severity level for this type of simulator generated message is PROBLEM and this can result in the run stopping depending on the parameters entered on the MESSAGES keyword. MESSOPTS can be used to reset the severity level to MESSAGE, COMMENT, WARNING, or PROBLEM; for example, to avoid the run terminating due to too many PROBLEM messages.

Note that the MESSAGES keyword is a global keyword can therefore be used in any section; however, only the last instance of the keywords is active. The MESSOPTS keyword can only be used in the SCHEDULE section but can be used multiple times to change the severity level for forced time steps. Again, only the last occurrence of the keyword is active.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.
