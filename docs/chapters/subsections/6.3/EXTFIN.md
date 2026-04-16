### EXTFIN -- Define an External Unstructured Local Grid Refinement

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [EXTFIN](#__RefHeading___Toc269728_803326780) keyword defines an external Unstructured Local Grid Refinement ("LGR") in a cell or a group of cells in the global grid, and for when LGRs have been activated for the model using the [LGR](#__RefHeading___Toc55049_4106839650) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Note the global grid can be either structured, see the [EXTREPGL](#__RefHeading___Toc274959_803326780) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section for global structure grids, or unstructured, see the [EXTHOST](#__RefHeading___Toc269730_803326780) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section for unstructured global grids.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
