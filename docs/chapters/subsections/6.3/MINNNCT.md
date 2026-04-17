### MINNNCT -- Set a Minimum Non-Neighbor Connection Transmissibility

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The MINNNCT keyword defines a minimum non-neighbor connection transmissibility below which the non-neighbor connection is deleted. The keyword allows for three minimum values, one for the transmissibility, one for the diffusivity and one for the thermal transmissibility. If the keyword is absent from the input deck then no minimum cut-off is applied.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
