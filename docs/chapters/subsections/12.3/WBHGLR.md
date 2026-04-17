### WBHGLR -- Define Well Bottom-Hole GLR Constraint

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, WBHGLR, defines a well's bottom-hole Gas Liquid Ratio ("GLR") constraint, where the GLR is the is the ratio of the "free" gas rate and liquid rate at bottom-hole conditions. The reference depth for bottom-hole conditions is given by the BHPREF variable on the WELSPECS keyword in the SCHEDULE section.

Normally this type of well control is applied to pumping wells to avoid the well "pumping off", that is when the liquid column above the pump is low, resulting in an increase in gas intake and an associated loss in pump efficiency.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
