### ACTDIMS -- ACTION Keyword Dimensions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The ACTDIMS keyword defines the maximum number of properties associated with the ACTION keyword. The ACTION keyword allows the user to enter computational logic and calculations to the simulation run based on the how the simulation run is proceeding.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | MXACTNS | A positive integer value that defines the maximum number of ACTION keywords defined in the input deck. | 2 |
| 2 | MXLINES | A positive integer value that defines the maximum number of lines in an ACTION statement. | 50 |
| 3 | MXCHARS | A positive integer value that defines the maximum characters in an ACTION statement. | 80 |
| 4 | MXSTATMS | A positive integer value that defines the maximum number of conditional statements in the ACTION statement. | 3 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.3: ACTDIMS Keyword Description

Only the ACTIONX keyword and computational logic have been implemented in OPM Flow.

#### Example

\-- ACTION ACTION ACTION ACTION

\-- MXACTNS MXLINES MXCHARS MXSTATMS

ACTDIMS

2 50 80 3 /

The above example defines the default values for the ACTDIMS keyword.
