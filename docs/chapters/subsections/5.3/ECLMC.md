### ECLMC -- Activate Multi-Component Brine Model

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [ECLMC](#__RefHeading___Toc206960_803326780) keyword activates the Multi-Component Brine model that allows for the water phase to have multiple water salinities. The keyword should be used in conjunction with the [BRINE](#__RefHeading___Toc162083_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979). Both keywords must be specified to activate the Multi-Component Brine model, whereas the [BRINE](#__RefHeading___Toc162083_289573908) keyword only is required to activate the standard brine tracking model.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

The first example activates the standard Brine Tracking model.

\--

\-- ACTIVATE STANDARD BRINE MODEL

\--

BRINE

The next example shows the [ECLMC](#__RefHeading___Toc206960_803326780) and [BRINE](#__RefHeading___Toc162083_289573908) keywords for when the Multi-Component Brine model is required.

\--

\-- ACTIVATE MULTI-COMPONENT BRINE MODEL

\--

ECLMC

\--

\-- DEFINE WATER PHASE MULTI-COMPONENT BRINE COMPONENTS

\--

\-- SALT1 SALT2 SALT3 SALT4 SALT5

BRINE

NACL CACL2 MGC03 /

The above example activates the Multi-Component Brine model with three different water salinities.
