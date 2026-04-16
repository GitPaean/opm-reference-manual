### INCLUDE -- Load Another Data File at the Current Position

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [INCLUDE](#__RefHeading___Toc55749_2479612490) keyword informs OPM Flow to continue reading input data from the specified [INCLUDE](#__RefHeading___Toc55749_2479612490) file. When the end of the [INCLUDE](#__RefHeading___Toc55749_2479612490) file is reached, or the [ENDINC](#__RefHeading___Toc51671_2479612490) keyword is encountered in the included file, input data is read from the next keyword in the current file. Although [INCLUDE](#__RefHeading___Toc55749_2479612490) files can be nested, that is [INCLUDE](#__RefHeading___Toc55749_2479612490) files within [INCLUDE](#__RefHeading___Toc55749_2479612490) files etc., in practice this should be avoided due to the complexity of tracking the files.

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
