### GASMONTH -- Define Start of Annual Scheduling Event

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, GASMONTH, states the month for which subsequent scheduling events take place within an Annual Schedule section for when the Gas Field Operations option has been activated by the GASFIELD keyword in the RUNSPEC section. The keyword must lie in between the GASBEGIN, that defines the start of an Annual Scheduling section and the GASEND keyword that ends the section. Optionally, the keyword can be used to write a report to the print file (\*.PRT) at the requested month.

See also the GASBEGIN and GASEND keywords in the RUNSPEC section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
