### BLACKOIL -- Activate Black-Oil Phases

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword switches on the black-oil formulation, and is equivalent to setting the phases present in the model to be oil, vaporized oil, gas, and dissolved gas. Note if water is present in the model this needs to be explicitly stated via the [WATER](#__RefHeading___Toc38611_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section (see also the [LIVEOIL](#__RefHeading___Toc146521_1576452438) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section). The keyword is used by the commercial simulator's compositional [THERMAL](#__RefHeading___Toc137276_650382403) option to set the phases present in the model.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

The following example activates the black-oil phases in the model.

\--

\-- ACTIVATE BLACK-OIL PHASES

\--

BLACKOIL

Alternatively one could explicitly declare the phases using the following keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

\--

\-- OIL PHASE IS PRESENT IN THE RUN

\--

OIL

\--

\-- VAPORIZED OIL IN WET GAS IS PRESENT IN THE RUN

\--

VAPOIL

\--

\-- GAS PHASE IS PRESENT IN THE RUN

\--

GAS

\--

\-- DISSOLVED GAS IN LIVE OIL IS PRESENT IN THE RUN

\--

DISGAS

The above example switches on the black-oil phases in the model.
