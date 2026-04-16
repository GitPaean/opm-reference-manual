### RESTART -- Restart Run From an Existing Restart File

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [RESTART](#__RefHeading___Toc135629_1317547213) keyword defines the parameters to restart the simulation from a previous run that has written a [RESTART](#__RefHeading___Toc135629_1317547213) file out to disk. Only restarting from [RESTART](#__RefHeading___Toc135629_1317547213) files is permitted by OPM Flow; restarting from [SAVE](#__RefHeading___Toc55597_1778172979) files is not implemented.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > No.                                                                                                                                                                                                                                | > Name     | > Description                                                                                                                                                                                                                                                                 | > Default |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 1                                                                                                                                                                                                                                  | > RSNAME   | > The RSNAME variable is a character string that defines the root name of the [RESTART](#__RefHeading___Toc135629_1317547213) file to be read into the current input deck.                                                                                                    | > None    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 2                                                                                                                                                                                                                                  | > RSNUM    | > A positive integer that defines the restart point on the [RESTART](#__RefHeading___Toc135629_1317547213) file to be read and to be used to initialize the model.                                                                                                            | > None    |
|                                                                                                                                                                                                                                      |            |                                                                                                                                                                                                                                                                               |           |
|                                                                                                                                                                                                                                      |            | > When OPM Flow writes a restart point a message is printed to the \*.PRT file indicating the time step the restart was written out.                                                                                                                                          |           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 3                                                                                                                                                                                                                                  | > RSTYPE   | > A defined character sting set to [SAVE](#__RefHeading___Toc55597_1778172979) to read the restart data from the [SAVE](#__RefHeading___Toc55597_1778172979) file, otherwise defaulted to 1\* to read the data from the [RESTART](#__RefHeading___Toc135629_1317547213) file. | > 1\*     |
|                                                                                                                                                                                                                                      |            |                                                                                                                                                                                                                                                                               |           |
|                                                                                                                                                                                                                                      |            | > The [SAVE](#__RefHeading___Toc55597_1778172979) file option is not supported by OPM Flow and should be defaulted with 1\*.                                                                                                                                                  |           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 4                                                                                                                                                                                                                                  | > RSFORMAT | > A defined character string that defines the format of the [SAVE](#__RefHeading___Toc55597_1778172979) file to be read if RSTYPE has been set to [SAVE](#__RefHeading___Toc55597_1778172979), and should be set to one of the following:                                     | > U       |
|                                                                                                                                                                                                                                      |            |                                                                                                                                                                                                                                                                               |           |
|                                                                                                                                                                                                                                      |            | 1)  FORMATTED: If the file is formatted as ASCII i.e. a text file, as oppose to a binary file. The option can be abbreviated to just the letter F.                                                                                                                            |           |
|                                                                                                                                                                                                                                      |            |                                                                                                                                                                                                                                                                               |           |
|                                                                                                                                                                                                                                      |            | 2)  UNFORMATTED: If the file is in binary format, note this option can be abbreviated to just the letter U. This type of file is operating system dependent                                                                                                                   |           |
|                                                                                                                                                                                                                                      |            |                                                                                                                                                                                                                                                                               |           |
|                                                                                                                                                                                                                                      |            | > If the variable RSFORMAT omitted then the default is for binary file input.                                                                                                                                                                                                 |           |
|                                                                                                                                                                                                                                      |            |                                                                                                                                                                                                                                                                               |           |
|                                                                                                                                                                                                                                      |            | > This option is not supported by OPM Flow and should be defaulted with 1\*.                                                                                                                                                                                                  |           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Notes:                                                                                                                                                                                                                             |            |                                                                                                                                                                                                                                                                               |           |
|                                                                                                                                                                                                                                      |            |                                                                                                                                                                                                                                                                               |           |
| 1)  OPM Flow can only restart runs from a [RESTART](#__RefHeading___Toc135629_1317547213) file, the commercial simulator\'s [SAVE](#__RefHeading___Toc55597_1778172979) file format is not supported.                                |            |                                                                                                                                                                                                                                                                               |           |
|                                                                                                                                                                                                                                      |            |                                                                                                                                                                                                                                                                               |           |
| 2)  Note that due to the complexities of the [RESTART](#__RefHeading___Toc135629_1317547213) file, OPM Flow may not always be able to restart from the commercial simulators [RESTART](#__RefHeading___Toc135629_1317547213) file.   |            |                                                                                                                                                                                                                                                                               |           |
|                                                                                                                                                                                                                                      |            |                                                                                                                                                                                                                                                                               |           |
| 3)   The keyword is terminated by a "/".                                                                                                                                                                                             |            |                                                                                                                                                                                                                                                                               |           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Table 10.25: RESTART Keyword Description

