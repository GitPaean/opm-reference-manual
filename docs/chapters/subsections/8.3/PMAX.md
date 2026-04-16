### PMAX -- Maximum and Minimum Pressure for Total Compressibility Check

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [PMAX](#__RefHeading___Toc276524_501926209) keyword defines the maximum and minimum pressures expected to be encountered during the run. The data is used to perform the PVT total compressibility check that ensures that the total compressibility of a mixture of oil-gas, for when the gas-oil ratio is increasing for an oil, or the condensate gas ratio is increasing for a gas condensate, is positive respect to pressure. The total compressibility check is used to ensure that the entered oil and gas PVT data is consistent. If the check fails for given oil-gas mixture at a given pressure, resulting in a negative total compressibility, then this will result in numerical instabilities in the run causing this simulator difficulties in converging to a solution.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
