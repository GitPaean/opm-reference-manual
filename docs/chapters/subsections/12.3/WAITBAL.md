### WAITBAL -- Wait On Network Balance Before Allowing Further Actions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword sets the network balance option for all networks when networks are active in the model. Basically, the keyword either activates the PRORDER and GDRILPOT stipulated actions before or after the network has been balanced

The network option is normally used to ensure that the tubing head pressure ("THP") of a group of wells flowing into a common network node is consistent with a group's flow rates, that is each well's THP is flowing at the same THP and at the same time satisfying well and group targets and constraints. This is accomplished by calculating the well THP limits dynamically by balancing the flow rates and pressure losses in the network.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
