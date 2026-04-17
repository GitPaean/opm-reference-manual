### RPTREGS -- Define REGIONS Section Reporting

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the data in the REGIONS section that is to be printed to the output print file in human readable format. The keyword has two distinct forms, the first of which consists of the keyword followed by a series of integers on the next line indicating the data to be printed (see the first example). This is the original formal in the commercial simulator and was subsequently superseded by the second format. The second format consists of the keyword followed by a series of character strings that indicate the data to be printed. In most cases the character string is the keyword used to load the data in the OPM Flow input deck, for example FIPNUM for the fluid in-place array. Its is anticipated that OPM Flow will eventually support the functionality of the second format only, the first format although recognized will be completely ignored.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | EQLNUM | Print the equilibration region array. | N/A |
| 2 | FIPNUM | Print the fluid in-place array. | N/A |
| 3 | PVTNUM | Print the PVT table assignment array. | N/A |
| 4 | SATNUM | Print the saturation function (relative permeability) assignment array. | N/A |
| .... |  | .... | N/A |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 9.20: RPTREGS Keyword Description

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

#### Examples

The first example shows the original format of this keyword; although the keyword and format are recognized by OPM Flow, the format is ignored and is unlikely to be implemented in in the simulator.

\--

\-- DEFINE REGIONS SECTION REPORT OPTION (ORIGINAL FORMAT)

--

RPTREGS

1 2\*0 1 3\*1 /

The next example shows the second format of the keyword which may be supported in a future release of OPM Flow.

\-- DEFINE REGIONS SECTION REPORT OPTIONS

\--

RPTREGS

FIPMUM EQLNUM PVTNUM SATNUM /
