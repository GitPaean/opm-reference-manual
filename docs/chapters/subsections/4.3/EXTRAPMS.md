### EXTRAPMS -- Activate Extrapolation Warning Messages

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [EXTRAPMS](#__RefHeading___Toc45777_719036256) keyword activates extrapolation warning messages for when OPM Flow extrapolates the PVT or VFP tables. Frequent extrapolation warning messages should be investigated and resolved as this would indicate possible incorrect data and may result in the simulator extrapolating to unrealistic values.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | EXTRAP | Defines a single integer that activates the extrapolation warning message options for PVT and VFP tables. EXTRAP can have the following values:<br>1)  0 -- No warning messages are give (the default).<br>2)  1 -- PVT table extrapolation warnings are printed.<br>3)  2 -- VFP table extrapolation warnings are printed.<br>4)  3 -- PVT and VFP table extrapolation warnings are printed.<br>5)  4 - PVT and VFP table extrapolation warnings are printed with additional information. | 0 |
| Notes:<br>1)  In addition extrapolation warnings will also be given for Rs and Rv if options (1), (3), and (4) are requested.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 4.2: EXTRAPMS Keyword Description

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

#### Example

\--

\-- ACTIVATE EXTRAPOLATION MESSAGES

\--

EXTRAPMS

2 /

The above example activates the default the VFP table extrapolation warnings option.
