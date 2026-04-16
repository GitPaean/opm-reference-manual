### SIMULATE -- Activate the Simulation Mode

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[SIMULATE](#__RefHeading___Toc1235335_516898843) switches the mode of the simulation to run simulation mode from the data input checking mode activated by the [NOSIM](#__RefHeading___Toc27585_2267116897) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. Note that if [NOSIM](#__RefHeading___Toc27585_2267116897) has been used in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section then [SIMULATE](#__RefHeading___Toc1235335_516898843) will have no effect.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

The example below switches OPM Flow to no simulation mode for data checking of the input deck.

\--

\-- ACTIVATE SIMULATION MODE TO RUN THE MODEL

\--

SIMULATE
