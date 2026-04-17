### HMMROCK -- History Match Rock Compressibility Gradient Cumulative Multipliers

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

HMMROCK defines the rock compressibility gradient cumulative multipliers to be applied to the rock compressibility as defined by the ROCK keyword in the PROPS section, for when the History Match Gradient option has been activated by the HMDIMS keyword in the RUNSPEC section. The constant should be a real number.

The allocation of the ROCK tables to different grid blocks in the model is done via the PVTNUM or the SATNUM keywords in the REGION section.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.
