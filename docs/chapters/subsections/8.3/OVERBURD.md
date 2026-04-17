### OVERBURD -- Define Rock Overburden Pressure versus Depth Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The OVERBURD keyword defines the overburden pressures versus depth relationship to be applied for when the rock compaction option has been invoked by the ROCKCOMP keyword in the RUNSPEC section.

The rock compaction pore volume and transmissibility multipliers, entered via the ROCKTAB, ROCK2D and ROCK2DTR keywords, are applied to the pore pressure, unless the OVERBURD keyword is included in the input deck. When the OVERBURD keyword is present the multipliers are applied to the effective pore volume pressure, that is . If the keyword is not present in the input deck then the overburden pressure is set to zero.

This keyword should only be used if compaction option has been enabled.

| 1 | DEPTH | A columnar vector of real monotonically increasing down the column values that defines the depth for corresponding overburden pressure parameter PRESS. | None |
| --- | --- | --- | --- |
| feet | m | cm |  |
| 2 | PRESS | A columnar vector of real monotonically increasing down the column values that defines the corresponding overburden pressure for the given DEPTH. | None |
| psia | bars | atm |  |
| Notes:<br>1)  The keyword is followed by NTROCC tables as declared on the ROCKCOMP keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NPPVT rows as declared on the TABDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.94: OVERBURD Keyword Description

See also the ROCKTAB, ROCK2D, ROCK2DTR, and ROCKWNOD keywords in the PROPS section.

#### Examples

The example below defines three overburden tables, assuming NTROCC is equal to three on the ROCKCOMP keyword and NPPVT is greater than or equal to four on the TABDIMS keyword.

\--

\-- OVERBURDEN PRESSURE VERSUS DEPTH TABLES

\--

OVERBURD

\-- DEPTH OVERBURDEN

\-- FEET PRESSURE

\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-\--

1000.0 300.000

2000.0 600.000

3000.0 900.000

4000.0 1200.000 / TABLE N0. 01

\-- DEPTH OVERBURDEN

\-- FEET PRESSURE

\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-\--

1000.0 200.000

2000.0 400.000

3000.0 800.000

4000.0 1000.000 / TABLE N0. 02

\-- DEPTH OVERBURDEN

\-- FEET PRESSURE

\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-\--

1000.0 400.000

2000.0 800.000

3000.0 1100.000

4000.0 1500.000 / TABLE N0. 03

Note that there must be exactly NTROCC tables entered for this keyword, otherwise an error will occur.

\--

\-- ROCK COMPACTION TABLES

\--

ROCKTAB

\-- PRESS PORV TX(YZ)

\-- MULT MULT

\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\--

1000.0 0.9600 0.9650

1500.0 0.9800 0.9850

3000.0 0.9900 0.9950

4500.0 1.0000 1.0000

4750.0 1.0100 1.0100 / TABLE NO. 01

\-- PRESS PORV TX(YZ)

\-- MULT MULT

\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\--

1000.0 0.9600 0.9650

1500.0 0.9800 0.9850

3000.0 0.9900 0.9950

4500.0 1.0000 1.0000

4750.0 1.0100 1.0100 / TABLE NO. 02

\-- PRESS PORV TX(YZ)

\-- MULT MULT

\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\--

1000.0 0.9600 0.9650

2000.0 0.9800 0.9850

3000.0 0.9900 0.9950

4000.0 1.0100 1.0100 / TABLE NO. 03

Here ROCKTAB tables one and two are identical.
