### CSKIN -- Re-Define Well Connection Skin Factors

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword, [CSKIN](#__RefHeading___Toc263614_1539708736), is used to re-define a well's connection skin factors and as such will result in the well's connection transmissibility factors being updated accordingly. The well connections must already be defined using the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section before this keyword can be used.

+-----------------------------------------------------------------------------------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 1                                                                                     | > WELNAME       | > A character string of up to eight characters in length that defines the well name for which the well connection skin is being re-defined.                                                                                            | > None |
|                                                                                         |                 |                                                                                                                                                                                                                                        |        |
|                                                                                         |                 | > Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. |        |
+-----------------------------------------------------------------------------------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 2                                                                                     | > I             | > A positive integer greater than or equal to one and less than or equal to NX that defines the connection location in the I-direction.                                                                                                | > 0    |
|                                                                                         |                 |                                                                                                                                                                                                                                        |        |
|                                                                                         |                 | > If set to zero or defaulted with 1\* then connections in any I-direction location will be modified.                                                                                                                                  |        |
+-----------------------------------------------------------------------------------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 3                                                                                     | > J             | > A positive integer greater than or equal to one and less than or equal to NY that defines the connection location in the J-direction.                                                                                                | > 0    |
|                                                                                         |                 |                                                                                                                                                                                                                                        |        |
|                                                                                         |                 | > If set to zero or defaulted with 1\* then connections in any J-direction location will be modified.                                                                                                                                  |        |
+-----------------------------------------------------------------------------------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 4                                                                                     | > K1            | > A positive integer greater than or equal to one and less than or equal to K2 and NZ that defines the UPPER connection location in the K-direction.                                                                                   | > 0    |
|                                                                                         |                 |                                                                                                                                                                                                                                        |        |
|                                                                                         |                 | > If set to zero or defaulted with 1\* then this will be taken from the top connection of the well.                                                                                                                                    |        |
+-----------------------------------------------------------------------------------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 5                                                                                     | > K2            | > A positive integer greater than or equal to K1 and less than or equal to NZ that defines the LOWER connection location in the K-direction.                                                                                           | > 0    |
|                                                                                         |                 |                                                                                                                                                                                                                                        |        |
|                                                                                         |                 | > If set to zero or defaulted with 1\* then this will be taken from the bottom connection of the well.                                                                                                                                 |        |
+-----------------------------------------------------------------------------------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 6                                                                                     | > SKIN          | > A real value that defines the connections' dimensionless skin factors.                                                                                                                                                               | > 0.0  |
+-----------------------------------------------------------------------------------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > dimensionless                                                                         | > dimensionless | > dimensionless                                                                                                                                                                                                                        |        |
+-----------------------------------------------------------------------------------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > Notes:                                                                                |                 |                                                                                                                                                                                                                                        |        |
|                                                                                         |                 |                                                                                                                                                                                                                                        |        |
| 1)  Each record is terminated by a "/" and the keyword should be terminated by a "/".   |                 |                                                                                                                                                                                                                                        |        |
+-----------------------------------------------------------------------------------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+

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
