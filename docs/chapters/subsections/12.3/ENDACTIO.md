### ENDACTIO -- End the Definition of ACTION Commands

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [ENDACTIO](#__RefHeading___Toc109407_332691817) keyword defines the end of a series of conditions that invoke run time processing of the [ACTION](#__RefHeading___Toc148342_63720426) series of keywords, namely: [ACTION](#__RefHeading___Toc148342_63720426), [ACTIONG](#__RefHeading___Toc152219_2992482751), [ACTIONR](#__RefHeading___Toc152221_2992482751), [ACTIONS](#__RefHeading___Toc152223_2992482751), [ACTIONW](#__RefHeading___Toc152225_2992482751) and [ACTIONX](#__RefHeading___Toc152227_2992482751). Only the [ACTIONX](#__RefHeading___Toc152227_2992482751) keyword is implemented in OPM Flow as this keyword implements the [ACTION](#__RefHeading___Toc148342_63720426), [ACTIONG](#__RefHeading___Toc152219_2992482751), [ACTIONR](#__RefHeading___Toc152221_2992482751), [ACTIONS](#__RefHeading___Toc152223_2992482751), [ACTIONW](#__RefHeading___Toc152225_2992482751) functionality with greater flexibility. See the [ACTIONX](#__RefHeading___Toc152227_2992482751) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section for a full description of the [ACTION](#__RefHeading___Toc148342_63720426) facility.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

The example shows the use of the [ACTIONX](#__RefHeading___Toc152227_2992482751) and [ENDACTIO](#__RefHeading___Toc109407_332691817) keywords to test if the field's gas production rate is less than 600 MMscf/d after 2020 and to open up additional wells if this occurs.

\--

\-- START OF ACTIONX FIELD PHASE-2 DEVELOPMENT DEFINITION

\--

ACTIONX

PHASE2 1 /

GGPR \'FIELD\' \< 600E3 AND /

YEAR \> 2020 /

/

\-- WELL PRODUCTION STATUS

\--

\-- WELL WELL \--LOCATION\-- COMPLETION

\-- NAME STAT I J K FIRST LAST

WELOPEN

GP10 OPEN /

GP11 OPEN /

/

\--

\-- END OF ACTIONX FIELD PHASE-2 DEVELOPMENT DEFINITION

\--

ENDACTIO
