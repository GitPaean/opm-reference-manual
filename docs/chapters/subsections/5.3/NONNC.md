### NONNC -- Deactivate Non-Neighbor Connections

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The NONNC keyword deactivates non-neighbor connections ("NNCs") in the current run. NNCs create off-diagonal elements in the Jacobi matrix that impact the numerical efficiency of the solution algorithms, and thus if the run does not contain NNCs then there is the potential for greater computation efficiency. Unfortunately, nearly all models, except for the most simple models, generate NNCs via for example:

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
