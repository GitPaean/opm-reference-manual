### DUMPFLUX -- Activate Writing Out of a Flux File

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword activates the writing out of a full field (the full grid) FLUX file for later processing in a Flux Boundary run. The Flux Boundary feature allows for the segmentation of the full grid into flux boundary areas which allow for a sub-area of the grid to be run and at the same time model the flux across the boundary derived from the main grid. The object of this feature is to be able to investigate the performance of various areas of the model without having to run the full field, thus improving computational efficiency and run times, but still obtain "reasonable" results due to the incorporation of the fluxes across the boundary.

This feature is not available in OPM Flow; however it is documented here for completeness.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- ACTIVATE WRITING OUT OF A FLUX FILE

\--

DUMPFLUX /

The above example switches on the writing of the FLUX output file; the keyword has no effect and is ignored by the simulator.
