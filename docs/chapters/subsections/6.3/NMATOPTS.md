### NMATOPTS -- Define the Discretized Matrix Dual Porosity Parameters

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [NMATOPTS](#__RefHeading___Toc238503_718033703) keyword defines the Discretized Matrix Dual Porosity parameters for when the Discretized Matrix Dual Porosity option has been activated by [NMATRIX](#__RefHeading___Toc244469_718033703) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The option allows the matrix grid blocks to be subdivided into smaller cells for more accurate flow calculations, in particular the modeling of transient flow within the matrix grid blocks.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
