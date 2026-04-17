### RPTSOL -- Define SOLUTION Section Reporting

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the data in the SOLUTION section that is to be printed to the output print file in human readable format. The keyword has two distinct forms, the first of which consists of the keyword followed by a series of integers on the next line indicating the data to be printed (see the first example). This is the original formal in the commercial simulator and was subsequently superseded by the second format. The second format consists of the keyword followed by a series of character strings that indicate the data to be printed. In most cases the character string is the keyword used to load the data in the OPM Flow input deck, for example PVDG for the dry gas PVT tables. Its is anticipated that OPM Flow will eventually support the functionality of the second format only, the first format although recognized will be completely ignored.

OPM Flow provides only limited supported for this keyword and will ignore the unsupported options because they have no effect on the results.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | DENO | Print the oil reservoir density array | N/A |
| 2 | EQUIL | Print the equilibration report. | N/A |
| 3 | FIP | Print the fluid in-place report. The parameter is assigned a value, OPTION, using the form FIP=OPTION, where OPTION is an integer variable set to:<br>1)  OPTION = 1 then the report is for the field only.<br>2)  OPTION = 2 then in addition to the field report, a report is produced for each FIPNUM region, as defined by the FIPNUM keyword in the REGIONS section. Note the commercial simulator also prints the flows to other regions as well as the flows from the wells. This additional reporting option has not been implemented in OPM Flow.<br>3)  OPTION = 3 then in addition to the above, a balance report is also produced for fluid in-place regions defined by the FIP keyword in the REGIONS section. | FIP=2 |
| 4 | FIPRESV | Print the reservoir volumes in-place report. | N/A |
| 5 | WELSPECS | WELSPECS switches on reporting of the well connections, wells and groups at each report time step. There are numerous reports associated with this option.<br>Unlike the other reporting parameters that produce a report for each reporting time step, the WELSPECS report option only produces a report if an associated keyword has been activated at the current reporting time step.<br>For example, if the reporting time steps are January, February, and March 2020, and the RPTSCHED WELSPECS option is activated in January, with wells OP01 and OP02 being declared via the WELSPECS and COMPDAT keywords, then a report will be printed for January for these two wells. If there are no further well activations until March, with well OP03 being declared, then there will be no report for February, and only well OP03 will reported at the March reporting time step. | N/A |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 10.3.80.1: RPTSOL Keyword Description

#### Examples

The first example shows the original format of this keyword; although the keyword and format are recognized by OPM Flow, the format is ignored and is unlikely to be implemented in in the simulator.

\--

\-- DEFINE SOLUTION SECTION REPORT OPTION (ORIGINAL FORMAT)

--

RPTSOL

1 2\*0 1 3\*1 /

The next example shows the second format of the keyword which may be supported in a future release of OPM Flow.

\--

\-- DEFINE SOLUTION SECTION REPORT OPTIONS

\--

RPTSOL

FIP=2 FIPRESV RESTART=3 /
