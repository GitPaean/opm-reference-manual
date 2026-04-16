### GASWAT -- Activate the Gas-Water Model Formulation

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword activates the two-phase Gas-Water model, as such it is equivalent to using both the [GAS](#__RefHeading___Toc38607_2267116897) and [WATER](#__RefHeading___Toc38611_2267116897) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section..

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\-- ==============================================================================

\--

\-- RUNSPEC SECTION

\--

\-- ==============================================================================

RUNSPEC

\--

\-- ACTIVATE CO2 STORAGE IN THE MODEL (OPM FLOW CO2 STORAGE KEYWORD)

\--

CO2STORE

\--

\-- ACTIVATE COMPOSITIONAL MODELING FORMULATION (OPM FLOW KEYWORD)

\--

COMPS

2 /

\--

\-- ACTIVATE GAS-WATER THE MODEL (OPM FLOW KEYWORD)

\--

GASWAT

The above example declares that the run should use the Gas-Water model, together with the [CO2STORE](#__RefHeading___Toc387968_1616145207) option, and with two components.
