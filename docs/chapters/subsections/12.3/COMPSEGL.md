### COMPSEGL -- Define Well Connections for Multi-Segment Wells in a LGR

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The COMSEGSL keyword defines how a multi-segment well is connected to the reservoir by defining or modifying existing well connections in an LGR. Note that well must have been previously define by the WELSPECL keyword in the SCHEDULE section and the well connections must have been previously defined via the COMPDATL keyword in the SCHEDULE section. The COMPSEGL keyword should be repeated for each multi-segment well in the model.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1-1 | WELNAME | A character string of up to eight characters in length that defines the well name for which a multi-segment well is being defined.<br>Note that the well name (WELNAME) must have been declared previously using the WELSPECL keyword in the SCHEDULE section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 1-2 | / | Record terminated by a "/" | Not Applicable |
| 2-1 | LGRNAME | A character string of up to eight characters in length that defines the name of the local grid refinement for which the well is assigned to. | None |
| 2-2 | I | A positive integer greater than or equal to one and less than or equal to NX that defines the connection location in the I-direction. | None |
| 2-3 | J | A positive integer greater than or equal to zero and less than or equal to NY that defines the connection location in the J-direction. | None |
| 2-4 | K | A positive integer greater than or equal to zero and less than or equal to NZ that defines the connection location in the K-direction. | None |
| 2-5 | IBRANCH | A positive integer greater than or equal to one and less than or equal to MXBRAN on WSEGDIMS keyword in the RUNSPEC section that defines the branch number of the defined I, J and K connection. | None |
| 2.6 | DEPTH1 | DEPTH1 is a real positive value that defines the length of the tubing from the tubing head or wellhead at the surface to the *start *of the connection in the I, J, K cell. | None |
| feet | m | cm |  |
| 2-7 | DEPTH2 | DEPTH2 is a real positive value that defines the length of the tubing from the tubing head or wellhead at the surface to the end of the connection in the I, J, K cell. |  |
| feet | m | cm | None |
| 2-8 | DIRECT | A one letter character string that defines the orientation of the connections and should be set to either X, Y, or Z. The direction of connections also determines the length of the connection<br>The default value is for a vertical connection, that is DIRECT is defaulted to Z. | Z |
| 2-9 | IEND | IEND is positive or negative integer, that is not equal to zero that is set to one of the following:<br>1)  a value between -NX and +NX that is not equal to zero that defines the last connection location in the I-direction,<br>2)  a value between -NY and +NY that is not equal to zero that defines the last connection location in the J-direction, or<br>3)  a value between -NZ and +NZ that is not equal to zero that defines the last connection location in the K-direction,<br>that defines the end of the range of the connections depending on the value of DIRECT.<br>For example, if DIRECT is equal to Y or J then the IEND will be associated with the J-direction. The value may be positive or negative but must be calculated to remain within the grid. For example for NY is set 100 on the DIMENS keyword in the RUNSPEC section and J on this record set to 50, then IEND most range between -49 to +50.<br>Currently this option is not supported by OPM Flow. | None |
| 2-10 | DEPTH3 | DEPTH3 is a real positive value that defines the datum depth for this set of connection, normally taken as the mid-point of the perforations associated with this set of connections.<br>Currently this option is not supported by OPM Flow. | None |
| feet | m | cm |  |
| 2-11 | LENGTH | LENGTH is a real positive value that defines the length of the well for this set of completions that is used in thermal calculations..<br>Currently this option is not supported by OPM Flow. | None |
| feet | m | cm |  |
| 2-12 | ISEG | A real positive values equal to or greater than zero that defines the coordinate in the x-direction of the nodal point of this segment that is used for display purposes only.<br>Currently this option is not supported by OPM Flow. | None |
| feet | m | cm |  |
| 2-13 | / | Record terminated by a "/" | Not Applicable |
| Notes:<br>1)  Each multi-segment wells must be defined by a separate COMPSEGL keyword that consists of two records, with entries 1-1 to 1-2 representing record one items and 2-1 to 2-13 representing record number two items in the "No." column in this table.<br>2)  Record number two of the keyword, items 2-1 to 2-13 is followed by up to MXCONS records as declared on the WSEGDIMS keyword in the RUNSPEC section.<br>3)  Each of the records are terminated by a "/" and is explicitly shown in the above rows and the keyword should be terminated by a "/". |  |  |  |

Table 12.16: COMPSEGL Keyword Description

The total number of wells and completions should be defined via the WELLSDIMS keyword and the number of multi-segment wells and completions should be declared on the WSEGDIMS keyword, both keywords are in the RUNSPEC section.

See also the WELSPECL keyword to define wells in an LGR, the COMPDATL keyword to define the well connections for both ordinary wells and multi-segment wells with an LGR, and the COMPSEGS keyword to define a multi-segment connections in the global grid. All the aforementioned keywords are described in the SCHEDULE section.

#### Example

The following example defines the completions for two oil producing segment oil wells (OP01 and OP02) using the COMPSEGS keywords.

\-- COMPLETION SEGMENT SPECIFICATION DATA

\--

\-- WELL

\-- NAME

COMPSEGS

OP01 /

\-- LGR \--LOCATION\-- BRAN TUBING NODAL DIR LOC MID COMP ISEG

\-- NAME II JJ K1 NO LENGTH DEPTH PEN I,J,K PERFS LENGTH

LGR01 10 10 1 1 2512.5 2525.0 /

LGR01 10 10 2 1 2525.0 2550.0 /

LGR01 10 10 3 1 2550.0 2575.0 /

LGR01 10 10 4 1 2575.0 2600.0 /

LGR01 10 10 5 1 2600.0 2625.0 /

LGR01 10 10 6 1 2625.0 2650.0 /

LGR01 9 10 2 2 2637.5 2837.5 /

LGR01 8 10 2 2 2837.5 3037.5 /

LGR01 7 10 2 2 3037.5 3237.5 /

LGR01 6 10 2 2 3237.5 3437.5 /

LGR01 5 10 2 2 3437.5 3637.5 /

/

Note that the COMPDATL keyword in the SCHEDULE section must also be defines for this well.
