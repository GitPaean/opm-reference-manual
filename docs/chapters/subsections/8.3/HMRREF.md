### HMRREF -- History Match Rock Table Reference Pressure Values

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The HMRREF keyword defines the history match rock compaction reference pressure gradient values to be used in conjunction with HMMROCKT, ROCKTAB and ROCKTABH keywords in the PROPS section, for when the History Match Gradient option has been activated by the HMDIMS keyword in the RUNSPEC section. The history match rock compaction data is entered via the HMMROCKT, ROCKTAB and ROCKTABH keywords in the PROPS section.

See also the HMDIMS keyword in the RUNSPEC section that specifies the dimensions for the gradient option, including the maximum number of rock gradient parameters that can be used with the History Match Gradient option.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
