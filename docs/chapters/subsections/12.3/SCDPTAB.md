### SCDPTAB -- Well Connection Scale Deposition Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

SCDATAB defines the well connection scale deposition rate as a function of sea water flow rate, for when the Scale Deposition option has been activated by declaring the dimensions of the scaling deposition tables using the SCDPDIMS keyword in the RUNSPEC section. The SCDATAB tables are allocated to individual wells using the WSCTAB keyword and the sea water fraction is based on a water tracer entered via the SCDPTRAC keyword; both keywords are in the SCHEDULE section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
