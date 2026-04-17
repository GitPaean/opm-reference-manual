### RPTSCHED -- Define SCHEDULE Section Reporting

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the data in the SCHEDULE section that is to be printed to the output print file in human readable format. The keyword has two distinct forms, the first of which consists of the keyword followed by a series of integers on the next line indicating the data to be printed (see the first example). This is the original format in the commercial simulator and was subsequently superseded by the second format. The second format consists of the keyword followed by a series of character strings that indicate the data to be printed. In most cases the character string is the keyword used to define the data in the OPM Flow input deck, for example WELSPECS to defined the basic well definitions.

| 1 | FIP | Print the fluid in-place report. The parameter is assigned a value, OPTION, using the form FIP = OPTION, where OPTION is an integer variable set to:<br>1)  OPTION = 1 then the report is for the field only.<br>2)  OPTION = 2 then in addition to the field report, a report is produced for each FIPNUM region, as defined by the FIPNUM keyword in the REGIONS section. Note the commercial simulator also prints the flows to other regions as well as the flows from the wells. This additional reporting option has not been implemented in OPM Flow.<br>3)  OPTION = 3 then in addition to the above, a balance report is also produced for fluid in-place regions defined by the FIP keyword in the REGIONS section. | FIP=2 |
| --- | --- | --- | --- |
| 2 | FIPRESV | Print the reservoir volumes in-place report. | None |
| 3 | NOTHING | Switches off all printed reports in the SCHEDULE section. | N/A |
| 4 | SALT | Print grid block salt concentration values. Note this is an OPM Flow specific keyword. | N/A |
| 5 | RESTART | RESTART defines the frequency at which the restart data for restarting a run is written to the RESTART file. The parameter is assigned a value, OPTION, using the form RESTART = OPTION, where OPTION is an integer variable set to:<br>1)  OPTION = 1 then the restart files are written at every report time, but only the last one in the run is kept. This minimizes the restart file size but only the final results are stored, limiting the visualization in OPM ResInsight.<br>2)  OPTION = 2 then the phase inter-blocks are written to the restart files, in addition to the standard data.<br>3)  OPTION = 3 then the fluid in-place and phase potentials are also written to the restart file.<br>4)  OPTION = 6 then the restart files are written at every time step.<br>See the RPTRST keyword in the SOLUTION section for a more flexible way to write out restart files. |  |
| 6 | WELLS | The WELLS option turns on production and injection rate and cumulative volume reporting for produced and injected fluids. The parameter has several levels of reporting details set by the assigned OPTION value, using the form WELLS = OPTION, where OPTION is an integer variable set to:<br>1)  OPTION = 1 report volumes at the well level.<br>2)  OPTION = 2 report volumes at the well and the well connection levels.<br>3)  OPTION = 3 report volumes for layer totals.<br>4)  OPTION = 4 report volumes for layer totals and for wells.<br>5)  OPTION = 5 report volumes for layer totals and for wells and well connections.<br>Only OPTION equal to one is supported by OPM Flow. | WELLS=1 |
| 7 | WELSPECS | WELSPECS switches on reporting of the well connections, wells and groups at each report time step. There are numerous reports associated with this option.<br>Unlike the other reporting parameters that produce a report for each reporting time step, the WELSPECS report option only produces a report if an associated keyword has been activated at the current reporting time step.<br>For example, if the reporting time steps are January, February, and March 2020, and the RPTSCHED WELSPECS option is activated in January, with wells OP01 and OP02 being declared via the WELSPECS and COMPDAT keywords, then a report will be printed for January for these two wells. If there are no further well activations until March, with well OP03 being declared, then there will be no report for February, and only well OP03 will reported at the March reporting time step. |  |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 12.62: RPTSCHED Keyword Description

Development is current progressing on developing reports in a similar format to the commercial simulator and this section will be updated as additional reports are added to OPM Flow's functionality.

An example FIP report is shown in from the Norne field, note only the field and the first two region reports are shown.

illustrates the reservoir volumes in-place report for the first two regions from the Norne field.

The WELLS report consists of several sub-reports depending on the selected option for this report type. and show example Injection and Production sub-reports

The third and final report is the Cumulative Production and Injection sub-report, shown in .

Similarly as for the WELLS report, the WELSPECS report consists of several sub-reports, including the Well Production Control report shown in for the Volve field.

The COMPDAT keyword data is listed on the Well Connection Data sub-report as depicted in for the I-F-5 well. Note that the data is repeated for all connections and for all wells declared at the reporting time step.

For multi-segment wells both the Production Well Control and Well Connection sub-reports are printed as per and , and in addition the equivalent multi-segment well data is printed as well, as shown in and , as shown on the following page.

shows the Multi-Segment Well Segment Structure sub-report for a single multi-segment well, OP01. See the WELSEGS keyword [Example](#anchor-2) in the SCHEDULE section to see how the OP01 well is defined.

And depicts Multi-Segment Well Connection Data sub-report for the same well.

#### Example

The first example shows the original format of this keyword.

\--

\-- DEFINE SCHEDULE SECTION REPORT OPTION (ORIGINAL FORMAT)

\--

RPTSCHED

1 2\*0 1 3\*1 /

The next example shows the second format of the keyword.

\-- ==============================================================================

\--

\-- SCHEDULE SECTION

\--

\-- ==============================================================================

SCHEDULE

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\-- SCHEDULE SECTION - 2000-01-01

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

RPTSCHED

\'WELLS=2\' \'WELSPECS\' \'CPU=2\' \'FIP=2\' /

DATES

1 JAN 2000 /

/

RPTSCHED

\'NOTHING\' /

DATES

1 FEB 2000 /

1 MAR 2000 /

1 APR 2000 /

1 MAY 2000 /

1 JUN 2000 /

1 JLY 2000 /

1 AUG 2000 /

1 SEP 2000 /

1 OCT 2000 /

1 NOV 2000 /

1 DEC 2000 /

/

In the above example monthly reporting time steps have been used with a SCHEDULE section report on the January 1, 2000; after which all reports are switched off for the subsequent reporting time steps.
