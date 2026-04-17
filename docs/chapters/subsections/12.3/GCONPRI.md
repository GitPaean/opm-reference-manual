### GCONPRI -- Group Production Priority Targets and Constraints

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The GCONPRI keyword defines production targets and constraints for groups, including the top most group in the group hierarchy known as the FIELD group, for when groups and their associated wells are operating under priority control as oppose to guide rate control. Priority control is activated by the PRIORITY keyword in the SCHEDULE section. Wells are allocated to groups when the wells are specified by the WELSPECS keyword in the SCHEDULE section. Wells defined to be under group control will have their production rates controlled by the group to which they belong, in addition to any well constraints defined for the wells.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | GRPNAME | A character string of up to eight characters in length that defines the group name for which the group target and constraints are being defined. The group named FIELD is the top most group and should be used to set targets and constraints for the field.<br>Note that the group hierarchy should be defined by the GRUPTREE keyword when there is more than one level of groups, otherwise all the groups will sit directly under the FIELD group in the group tree hierarchy. | None |
| --- | --- | --- | --- |
| 2 | ORAT | A real positive value that defines the maximum surface oil production rate constraint.<br>This value may be specified using a User Defined Argument (UDA). | None |
| stb/d | sm^3^/day | scc/hour |  |
| 3 | OILACT | A defined character string that defines the action to be taken if ORAT is exceeded. OILACT should be set to one of the following character strings:<br>1)  NONE: no action is taken.<br>2)  CON: close the worst offending connection in the worst offending well. If connections have been grouped as completions then the worst offending completion in the worst offending well will be closed.<br>3)  +CON: close the worst offending connection and all below it in the worst offending well. If connections have been grouped as completions then the worst offending completion and all below it in the worst offending well will be closed.<br>4)  WELL: close the worst offending well.<br>5)  PLUG: plug back the worst offending well based on the plug back length and options defined on the WPLUG keyword in the SCHEDULE.<br>6)  PRI: control the group production rate using the first priority formulae defined by the PRIORITY keyword in the SCHEDULE section.<br>7)  PR2: control the group production rate using the second priority formulae defined by the PRIORITY keyword in the SCHEDULE section. | "NONE" |
| 4 | WRAT | A real positive value that defines the maximum surface water production rate constraint.<br>This value may be specified using a User Defined Argument (UDA). | None |
| stb/d | sm^3^/day | scc/hour |  |
| 5 | WATACT | A defined character string that defines the action to be taken if WRAT is exceeded. WATACT should be set to a character string described by the OILACT parameter on this record. | None |
| 6 | GRAT | A real positive value that defines the maximum surface gas production rate constraint<br>This value may be specified using a User Defined Argument (UDA). | None |
| Mscf/d | sm^3^/day | scc/hour |  |
| 7 | GASACT | A defined character string that defines the action to be taken if GRAT is exceeded. GASACT should be set to a character string described by the OILACT parameter on this record. | None |
| 8 | LRAT | A real positive value that defines the maximum surface liquid (oil plus water) production rate constraint.<br>This value may be specified using a User Defined Argument (UDA). | None |
| stb/d | sm^3^/day | scc/hour |  |
| 9 | LIQACT | A defined character string that defines the action to be taken if LRAT is exceeded. LIQACT should be set to a character string described by the OILACT parameter on this record. | None |
| 10 | RESV | A real positive value that defines the maximum reservoir volume production rate constraint.<br>This value may be specified using a User Defined Argument (UDA). | None |
| rb/d | rm^3^/day | rcc/hour |  |
| 11 | RESVFRAC | A real positive value that defines a group\'s maximum production balancing fraction constraint.<br>This value may be specified using a User Defined Argument (UDA). | None |
| dimensionless | dimensionless | dimensionless |  |
| 12 |  | Not used should be defaulted with 1\*. | 1\* |
| 13 |  | Not used should be defaulted with 1\*. | 1\* |
| 14 |  | Not used should be defaulted with 1\*. | 1\* |
| 15 |  | Not used should be defaulted with 1\*. | 1\* |
| 16 | LINCOMB | A real positive value that defines the linearly combined maximum surface target rate or constraint, as per the LINCOM keyword in the SCHEDULE section. | 1\* |
| 17 | LINACT | A defined character string that defines the action to be taken if LINCOMB is exceeded. LINACT should be set to a character string described by the OILACT parameter on this record. | None |
| Notes:<br>1)  User Defined Quantities (\"UDQ\") can be used as User Defined Arguments (\"UDA\") for various group, well, and connection keywords in the SCHEDULE section. User Defined Arguments are activated using the UDADIMS keyword in the RUNSPEC section, and defined by the UDQ keyword in the SCHEDULE section.<br>2)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.30: GCONPRI Keyword Description

See also the GRUPTREE keyword to define the hierarchy of the groups below the FIELD level, the GCONPROD keyword to define a group's production targets and constraints, the GCONINJE keyword to define a group's injection targets and constraints, the WCONPROD keyword to define a production well's targets and constraints, and the WCONINJE keyword to define an injection well's targets and constraints. All the aforementioned keywords are described in the SCHEDULE section.

#### Example

The following example defines the production targets and constraints for the field and two groups that are one level below the field group, since the GRUPTREE keyword has not been entered to define the group hierarchy.

\--

\-- GROUP PRIORITY PRODUCTION CONTROLS

\--

\-- GRUP ORAT ORAT WRAT WRAT GRAT GRAT LRAT LRAT RVOL RVOL

\-- NAME LIMT ACTN LIMT ACTN LIMT ACTN LIMT ACTN LIMT ACTN

GCONPRI

FIELD 40E3 PRI 30E3 +CON 125E3 PRI 1\* 1\* 1\* 1\* /

GRP01 25E3 PRI 1\* 1\* 1\* 1\* 1\* 1\* 1\* 1\* /

GRP02 25E3 PRI 1\* 1\* 1\* 1\* 1\* 1\* 1\* 1\* /

/

All groups are controlled by oil constraints, but only the field level has water and gas constraints to reflect the actual production facility constraints. The oil production constraint of 40,000, 25,000 and 25,000 stb/d are defined for the field, GRP01 and GRP02 groups, respectively. If the oil rate constraint is exceeded then the wells will be controlled using the priority formulae one, as defined on the PRIORITY keyword in the SCHEDULE section. Similarly for the field, for when the gas constraint is exceeded. Finally, if the field water constraint is surpassed then the worst offending connection and below in the worst offending well are shut.
