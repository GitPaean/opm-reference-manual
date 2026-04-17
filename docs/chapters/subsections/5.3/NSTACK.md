### NSTACK -- Define the Stack Length for the Iterative Linear Solver

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The NSTACK keyword defines the maximum number of previous search directions stored by the linear solver. Increasing the value of NSTACK may improve the efficiency of the solver on difficult problems, but will increase the memory requirements of the simulator. The default value of 10 should be sufficient for most problems; however, if OPM Flow is having issues with the convergence of the linear questions then increasing NSTACK and the value of LITMAX on the TUNING keyword may improve performance.

OPM Flow uses a different numerical scheme which makes this keyword redundant; see section [Running OPM Flow From The Command Line](#running-opm-flow-from-the-command-line) on how to invoke various numerical schemes via the OPM Flow command line interface.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | NSTACK | A positive integer that defines the maximum number of previous search directions stored by the linear solver. | 10 |
| Notes:<br>1)  The value of NSTACK and the value of LITMAX on the TUNING keyword are related such that NSTACK should always be less than or equal to LITMAX.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 5.29: NSTACK Keyword Description

#### Example

\--

\-- SET STACK SIZE FOR LINEAR SOLVER

\--

NSTACK

30 /

The above example sets maximum number of previous search directions stored by the linear solver to 30, this has no effect in OPM Flow input decks.
