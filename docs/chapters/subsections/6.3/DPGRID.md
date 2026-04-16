### DPGRID -- Activate The Matrix Cell to Fracture Cell Option

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [DPGRID](#__RefHeading___Toc204908_1772380413) keyword activates the matrix cell to fracture cell option for dual porosity runs for when a Dual Porosity model has been activated by either the [DUALPORO](#__RefHeading___Toc241173_1772380413) or [DUALPERM](#__RefHeading___Toc241171_1772380413) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The keyword allows for only the matrix grid data to be entered and the missing fracture cells are set to the inputted matrix cells.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
