### GRAVDR -- Activate Gravity Drainage and Imbibition for Dual Porosity Model

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword switches on gravity drainage and imbibition modeling between the matrix and the fracture grid blocks in dual porosity and dual permeability runs. Note that either DZMTRX or DZMTRXV keywords in the GRID section should be used to set the matrix vertical dimensions if this option is activated.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

\--

\-- ACTIVATE GRAVITY DRAINAGE AND IMBIBITION FOR DUAL POROSITY MODEL

\--

GRAVDR

The above example switches on the gravity drainage and imbibition option for the run.
