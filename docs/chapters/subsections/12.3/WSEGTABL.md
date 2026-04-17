### WSEGTABL -- Assign Multi-Segment Well VLP Tables to Segments

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

WSEGTABL assigns previously defined Vertical Lift Performance ("VLP") tables as specified by the VFPPROD keyword in the SCHEDULE section, to multi-segment well segments, as well as stipulating how the tables are to be applied.

The FLOWOPT parameter on the WELSEGS keyword in the SCHEDULE section sets the default multi-segment well model. FLOWOPT either activates the homogeneous model, that is all phases flow at the same velocity, or the Drift Flux Slip model. However, the WSEGFMOD keyword in the SCHEDULE section, can be used to set the flow model for a segment to either the homogeneous model or the Drift Flux Slip model, and addition a: VLP table allocated via the WSEGTABL keyword, or a specific model as defined by the WSEGVALV, WSEGFLIM and WSEGLABY keywords.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
