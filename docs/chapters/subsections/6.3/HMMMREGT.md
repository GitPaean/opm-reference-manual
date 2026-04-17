### HMMMREGT -- History Match Region Transmissibility Gradient Cumulative Multipliers

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The HMMMREGT keyword multiplies the transmissibility between two regions by a constant, for when the History Match Gradient option has been activated by the HMDIMS keyword in the RUNSPEC section. The constant should be a real number. Unlike the MULTREGT keyword in the GRID section, the HMMMREGT keyword modifications are cumulative.

Note that the HMMMREGT keyword only declares the two regions and the multiplier between those regions, the transmissibility direction (DIR on the MULTREGT keyword), type of transmissibility multiplier (TYPE on the MULTREGT keyword), and the region number array to use (ARRAY on the MULTREGT keyword), are all taken from the MULTREGY keyword. For example, the region number array can be FLUXNUM, MULTNUM or OPERNUM and these arrays must be defined and be available before the MULTREGT keyword is read by the simulator, and before the HMMMREGT keyword is used.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.
