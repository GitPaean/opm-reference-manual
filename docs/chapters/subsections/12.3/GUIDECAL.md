### GUIDECAL -- Scale Guide Rates Based on Gas Calorific Value

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The GUIDECAL keyword defines a well or group's guide rate as a function of their calorific values, for when the individual wells and groups are under guide rate control. Group and well guide rates that have not been directly defined are set equal to their production potentials at the start of each time step. In this case the GUIDECAL keyword can be used to specify the coefficients of a function that takes into account the calorific value of the produced gas, effectively scaling the guide rates based on the calorific value of the gas being produced.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
