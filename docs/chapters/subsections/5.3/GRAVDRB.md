### GRAVDRB -- Activate Vertical Discretized Gravity Drainage and Imbibition for Dual Porosity Model

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword switches on vertical discretized gravity drainage and imbibition modeling between the matrix and the fracture grid blocks in dual porosity and dual permeability runs. Note that the geometry of the matrix sub-cells should be set to VERTICAL on the NMATOPS keyword in the GRID section if this option is activated.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

\--

\-- ACTIVATE VERTICAL DISCRETIZED GRAVITY DRAINAGE AND IMBIBITION

\--

GRAVDRB

The above example switches on the vertical discretized gravity drainage and imbibition option for the run.
