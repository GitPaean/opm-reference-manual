### NOSIM -- Activate the No Simulation Mode for Data File Checking

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

NOSIM switches the mode of OPM Flow to data input checking mode. In this mode the input file is read and all messages and print instructions are sent to the respective output files. The SCHEDULE section is read but the simulation is not performed.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

The example below switches OPM Flow to no simulation mode for data checking of the input deck.

\--

\-- SWITCH NO SIMULATION MODE FOR DATA CHECKING COMMENT OUT TO RUN THE MODEL

\--

NOSIM

And the next example shows how to commented out the NOSIM activation keyword so that the simulation will proceed.

\--

\-- SWITCH NO SIMULATION MODE FOR DATA CHECKING COMMENT OUT TO RUN THE MODEL

\--

\-- NOSIM
