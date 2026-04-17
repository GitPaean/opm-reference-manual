### RESTART -- Restart Run From an Existing Restart File

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The RESTART keyword defines the parameters to restart the simulation from a previous run that has written a RESTART file out to disk. Only restarting from RESTART files is permitted by OPM Flow; restarting from SAVE files is not implemented.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | RSNAME | The RSNAME variable is a character string that defines the root name of the RESTART file to be read into the current input deck. | None |
| 2 | RSNUM | A positive integer that defines the restart point on the RESTART file to be read and to be used to initialize the model.<br>When OPM Flow writes a restart point a message is printed to the \*.PRT file indicating the time step the restart was written out. | None |
| 3 | RSTYPE | A defined character sting set to SAVE to read the restart data from the SAVE file, otherwise defaulted to 1\* to read the data from the RESTART file.<br>The SAVE file option is not supported by OPM Flow and should be defaulted with 1\*. | 1\* |
| 4 | RSFORMAT | A defined character string that defines the format of the SAVE file to be read if RSTYPE has been set to SAVE, and should be set to one of the following:<br>1)  FORMATTED: If the file is formatted as ASCII i.e. a text file, as oppose to a binary file. The option can be abbreviated to just the letter F.<br>2)  UNFORMATTED: If the file is in binary format, note this option can be abbreviated to just the letter U. This type of file is operating system dependent<br>If the variable RSFORMAT omitted then the default is for binary file input.<br>This option is not supported by OPM Flow and should be defaulted with 1\*. | U |
| Notes:<br>1)  OPM Flow can only restart runs from a RESTART file, the commercial simulator\'s SAVE file format is not supported.<br>2)  Note that due to the complexities of the RESTART file, OPM Flow may not always be able to restart from the commercial simulators RESTART file.<br>3)   The keyword is terminated by a "/". |  |  |  |

Table 10.25: RESTART Keyword Description

The most direct way to start a restart run is to:

1)  1)  1)  Copy the existing data file that created the RESTART file and give it a new name. For example if the RESTART file is from a case named NOR-OPM-A01.DATA, then the copied data file could be named NOR-OPM-A01-R1.DATA.

        2)  Edit the copied data file (NOR-OPM-A01-R1.DATA) and delete all equilibration keywords (EQUIL, RSVD, etc.) or the enumeration equilibration keywords (PRESSURE, SGAS, SOIL. SWAT, etc.) in the SOLUTION section used to initialize the model.

        3)  In the SOLUTION section of NOR-OPM-A01-R1.DATA file insert the RESTART keyword, using NOR-OPM-A01 as RSNAME and the required RSNUM value for the time step to restart from.

        4)  In the SCHEDULE section of NOR-OPM-A01-R1.DATA file insert the SKIPREST keyword at the very beginning of the SCHEDULE section. The SKIPREST keyword causes the simulator to only read in data it requires for restarting the run up to the RESTART point (RSNUM). Note that certain keywords always need to be present in a restart run in the SCHEDULE section as the data is not stored on the RESTART file, for example the VFP tables (VFPPROD and VFPINJ keywords). The SKIPREST keyword automatically processes the input deck and reads the required data.

        5)  In the SCHEDULE section of NOR-OPM-A01-R1.DATA file after the RESTART point make any required changes, save the file and run the NOR-OPM-A01-R1.DATA with OPM Flow.

See also RPTRST, RPTSCHED and SKIPREST keywords.

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

In addition in the SCHEDULE section the SKIPREST keyword should be used to correctly read in the schedule data up to the RESTART point.

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

Note is advisable to place the SKIPREST keyword at the very beginning of the SCHEDULE section.
