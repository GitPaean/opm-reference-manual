### WNETDP -- Define Well THP to Network Pressure Drop

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WNETDP](#__RefHeading___Toc606927_4263943340) keyword allows for a constant pressure drop between a well's Tubing Head Pressure ("THP") and the well's connecting network node, for when the either the Standard Network or the Extended Network options have been activated, and the well is part of a network. For production wells in a production network, [WNETDP](#__RefHeading___Toc606927_4263943340) is added to the well's connecting network node pressure to arrive at the well's THP value. Whereas for injection wells in an injection network, [WNETDP](#__RefHeading___Toc606927_4263943340) is subtracted from the well's connecting network node pressure to arrive at the well's THP value. The Standard Network option is invoked if the [GRUPTREE](#__RefHeading___Toc118321_1596574740), [GRUPNET](#__RefHeading___Toc118319_1596574740), [GNETINJE](#__RefHeading___Toc114199_332691817), [GNETPUMP](#__RefHeading___Toc421755_1414963541), etc. series of keywords have been used in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. The Extended Network option is activated by the [NETWORK](#__RefHeading___Toc311583_1841740821) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
