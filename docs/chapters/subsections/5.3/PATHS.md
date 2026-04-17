### PATHS -- Define Filename Directory Path Aliases

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

PATHS allows the user to define alias directory filenames to avoid long filenames with the INCLUDE, IMPORT, RESTART or GDFILE keywords. To use the alias with the aforementioned keywords PATHS should be prefixed with the \$ symbol.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | ALIAS | A character string enclosed in quotes defining the alias. | None |
| 2 | DIRC | A character string enclosed in quotes defining the directory filename. | None |
| Notes:<br>1)  Multiple entries must be on separate lines (see the example).<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 5.34: PATHS Keyword Description

#### Examples

\--

\-- PATH PATH

\-- ALIAS DIRECTORY FILENAME

PATHS

\'GRID\' \'/DISK1/NORNE/2017/GRID-INCLUDES\' /

\'SCHD\' \'/DISK1/NORNE/2017/SCHD-INCLUDES\' /

/

The above example defines "GRID" and "SCHD" aliases in the RUNSPEC section than can be used in the GRID and SCHEDULE sections of the input deck. The next example shows how to use the "GRID" alias with the INCLUDE keyword in the GRID section.

\--

\-- LOAD INCLUDE FILES

\--

INCLUDE

\'\$GRID/PORO.INC\' /

INCLUDE

\'\$GRID/PERMX.INC\' /

INCLUDE

\'\$GRID/NTG.INC\' /

Here the porosity, permeability and net-to-gross arrays are loaded in the GRID section using the directory filename aliases declared in the RUNSPEC section.
