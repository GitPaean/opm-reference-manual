### FOAM -- Activate the Foam Phase and Model

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword activates the foam phase and modeling option. The keyword will also invoke data input file checking to ensure that all the required foam phase input parameters are defined in the input deck. Note in the commercial simulator the [FOAM](#__RefHeading___Toc171586_289573908) phase and model can be used in conjunction with the [POLYMER](#__RefHeading___Toc38609_2267116897) and [SURFACT](#__RefHeading___Toc863854_4250154414) phases; this is not the case for OPM Flow. OPM Flow's [FOAM](#__RefHeading___Toc171586_289573908) phase and model is a standalone implementation and cannot be used in conjunction with either the [POLYMER](#__RefHeading___Toc38609_2267116897) or [SURFACT](#__RefHeading___Toc863854_4250154414) phases.

Foam flooding is an enhanced oil recovery flood process that attempts to control injected gas breakthrough in an oil reservoir by changing the mobility of the injected fluid.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- ACTIVATE THE FOAM PHASE IN THE MODEL

\--

FOAM

The above example declares that the foam phase is active in the model.
