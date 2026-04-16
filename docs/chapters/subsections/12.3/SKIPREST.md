### SKIPREST -- Activate Skipping of Restart Schedule Data

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword turns on skipping of keywords up to the start of the restart point, as defined on the [RESTART](#__RefHeading___Toc135629_1317547213) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The [RESTART](#__RefHeading___Toc135629_1317547213) keyword defines the parameters to restart the simulation from a previous run that has written a [RESTART](#__RefHeading___Toc135629_1317547213) file out to disk. Activating the [SKIPREST](#__RefHeading___Toc117631_2179381650) keyword causes the simulator to only read in data it requires for restarting the run up to the [RESTART](#__RefHeading___Toc135629_1317547213) point (RSNUM on the [RESTART](#__RefHeading___Toc135629_1317547213) keyword in the [SOLUTION](#__RefHeading___Toc43947_784232322) section). Note that certain keywords always need to be present in a restart run in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section as the data is not stored on the [RESTART](#__RefHeading___Toc135629_1317547213) file, for example the VFP tables ([VFPPROD](#__RefHeading___Toc121919_2556401936) and [VFPINJ](#__RefHeading___Toc121917_2556401936) keywords). The [SKIPREST](#__RefHeading___Toc117631_2179381650) keyword automatically processes the input deck and reads the required data.

There is no data required for this keyword.

#### Example

The example below defines a restart from the previously run NOR-OPM-A01 case at time step number 40.

\-- ==============================================================================

\--

\-- SOLUTION SECTION

\--

\-- ==============================================================================

SOLUTION

\--

\-- FLEXIBLE RESTART FROM PREVIOUS SIMULATION RUN

\--

\-- FILE RESTART RESTART FILE

\-- NAME NUMBER TYPE FORMAT

RESTART

\'NOR-OPM-A01\' 40 1\* 1\* /

Then in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section the [SKIPREST](#__RefHeading___Toc117631_2179381650) keyword is used to correctly read in the schedule data up to the [RESTART](#__RefHeading___Toc135629_1317547213) point.

\-- ==============================================================================

\--

\-- SCHEDULE SECTION

\--

\-- ==============================================================================

SCHEDULE

\--

\-- ACTIVATE SKIPREST OPTION TO AVOID MODIFYING SCHEDULE SECTION

\--

SKIPREST
