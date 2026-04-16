### NONNC -- Deactivate Non-Neighbor Connections

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [NONNC](#__RefHeading___Toc77075_4106839650) keyword deactivates non-neighbor connections ("NNCs") in the current run. NNCs create off-diagonal elements in the Jacobi matrix that impact the numerical efficiency of the solution algorithms, and thus if the run does not contain NNCs then there is the potential for greater computation efficiency. Unfortunately, nearly all models, except for the most simple models, generate NNCs via for example:

1)  aquifer connections,

2)  faults, and

3)  manually entered NNCs, including those automatically generate by pre-processing software.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- DEACTIVATE NON-NEIGHBOR CONNECTIONS

\--

NONNC

The above example switches off the NNCs.
