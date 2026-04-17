### GRUPSLAV -- Define Slave Groups in Slave Reservoirs

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The GRUPSLAV keyword defines slave groups in a slave input deck and their associated master groups in the master run, for when the Reservoir Coupling option as been activated by the GRUPMAST and SLAVES keywords in the SCHEDULE section. This keyword is required for every slave input deck. Reservoir coupling allows for independent reservoir simulation decks (SLAVES) to be controlled by a separate master run file. For example, if there are five separate reservoir models each representing one field, one of the four would be used as the master and the other four would be the subordinate SLAVES.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
