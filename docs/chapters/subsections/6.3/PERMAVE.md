### PERMAVE -- Define Average Transmissibility Coefficients

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The PERMAVE keyword defines the three directional exponent coefficients used to average the grid block permeabilities between two neighboring cells when calculating the transmissibility between the two blocks. The keyword can be used to change from the default weighted harmonic averaging (coefficient set equal to -1), to geometric (coefficient equal to zero), or to arithmetic averaging (coefficient equal to 1). The three coefficients represent the averaging in the x-, y- and z-directions.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
