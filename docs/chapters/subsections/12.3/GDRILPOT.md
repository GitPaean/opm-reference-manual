### GDRILPOT -- Define Group Potential Rates for Automatic Drilling

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, GDRILPOT, defines the minimum group potential rate that will result in a well from the one of the automatic drilling queues, as defined by either the QDRILL or WDRILPRI keywords in the SCHEDULE section, to be drilled and placed on production. The advantage of using a group's potential, as oppose to a minimum rate limit, is that setting the potential greater than the group's minimum flow rate, will result in well being drilled in time to support the desired production rate.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
