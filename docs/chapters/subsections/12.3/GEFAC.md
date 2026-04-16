### GEFAC -- Define Group Efficiency

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

Defines a group's efficiency or up-time factor as opposed to setting the efficiency factors for individual wells.

Note that wells are allocated to a group when they are specified by the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword and wells can also have efficiency factors.

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 1                                                                                                                                        | > GRPNAME       | > A character string of up to eight characters in length that defines the group name for which the group efficiency factor is being defined. The group named FIELD is the top most group and cannot have an efficiency factor set.                           | > None |
|                                                                                                                                            |                 |                                                                                                                                                                                                                                                              |        |
|                                                                                                                                            |                 | > Note that the group hierarchy should be defined by the [GRUPTREE](#__RefHeading___Toc118321_1596574740) keyword when there is more than one level of groups, otherwise all the groups will sit directly under the FIELD group in the group tree hierarchy. |        |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 2                                                                                                                                        | > FACTOR        | > A real positive value less than or equal to one that defines the efficiency factor for the group.                                                                                                                                                          | > 1.0  |
|                                                                                                                                            |                 |                                                                                                                                                                                                                                                              |        |
|                                                                                                                                            |                 | > If a group's down time is 5% then FACTOR should be set to 0.95 (1.0 -- 0.05).                                                                                                                                                                              |        |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > dimensionless                                                                                                                            | > dimensionless | > dimensionless                                                                                                                                                                                                                                              |        |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 3                                                                                                                                        | > GRPNETWK      | > A defined character string that determines if the GRPNAME efficiency factor should be transferred to the equivalent Extended Network Model node, and should be set to either:                                                                              | > YES  |
|                                                                                                                                            |                 |                                                                                                                                                                                                                                                              |        |
|                                                                                                                                            |                 | 1)  NO: The group's equivalent Extended Network Model node flow rates are not multiplied by the efficiency factor FACTOR.                                                                                                                                    |        |
|                                                                                                                                            |                 |                                                                                                                                                                                                                                                              |        |
|                                                                                                                                            |                 | 2)  YES: The group's equivalent Extended Network Model node flow rates are multiplied by the efficiency factor FACTOR                                                                                                                                        |        |
|                                                                                                                                            |                 |                                                                                                                                                                                                                                                              |        |
|                                                                                                                                            |                 | > This option is only applicable for the Extended Network Model. In the Standard Network Model groups\' reported flow rates are always used in the calculation of pressure drops.                                                                            |        |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > Notes:                                                                                                                                   |                 |                                                                                                                                                                                                                                                              |        |
|                                                                                                                                            |                 |                                                                                                                                                                                                                                                              |        |
| 1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/".   |                 |                                                                                                                                                                                                                                                              |        |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+

Table 12.38: GEFAC Keyword Description

See also the [WEFAC](#__RefHeading___Toc48856_327352552) and [NEFAC](#__RefHeading___Toc299702_1841740821) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section to define the efficiency factor for a well or a node.

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
