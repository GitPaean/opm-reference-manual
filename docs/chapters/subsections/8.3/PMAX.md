### PMAX -- Maximum and Minimum Pressure for Total Compressibility Check

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The PMAX keyword defines the maximum and minimum pressures expected to be encountered during the run. The data is used to perform the PVT total compressibility check that ensures that the total compressibility of a mixture of oil-gas, for when the gas-oil ratio is increasing for an oil, or the condensate gas ratio is increasing for a gas condensate, is positive respect to pressure. The total compressibility check is used to ensure that the entered oil and gas PVT data is consistent. If the check fails for given oil-gas mixture at a given pressure, resulting in a negative total compressibility, then this will result in numerical instabilities in the run causing this simulator difficulties in converging to a solution.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
