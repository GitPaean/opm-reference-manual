### CSKIN -- Re-Define Well Connection Skin Factors

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, CSKIN, is used to re-define a well's connection skin factors and as such will result in the well's connection transmissibility factors being updated accordingly. The well connections must already be defined using the COMPDAT keyword in the SCHEDULE section before this keyword can be used.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well connection skin is being re-defined.<br>Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | I | A positive integer greater than or equal to one and less than or equal to NX that defines the connection location in the I-direction.<br>If set to zero or defaulted with 1\* then connections in any I-direction location will be modified. | 0 |
| 3 | J | A positive integer greater than or equal to one and less than or equal to NY that defines the connection location in the J-direction.<br>If set to zero or defaulted with 1\* then connections in any J-direction location will be modified. | 0 |
| 4 | K1 | A positive integer greater than or equal to one and less than or equal to K2 and NZ that defines the UPPER connection location in the K-direction.<br>If set to zero or defaulted with 1\* then this will be taken from the top connection of the well. | 0 |
| 5 | K2 | A positive integer greater than or equal to K1 and less than or equal to NZ that defines the LOWER connection location in the K-direction.<br>If set to zero or defaulted with 1\* then this will be taken from the bottom connection of the well. | 0 |
| 6 | SKIN | A real value that defines the connections' dimensionless skin factors. | 0.0 |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  Each record is terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.3.43.1: CSKIN Keyword Description

#### Example

The following example re-defines the skin factor for all well OP01 connections in layers 4 to 6.

\--

\-- CONNECTION SKIN DATA

\--

\-- WELL \-\-- LOCATION \-\-- SKIN

\-- NAME II JJ K1 K2 FACT

CSKIN

OP01 1\* 1\* 4 6 2.0 /

/
