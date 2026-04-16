### GCONINJE -- Group Injection Targets and Constraints

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [GCONINJE](#__RefHeading___Toc134874_2055188184) keyword defines injection targets and constraints for groups, including the top most group in the group hierarchy known as the FIELD group. Wells are allocated to groups when the wells are specified by the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. Wells defined to be under group control will have their injection rates controlled by the group to which they belong, in addition to any well constraints defined for the wells.

| 1 | GRPNAME | A character string of up to eight characters in length that defines the group name for which the group target and constraints are being defined. The group named FIELD is the top most group and should be used to set targets and constraints for the whole field.<br>Note that the group hierarchy should be defined by the [GRUPTREE](#__RefHeading___Toc118321_1596574740) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322), when there is more than one level of groups, otherwise all the groups will sit directly under the FIELD group in the group tree hierarchy. | None |
| --- | --- | --- | --- |
| 2 | TYPE | A defined character string that defines the type of injection fluid. TYPE should be set to one of the following character strings:<br>1)  [GAS](#__RefHeading___Toc38607_2267116897): for a gas injection well.<br>2)  [OIL](#__RefHeading___Toc97439_1778172979): for a water injection well.<br>3)  WAT: for a water injection well. | None |
| 3 | TARGET | A defined character string that sets the target injection control for the group, all the other phases will therefore act as constraints. The simulator will attempt to meet the TARGET based on the phase rate stated in items (4) to (7) on this keyword. TARGET should be set to one of the following character strings:<br>1)  NONE: the group has no target phase, but if entered, constraints are still defined and active.<br>2)  FLD: this group is controlled from a higher level group, including the FIELD group.<br>3)  RATE: the injection phase will be control by the surface fluid rate for the phase defined by the TYPE variable. For example, if TYPE has been set to WAT then this would mean the water injection rate as defined by item (4).<br>4)  RESV: the target is set to the in situ reservoir volume rate as defined by item (5).<br>5)  REIN: the target is set to the group\'s production of the phase defined by TYPE multiplied by the value on item (6). For example, if TYPE has been set to WAT then this would mean the group\'s water production multiplied by item (6).<br>6)  VREP: the target is set to the group\'s voidage replacement ratio as defined by item (7). | None |
| 4 | RATE | A real positive value that defines the maximum surface injection rate target or constraint for the phase declared by the TYPE variable.<br>This value may be specified using a User Defined Argument (UDA). | None |
| Liquid stb/d<br>Gas Mscf/d | Liquid sm^3^/day<br>Gas sm3/day | Liquid scc/hour<br>Gas scc/hour |  |
| 5 | RESV | A real positive value that defines the maximum reservoir volume injection rate target or constraint.<br>This value may be specified using a User Defined Argument (UDA).<br>Note setting a value here other than the default means that TYPE, item (2) will be the supplement or "make up" phase. | None |
| rtb/d | rm^3^/day | rcc/hour |  |
| 6 | REIN | A real positive value that defines the target or constraint re-injection fraction for the produced phase defined by the TYPE variable.<br>This value may be specified using a User Defined Argument (UDA).<br>For example, if TYPE is equal to [GAS](#__RefHeading___Toc38607_2267116897) and REIN is equal to 0.85, then 85% of the produced gas will be re-injected. | None |
| dimensionless | dimensionless | dimensionless |  |
| 7 | VREP | A real positive value that defines the target or constraint of the voidage replacement ratio based on all the produced fluids.<br>This value may be specified using a User Defined Argument (UDA).<br>For example, if TYPE is equal to WAT and VREP is equal to 1.00, then 100% of the produced reservoir volume will be re-inject as an equivalent water volume.<br>Note setting a value here other than the default means that TYPE, item (2) will be the supplement phase. | None |
| dimensionless | dimensionless | dimensionless |  |
| 8 | GRPCNTL | A defined character string that determines if this group is subject to higher level group control.<br>1)  YES: then this group is subject to a higher level group's control and the flow rates for this group will be adjusted accordingly.<br>2)  NO: then this group is NOT subject to a higher level group's control and the flow rates for this group will only be controlled by the parameters for this group.<br>This variable is ignored if GRPNAME is equal to [FIELD](#__RefHeading___Toc71850_2267116897). | YES |
| 9 | GRPGUIDE | A real positive value that defines a group\'s injection guide rate expressed as a dimensionless number. A group requires a value for GRPGUIDE only if it is required to produce a specified proportion of a higher level group's rate.<br>Defaulting GRPGUIDE results in the subordinate groups and wells under guide control having their rates dictated by any higher level groups under guide rate control. In other words the GRPNAME is masked out.<br>Setting GRPGUIDE to a real positive value and GUIPHASE to either RATE or RESV will result in a constant injection guide rate. | None |
| dimensionless | dimensionless | dimensionless |  |
| 10 | GUIPHASE | A defined character string that sets the guide phase to which the guide rate in item (9) applies. GUIPHASE should be set to one of the following character strings:<br>1)  NETV: the guide phase is set to production rate minus any injected reservoir rate from the other phases. The net volume is calculated at the beginning of a time step and the option should only be used for groups under voidage replacement control. Note that using this option means that TYPE, item (2) will be the supplement or "make up" phase and the value entered for the group\'s guide rate (GRPGUIDE) will be ignored with this option.<br>2)  RATE: the guide phase is set to the surface injection rate. Setting GUIPHASE to RATE and GRPGUIDE to a real positive value will result in a constant injection guide rate.<br>3)  RESV: the guide phase is set to the in situ reservoir volume rate. Setting GUIPHASE to RESV and GRPGUIDE to a real positive value will result in a constant injection guide rate.<br>4)  VOID: the guide rate is calculated at the beginning of each time step based on the group's net voidage rate.<br>OPM Flow now supports all guide rate options. The default value of 1\* means that the group has no injection guide rate for this phase. | None |
| 11 | GRPREIN | A character string of up to eight characters in length that defines the group name whose production rate should be used for applying the REIN quantity to be injected into GRPNAME.<br>This variable is used to re-inject the REIN production faction from another group (GRPREIN) via this group (GRPNAME). If GRPREIN is defaulted then the re-injection quantity for GRPNAME will be based on the production from GRPNAME itself. | GRPNAME |
| 12 | GRPVREP | A character string of up to eight characters in length that defines the group name whose production rate should be used for applying the VREP quantity to be injected into GRPNAME.<br>This variable is used to re-inject the VREP production faction from another group (GRPVREP) via this group (GRPNAME). If GRPVREP is defaulted then the voidage quantity for GRPNAME will be based on the production from GRPNAME itself. | GRPNAME |
| 13 | WGASRATE | Wet gas injection rate used in the commercial compositional simulator.<br>Not used and should be defaulted with 1\*. | 1\* |
| Notes:<br>1)  User Defined Quantities (\"UDQ\") can be used as User Defined Arguments (\"UDA\") for various group, well, and connection keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. User Defined Arguments are activated using the [UDADIMS](#__RefHeading___Toc65914_1778172979) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, and defined by the [UDQ](#__RefHeading___Toc161095_2932703077) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.<br>2)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.29: GCONINJE Keyword Description

See also the [GRUPTREE](#__RefHeading___Toc118321_1596574740) keyword to define the hierarchy of the groups below the FIELD level, the [GCONPROD](#__RefHeading___Toc146746_4203985108) keyword to define a group's production targets and constraints, the [WCONPROD](#__RefHeading___Toc146754_4203985108) keyword to define a production well's targets and constraints, and the [WCONINJE](#__RefHeading___Toc146750_4203985108) keyword to define an injection well's targets and constraints. All the aforementioned keywords are described in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Example

The following example defines the injection targets and constraints for the field and two groups that are one level below the field group, since the [GRUPTREE](#__RefHeading___Toc118321_1596574740) keyword has not been entered to define the group hierarchy.

\--

\-- GROUP INJECTION TARGETS AND CONSTRAINTS

\--

\-- GRUP FLUID CNTL SURF RESV REINJ VOID GRUP GUIDE GUIDE GRUP GRUP

\-- NAME TYPE MODE RATE RATE FRAC FRAC CNTL RATE DEF REINJ RESV

GCONINJE

FIELD WAT VREP 35E3 1\* 1\* 1\* NO 1\* 1\* 1\* 1\* /

GRP01 WAT VREP 1\* 1\* 1\* 1.0 YES 1\* 1\* 1\* 1\* /

GRPO2 WAT VREP 1\* 1\* 1\* 1.0 YES 1\* 1\* 1\* 1\* /

/

In this example, group GRP01 and GRP02 are injecting water via voidage replacement with a voidage replacement of one and are under the control on the field group, that imposes a 35,000 m3/day total water injection limit.
