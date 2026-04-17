### SCALELIM -- End-Point Scaling versus Depth Maximum Water Saturation

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the maximum water saturation allowed in a cell for when the end-point versus depth tables are used in the End-Point Scaling option to calculate the water saturation for a grid block. The End-Point Scaling option must be invoked by the ENDSCALE keyword in the RUNSPEC section to use this keyword, and the keyword may only be used in two phase runs containing water, or if the Miscible Flood option has been activated by the MISCIBLE keyword in the RUNSPEC section. This keyword functionality is not supported in OPM Flow.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
