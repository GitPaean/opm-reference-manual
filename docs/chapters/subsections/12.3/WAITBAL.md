### WAITBAL -- Wait On Network Balance Before Allowing Further Actions

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword sets the network balance option for all networks when networks are active in the model. Basically, the keyword either activates the [PRORDER](#__RefHeading___Toc601903_501926209) and [GDRILPOT](#__RefHeading___Toc262268_156692946) stipulated actions before or after the network has been balanced

The network option is normally used to ensure that the tubing head pressure ("THP") of a group of wells flowing into a common network node is consistent with a group's flow rates, that is each well's THP is flowing at the same THP and at the same time satisfying well and group targets and constraints. This is accomplished by calculating the well THP limits dynamically by balancing the flow rates and pressure losses in the network.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
