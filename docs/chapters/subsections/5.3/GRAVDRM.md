### GRAVDRM -- Activate Alternative Gravity Drainage and Imbibition for Dual Porosity Model

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword switches on the alternative gravity drainage and imbibition modeling between the matrix and the fracture grid blocks in dual porosity and dual permeability runs. Either the [GRAVDRM](#__RefHeading___Toc471678_1414963541) or [GRAVDR](#__RefHeading___Toc455285_1414963541) keywords should be used to activate this standard or alternative type of formulation.

There is no data required for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

+-------------------------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > No.                                     | > Name    | > Description                                                                                                                            | > Default |
+-------------------------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 1                                       | > OPTION1 | > A defined character string that sets the matrix flow in and out of the matrix block option, and should be set to one of the following: | > YES     |
|                                           |           |                                                                                                                                          |           |
|                                           |           | 1)  YES: oil flow is bi-directional, that is oil can flow into and out of the matrix block.                                              |           |
|                                           |           |                                                                                                                                          |           |
|                                           |           | 2)  NO: oil flow is uni-directional, that is oil can flow out of the matrix block.                                                       |           |
+-------------------------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Notes:                                  |           |                                                                                                                                          |           |
|                                           |           |                                                                                                                                          |           |
| 1)  The keyword is terminated by a "/".   |           |                                                                                                                                          |           |
+-------------------------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Table 5.17: GRAVDRM Keyword Description

#### Example

\--

\-- ACTIVATE ALTERNATIVE GRAVITY DRAINAGE AND IMBIBITION MODEL

\--

\-- MATRIX

\-- OPTION

GRAVDRM

YES /

The above example switches on the alternative gravity drainage and imbibition option for the run and sets oil flow to be bi-directional, that is oil can flow into and out of the matrix block.
