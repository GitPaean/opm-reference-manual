### ACTDIMS -- ACTION Keyword Dimensions

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [ACTDIMS](#__RefHeading___Toc4408_421927891) keyword defines the maximum number of properties associated with the [ACTION](#__RefHeading___Toc148342_63720426) keyword. The [ACTION](#__RefHeading___Toc148342_63720426) keyword allows the user to enter computational logic and calculations to the simulation run based on the how the simulation run is proceeding.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | MXACTNS | A positive integer value that defines the maximum number of [ACTION](#__RefHeading___Toc148342_63720426) keywords defined in the input deck. | 2 |
| 2 | MXLINES | A positive integer value that defines the maximum number of lines in an [ACTION](#__RefHeading___Toc148342_63720426) statement. | 50 |
| 3 | MXCHARS | A positive integer value that defines the maximum characters in an [ACTION](#__RefHeading___Toc148342_63720426) statement. | 80 |
| 4 | MXSTATMS | A positive integer value that defines the maximum number of conditional statements in the [ACTION](#__RefHeading___Toc148342_63720426) statement. | 3 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.3: ACTDIMS Keyword Description

Only the [ACTIONX](#__RefHeading___Toc152227_2992482751) keyword and computational logic have been implemented in OPM Flow.

#### Example

\-- ACTION ACTION ACTION ACTION

\-- MXACTNS MXLINES MXCHARS MXSTATMS

ACTDIMS

2 50 80 3 /

The above example defines the default values for the [ACTDIMS](#__RefHeading___Toc4408_421927891) keyword.
