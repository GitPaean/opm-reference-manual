### FRICTION -- Activate Wellbore Friction Option

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [FRICTION](#__RefHeading___Toc327648_803326780) keyword activates the Wellbore Friction option and defines the maximum number of wellbore friction wells together with the maximum number of well branches.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

+-------------------------------------------+----------+---------------------------------------------------------------------------------------------+-----+
| > 1                                       | > MXWELS | > A positive integer defining the maximum number of wellbore friction wells for this model. | > 0 |
+-------------------------------------------+----------+---------------------------------------------------------------------------------------------+-----+
| > 3                                       | > MXBRAN | > A positive integer defining the maximum number of branches per well.                      | > 1 |
|                                           |          |                                                                                             |     |
|                                           |          | > The default value of one implies a standard well with no branches.                        |     |
+-------------------------------------------+----------+---------------------------------------------------------------------------------------------+-----+
| > Notes:                                  |          |                                                                                             |     |
|                                           |          |                                                                                             |     |
| 1)  The keyword is terminated by a "/".   |          |                                                                                             |     |
+-------------------------------------------+----------+---------------------------------------------------------------------------------------------+-----+

Table 5.16: FRICTION Keyword Description

#### Example

\--

\-- WELL BRANCH

\-- MXWELS MXBRAN

FRICTION

5 1 /

The above example defines the maximum number of wellbore friction wells to be five and the maximum number of branches set to one, for standard wells.
