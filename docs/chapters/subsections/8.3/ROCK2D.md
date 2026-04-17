### ROCK2D -- Pore Volume Compaction versus Pressure and Sw Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The ROCK2D keyword defines rock compressibility pore volume multipliers as a function of pressure and water saturation ("Sw") for when the rock compaction option has been invoked by the ROCKCOMP keyword in the RUNSPEC section. The pressure values are defined on this keyword and the water saturations are declared on the associated ROCKWNOD keyword in the PROPS section

The rock compaction pore volume and transmissibility multipliers, entered via the ROCKTAB, ROCK2D and ROCK2DTR keywords, are applied to the pore pressure, unless the OVERBURD keyword in PROPS section is included in the input deck. When the OVERBURD keyword is present the multipliers are applied to the effective pore volume pressure, that is. If the keyword is not present in the input deck then the overburden pressure is set to zero.

This keyword should only be used if compaction option has been enabled.

| 1 | PRESS | A columnar vector of real monotonically increasing down the column values that defines the corresponding overburden pressure for the subsequent MULT columnar vector. | None |
| --- | --- | --- | --- |
| psia | bars | atm |  |
| 2 | MULT | A columnar vector of real equal or decreasing down the column values that are less than or equal to one, that defines the rock compressibility pore volume multipliers corresponding to PRESS and for each water saturation entry in the ROCKWNOD keyword. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by NTROCC tables as declared on the ROCKCOMP keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NSSFUN rows as declared on the TABDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.126: ROCK2D Keyword Description

See also the OVERBURD, ROCKTAB, ROCK2DTR, and ROCKWNOD keywords in the PROPS section.

#### Example

The following example defines two pore volume compaction tables, assuming NTROCC is equal to two on the ROCKCOMP keyword and NSSFUN is greater than or equal to four on the TABDIMS keyword.

\--

\-- ROCK COMPACTION VERSUS PRESSURE AND SW TABLES

\--

ROCK2D

\-- PRESS PORV FIRST ROCK2D TABLE DATA

\-- PSIA MULTIPLER

\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-\--

0.0 0.850

0.850

0.850

0.085 / P-SW SET TABLE NO. 01

\-- PRESS PORV

\-- PSIA MULTIPLER

\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-\--

1000.0 0.900

0.900

0.900

0.900 / P-SW SET TABLE NO. 01

\-- PRESS PORV

\-- PSIA MULTIPLER

\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-\--

2500.0 0.950

0.950

0.950

0.950 / P-SW SET TABLE NO. 01

\-- PRESS PORV

\-- PSIA MULTIPLER

\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-\--

5000.0 1.000

1.000

1.000

1.000 / P-SW SET TABLE NO. 01

\--

\-- PRESS PORV SECOND ROCK2D TABLE DATA

\-- PSIA MULTIPLER

\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-\--

0.0 0.800

0.800

0.800

0.800 / P-SW SET TABLE NO. 02

\-- PRESS PORV

\-- PSIA MULTIPLER

\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-\--

1000.0 0.880

0.880

0.880

0.880 / P-SW SET TABLE NO. 02

\-- PRESS PORV

\-- PSIA MULTIPLER

\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-\--

2500.0 0.950

0.950

0.950

0.950 / P-SW SET TABLE NO. 02

\-- PRESS PORV

\-- PSIA MULTIPLER

\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-\--

5000.0 1.000

1.000

1.000

1.000 / P-SW SET TABLE NO. 02

Note that there must be exactly NTROCC tables entered for this keyword, otherwise an error will occur.
