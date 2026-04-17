### ROCKTAB -- Rock Compaction Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The ROCKTAB keyword defines the rock compaction attributes to be applied when the rock compaction option has been invoked by the ROCKCOMP keyword in the RUNSPEC section. ROCKTAB defines pore volume and transmissibility multipliers versus pressure that are used in the compaction calculations. If the RKTRMDIR has been activated in the PROPS section, then the transmissibility multiplier is directional dependent and two additional columns are used to define the y and z direction transmissibility multipliers.

| 1 | PRESS | If the ROCKOPT1 variable has been set to PRESSURE on the ROCKOPTS keyword in the PROPS section, then PRESS should be a columnar vector of real monotonically *increasing* down the column values, that define the reference pressure for which the other parameters correspond to.<br>If ROCKOPT1 has been set to STRESS, then PRESS should be a columnar vector of real monotonically *decreasing* down the column values. | None |
| --- | --- | --- | --- |
| psia | bars | atm |  |
| 2 | PORV | A columnar vector of real positive values that are either equal or increasing down the column that define the rock pore volume multiplier for a given PRESS. | None |
| dimensionless | dimensionless | dimensionless |  |
| 3 | TRANS | If the RKTRMDIR is absent from the input deck, then TRANS is a columnar vector of real positive values that are either equal or increasing down the column that define the x, y, and z directional transmissibility multipliers for the corresponding PRESS.<br>If the RKTRMDIR is present in the input deck, then TRANS is a columnar vector of real positive values that are either equal or increasing down the column that define only the x directional transmissibility multipliers for the corresponding PRESS. | None |
| dimensionless | dimensionless | dimensionless |  |
| 4 | TRANSY | If the RKTRMDIR is absent from the input deck, then TRANSY is ignored.<br>If the RKTRMDIR is present in the input deck, then TRANSY is a columnar vector of real positive values that are either equal or increasing down the column that define only the y directional transmissibility multipliers for the corresponding PRESS. | None |
| dimensionless | dimensionless | dimensionless |  |
| 5 | TRANSZ | If the RKTRMDIR is absent from the input deck, then TRANSZ is ignored.<br>If the RKTRMDIR is present in the input deck, then TRANSZ is a columnar vector of real positive values that are either equal or increasing down the column that define only the z directional transmissibility multipliers for the corresponding PRESS. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by NTROCC tables as declared on the ROCKCOMP keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NPPVT rows as declared on the TABDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.129: ROCKTAB Keyword Description

#### Examples

The example below defines two rock compaction tables, assuming NTROCC is equal to two on the ROCKCOMP keyword and NPPVT is greater than or equal to five on the TABDIMS keyword and that the RKTRMDIR keyword is present in the input deck.

\--

\-- ROCK COMPACTION TABLES

\--

ROCKTAB

\-- PRESS PORV TX(YZ) TY TZ

\-- MULT MULT MULT MULT

\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\--

1000.0 0.9600 0.9650 0.9650 0.9650

1500.0 0.9800 0.9850 0.9850 0.9500

3000.0 0.9900 0.9950 0.9950 0.9950

4500.0 1.0000 1.0000 1.0000 1.0000

4750.0 1.0100 1.0100 1.0100 1.0100 / TABLE NO. 01

\-- PRESS PORV TX(YZ) TY TZ

\-- MULT MULT MULT MULT

\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\--

1000.0 0.9600 0.9650 0.9650 0.9650

1500.0 0.9800 0.9850 0.9850 0.9500

3000.0 0.9900 0.9950 0.9950 0.9950

4500.0 1.0000 1.0000 1.0000 1.0000

4750.0 1.0100 1.0100 1.0100 1.0100 / TABLE NO. 02

As the x, y and z directional transmissibility multipliers are identical in the above example, we could eliminate the RKTRMDIR keyword from the input deck and enter the data in the three column format, as shown on the next page.

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

The net result of the two examples in this case is identical.
