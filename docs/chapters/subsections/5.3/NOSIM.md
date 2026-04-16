### NOSIM -- Activate the No Simulation Mode for Data File Checking

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[NOSIM](#__RefHeading___Toc27585_2267116897) switches the mode of OPM Flow to data input checking mode. In this mode the input file is read and all messages and print instructions are sent to the respective output files. The [SCHEDULE](#__RefHeading___Toc43945_784232322) section is read but the simulation is not performed.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

The example below switches OPM Flow to no simulation mode for data checking of the input deck.

\--

\-- SWITCH NO SIMULATION MODE FOR DATA CHECKING COMMENT OUT TO RUN THE MODEL

\--

NOSIM

And the next example shows how to commented out the [NOSIM](#__RefHeading___Toc27585_2267116897) activation keyword so that the simulation will proceed.

\--

\-- SWITCH NO SIMULATION MODE FOR DATA CHECKING COMMENT OUT TO RUN THE MODEL

\--

\-- NOSIM
