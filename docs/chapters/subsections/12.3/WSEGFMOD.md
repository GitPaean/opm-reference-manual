### WSEGFMOD -- Define Multi-Segment Well Model

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WSEGFMOD declares the multi-phase flow model to be used to calculate the pressure drop within an individual segment for multi-segment wells. The FLOWOPT parameter on the WELSEGS keyword in the SCHEDULE section sets the default multi-segment well model. FLOWOPT is a character string that can be set to HO that activates the homogeneous model, that is all phases flow at the same velocity, or DF that invokes the Drift Flux Slip model (note OPM Flow only supports the default value of HO for the homogeneous model). Here WSEGFMOD can be used to set the flow model for a segment to either the homogeneous model or the Drift Flux Slip model, and addition a: VLP table allocated via the WSEGTABL keyword, or a specific model as defined by the WSEGVALV, WSEGFLIM and WSEGLABY keywords. All the aforementioned keywords are in the SCHEDULE section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
