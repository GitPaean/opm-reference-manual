### SURFACT -- Activate the Surfactant Phase in the Model

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword indicates that the surfactant phase is present in the model and to activate the surfactant flooding model. The keyword will also invoke data input file checking to ensure that all the required surfactant phase input parameters are defined in the input deck. See also the SURFACTW keyword in the RUNSPEC section that actives the surfactant phase, but with the changes to the wettability option activated as well.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

\--

\-- ACTIVATE THE SURFACTANT PHASE IN THE MODEL

\--

SURFACT

The above example declares that the surfactant phase is active in the model.
