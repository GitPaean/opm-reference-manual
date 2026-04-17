### PLYVISC -- Define Polymer Viscosity Scaling Factors

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

PLYSVISC defines the polymer viscosity scaling factors used to determine the relationship of pure water viscosity with respect to increasing polymer concentration within a grid block. The polymer option must be activated by the POLYMER keyword in the RUNSPEC section in order to use this keyword.

The BRINE option in the RUNSPEC should be deactivated if this keyword is to be used.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | POLCON | A columnar vector of real monotonically increasing down the column values that defines the polymer concentration in the solution surrounding the rock.<br>The first entry should be zero to define a no polymer concentration. | None |
| lb/stb | kg/sm^3^ | gm/scc |  |
| 2 | VISFAC | A columnar vector of real increasing or equal values that defines a factor that scales the effective viscosity of the solution for the given POLCON entry.<br>Normally VISFAC value for the first row in the table should be one. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by NTPVT tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NPPVT rows as declared on the TABDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.108: PLYVISC Keyword Description

#### Example

\--

\-- POLYMER VISCOSITY SCALING FACTOR TABLES

\--

PLYVISC

\-- POLYMER VISCOSITY

\-- POLCON VISFAC

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-\--

0.0000 1.000

0.0002 10.000

0.0004 20.000

0.0008 40.000 / TABLE NO. 01

\-- POLYMER VISCOSITY

\-- POLCON VISFAC

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-\--

0.0000 1.000

0.0003 10.000

0.0005 20.000

0.0007 40.000

0.0009 45.000

0.0011 55.000 / TABLE NO. 02

The example defines two polymer viscosity scaling factor tables, based on the NTPVT variable on the TABDIMS keyword in the RUNSPEC section being equal to two and NPPVT variable on the same keyword being greater than or equal to six.
