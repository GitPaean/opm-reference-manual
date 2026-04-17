### HMMULTFT -- History Match Fault Transmissibility Gradient Cumulative Multipliers

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

HMMULTFT defines the history match fault transmissibility gradient cumulative multipliers to be applied to the fault transmissibilities for faults declared by the FAULT keyword in the GRID section, for when the History Match Gradient option has been activated by the HMDIMS keyword in the RUNSPEC section. The keyword allows for the re-scaling of the existing fault transmissibilities calculated by OPM Flow, or if the MULTFLT keyword has been entered, then HMMULTFT is applied to the existing MULTFLT multipliers.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
