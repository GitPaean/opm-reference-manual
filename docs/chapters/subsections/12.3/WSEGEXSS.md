### WSEGEXSS -- Define Multi-Segment Well Import-Export Segment Volumes

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, [WSEGEXSS](#__RefHeading___Toc985555_4263943340), enables the import or export of fluids from a segment in a multi-segment well. This can be used to, for example, model gas lift injection for oil wells under artificial lift, or to approximate the behavior of a down-hole separator. The import-export fluid volumes can either be expressed as rates or defined as a function of a segment's pressure value.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
