### NWATREM -- Node Water Removal (Extended Network)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The NWATREM keyword defines an extended network node as a point where water is removed from the network, for when the Extended Network option has been activated by the NETWORK keyword in the RUNSPEC section. The water to be removed can be specified as a rate or as a fraction of the total volume passing through the node.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
