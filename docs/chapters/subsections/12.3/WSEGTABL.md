### WSEGTABL -- Assign Multi-Segment Well VLP Tables to Segments

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[WSEGTABL](#__RefHeading___Toc1084759_4263943340) assigns previously defined Vertical Lift Performance ("VLP") tables as specified by the [VFPPROD](#__RefHeading___Toc121919_2556401936) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, to multi-segment well segments, as well as stipulating how the tables are to be applied.

The FLOWOPT parameter on the [WELSEGS](#__RefHeading___Toc97661_3261743917) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section sets the default multi-segment well model. FLOWOPT either activates the homogeneous model, that is all phases flow at the same velocity, or the Drift Flux Slip model. However, the [WSEGFMOD](#__RefHeading___Toc999697_4263943340) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, can be used to set the flow model for a segment to either the homogeneous model or the Drift Flux Slip model, and addition a: VLP table allocated via the [WSEGTABL](#__RefHeading___Toc1084759_4263943340) keyword, or a specific model as defined by the [WSEGVALV](#__RefHeading___Toc1091865_4263943340), [WSEGFLIM](#__RefHeading___Toc992622_4263943340) and [WSEGLABY](#__RefHeading___Toc1013848_4263943340) keywords.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
