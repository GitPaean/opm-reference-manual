### SOLVENT -- Activate the SOLVENT Phase in the Model

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword indicates that the solvent phase is present in the model and to activate the four component solvent model for this run. In addition to this keyword, the oil, water and gases phases should also be declared for the run using the OIL, WATER and GAS keywords. The keyword will also invoke data input file checking to ensure that all the required Solvent phase input parameters are defined in the input deck.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- SOLVENT PHASE IS PRESENT IN THE RUN

\--

SOLVENT

The above example declares that the solvent phase is active in the model.
