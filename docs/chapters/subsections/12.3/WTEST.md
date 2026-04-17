### WTEST -- Well Testing Criteria for Re-Opening Closed Wells

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WTEST keyword outlines the testing procedures to be applied to wells that are closed for various reasons to see if the wells are capable flowing under the current operating conditions. The keyword can be applied to single wells or groups of wells.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name of the well to be tested.<br>Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | TIME | A real value greater than zero that defines the minimum period of time that must elapse between well tests. The next well test is performed at the beginning of the next time step after the specified period of time has elapsed since the previous well test, for example if TIME is set equal to 365.25 (days), the test is performed approximately every year. | None |
| days | days | hours |  |
| 3 | TEST | A character string of up to five characters in length that defines a list of reasons why a well could have been closed. If a well was closed for one of the specified reasons then the well is tested to see if it can be put back on production. The characters that can be used to define TEST are as follows:<br>1)  P: meaning the well was closed due to a bottom-hole or tubing head pressure limit, or other physical limit then the well is tested to see if it can flow, if it can, then it is put back on production, otherwise it remains closed.<br>2)  E: meaning the well was closed due to a well or a well connection economic constraint then the well is tested to see if it can flow, if it can then it is put back on production, otherwise it remains closed.<br>Here, if the well has at least one connection open then the well is opened.<br>If a well has no open connections, then those connections that have been closed due to an economic limit test (\"ELT\"), are all individually tested and reopened if they meet the ELT criteria as defined by the WECON, CECON and WECONINJ keywords in the SCHEDULE section. And the well is opened if it has at least one open connection. Where the ELT applies to ORAT, GRAT, WCUT, GOR and WGR etc.<br>1)  G: meaning the well was closed due to a group economic constraint, as per the GECON, GECONT, GCONCAL, GCONPRI, GCONPROD, and GCONSALE, keywords in the SCHEDULE section, then the well is tested to see if it can flow, if it can, then it is put back on production, otherwise it remains closed.<br>2)  D: not supported by OPM Flow.<br>3)  C: not supported by OPM Flow.<br>The default value is an empty string " " that switches off testing.<br>Note that only the P, E and G options are currently supported in OPM Flow. | " " |
| 4 | NTIME | A positive integer greater than or equal to zero that define the number of times a well can be tested.<br>The default value of zero means an infinite number of times. | 0 |
| 5 | START | A real positive value that defines the start up time used to prorate the rate at which the well is put back on production. If START is large compared to the time step size, then the well is brought on gradually, if it is less than the time step size, then the well is opened faster. The rate is prorated based on the following:<br>The default value of 0.0 means the well is opened immediately. | 0.0 |
| days | days | hours |  |
| Notes:<br>1)  The keyword is followed by any number of records and each record is terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.127: WTEST Keyword Description

See also the WELSPECS keyword to define a wells shut-in or stop options, WECON for setting a well's economic criteria, GCONPROD and GCONINJE for group controls, and GECON for setting a group's economic criteria. All the aforementioned keywords are described in the SCHEDULE section.

#### Example

The following example defines test criteria for all gas wells ('GP\*') and three oil wells (OP01, OP02, and OP03).

\--

\--

\-- WELL TESTING CRITERIA FOR RE-OPENING CLOSED WELLS

\--

\-- WELL TST TST NO. STRT

\-- NAME INTV TYPE TSTS TIME

\-- \-\-\-- \-\-\-- \-\-\-- \-\-\-- \-\-\--

WTEST

'GP\*' 365.25 P 5 0.0

OP01 30.0 PEG 0 0.0 /

OP02 30.0 PEG 0 0.0 /

OPO3 30.0 PEG 0 0.0 /

/

All the gas wells are test annually if they have been shut-in due to a bottom-hole or tubing head pressure limit, are tested five times after they have been closed, and are opened up immediately. The oil wells are tested every 30 days if they have been closed due to a bottom-hole or tubing head pressure limit, a well economic limit or a group economic limit. All the oil wells are tested an infinite amount of times and are opened up immediately. Note that only the P, E and G options are currently supported in OPM Flow.
