### PMISC -- Define Miscibility versus Pressure Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

PMISC defines the transition between immiscible and miscible displacement as a function of oil pressure tables, for when the MISCIBLE keyword in the RUNSPEC section has be activated. If this keyword is absent from the input deck and MISCIBLE keyword in the RUNSPEC keyword has been activated, then miscibility is independent of the oil phase pressure.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | PRESS | A columnar vector of real monotonically increasing down the column values that defines the oil phase pressure. | None |
| psia | barsa | atma |  |
| 2 | MISC | A columnar vector of real equal or increasing down the column values that defines the corresponding miscibility factor.<br>MISC is a scaling that should lie be zero and one, where zero means no miscibility and one means full miscibility. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by NTMISC tables as declared on the MISCIBLE keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NSMISC rows as declared on the MISCIBLE keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.110: PMISC Keyword Description

#### Example

\--

\-- MISCIBILITY VERSUS PRESSURE TABLES

\--

PMISC

\-- OIL MISCIBILE

\-- PRESS FACTOR

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\-\--

1000.0 0.000

2000.0 0.250

3000.0 1.000

4000.0 1.000 / TABLE NO. 01

\-- OIL MISCIBILE

\-- PRESS FACTOR

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\-\--

1500.0 0.000

2000.0 0.000

2500.0 0.250

3000.0 0.350

3500.0 1.000

4000.0 1.000 / TABLE NO. 02

The above example defines two miscibility versus pressure tables assuming NTMISC equals two and NSMISC is greater than or equal to six on the MISCIBLE keyword in the RUNSPEC section.
