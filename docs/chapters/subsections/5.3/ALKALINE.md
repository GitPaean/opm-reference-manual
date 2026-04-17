### ALKALINE -- Activate the Alkaline Phase and Model

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword indicates that an alkaline phase is present in the model and to activate the Alkaline Model in the run. The keyword will also invoke data input file checking to ensure that all the required Alkaline Model input parameters are defined in the input deck.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

\--

\-- ALKALINE PHASE IS PRESENT IN THE RUN

\--

ALKALINE

The above example declares that the alkaline phase is active in the model to activate Alkaline Model.
