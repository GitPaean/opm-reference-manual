### INCLUDE -- Load Another Data File at the Current Position

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The INCLUDE keyword informs OPM Flow to continue reading input data from the specified INCLUDE file. When the end of the INCLUDE file is reached, or the ENDINC keyword is encountered in the included file, input data is read from the next keyword in the current file. Although INCLUDE files can be nested, that is INCLUDE files within INCLUDE files etc., in practice this should be avoided due to the complexity of tracking the files.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | FILENAME | A character string enclosed in quotes that defines a file to read in and be processed by OPM Flow. | None |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 4.4: INCLUDE Keyword Description

#### Examples

The first example shown below loads the grid file from the same directory as the data file.

\--

\-- LOAD INCLUDE FILE

\--

INCLUDE

\'NOR-OPM-A00-GRID.inc\' /

The next example loads the same file one directory above from where the data file is located.

\--

\-- LOAD INCLUDE FILE

\--

INCLUDE

\'../NOR-OPM-A00-FAULTS.inc\' /

The final example loads the same file from a separate include directory found in the parent directory relative to where the data file is located.

\--

\-- LOAD INCLUDE FILE

\--

INCLUDE

\'../INCLUDE/NOR-OPM-A00-FAULTS.inc\' /
