### GEFAC -- Define Group Efficiency

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

Defines a group's efficiency or up-time factor as opposed to setting the efficiency factors for individual wells.

Note that wells are allocated to a group when they are specified by the WELSPECS keyword and wells can also have efficiency factors.

| 1 | GRPNAME | A character string of up to eight characters in length that defines the group name for which the group efficiency factor is being defined. The group named FIELD is the top most group and cannot have an efficiency factor set.<br>Note that the group hierarchy should be defined by the GRUPTREE keyword when there is more than one level of groups, otherwise all the groups will sit directly under the FIELD group in the group tree hierarchy. | None |
| --- | --- | --- | --- |
| 2 | FACTOR | A real positive value less than or equal to one that defines the efficiency factor for the group.<br>If a group's down time is 5% then FACTOR should be set to 0.95 (1.0 -- 0.05). | 1.0 |
| dimensionless | dimensionless | dimensionless |  |
| 3 | GRPNETWK | A defined character string that determines if the GRPNAME efficiency factor should be transferred to the equivalent Extended Network Model node, and should be set to either:<br>1)  NO: The group's equivalent Extended Network Model node flow rates are not multiplied by the efficiency factor FACTOR.<br>2)  YES: The group's equivalent Extended Network Model node flow rates are multiplied by the efficiency factor FACTOR<br>This option is only applicable for the Extended Network Model. In the Standard Network Model groups\' reported flow rates are always used in the calculation of pressure drops. | YES |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.38: GEFAC Keyword Description

See also the WEFAC and NEFAC keywords in the SCHEDULE section to define the efficiency factor for a well or a node.

#### Example

\--

\-- GROUP EFFICIENCY FACTORS

\--

\-- GRUP EFF NETWK

\-- NAME FACT OPTN

\-- \-\-\-\-\-- \-\-\-\-\--

GEFAC

PLATFORM 0.950 /

SUBSEA1 0.860 /

/

In the above example the group PLATFORM has its up-time factor set to 95% and the subsea group SUBSEA1 has an up-time factor of 86%.
