### NSTACK -- Define the Stack Length for the Iterative Linear Solver

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [NSTACK](#__RefHeading___Toc34963_1640804870) keyword defines the maximum number of previous search directions stored by the linear solver. Increasing the value of NSTACK may improve the efficiency of the solver on difficult problems, but will increase the memory requirements of the simulator. The default value of 10 should be sufficient for most problems; however, if OPM Flow is having issues with the convergence of the linear questions then increasing NSTACK and the value of LITMAX on the [TUNING](#__RefHeading___Toc146744_4203985108) keyword may improve performance.

OPM Flow uses a different numerical scheme which makes this keyword redundant; see section [[2.2](#anchor-2)](#2.2.Running OPM Flow 2018-10 |outline)[](#2.2.Running OPM Flow 2018-10 |outline)[[Running OPM Flow 2023-04 From The Command Line](#anchor-2)](#2.2.Running OPM Flow 2018-10 |outline) on how to invoke various numerical schemes via the OPM Flow command line interface.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------------+-----------+
| > No.                                                                                                                                                                                        | > Name   | > Description                                                                                                   | > Default |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------------+-----------+
| > 1                                                                                                                                                                                          | > NSTACK | > A positive integer that defines the maximum number of previous search directions stored by the linear solver. | > 10      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------------+-----------+
| > Notes:                                                                                                                                                                                     |          |                                                                                                                 |           |
|                                                                                                                                                                                              |          |                                                                                                                 |           |
| 1)  The value of NSTACK and the value of LITMAX on the [TUNING](#__RefHeading___Toc146744_4203985108) keyword are related such that NSTACK should always be less than or equal to LITMAX.    |          |                                                                                                                 |           |
|                                                                                                                                                                                              |          |                                                                                                                 |           |
| 2)  The keyword is terminated by a "/".                                                                                                                                                      |          |                                                                                                                 |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------------+-----------+

Table 5.29: NSTACK Keyword Description

#### Example

\--

\-- SET STACK SIZE FOR LINEAR SOLVER

\--

NSTACK

30 /

The above example sets maximum number of previous search directions stored by the linear solver to 30, this has no effect in OPM Flow input decks.
