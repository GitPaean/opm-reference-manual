### GRIDFILE -- Set the Grid File Output Options

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword controls the output of a standard GRID or extended GRID file, as well as the extensible EGRID file for post-processing applications. The extended and extensible GRID formats are comparable; however, the extensible GRID format is more compact and is the only format supported by OPM Flow.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | NGRID | A positive integer that controls the output of the GRID geometry file:<br>1)  \- for no GRID file to be written out.<br>2)  \- for the standard GRID file to be written out.<br>3)  \- for the extended GRID file to be written out.<br>Only the default value of zero is supported. | 0 |
| 2 | NEGRID | A positive integer that controls the output of the EGRID geometry file:<br>1)  \- for no extensible GRID file to be written out.<br>2)  \- for the extensible GRID file to be written out.<br>Only the default value of one is supported. | 1 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 6.41: GRIDFILE Keyword Description

#### Example

\--

\-- GRID FILE OUTPUT OPTIONS

\-- GRID EGRID

\-- OPTN OPTN

GRIDFILE

0 1 /

The above example defines that no GRID file will be written out and that the extensible GRID (that is the EGRID geometry format) file will be produced. This is the only configuration that OPM Flow supports
