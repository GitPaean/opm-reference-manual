### MINNNCT -- Set a Minimum Non-Neighbor Connection Transmissibility

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [MINNNCT](#__RefHeading___Toc569201_3181922006) keyword defines a minimum non-neighbor connection transmissibility below which the non-neighbor connection is deleted. The keyword allows for three minimum values, one for the transmissibility, one for the diffusivity and one for the thermal transmissibility. If the keyword is absent from the input deck then no minimum cut-off is applied.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
