### NUPCOL -- Define the Maximum Number of Newton Iterations Used to Update Well Targets

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The NUPCOL keyword defines the maximum number of Newton iterations within a time step that may be used to update the well production and injection targets, after which the well targets will be frozen until the time step calculations have converged and the time step is complete.

Wells under group control may suffer from some dependency with other wells in the same group that are also under group control. This can cause oscillations in the production and injection well rates within the group. In order to avoid this, after the number Newton iterations within a time step exceeds NUPCOL, the group well rates are frozen until the time step has converged. Reducing the potential for well rate oscillations within the time step may result in the group targets and limits not being exactly met in this case. Increasing the value of NUPCOL will improve the accuracy of the group targets and limits at the expense of computational efficiency.

See also section [Running OPM Flow From The Command Line](#running-opm-flow-from-the-command-line) on how to set various other numerical control parameters for OPM Flow.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | NUPCOL | A positive integer that defines the maximum number of Newton iterations used to update well targets within a time step. | 3 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.31: NUPCOL Keyword Description

See also the MINNPCOL keyword in the RUNSPEC section that sets the minimum number of Newton iterations within a time step that may be used to update the well production and injection targets, after which the well targets will be frozen until the time step calculations have converged and the time step is complete. Note that MINNPCOL is an OPM Flow specific keyword.

#### Example

\--

\-- DEFINE THE MAX NUMBER OF ITERATIONS TO UPDATE WELL FLOW TARGETS

\--

NUPCOL

3 /

The above example sets the NUPCOL value to its default value of 3.
