### MINNPCOL -- Define the Minimum Number of Newton Iterations Used to Update Well Targets

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The MINNPCOL keyword defines the *minimum* number of Newton iterations within a time step where the well production and injection targets may be updated, after which the well targets will be frozen until the time step calculations have converged and the time step is complete.

The MINNPCOL keyword has been deprecated and the NUPCOL keyword should be used instead.

Wells under group control may suffer from some dependency with other wells in the same group that are also under group control. This may cause oscillations in the production and injection well rates within the group. In order to avoid this, the NUPCOL keyword in the RUNSPEC section can be used to set the maximum number of Newton iterations within a time step, after which the group well rates are frozen until the time step has converged. Reducing the potential for well rate oscillations within the time step may result in the group targets and limits not being exactly met in this case. Increasing the value of NUPCOL, will improve the accuracy of the group targets and limits at the expense of computational efficiency. Here, the MINNPCOL keyword sets the minimum number of Newton iterations within a timestep where the well production and injection targets may be updated.

See also section [Running OPM Flow From The Command Line](#running-opm-flow-from-the-command-line) on how to set various other numerical control parameters for OPM Flow.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | MINNPCOL | A positive integer that defines the minimum number of Newton iterations within a timestep where well targets may be updated. | 3 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.20: MINNPCOL Keyword Description

#### Example

\--

\-- DEFINE THE MIN NUMBER OF ITERATIONS TO UPDATE WELL FLOW TARGETS

\--

MINNPCOL

3 /

The above example sets the MINNPCOL value to its default value of three.
