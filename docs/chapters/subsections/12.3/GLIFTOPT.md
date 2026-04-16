### GLIFTOPT -- Define Group Gas Optimization Limits

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [GLIFTOPT](#__RefHeading___Toc111805_332691817) keyword defines the maximum amount of gas lift gas available and the maximum amount of gas the group can produce, including the top most group in the group hierarchy known as the FIELD group, for when gas lift optimization has been activated via the [LIFTOPT](#__RefHeading___Toc118992_332691817) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. Note that the [LIFTOPT](#__RefHeading___Toc118992_332691817) keyword should precede the [GLIFTOPT](#__RefHeading___Toc111805_332691817) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section in order to activate the gas lift optimization facility.

Wells are allocated to groups when the wells are specified by the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. Wells defined to be under group control will have their production rates controlled by the group to which they belong, in addition to any well constraints defined for the wells, including any well gas lift optimization parameters on the [WLIFTOPT](#__RefHeading___Toc571903_4263943340) keyword.

| 1 | GRPNAME | A character string of up to eight characters in length that defines the group name for which the group's gas lift optimization parameters are being defined. The group named FIELD is the top most group and should be used to set targets and constraints for the field.<br>Note that the group hierarchy should be defined by the [GRUPTREE](#__RefHeading___Toc118321_1596574740) keyword when there is more than one level of groups, otherwise all the groups will sit directly under the FIELD group in the group tree hierarchy. | None |
| --- | --- | --- | --- |
| 2 | MXLIFT | A real value that defines the total amount of gas lift gas available for this group and any subordinate groups, multiplied by their respective efficiency factors.<br>The units for MXLIFT are the same as that defined by the ALQ parameter on the [VFPPROD](#__RefHeading___Toc121919_2556401936) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. In this case ALQ should be GRAT on the [VFPPROD](#__RefHeading___Toc121919_2556401936) keyword, as MXLIFT applies to the maximum amount of gas lift gas available.<br>The default value of zero, or a negative value implies that there is no limit applied to the group and its subordinate groups. | 0 |
| Mscf/d | sm^3^/day | scc/hour |  |
| 3 | MXGAS | A real value that defines the total amount of gas the group can process. This is the sum of the gas lift gas plus the produced gas for this group and any subordinate groups, multiplied by their respective efficiency factors.<br>The default value of zero, or a negative value implies that there is no limit applied to the group and its subordinate groups | 0 |
| Mscf/d | sm^3^/day | scc/hour |  |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.40: GLIFTOPT Keyword Description

See also the [LIFTOPT](#__RefHeading___Toc118992_332691817) keyword to activate gas lift optimization, the [WLIFTOPT](#__RefHeading___Toc571903_4263943340) keyword to define the wells under gas lift optimization control, the [GRUPTREE](#__RefHeading___Toc118321_1596574740) keyword to define the hierarchy of the groups below the FIELD level, the [GCONPROD](#__RefHeading___Toc146746_4203985108) and [GCONINJE](#__RefHeading___Toc134874_2055188184) keywords to define a group's production and injection rate targets and constraints. All the aforementioned keywords are described in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Example

The following example first switches on gas lift optimization via the [LIFTOPT](#__RefHeading___Toc118992_332691817) keyword and then defines the artificial lift constraints for the field, assuming all the well are on gas lift, using the [GLIFTOPT](#__RefHeading___Toc111805_332691817) keyword.

\-- ACTIVATE GAS LIFT OPTIMIZATION AND PARAMETERS

\--

\-- INCR INCR TSTEP NEWTON

\-- GAS OIL INTVAL OPTN

LIFTOPT

12.5E3 5E-3 0.0 YES /

/

\--

\-- GROUP GAS LIFT OPTIMIZATION CONSTRAINTS

\--

\-- GRUP MAX MAX

\-- NAME GAS ALQ TOTAL GAS

GLIFTOPT

FIELD 200E3 1\* /

/

Here the [LIFTOPT](#__RefHeading___Toc118992_332691817) keyword defines the maximum incremental gas lift gas quantity to be 12.5 x 103 m3, the minimum incremental oil gain per m3 of gas lift gas is set to 5.0 x 10-3 m3, the time step interval is set to zero to perform the gas optimization every time step, and finally the gas lift optimization will be performed [NUPCOL](#__RefHeading___Toc86969_4106839650) Newton iterations for the time step.

The [GLIFTOPT](#__RefHeading___Toc111805_332691817) sets the maximum amount of gas lift gas for the field to 200,000 m3 and there is no maximum limit for the total maximum amount of gas that the group can process.
