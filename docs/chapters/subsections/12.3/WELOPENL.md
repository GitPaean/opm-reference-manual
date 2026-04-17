### WELOPENL -- Define Well and Well Connections Flowing Status (LGR)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WELOPENL keyword defines the status of wells and well connection in Local Grid Refinement Grids ("LGR") and is used to open and shut previously defined well and well connections without having to re-specify all the data on the well control keywords: WCONPROD, WCONHIST, WCONINJE, or WCONINJH keywords. Note that the well must still be initially be fully defined using the WCONPROD or WCONINJE keywords. All the aforementioned keywords are described in the SCHEDULE section

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well and well connection status data is being defined.<br>Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | LGRNAME | A character string of up to eight characters in length that defines the LGR name for which the well LGR connection data are being defined.<br>Note that the well name (LGRNAME) must have been declared previously using the WELSPECL keyword in the SCHEDULE section, otherwise an error may occur.<br>If defaulted with 1\* the LGR on the WELSPECL keyword will be utilized. | Defined |
| 3 | STATUS | A character string of length four that defines the well and a well's connections' operational status, STATUS should be set to one of the following character strings:<br>1)  OPEN: the connections are open to flow.<br>2)  SHUT: the connections are closed to flow (shut-in).<br>3)  AUTO: the connection are initially closed, but may be opened automatically if an economic limit is violated. | OPEN |
| 4 | I | An integer less than or equal to NX that defines the connection location in the I-direction. | 1\* |
| 5 | J | An integer less than or equal to NY that defines the connection location in the J-direction. | 1\* |
| 6 | K | An integer less than or equal to NZ that defines the connection location in the K-direction. | 1\* |
| 7 | K1 | An integer less than or equal to NZ that defines the UPPER completion location in the K-direction.<br>Connections are lumped into completions via the COMPLUMP keyword, and K1 refers to the first completion number, as defined by the COMPLUMP keyword, and all the connections contained within the K1 completion. | 1\* |
| 8 | K2 | An integer less than or equal to NZ that defines the LOWER completion location in the K-direction.<br>Connections are lumped into completions via the COMPLUMP keyword, and K2 refers to the last completion number, as defined by the COMPLUMP keyword, and all the connections contained within the K2 completion. | 1\* |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.88: WELOPENL Keyword Description

If variables I, J K, K1 and K2 are all set to a negative number or defaulted with 1\* then STATUS is applied to the well and the well connection remain unchanged.

If variables I, J K, K1 and K2 are all set to zero or a positive value then STATUS is applied to the defined connections and the well status remains unchanged. The defined connections are those values with the I, J, K specified locations and connections within the completion number range specified by K1 and K2.

See also the COMPDAT keyword to define a well's connections, the COMPLUMP keyword to group well connections into well completions, the WCONPROD and WCONINJE keywords to define a well's production and injections targets and constraints. All the aforementioned keywords are described in the SCHEDULE section.

#### Example

The following example shows the use of the COMPLMPL keyword to group the well connections into well completions for well OP01 and then use the WELOPEN keyword to open the well and the well connections.

\--

\-- ASSIGN WELL LGR CONNECTIONS TO COMPLETIONS

\--

\-- WELL LGR \-\--LOCATION\-\-- COMPL

\-- NAME NAME II JJ K1 K2 NO.

COMPLMPL

OP01 LGR1 26 58 1 3 1 /

OP01 LGR1 26 58 4 10 2 /

OP01 LGR1 26 58 11 12 3 /

/

\--

\-- WELL PRODUCTION STATUS FOR LGR WELLS

\--

\-- WELL LGR WELL \--LOCATION\-- COMPLETION

\-- NAME NAME STAT I J K FIRST LAST

WELOPENL

OP01 LGR1 OPEN /

OP01 LGR1 OPEN 0 0 0 1 2 /

OP01 LGR2 SHUT 0 0 0 3 3 /

/

The first record of the WELOPENL keyword changes the well status from shut (as per the WCONPROD keyword) to open, in case it has been shut-in. Then well completion number one and two are opened (connections 1 to 10), and completion number three shut-in (connections 11 to 12).
