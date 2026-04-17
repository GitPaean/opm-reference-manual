### SGCWMIS -- Miscible Critical Gas versus Water Saturation Functions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

SGCWMIS defines the dependency between the miscible critical gas saturation and the water saturation, for when the MISCIBLE keyword in the RUNSPEC section has been activated. The keyword can only be used with the MISCIBLE option and for when the oil, water and gas phases are active in the model.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SWAT | A columnar vector of real monotonically increasing down the column values starting from zero and terminating atone, that defines the water saturation. | None |
| dimensionless | dimensionless | dimensionless |  |
| 2 | SGCMIS | A columnar vector of real equal or increasing down the column values that are greater than or equal to zero and less than one, that define the corresponding miscible gas critical gas saturation for the corresponding water saturation SWAT. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by NTMISC tables as declared on the MISCIBLE keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NSMISC rows as declared on the MISCIBLE keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.147: SGCWMIS Keyword Description

#### Example

\--

\-- MISCIBLE CRITICAL GAS VERSUS WATER SATURATION TABLE

\--

SGCWMIS

\-- SWAT SGCRMIS

\-- FRAC FRAC

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.0000 0.0000

0.2000 0.0300

1.0000 0.0300 / TABLE NO. 01

\-- SWAT SGCRMIS

\-- FRAC FRAC

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.0000 0.0000

0.3000 0.0500

1.0000 0.0500 / TABLE NO. 02

The above example defines two miscible critical gas saturation versus water saturation tables assuming NTMISC equals two and NSMISC is greater than or equal to three on the MISCIBLE keyword in the RUNSPEC section.
