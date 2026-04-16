### WSEGMULT -- Define Multi-Segment Well Frictional Pressure Loss Multipliers

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[WSEGMULT](#__RefHeading___Toc1042181_4263943340) supplies a set of constants used to modify (or scale) a multi-segment well's segment frictional pressure drop between connecting segments The constants enable either a constant pressure to be applied, or for the pressure drop to vary as a function of the Gas-Oil Ratio ("GOR") or the Water-Oil Ratio ("WOR"). The simulator calculated pressure drop is multiplied by the following resulting value:

Where the constants x~1~ to x~5~ are defined by the values on this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