The most direct way to start a restart run is to:

1)  1)  1)  Copy the existing data file that created the [RESTART](#__RefHeading___Toc135629_1317547213) file and give it a new name. For example if the [RESTART](#__RefHeading___Toc135629_1317547213) file is from a case named NOR-OPM-A01.DATA, then the copied data file could be named NOR-OPM-A01-R1.DATA.

        2)  Edit the copied data file (NOR-OPM-A01-R1.DATA) and delete all equilibration keywords ([EQUIL](#__RefHeading___Toc135617_1317547213), [RSVD](#__RefHeading___Toc137363_1317547213), etc.) or the enumeration equilibration keywords ([PRESSURE](#__RefHeading___Toc135627_1317547213), [SGAS](#__RefHeading___Toc137369_1317547213), [SOIL](#__RefHeading___Toc137371_1317547213). [SWAT](#__RefHeading___Toc137373_1317547213), etc.) in the [SOLUTION](#__RefHeading___Toc43947_784232322) section used to initialize the model.

        3)  In the [SOLUTION](#__RefHeading___Toc43947_784232322) section of NOR-OPM-A01-R1.DATA file insert the [RESTART](#__RefHeading___Toc135629_1317547213) keyword, using NOR-OPM-A01 as RSNAME and the required RSNUM value for the time step to restart from.

        4)  In the [SCHEDULE](#__RefHeading___Toc43945_784232322) section of NOR-OPM-A01-R1.DATA file insert the [SKIPREST](#__RefHeading___Toc117631_2179381650) keyword at the very beginning of the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. The [SKIPREST](#__RefHeading___Toc117631_2179381650) keyword causes the simulator to only read in data it requires for restarting the run up to the [RESTART](#__RefHeading___Toc135629_1317547213) point (RSNUM). Note that certain keywords always need to be present in a restart run in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section as the data is not stored on the [RESTART](#__RefHeading___Toc135629_1317547213) file, for example the VFP tables ([VFPPROD](#__RefHeading___Toc121919_2556401936) and [VFPINJ](#__RefHeading___Toc121917_2556401936) keywords). The [SKIPREST](#__RefHeading___Toc117631_2179381650) keyword automatically processes the input deck and reads the required data.

        5)  In the [SCHEDULE](#__RefHeading___Toc43945_784232322) section of NOR-OPM-A01-R1.DATA file after the [RESTART](#__RefHeading___Toc135629_1317547213) point make any required changes, save the file and run the NOR-OPM-A01-R1.DATA with OPM Flow.

See also [RPTRST](#__RefHeading___Toc210154_2884651453), [RPTSCHED](#__RefHeading___Toc268459_1366622701) and [SKIPREST](#__RefHeading___Toc117631_2179381650) keywords.

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

In addition in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section the [SKIPREST](#__RefHeading___Toc117631_2179381650) keyword should be used to correctly read in the schedule data up to the [RESTART](#__RefHeading___Toc135629_1317547213) point.

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

Note is advisable to place the [SKIPREST](#__RefHeading___Toc117631_2179381650) keyword at the very beginning of the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.
