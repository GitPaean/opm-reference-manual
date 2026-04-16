### GSEPCOND -- Assign Group Separators

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [GSEPCOND](#__RefHeading___Toc207526_870710203) keyword assigns previously defined separators to a group. Group separators are specified by the [SEPVALS](#__RefHeading___Toc663272_516898843) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. The facility is used in black-oil modeling to re-scale the PVT data entered via the [PROPS](#__RefHeading___Toc39329_784232322) section, based on the saturation point oil formation volume factor (Bob) and the initial saturated gas-oil ratio (Rsi) entered on the SEVPALS keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
