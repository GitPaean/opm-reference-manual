### COMPDATM -- Define Well Connections to an Amalgamated LGR Grid

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The COMPDATM keyword is an alias for the COMPDATL keyword. COMPDATM defines how a well in an amalgamated Local Grid Refinement ("LGR") is connected to the reservoir by declaring the LGR and defining or modifying existing well connections. Ideally the connections should be declared in the correct sequence, starting with the connection nearest the well head and then working along the wellbore towards the bottom or toe of the well, however this may not be possible or convenient, for example when connections are added or removed from a well during the simulation (see the COMPORD keyword in the SCHEDULE section for options regarding connection ordering).

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
