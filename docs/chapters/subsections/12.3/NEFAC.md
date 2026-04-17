### NEFAC -- Node Efficiency Factors (Extended Network)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The NEFAC keyword defines an extended network node's efficiency factor, for when the Extended Network option has been activated by the NETWORK keyword in the RUNSPEC section. See also the GEFAC keyword in the SCHEDULE section that can also be used with the Extended Network option.

| 1 | NODE | A character string of up to eight characters in length that defines the node name for which the node efficiency factor is being defined. | None |
| --- | --- | --- | --- |
| 2 | FACTOR | A real positive value that is less than or equal to one that defines the efficiency factor for the node. If a node's down time is 5% then FACTOR should be set to 0.95 (1.0 -- 0.05). | 1.0 |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.3.159.1: NEFAC Keyword Description

See also the WEFAC keyword in the SCHEDULE section to define a well's' efficiency factor.
