### LIVEOIL -- Activate the Live Oil Phase (Oil with Free and Dissolved Gas)

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword activates oil, free and dissolved gas in the model and therefore makes the oil phase live oil[^1] in the black-oil formulation, and is equivalent to setting the phases present in the model to be oil, dissolved gas, gas and water phases. Note if water is present in the model this needs to be explicitly stated via the [WATER](#__RefHeading___Toc38611_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section (see also the [BLACKOIL](#__RefHeading___Toc121257_2318984819) and DEADOIL keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section). The keyword is used by the commercial simulator's compositional [THERMAL](#__RefHeading___Toc137276_650382403) option to set the phases present in the model.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

#### Example

The following example activates the black-oil phases in the model.

\--

\-- ACTIVATE LIVE-OIL PHASE

\--

LIVEOIL

Alternatively one could explicitly declare the phases using the following keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

\--

\-- OIL PHASE IS PRESENT IN THE RUN

\--

OIL

\--

\-- DISSOLVED GAS IN LIVE OIL IS PRESENT IN THE RUN

\--

DISGAS

\--

\-- GAS PHASE IS PRESENT IN THE RUN

\--

GAS

\--

\-- WATER PHASE IS PRESENT IN THE RUN

\--

WATER

The above example switches on the oil, dissolved gas, gas and water phases in the model.

[^1]: "Live" oil is oil that contains gas in solution, which is normally the case for most conventional oil reservoirs. However, for oil reservoirs classified as heavy oil reservoirs, the in situ dissolved gas may be negligible and oil would then be classified as gas-free oil which is commonly referred to as "dead" oil.
