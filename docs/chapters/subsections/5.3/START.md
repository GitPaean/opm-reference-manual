### START -- Simulation Start Date

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword sets the start date for the simulation switches. If the [DATES](#__RefHeading___Toc117621_2179381650) keyword is to be used during the simulation, then a start date should be entered.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | DAY | A positive integer that defines the day of the month, the value should be greater than or equal to one and less than or equal to 31. | None |
| 2 | MONTH | Character string for the month and should be one of the following \'JAN\', \'FEB\', \'MAR\', \'APR\', \'MAY\', \'JUN\', \'JUL\' (or \'JLY\'), \'AUG\', \'SEP\', \'OCT\', \'NOV\', or \'DEC\' | None |
| 3 | YEAR | A positive four digit integer value of the start year, which must be specified fully by four digits, that is 1986. | None |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

*Table 5.43: START Keyword Description*
#### Example

\--

\-- DEFINE THE START DATE FOR THE RUN

\--

START

01 \'JAN\' 2014 /

The above example sets the start date for the run to be January 1, 2014.
