### WTEMPQ -- Output Well Names and Well Lists to the Print File

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WTEMPQ prints out a user defined selected list of currently defined wells and well lists to the print file (\*.PRT). The keyword allows for sub-setting the well names etc., using the normal well and well list naming conventions. For example to list all wells beginning with the characters "OP" then one would use "OP\*" as the well name on this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
