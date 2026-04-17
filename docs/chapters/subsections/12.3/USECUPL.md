### USECUPL -- Load a Reservoir Coupling File

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The USECUPL keyword causes the simulator to read a Reservoir Coupling file that has been previously created in a master run using the DUMPCUPL keyword in the SCHEDULE section, for when reservoir coupling is invoked by the GRUPMAST and SLAVES keywords in the SCHEDULE section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
