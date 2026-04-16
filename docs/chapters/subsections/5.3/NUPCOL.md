### NUPCOL -- Define the Maximum Number of Newton Iterations Used to Update Well Targets

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [NUPCOL](#__RefHeading___Toc86969_4106839650) keyword defines the maximum number of Newton iterations within a time step that may be used to update the well production and injection targets, after which the well targets will be frozen until the time step calculations have converged and the time step is complete.

Wells under group control may suffer from some dependency with other wells in the same group that are also under group control. This can cause oscillations in the production and injection well rates within the group. In order to avoid this, after the number Newton iterations within a time step exceeds [NUPCOL](#__RefHeading___Toc86969_4106839650), the group well rates are frozen until the time step has converged. Reducing the potential for well rate oscillations within the time step may result in the group targets and limits not being exactly met in this case. Increasing the value of [NUPCOL](#__RefHeading___Toc86969_4106839650) will improve the accuracy of the group targets and limits at the expense of computational efficiency.

See also section [Running OPM Flow From The Command Line](#running-opm-flow-from-the-command-line) on how to set various other numerical control parameters for OPM Flow.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | NUPCOL | A positive integer that defines the maximum number of Newton iterations used to update well targets within a time step. | 3 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.31: NUPCOL Keyword Description

See also the [MINNPCOL](#__RefHeading___Toc451205_1352344891) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section that sets the minimum number of Newton iterations within a time step that may be used to update the well production and injection targets, after which the well targets will be frozen until the time step calculations have converged and the time step is complete. Note that [MINNPCOL](#__RefHeading___Toc451205_1352344891) is an OPM Flow specific keyword.

#### Example

\--

\-- DEFINE THE MAX NUMBER OF ITERATIONS TO UPDATE WELL FLOW TARGETS

\--

NUPCOL

3 /

The above example sets the [NUPCOL](#__RefHeading___Toc86969_4106839650) value to its default value of 3.
