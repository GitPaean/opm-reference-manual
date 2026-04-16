### RCMASTS -- Reservoir Coupling Group Minimum Time Step for Flow Restriction

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[RCMASTS](#__RefHeading___Toc637253_501926209) is used when reservoir coupling is invoked by the [GRUPMAST](#__RefHeading___Toc488185_1414963541) and [SLAVES](#__RefHeading___Toc1268538_516898843) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. The keyword should be placed within the master file and it sets the minimum time step size for groups for when a group is being restricted by a group's limiting flow rate fractional change (see the [GRUPMAST](#__RefHeading___Toc488185_1414963541) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section).

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
