### GDFILE -- Load a Grid File

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The GDFILE keyword loads a GRID file that contains the structural data for the grid as a set of topological cuboidal cells, and EGRID files that contain structural and property data. Note OPM Flow only supports reading in EGRID files at this time.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | GRIDFILE | A character string enclosed in quotes that defines the GRID or EGRID file to be read in and be processed by OPM Flow.<br>Again, OPM Flow only supports reading in EGRID files. | None |
| 2 | FMTOPT | A defined character string that defines the format of the GRID or EGRID file to be read and should be set to one of the following:<br>1)  FORMATTED: If the file is formatted as ASCII i.e. a text file, as oppose to a binary file. The option can be abbreviated to just the letter F.<br>2)  UNFORMATTED: If the file is in binary format, note this option can be abbreviated to just the letter U.<br>If the variable FMTOPT is omitted then the default is for binary file input for the commercial simulator; whereas, OPM Flow derives FMTOPT from the file extension (\*.EGRID or \*.FEGRID), making FMTOPT superfluous. | U |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 6.40: GDFILE Keyword Description

See also the GRIDFILE keyword in the GRID section for exporting the GRID and EGRID files from the current simulation run.

#### Examples

The first example shown below loads the NOR-OPM-A00-GRID.EGRID file in binary format from the same directory as the data file.

\--

\-- LOAD A GRID FILE

\--

GDFILE

\'NOR-OPM-A00-GRID.EGRID\' /

The next example loads the same EGRID file one directory above from where the data file is located.

\--

\-- LOAD a GRID FILE

\--

GDFILE

\'../NOR-OPM-A00-GRID.EGRID\' /
