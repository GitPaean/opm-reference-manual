### PERMAVE -- Define Average Transmissibility Coefficients

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [PERMAVE](#__RefHeading___Toc307718_2928331029) keyword defines the three directional exponent coefficients used to average the grid block permeabilities between two neighboring cells when calculating the transmissibility between the two blocks. The keyword can be used to change from the default weighted harmonic averaging (coefficient set equal to -1), to geometric (coefficient equal to zero), or to arithmetic averaging (coefficient equal to 1). The three coefficients represent the averaging in the x-, y- and z-directions.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
