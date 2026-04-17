### SKIP300 -- Activate Skipping of Keywords by Compositional Simulator

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SKIP300 keyword activates skipping of all keywords and input data by the commercial compositional simulator until the ENDSKIP keyword is encountered. All keywords between the SKIP300 and ENDSKIP keywords are ignored by the commercial compositional simulator. The SKIP300 keyword is ignored by the commercial black-oil simulator. Each SKIP300 keyword should be paired with an ENDSKIP keyword. See also the SKIP and SKIP100 keywords.

There is no data required for this keyword.

By default OPM Flow behaves like the commercial black-oil simulator. However, this behaviour can be changed using the \--input-skip-mode command line parameter.

The nesting of pairs of either the SKIP, SKIP100, or SKIP300 keyword and the ENDSKIP keyword is not supported by OPM Flow.

#### Example

If the following example is read using the commercial compositional simulator then the SKIP300 keyword will cause the black-oil PVT data to be ignored, the input will continue to be read after the next ENDSKIP keyword is encountered, and the SKIP100 keyword will be ignored and the compositional PVT data will be read along with the remainder of the input.

\--

\-- ACTIVATE SKIPPING OF KEYWORDS BY COMPOSITIONAL SIMULATOR

\--

SKIP300

\--

\-- INCLUDE BLACK-OIL PVT DATA

\--

INCLUDE

\'./INCLUDE/'BLACK-OIL-PVT\' /

\--

\-- DEACTIVATE SKIPPING OF KEYWORDS

\--

ENDSKIP

\--

\-- ACTIVATE SKIPPING OF KEYWORDS BY BLACK-OIL SIMULATOR

\--

SKIP100

\--

\-- INCLUDE COMPOSITIONAL PVT DATA

\--

INCLUDE

\'./INCLUDE/'COMPOSITION-PVT-EOS\' /

\--

\-- SWITCH ON READING OF ALL KEYWORDS AND DATA

\--

ENDSKIP

\--

\-- WATER PVT TABLE

\--

PVTW

\-- REF PRES BW CW VISC VISC

\-- PSIA RB/STB 1/PSIA CPOISE GRAD

\-- \-\-\-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\--

4840.0 1.019 2.7E-6 0.370 1\* / WATER DATA REGION 1

\--

\-- OIL WAT GAS

\-- DENSITY DENSITY DENSITY

\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\--

DENSITY

39.0 62.37 0.04520 / PVT DATA REGION 1

\-- ROCK COMPRESSIBILITY

\--

\-- REF PRES CF

\-- PSIA 1/PSIA

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\--

ROCK

3966.9 5.0E-06 / ROCK COMPRESSIBILITY
