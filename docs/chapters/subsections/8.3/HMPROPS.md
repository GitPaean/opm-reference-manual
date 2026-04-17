### HMPROPS -- History Match End-Point Section Start

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

HMPROPS defines the start of a history match end-points section, for when the History Match Gradient option has been activated by the HMDIMS keyword in the RUNSPEC section. In addition, the End-Point Scaling option must also be activated by the ENDSCALE keyword which is also in the RUNSPEC section. The keyword allows for the BOX, EQUALS, COPY, MINVALUE, MAXVALUE and ADD keywords to be used with the HA and HM series of keywords that reference the end-point scaling arrays, that is: HMKRG, HMKRGR, HMKRO, HMKRORG, HMKRORW, HMKRW, HMKRWR, HMPCW, HMPCG, HMSGCR, HMSOWCR, HMSOGCR, HMSWCR, and HMSWL keywords.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
