### WPAVEDEP -- Define Well Reference Depth for Pressure Calculations

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WPAVEDEP](#__RefHeading___Toc121639_2412586160) keyword defines the reference depth to be used to calculate and report grid block average bottom-hole pressures for a well. This keyword can be used to override the values entered or defaulted on the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. The simulator corrects the grid block calculated pressures to a well's reference depth using the hydrostatic well of the producing fluids.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well and well connection status data is being defined.<br>Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | BHPREF | A real value that defines the reference depth for reporting the bottom-hole pressure for the well. Ideally this value should be set to the midpoint of the perforations as defined by the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.<br>If defaulted by 1\* or set to a value less than or equal to zero, then the mid-point of shallowest connection defined by the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword will be used. | Mid-point of shallowest connection defined by the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword |
| feet | m | cm |  |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.109: WPAVDEP Keyword Description

See also the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword that defines a well, the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword to define a well's connections, and the [WPAVE](#__RefHeading___Toc121923_2556401936) for defining how the average bottom-hole pressure should be calculated. All the aforementioned keywords are described in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Example

The following example illustrates how to set the bottom-hole reference depth for wells completed in different reservoirs that have different datum depths. Here it is assumed that all wells in a reservoir A have RES-A as part of their well name, and similarly for reservoirs B and C.

\--

\-- WELL SPECIFICATION DATA

\--

\-- WELL GROUP LOCATION BHP PHASE DRAIN INFLOW SHUT CROSS PRESS

\-- NAME NAME I J DEPTH FLUID AREA EQUA. IN FLOW TABLE

WELSPECS

RES-AOP1 PLATFORM 14 13 1\* OIL 1\* STD OPEN NO 1\* /

RES-AOP2 PLATFORM 17 16 1\* OIL 1\* STD OPEN NO 1\* /

RES-AOP3 PLATFORM 21 19 1\* OIL 1\* STD OPEN NO 1\* /

RES-BOP4 PLATFORM 28 96 1\* OIL 1\* STD OPEN NO 1\* /

RES-BOP5 PLATFORM 34 89 1\* OIL 1\* STD OPEN NO 1\* /

RES-COP6 PLATFORM 128 52 1\* OIL 1\* STD OPEN NO 1\* /

RES-COP7 PLATFORM 134 56 1\* OIL 1\* STD OPEN NO 1\* /

RES-COP8 PLATFORM 138 50 1\* OIL 1\* STD OPEN NO 1\* /

RES-COP9 PLATFORM 120 52 1\* OIL 1\* STD OPEN NO 1\* /

/

\--

\-- DEFINE WELL REFERENCE DEPTH FOR PRESSURE CALCULATIONS

\--

\-- WELL REF

\-- NAME DEPTH

\-- \-\-\-- \-\-\-\-\--

WPAVEDEP

\'RES-A\*' 3100.0 /

\'RES-B\*' 3300.0 /

\'RES-C\*' 5909.0 /

/

In the example the all wells dedicated to RES-A will have their bottom-hole reference depth set to 3,000 ft. TVDSS, RES-B wells to 3,300 ft. TVDSS and well RES-C wells to 5909 ft. TVDSS.
