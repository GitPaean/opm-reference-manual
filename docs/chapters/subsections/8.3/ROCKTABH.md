### ROCKTABH -- Rock Compaction Hysteresis Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The ROCKTABH keyword defines the rock compaction hysteresis attributes to be applied for when the rock compaction option has been invoked by the ROCKCOMP keyword in the RUNSPEC section. ROCKTABH defines pore volume and transmissibility multipliers versus pressure that are used in the compaction calculations. If the RKTRMDIR has been activated in the PROPS section, then the transmissibility multiplier is directional dependent and two additional columns are used to define the y and z direction transmissibility multipliers. The keyword should only be used if the Rock Compaction Hysteresis option has been activated by either setting the ROCKOPT parameter on the ROCKCOMP keyword to HYSTER or BOBERG.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | PRESS | If the ROCKOPT1 variable has been set to PRESSURE on the ROCKOPTS keyword in the PROPS section, then PRESS should be a columnar vector of real monotonically *increasing* down the column values, that define the reference pressure for which the other parameters correspond to.<br>If ROCKOPT1 has been set to STRESS, then PRESS should be a columnar vector of real monotonically *de*creasing down the column values. | None |
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

Table 8.130: ROCKTABH Keyword Description

Each data set consists of columnar vectors of pore volume and transmissibility multipliers versus pressure that specify the elastic contraction and expansion and of the reservoir rock. The deflation curve is derived from the first data elements on each elastic curve. If the ROCKOPT parameter on the ROCKCOMP keyword has been set to HYSTER, then the dilation curves are extrapolated to infinite pressure, that is the curves are unbounded. However, if ROCKCOMP is set to BOBERG the last points of each elastic curve are used as the dilation curves.

#### Example

The example below defines two rock compaction tables, assuming NTROCC is equal to two on the ROCKCOMP keyword and NPPVT is greater than or equal to four on the TABDIMS keyword and that the RKTRMDIR keyword is not present in the input deck.

\--

\-- ROCK COMPACTION HYSTERESIS TABLES

\--

ROCKTABH

\-- PRESS PORV TX(YZ) TY TZ

\-- MULT MULT MULT MULT

\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\--

1500.0 0.9600 0.9800

2500.0 0.9700 0.9850

3500.0 0.9800 0.9900

4500.0 0.9900 0.9950 / NPPVT = 1

2500.0 0.9900 0.9900

3500.0 0.9950 0.9950

4750.0 0.9980 0.9980 / NPPVT = 2

3500.0 1.0000 1.0000

5500.0 1.0100 1.0100 / NPPVT = 3

4500.0 1.0100 1.0100

5750.0 1.0200 1.0200 / NPPVT = 4

/ TABLE NO. 01 \-- PRESS PORV TX(YZ) TY TZ

\-- MULT MULT MULT MULT

\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\--

1500.0 0.9400 0.9700

2750.0 0.9400 0.9700 / NPPVT = 1

2250.0 0.9800 0.9900

3250.0 0.9800 0.9900 / NPPVT = 2

3000.0 1.0000 1.0000

4250.0 1.0000 1.0000 / NPPVT = 3

4550.0 1.0200 1.0100

5750.0 1.0200 1.0100 / NPPVT = 4

/ TABLE NO. 02

Here the deflation curve is define for table number one is:

1500.0 0.9600 0.9800

2500.0 0.9900 0.9900

3500.0 1.0000 1.0000

4500.0 1.0100 1.0100

and for table number 2:

1500.0 0.9400 0.9700

2250.0 0.9800 0.9900

3250.0 1.0000 1.0000

4250.0 1.0200 1.0100

And the dilation curve is define for table number one is:

4500.0 0.9900 0.9950

4750.0 0.9980 0.9980

5500.0 1.0100 1.0100

5750.0 1.0200 1.0200

and for table number 2:

2250.0 0.9400 0.9700

3250.0 0.9800 0.9900

4250.0 1.0000 1.0000

5250.0 1.0200 1.0100
