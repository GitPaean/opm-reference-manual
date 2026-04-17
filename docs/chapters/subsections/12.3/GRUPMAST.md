### GRUPMAST -- Define Master and Slave Groups

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The GRUPMAST keyword defines master groups and their associated slave groups for when the Reservoir Coupling option as been activated by the GRUPMAST and SLAVES keywords in the SCHEDULE section. Reservoir coupling allows for independent reservoir simulation decks (SLAVES) to be controlled by a separate master run file. For example, if there are five separate reservoir models each representing one field, one of the four would be used as the master and the other four would be the subordinate SLAVES.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
