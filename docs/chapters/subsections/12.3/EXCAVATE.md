### EXCAVATE -- Set the Status of a Grid Block To Active or Excavate

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword, [EXCAVATE](#__RefHeading___Toc259231_803326780), sets the status of global and [LGR](#__RefHeading___Toc55049_4106839650) grid blocks to active or excavate. Excavated grid blocks have all the transmissibilities set to zero thus disabling flow between the surrounding grid blocks.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
