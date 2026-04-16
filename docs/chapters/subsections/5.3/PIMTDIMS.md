### PIMTDIMS -- Define Well Productivity Scaling Table Dimensions

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[PIMTDIMS](#__RefHeading___Toc31215_1640804870) keyword defines the maximum number of [PIMULTAB](#__RefHeading___Toc121637_2412586160) tables and the maximum number of entries (or rows) per [PIMULTAB](#__RefHeading___Toc121637_2412586160) table. The [PIMULTAB](#__RefHeading___Toc121637_2412586160) keyword is used to define a well's productivity index factor as a function of a well's producing water cut.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | NTPIMT | A positive integer value that defines the maximum number of [PIMULTAB](#__RefHeading___Toc121637_2412586160) keywords defined in the input deck. | 0 |
| 2 | NRPIMT | A positive integer value defining the maximum number of entries (rows) in the [PIMULTAB](#__RefHeading___Toc121637_2412586160) keyword. | 0 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.35: PIMTDIMS Keyword Description

#### Example

\--

\-- MAX MAX

\-- TABLES ENTRIES

PIMTDIMS

1 51 /

The above example defines that there is one [PIMULTAB](#__RefHeading___Toc121637_2412586160) table with a maximum number of 51 rows.
