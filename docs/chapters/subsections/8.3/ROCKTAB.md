### ROCKTAB -- Rock Compaction Tables

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [ROCKTAB](#__RefHeading___Toc107256_3812137098) keyword defines the rock compaction attributes to be applied when the rock compaction option has been invoked by the [ROCKCOMP](#__RefHeading___Toc55593_1778172979) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. [ROCKTAB](#__RefHeading___Toc107256_3812137098) defines pore volume and transmissibility multipliers versus pressure that are used in the compaction calculations. If the [RKTRMDIR](#__RefHeading___Toc111812_2939291539) has been activated in the [PROPS](#__RefHeading___Toc39329_784232322) section, then the transmissibility multiplier is directional dependent and two additional columns are used to define the y and z direction transmissibility multipliers.

| 1 | PRESS | If the ROCKOPT1 variable has been set to [PRESSURE](#__RefHeading___Toc135627_1317547213) on the [ROCKOPTS](#__RefHeading___Toc111814_2939291539) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section, then PRESS should be a columnar vector of real monotonically *increasing* down the column values, that define the reference pressure for which the other parameters correspond to.<br>If ROCKOPT1 has been set to STRESS, then PRESS should be a columnar vector of real monotonically *decreasing* down the column values. | None |
| --- | --- | --- | --- |
| psia | bars | atm |  |
| 2 | [PORV](#__RefHeading___Toc96547_718313858) | A columnar vector of real positive values that are either equal or increasing down the column that define the rock pore volume multiplier for a given PRESS. | None |
| dimensionless | dimensionless | dimensionless |  |
| 3 | TRANS | If the [RKTRMDIR](#__RefHeading___Toc111812_2939291539) is absent from the input deck, then TRANS is a columnar vector of real positive values that are either equal or increasing down the column that define the x, y, and z directional transmissibility multipliers for the corresponding PRESS.<br>If the [RKTRMDIR](#__RefHeading___Toc111812_2939291539) is present in the input deck, then TRANS is a columnar vector of real positive values that are either equal or increasing down the column that define only the x directional transmissibility multipliers for the corresponding PRESS. | None |
| dimensionless | dimensionless | dimensionless |  |
| 4 | TRANSY | If the [RKTRMDIR](#__RefHeading___Toc111812_2939291539) is absent from the input deck, then TRANSY is ignored.<br>If the [RKTRMDIR](#__RefHeading___Toc111812_2939291539) is present in the input deck, then TRANSY is a columnar vector of real positive values that are either equal or increasing down the column that define only the y directional transmissibility multipliers for the corresponding PRESS. | None |
| dimensionless | dimensionless | dimensionless |  |
| 5 | TRANSZ | If the [RKTRMDIR](#__RefHeading___Toc111812_2939291539) is absent from the input deck, then TRANSZ is ignored.<br>If the [RKTRMDIR](#__RefHeading___Toc111812_2939291539) is present in the input deck, then TRANSZ is a columnar vector of real positive values that are either equal or increasing down the column that define only the z directional transmissibility multipliers for the corresponding PRESS. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by NTROCC tables as declared on the [ROCKCOMP](#__RefHeading___Toc55593_1778172979) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each table must contain a minimum of two rows and a maximum of NPPVT rows as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.129: ROCKTAB Keyword Description

#### Examples

The example below defines two rock compaction tables, assuming NTROCC is equal to two on the [ROCKCOMP](#__RefHeading___Toc55593_1778172979) keyword and NPPVT is greater than or equal to five on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword and that the [RKTRMDIR](#__RefHeading___Toc111812_2939291539) keyword is present in the input deck.

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

As the x, y and z directional transmissibility multipliers are identical in the above example, we could eliminate the [RKTRMDIR](#__RefHeading___Toc111812_2939291539) keyword from the input deck and enter the data in the three column format, as shown on the next page.

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
