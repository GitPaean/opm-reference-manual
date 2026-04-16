### NEWTRAN -- Activate Irregular Corner-Point Grid Transmissibilities

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword switches on Irregular Corner-Point Grid geometry transmissibility calculation, which is the default option for this type of grid. Grids defined with the [COORD](#__RefHeading___Toc45757_719036256) and [ZCORN](#__RefHeading___Toc45757_7190362561) keywords will always invoke this option by default.

For Cartesian Regular Grids defined by the [DX](#__RefHeading___Toc92905_705534506), [DY](#__RefHeading___Toc45767_719036256), and [DZ](#__RefHeading___Toc45769_719036256) series of keywords the block center geometry transmissibility calculations should be activated via the [OLDTRAN](#__RefHeading___Toc103170_3218818441) keyword. Again this is automatically invoked if this type of grid is being employed.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- ACTIVATE IRREGULAR CORNER-POINT GRID TRANSMISSIBILITIES

\--

NEWTRAN

The above example manually activates Irregular Corner-Point Grid transmissibility calculations.
