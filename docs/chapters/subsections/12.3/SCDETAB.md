### SCDETAB -- Well Connection Karst Aquifer Properties for Scale Deposit

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

SCDETAB defines well connection karst[^1] aquifer properties for modeling scale deposited by dissolution of calcite from the aquifer water, for when the Scale Deposition option has been activated by declaring the dimensions of the scaling deposition tables using the SCDPDIMS keyword in the RUNSPEC section. The SCDETAB tables are allocated to individual wells using the WSCTAB keyword in the SCHEDULE section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

[^1]: Karst is a topography formed from the dissolution of soluble rocks such as limestone, dolomite, and gypsum. Karst aquifers are characterized by a network of conduits and caves, with the conduits and caves draining the pore space between the limestone grains (intergranular or primary porosity) and the fractures (secondary porosity) formed by joints, bedding planes, and faults.
