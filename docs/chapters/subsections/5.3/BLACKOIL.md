### BLACKOIL -- Activate Black-Oil Phases

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword switches on the black-oil formulation, and is equivalent to setting the phases present in the model to be oil, vaporized oil, gas, and dissolved gas. Note if water is present in the model this needs to be explicitly stated via the WATER keyword in the RUNSPEC section (see also the LIVEOIL keywords in the RUNSPEC section). The keyword is used by the commercial simulator's compositional THERMAL option to set the phases present in the model.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

The following example activates the black-oil phases in the model.

\--

\-- ACTIVATE BLACK-OIL PHASES

\--

BLACKOIL

Alternatively one could explicitly declare the phases using the following keywords in the RUNSPEC section.

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
