### FOAM -- Activate the Foam Phase and Model

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword activates the foam phase and modeling option. The keyword will also invoke data input file checking to ensure that all the required foam phase input parameters are defined in the input deck. Note in the commercial simulator the FOAM phase and model can be used in conjunction with the POLYMER and SURFACT phases; this is not the case for OPM Flow. OPM Flow's FOAM phase and model is a standalone implementation and cannot be used in conjunction with either the POLYMER or SURFACT phases.

Foam flooding is an enhanced oil recovery flood process that attempts to control injected gas breakthrough in an oil reservoir by changing the mobility of the injected fluid.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- ACTIVATE THE FOAM PHASE IN THE MODEL

\--

FOAM

The above example declares that the foam phase is active in the model.
