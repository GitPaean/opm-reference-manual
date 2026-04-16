### GUIDECAL -- Scale Guide Rates Based on Gas Calorific Value

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [GUIDECAL](#__RefHeading___Toc246066_870710203) keyword defines a well or group's guide rate as a function of their calorific values, for when the individual wells and groups are under guide rate control. Group and well guide rates that have not been directly defined are set equal to their production potentials at the start of each time step. In this case the [GUIDECAL](#__RefHeading___Toc246066_870710203) keyword can be used to specify the coefficients of a function that takes into account the calorific value of the produced gas, effectively scaling the guide rates based on the calorific value of the gas being produced.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
