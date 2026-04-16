### GRUPTREE -- Define Group Tree Hierarchy

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[GRUPTREE](#__RefHeading___Toc118321_1596574740) defines the group hierarchy of groups that have been created by having wells assigned to them via the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, By default three group levels are defined that sets the wells as level three, reporting directly to defined groups at level two, and the level two groups reporting to the FIELD group at level one. If a different configuration is required then the [GRUPTREE](#__RefHeading___Toc118321_1596574740) keyword should be used to define the group hierarchy by defining a lower level group that reports directly to a higher level group.

+--------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > No.                                                                                                                                      | > Name   | > Description                                                                                                                                                                                                                           | > Default |
+--------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 1                                                                                                                                        | > LOWER  | > A character string of up to eight characters in length that defines the group name which belongs to the HIGHER group. The group named FIELD is the top most group and should NOT be used as as a group name for the LOWER group name. | > None    |
|                                                                                                                                            |          |                                                                                                                                                                                                                                         |           |
|                                                                                                                                            |          | > Undefined group relationships are automatically assigned to the FIELD group.                                                                                                                                                          |           |
+--------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 2                                                                                                                                        | > HIGHER | > A character string of up to eight characters in length that defines the HIGHER group name that the LOWER group belongs to. The group named FIELD is the top most group and can be used as as the HIGHER group name.                   | > None    |
|                                                                                                                                            |          |                                                                                                                                                                                                                                         |           |
|                                                                                                                                            |          | > Undefined group relationships are automatically assigned to the FIELD group.                                                                                                                                                          |           |
+--------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Notes:                                                                                                                                   |          |                                                                                                                                                                                                                                         |           |
|                                                                                                                                            |          |                                                                                                                                                                                                                                         |           |
| 1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/".   |          |                                                                                                                                                                                                                                         |           |
+--------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Table 12.44: GRUPTREE Keyword Description

A group hierarchy can have any number of levels but groups that have other groups as LOWER groups cannot also have wells for the HIGHER group. Thus, a group either contains wells or has LOWER groups

See also the [GCONPROD](#__RefHeading___Toc146746_4203985108) and [GCONINJE](#__RefHeading___Toc134874_2055188184) for defining group production and injection volumes, and the [WELSPECS](#__RefHeading___Toc268463_1366622701) keywords to allocate wells to groups. All the aforementioned keywords are described in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Examples

The first example defines PLAT01 and PLAT03 reporting to the FIELD level (default if these records are omitted) and PLAT02 reporting to PLAT01.

\--

\-- DEFINE GROUP TREE HIERARCHY

\--

\-- LOWER HIGHER

\-- GROUP GROUP

GRUPTREE

PLAT01 FIELD /

PLAT02 PLAT01 /

PLAT03 FIELD /

/

The next example is more complex and is taken form the Norne model.

\--

\-- DEFINE GROUP TREE HIERARCHY

\--

\-- LOWER HIGHER

\-- GROUP GROUP

GRUPTREE

\'INJE\' \'FIELD\' /

\'PROD\' \'FIELD\' /

\'MANI-B2\' \'PROD\' /

\'MANI-B1\' \'PROD\' /

\'MANI-D1\' \'PROD\' /

\'MANI-D2\' \'PROD\' /

\'MANI-E1\' \'PROD\' /

\'MANI-E2\' \'PROD\' /

\'MANI-K1\' \'MANI-B1\' /

\'MANI-K2\' \'MANI-D2\' /

\'MANI-C\' \'INJE\' /

\'MANI-F\' \'INJE\' /

\'WI-GSEG\' \'INJE\' /

\'B1-DUMMY\' \'MANI-B1\' /

\'D2-DUMMY\' \'MANI-D2\' /

/

The group hierarchy for this example is shown below.

Here groups PROD, INJ, MAN-B1, and MAN-D2 report to higher level groups and the other remaining groups all have individual wells allocated to them instead.
