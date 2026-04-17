### WARN -- Activate Warning Messages

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

Turns on warning messages to be printed to the print file (\*.PRT); note that this keyword is activated by default and can subsequently be switched off by the NOWARN activation keyword. The warning messages may be turned on and off using keywords WARN and NOWARN. OPM Flow always prints error messages.

It is recommended that WARN should always be used and action taken if necessary for the initial runs, once the run has been "cleaned up" the warning messages can be turned off.

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

The example deactivates the warning messages before reading the grid geometry data using the INCLUDE keyword, and then activates the warning messages after reading the INCLUDE file.
