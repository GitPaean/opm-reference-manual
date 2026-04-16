### GLIFTLIM -- Group Artificial Lift Constraints

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [GLIFTLIM](#__RefHeading___Toc399999_1414963541) keyword defines the maximum number of wells on artificial lift and the maximum amount of the artificial lift that is available for a group, including the top most group in the group hierarchy known as the FIELD group. Wells are allocated to groups when the wells are specified by the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. Wells defined to be under group control will have their production rates controlled by the group to which they belong, in addition to any well constraints defined for the wells.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | GRPNAME | A character string of up to eight characters in length that defines the group name for which the group's artificial lift constraints are being defined. The group named FIELD is the top most group and should be used to set targets and constraints for the field.<br>Note that the group hierarchy should be defined by the [GRUPTREE](#__RefHeading___Toc118321_1596574740) keyword when there is more than one level of groups, otherwise all the groups will sit directly under the FIELD group in the group tree hierarchy. | None |
| --- | --- | --- | --- |
| 2 | MXLIFT | A real positive value that defines the total amount of artificial lift available for this group and any subordinate groups.<br>The units for MXLIFT are the same as that defined by the ALQ parameter on the [VFPPROD](#__RefHeading___Toc121919_2556401936) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. For example, if ALQ has been set to GRAT on the [VFPPROD](#__RefHeading___Toc121919_2556401936) keyword, then MXLIFT would be the maximum amount of gas lift gas available for this group and any subordinate groups, and the units would Mscf, assuming [FIELD](#__RefHeading___Toc71850_2267116897) units had been activated in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>The default value of zero implies that there is no limit applied to the group and its subordinate groups. | 0 |
| See [VFPPROD](#__RefHeading___Toc121919_2556401936) (ALQ) | See [VFPPROD](#__RefHeading___Toc121919_2556401936) (ALQ) | See [VFPPROD](#__RefHeading___Toc121919_2556401936) (ALQ) |  |
| 3 | MXWELS | A positive integer defining the maximum number of producing wells on artificial lift for this group and any subordinate groups.<br>The default value of zero implies that there is no limit to the number of wells. | 0 |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.39: GLIFTLIM Keyword Description

See also the [GRUPTREE](#__RefHeading___Toc118321_1596574740) keyword to define the hierarchy of the groups below the FIELD level, the [GCONPROD](#__RefHeading___Toc146746_4203985108) and [GCONINJE](#__RefHeading___Toc134874_2055188184) keywords to define a group's production and injection rate targets and constraints, the [WCONPROD](#__RefHeading___Toc146754_4203985108) keyword to define a production well's targets and constraints, and the [WCONINJE](#__RefHeading___Toc146750_4203985108) keyword to define an injection well's targets and constraints. All the aforementioned keywords are described in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Example

The following example defines the artificial lift constraints for the field, assuming all the wells are on gas lift.

\-\--

\-- GROUP ARTIFICIAL LIFT CONSTRAINTS

\--

\-- GRUP MAX MAX

\-- NAME ALQ WELLS

GLIFTLIM

FIELD 20E3 20 /

/

Here the maximum amount of gas lift gas for the field is set to 20.0 MMscf/f and a maximum of 20 wells can utilize gas lift at a time.
