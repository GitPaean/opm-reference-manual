### COMPORD -- Define Well Connection Ordering

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The COMPORD keyword defines how the well connection data entered on the COMPDAT keyword in the SCHEDULE section are to be ordered for a well.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well connection data are being defined.<br>Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | COMPORD | A character string that defines the method for ordering the well connections given on the COMPDAT keyword, and should be set to DEPTH, INPUT, or TRACK.<br>1)  DEPTH: The connections are ordered by a connection's true vertical depth from the shallowest to the deepest. If multiple connections are at the same depth then these connections are sub ordered by the sequence they were entered on the COMPDAT keyword.<br>2)  INPUT: This option results in the connections being ordered in the same sequence as entered via the COMPDAT keyword. In this case the connections should be declared in the correct sequence, starting with the connection nearest the well head and then working along the wellbore towards the bottom or toe of the well.<br>3)  TRACK: This option enables OPM Flow to trace the well connections through the grid to obtain the correct order for the connections. If the supplied COMPDAT indicates the well is vertical (via the DIRECT variable being equal to Z on the COMPDAT keyword) then the DEPTH option will be applied instead.<br>All options are now *supported by OPM Flow*. | TRACK |
| Notes:<br>1)  The keyword is followed by any number of records.<br>2)  Each record is terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.15: COMPORD Keyword Description

See also the COMPDAT keyword in the SCHEDULE section.

#### Example

The following example defines the connections for two vertical oil wells using the COMPDAT keyword and the COMPORD to defined the connection ordering for the wells.

\--

\-- WELL CONNECTION DATA

\--

\-- WELL \-\-- LOCATION \-\-- OPEN SAT CONN WELL KH SKIN D DIR

\-- NAME II JJ K1 K2 SHUT TAB FACT DIA FACT FACT FACT PEN

COMPDAT

OP01 1\* 1\* 20 56 OPEN 1\* 1\* 0.708 1\* 0.0 1\* \'Z\' /

OP01 1\* 1\* 75 100 SHUT 1\* 1\* 0.708 1\* 0.0 1\* \'Z\' /

OP02 35 96 75 100 OPEN 1\* 1\* 0.708 1\* 0.0 1\* \'Z\' /

\--

\-- DEFINE WELL CONNECTION ORDERING

\--

\-- WELL COMPL

\-- NAME ORDER

COMPORD

OP01 DEPTH /

OP02 DEPTH /

/

The DEPTH option has been chosen because both wells are vertical. Also one could use the following format instead for the COMPORD:

\--

\-- DEFINE WELL CONNECTION ORDERING

\--

\-- WELL COMPL

\-- NAME ORDER

COMPORD

\* DEPTH /

/

as both wells should utilize the DEPTH option. This version would set all wells in the model to DEPTH connection ordering.
