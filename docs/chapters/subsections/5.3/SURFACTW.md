### SURFACTW -- Activate the Surfactant Phase with Wettability Changes in the Model

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword indicates that the surfactant phase is present in the model and to activate the surfactant flooding mode with Changes to Wettability option activated as well. The keyword will also invoke data input file checking to ensure that all the required surfactant phase input parameters are defined in the input deck. See also the SURFACT keyword in the RUNSPEC section that actives the surfactant phase only, that is without the Changes to the Wettability option.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

\--

\-- ACTIVATE THE SURFACTANT PHASE WITH WETTABILITY CHANGES IN THE MODEL

\--

SURFACTW

The above example declares that the surfactant phase is active in the model together with the wettability changes.
