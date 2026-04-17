### COMPIMB -- Assign Imbibition Saturation Tables to Well Connections

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The COMPIMB keyword assigns imbibition saturation tables to well connections. The COMPDAT keyword in the SCHEDULE section also assigns imbibition saturation tables to connections, but in this case the table number is the same as for the drainage curve. If this is not the required assignment then the COMPIMB keyword can be used to reset the imbibition saturation table number. For this to be effective the COMPIMB keyword must precede the COMPDAT keyword, otherwise it will have no effect.

The COMPIMB keyword should only be used if the hysteresis option has been activated via the HYSTER variable on the SATOPTS keyword in the RUNSPEC section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well connection data is being defined.<br>Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | I | A positive integer greater than or equal to zero and less than or equal to NX that defines the connection location in the I-direction.<br>If set to zero or defaulted with 1\* then all connections in the I-direction that also satisfy J, K1 and K2 criteria are assigned the IMBNUM imbibition table number. | 0 |
| 3 | J | A positive integer greater than or equal to zero and less than or equal to NY that defines the connection location in the J-direction.<br>If set to zero or defaulted with 1\* then all connections in the J-direction that also satisfy I, K1 and K2 criteria are assigned the IMBNUM imbibition table number. | 0 |
| 4 | K1 | A positive integer greater than or equal to one and less than or equal to NZ that defines the UPPER connection location in the K-direction.<br>If set to zero or defaulted with 1\* then the upper most connection in the well is used. | 0 |
| 5 | K2 | A positive integer greater than or equal to K1 and less than or equal to NZ that defines the LOWER connection location in the K-direction.<br>If set to zero or defaulted with 1\* then the lowest most connection in the well is used. | 0 |
| 6 | IMBNUM | An integer greater than or equal to zero and less than NTSFUN as declared on the TABDIMS keyword in the RUNSPEC, that defines the imbibition saturation table number to be used for flow between the reservoir grid block and the well connections.<br>If IMBNUM is set to zero or defaulted with 1\* then the inhibition saturation table allocated to the grid block that the connections are located within is used.<br>If I, J, K1, K2 are all set to zero or defaulted to 1\*, then IMBNUM is allocated to all connections in the well. | 0 |
| Notes:<br>1)  The keyword is followed by up to MXCONS records as declared on the WELLDIMS keyword in the RUNSPEC section.<br>2)  Each record is terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.12: COMPIMB Keyword Description

Multiple grid block connections can be defined on one record for vertical wells by assigning different values to K1 and K2, for deviated and horizontal wells this may not be possible and therefore each grid block connection must be separately defines by setting K1 equal to K2.

See also the COMPDAT keyword in the SCHEDULE section.

#### Example

The following example defines the connections for two vertical oil wells using the COMPDAT keyword and then re-sets the imbibition saturation functions using the COMPIMP keyword.

\--

\-- WELL CONNECTION DATA

\--

\-- WELL \-\-- LOCATION \-\-- OPEN SAT CONN WELL KH SKIN D DIR

\-- NAME II JJ K1 K2 SHUT TAB FACT DIA FACT FACT FACT PEN

COMPDAT

OP01 1\* 1\* 20 56 OPEN 1 1\* 0.708 1\* 0.0 1\* \'Z\' /

OP01 1\* 1\* 75 100 SHUT 2 1\* 0.708 1\* 0.0 1\* \'Z\' /

OP02 35 96 75 100 OPEN 1 1\* 0.708 1\* 0.0 1\* \'Z\' /

\--

\-- ASSIGN IMBIBITION SATURATION TABLES TO CONNECTIONS

\--

\-- WELL \-\--LOCATION\-\-- SAT

\-- NAME II JJ K1 K2 TAB

COMPIMB

OP01 1\* 1\* 20 56 11 /

OP01 1\* 1\* 75 100 12 /

OP02 1\* 1\* 1\* 1\* 11 /

/

Well OP01 has two sets of COMPIMB records to overwrite the imbibition saturation tables, one for connections (14, 13, 20) to (14, 13, 56) resetting the imbibition saturation table number from one to 11 and one for connections (14, 13, 75) to (14, 13, 100) that resets the imbibition table number from 2 to 12. Well OP02 has only one connection from cells (35, 96, 75) to cells (35, 96, 100), so all the default values for I, J, K1, and K2 can be used to set the imbibition table numbers from 2 to 11. Note in all cases the drainage saturation table retains the value as specified by the COMPDAT keyword, that is one, two and one.
