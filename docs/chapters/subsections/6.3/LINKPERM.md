### LINKPERM -- Assign Cell Permeabilities to Cell Faces

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [LINKPERM](#__RefHeading___Toc292860_2843394514) keyword assigns the grid cell permeabilities entered via the [PERMX](#__RefHeading___Toc45791_719036256), [PERMY](#__RefHeading___Toc45793_719036256) and [PERMZ](#__RefHeading___Toc45795_719036256) keywords to a cell face (I±, J±, or K±) and results in the simulator using these values directly in the calculating the transmissibility between grid blocks. This is different to the conventional way of entering permeability data that consists of entering the cell centered permeability and the simulator calculating a weighted average transmissibility based on the cell centered permeability of the up-stream and down-stream grid blocks.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
