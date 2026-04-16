### RUNSPEC -- Define the Start of the RUNSPEC Section of Keywords

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [RUNSPEC](#__RefHeading___Toc55591_1778172979) activation keyword marks the start of the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section that defines the key parameters for the simulator including the dimensions of the model, phases present in the model (oil, gas and water for example), number of tables for a given property and the maximum number of rows for each table, the maximum number of groups, wells and well completions, as well as various options to be invoked by OPM Flow.

Apart from COMMENTS entered by "\--" in columns one and two, this keyword should be the first keyword in the input deck.

There is no data required for this keyword and there is no keyword terminating "/"

#### Example

\-- ==============================================================================

\--

\-- RUNSPEC SECTION

\--

\-- ==============================================================================

RUNSPEC

The above example marks the start of the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section in the OPM Flow data input file.
