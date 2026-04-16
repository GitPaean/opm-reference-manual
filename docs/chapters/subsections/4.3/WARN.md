### WARN -- Activate Warning Messages

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

Turns on warning messages to be printed to the print file (\*.PRT); note that this keyword is activated by default and can subsequently be switched off by the [NOWARN](#__RefHeading___Toc54928_2479612490) activation keyword. The warning messages may be turned on and off using keywords [WARN](#__RefHeading___Toc54930_2479612490) and [NOWARN](#__RefHeading___Toc54928_2479612490). OPM Flow always prints error messages.

It is recommended that [WARN](#__RefHeading___Toc54930_2479612490) should always be used and action taken if necessary for the initial runs, once the run has been "cleaned up" the warning messages can be turned off.

There is no data required for this keyword.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

#### Example

\--

\-- SWITCH OFF WARNING MESSAGES

\--

NOWARN

\--

\-- INCLUDE SIMULATION GRID WITH SLOPING FAULTS

\--

INCLUDE

\'./INCLUDE/GRID/IRAP_1005.GRDECL\' /

\--

\-- SWITCH ON WARNING MESSAGES

\--

WARN

The example deactivates the warning messages before reading the grid geometry data using the [INCLUDE](#__RefHeading___Toc55749_2479612490) keyword, and then activates the warning messages after reading the [INCLUDE](#__RefHeading___Toc55749_2479612490) file.
