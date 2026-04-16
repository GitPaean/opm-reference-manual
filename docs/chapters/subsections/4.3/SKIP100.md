### SKIP100 -- Activate Skipping of Keywords by Black-Oil Simulator

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [SKIP100](#__RefHeading___Toc65046_1640804870) keyword activates skipping of all keywords and input data by the commercial black-oil simulator until the [ENDSKIP](#__RefHeading___Toc52491_2479612490) keyword is encountered. All keywords between the [SKIP100](#__RefHeading___Toc65046_1640804870) and [ENDSKIP](#__RefHeading___Toc52491_2479612490) keywords are ignored by the commercial black-oil simulator. The [SKIP100](#__RefHeading___Toc65046_1640804870) keyword is ignored by the commercial compositional simulator. Each [SKIP100](#__RefHeading___Toc65046_1640804870) keyword should be paired with an [ENDSKIP](#__RefHeading___Toc52491_2479612490) keyword. See also the [SKIP](#__RefHeading___Toc52489_2479612490) and [SKIP300](#__RefHeading___Toc980121_1781444514) keywords.

There is no data required for this keyword.

By default OPM Flow behaves like the commercial black-oil simulator. However, this behaviour can be changed using the \--input-skip-mode command line parameter.

The nesting of pairs of either the [SKIP](#__RefHeading___Toc52489_2479612490), [SKIP100](#__RefHeading___Toc65046_1640804870), or [SKIP300](#__RefHeading___Toc980121_1781444514) keyword and the [ENDSKIP](#__RefHeading___Toc52491_2479612490) keyword is not supported by OPM Flow.

#### Example

If the following example is read using the commercial black-oil simulator then the [SKIP300](#__RefHeading___Toc980121_1781444514) keyword will be ignored and the black-oil PVT data will be read, the [SKIP100](#__RefHeading___Toc65046_1640804870) keyword will cause the compositional PVT data to be ignored, and then the remainder of the input will be read after the next [ENDSKIP](#__RefHeading___Toc52491_2479612490) keyword is encountered.

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
