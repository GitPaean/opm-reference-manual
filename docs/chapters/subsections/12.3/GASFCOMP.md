### GASFCOMP -- Define Automatic Gas Compressors

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, [GASFCOMP](#__RefHeading___Toc195056_2110098628), defines automatic gas compressors for when the Gas Field Operations option has been activated by the [GASFIELD](#__RefHeading___Toc195426_1190369742) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section and the Standard Network option has been specified by the [GRUPTREE](#__RefHeading___Toc118321_1596574740), [GRUPNET](#__RefHeading___Toc118319_1596574740) and [GNETINJE](#__RefHeading___Toc114199_332691817) series of keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. Automatic gas compressors are automatically switch on for a group if a group's gas production target cannot be satisfied. In addition, if a group's gas target is reduced then the automatic compressors are initially switch off to test that the reduced gas rate target can be met without compression, if not, compression is switched back on. Note that all automatic compressors are "switch on" when calculating a field's gas deliverability.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
