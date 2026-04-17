### WFRICSGL -- Convert Friction Well to Multi-Segment Well (LGR)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

WFRICSGL converts a previously defined Local Grid Refinement ("LGR") friction well, as per the WFRICTNL keyword in the SCHEDULE section, to a multi-segment LGR well. The keyword thus acts as a replacement for the WELSEGS and COMPSEGL keywords for LGR multi-segment wells. See also the WFRICSEG keyword in the SCHEDULE section that performs similar functionality for wells in the global grid.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
