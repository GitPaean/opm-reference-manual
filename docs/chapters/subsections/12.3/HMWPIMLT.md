### HMWPIMLT -- History Match Well Productivity Index Parameters

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, HMWPIMLT, defines the history match gradient parameters for well productiviity indices, for when the History Match Gradient option has been activated by the HMDIMS keyword in the RUNSPEC section. Wells must be specified using the WELPSECS keyword in the SCHEDULE section and their connections defined by the COMPDAT and/or COMPDATL keywords, also in the SCHEDULE section

See also the HMDIMS keyword in the RUNSPEC section that specifies the dimensions for the gradient option, including the maximum number of gradient wellss that can be used with the History Match Gradient option.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
