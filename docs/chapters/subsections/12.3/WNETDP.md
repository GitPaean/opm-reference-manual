### WNETDP -- Define Well THP to Network Pressure Drop

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WNETDP keyword allows for a constant pressure drop between a well's Tubing Head Pressure ("THP") and the well's connecting network node, for when the either the Standard Network or the Extended Network options have been activated, and the well is part of a network. For production wells in a production network, WNETDP is added to the well's connecting network node pressure to arrive at the well's THP value. Whereas for injection wells in an injection network, WNETDP is subtracted from the well's connecting network node pressure to arrive at the well's THP value. The Standard Network option is invoked if the GRUPTREE, GRUPNET, GNETINJE, GNETPUMP, etc. series of keywords have been used in the SCHEDULE section. The Extended Network option is activated by the NETWORK keyword in the RUNSPEC section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
