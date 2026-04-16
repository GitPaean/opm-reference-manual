### WATER -- Activate the Water Phase in the Model

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword indicate that the water phase is present in the model and must be used for gas-water, oil-water, oil-water-gas input decks that contain the water phase. The keyword will also invoke data input file checking to ensure that all the required water phase input parameters are defined in the input deck.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- WATER PHASE IS PRESENT IN THE RUN

\--

WATER

The above example declares that the water phase is active in the model.
