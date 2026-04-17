### WSEGFLIM -- Define Multi-Segment Well Artificial Choke Connections

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

WSEGFLIM enables an artificial choke that chokes a given phase flow rate for a segment in a multi-segment well. This can be used, for example, to constraint unwanted production phase through a section of tubing, or to model a down-hole choke. The keyword provides coefficients that are applied to the frictional pressure drop across a multi-segment well's segment in order to inhibit production from that particular zone or segment. As such, the keyword does not actually model a down-hole choke; hence, the term artificial.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
