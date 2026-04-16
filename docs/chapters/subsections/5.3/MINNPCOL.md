### MINNPCOL -- Define the Minimum Number of Newton Iterations Used to Update Well Targets

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [MINNPCOL](#__RefHeading___Toc451205_1352344891) keyword defines the *minimum* number of Newton iterations within a time step where the well production and injection targets may be updated, after which the well targets will be frozen until the time step calculations have converged and the time step is complete.

The [MINNPCOL](#__RefHeading___Toc451205_1352344891) keyword has been deprecated and the [NUPCOL](#__RefHeading___Toc86969_4106839650) keyword should be used instead.

Wells under group control may suffer from some dependency with other wells in the same group that are also under group control. This may cause oscillations in the production and injection well rates within the group. In order to avoid this, the [NUPCOL](#__RefHeading___Toc86969_4106839650) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section can be used to set the maximum number of Newton iterations within a time step, after which the group well rates are frozen until the time step has converged. Reducing the potential for well rate oscillations within the time step may result in the group targets and limits not being exactly met in this case. Increasing the value of [NUPCOL](#__RefHeading___Toc86969_4106839650), will improve the accuracy of the group targets and limits at the expense of computational efficiency. Here, the [MINNPCOL](#__RefHeading___Toc451205_1352344891) keyword sets the minimum number of Newton iterations within a timestep where the well production and injection targets may be updated.

See also section [[2.2](#anchor-2)](#2.2.Running OPM Flow 2018-10 |outline)[](#2.2.Running OPM Flow 2018-10 |outline)[[Running OPM Flow 2023-04 From The Command Line](#anchor-2)](#2.2.Running OPM Flow 2018-10 |outline) on how to set various other numerical control parameters for OPM Flow.

+-------------------------------------------+------------+--------------------------------------------------------------------------------------------------------------------------------+-----------+
| > No.                                     | > Name     | > Description                                                                                                                  | > Default |
+-------------------------------------------+------------+--------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 1                                       | > MINNPCOL | > A positive integer that defines the minimum number of Newton iterations within a timestep where well targets may be updated. | > 3       |
+-------------------------------------------+------------+--------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Notes:                                  |            |                                                                                                                                |           |
|                                           |            |                                                                                                                                |           |
| 1)  The keyword is terminated by a "/".   |            |                                                                                                                                |           |
+-------------------------------------------+------------+--------------------------------------------------------------------------------------------------------------------------------+-----------+

Table 5.20: MINNPCOL Keyword Description

#### Example

\--

\-- DEFINE THE MIN NUMBER OF ITERATIONS TO UPDATE WELL FLOW TARGETS

\--

MINNPCOL

3 /

The above example sets the [MINNPCOL](#__RefHeading___Toc451205_1352344891) value to its default value of three.
