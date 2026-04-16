### GRAVDR -- Activate Gravity Drainage and Imbibition for Dual Porosity Model

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword switches on gravity drainage and imbibition modeling between the matrix and the fracture grid blocks in dual porosity and dual permeability runs. Note that either [DZMTRX](#__RefHeading___Toc267162_1772380413) or [DZMTRXV](#__RefHeading___Toc267164_1772380413) keywords in the [GRID](#__RefHeading___Toc38674_784232322) section should be used to set the matrix vertical dimensions if this option is activated.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

\--

\-- ACTIVATE GRAVITY DRAINAGE AND IMBIBITION FOR DUAL POROSITY MODEL

\--

GRAVDR

The above example switches on the gravity drainage and imbibition option for the run.
