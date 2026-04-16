### SOLVENT -- Activate the SOLVENT Phase in the Model

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword indicates that the solvent phase is present in the model and to activate the four component solvent model for this run. In addition to this keyword, the oil, water and gases phases should also be declared for the run using the [OIL](#__RefHeading___Toc97439_1778172979), [WATER](#__RefHeading___Toc38611_2267116897) and [GAS](#__RefHeading___Toc38607_2267116897) keywords. The keyword will also invoke data input file checking to ensure that all the required Solvent phase input parameters are defined in the input deck.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- SOLVENT PHASE IS PRESENT IN THE RUN

\--

SOLVENT

The above example declares that the solvent phase is active in the model.
