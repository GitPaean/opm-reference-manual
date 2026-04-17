### PIMTDIMS -- Define Well Productivity Scaling Table Dimensions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

PIMTDIMS keyword defines the maximum number of PIMULTAB tables and the maximum number of entries (or rows) per PIMULTAB table. The PIMULTAB keyword is used to define a well's productivity index factor as a function of a well's producing water cut.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | NTPIMT | A positive integer value that defines the maximum number of PIMULTAB keywords defined in the input deck. | 0 |
| 2 | NRPIMT | A positive integer value defining the maximum number of entries (rows) in the PIMULTAB keyword. | 0 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.35: PIMTDIMS Keyword Description

#### Example

\--

\-- MAX MAX

\-- TABLES ENTRIES

PIMTDIMS

1 51 /

The above example defines that there is one PIMULTAB table with a maximum number of 51 rows.
