### ENDSKIP -- Deactivate Skipping of Keywords and Input Data

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The ENDSKIP keyword deactivates the skipping of keywords that was activated by the SKIP, SKIP100 or SKIP300 keywords. Each SKIP, SKIP100 or SKIP300 keyword should be paired with an ENDSKIP keyword.

There is no data required for this keyword.

The nesting of pairs of either the SKIP, SKIP100, or SKIP300 keyword and the ENDSKIP keyword is not supported by OPM Flow.

#### Example

\--

\-- SWITCH ON SKIPPING OF KEYWORDS AND DATA

\--

SKIP

\--

\-- INCLUDE SIMULATION GRID WITH SLOPING FAULTS

\--

INCLUDE

\'./INCLUDE/GRID/IRAP_1005.GRDECL\' /

\--

\-- SWITCH ON READING OF KEYWORDS AND DATA

\--

ENDSKIP

The example skips reading of the grid geometry data input using the INCLUDE keyword, and then reverts back to reading the remainder of the input file.
