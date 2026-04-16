### ROCKTABH -- Rock Compaction Hysteresis Tables

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [ROCKTABH](#__RefHeading___Toc266641_516898843) keyword defines the rock compaction hysteresis attributes to be applied for when the rock compaction option has been invoked by the [ROCKCOMP](#__RefHeading___Toc55593_1778172979) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. [ROCKTABH](#__RefHeading___Toc266641_516898843) defines pore volume and transmissibility multipliers versus pressure that are used in the compaction calculations. If the [RKTRMDIR](#__RefHeading___Toc111812_2939291539) has been activated in the [PROPS](#__RefHeading___Toc39329_784232322) section, then the transmissibility multiplier is directional dependent and two additional columns are used to define the y and z direction transmissibility multipliers. The keyword should only be used if the Rock Compaction Hysteresis option has been activated by either setting the ROCKOPT parameter on the [ROCKCOMP](#__RefHeading___Toc55593_1778172979) keyword to HYSTER or BOBERG.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | PRESS | If the ROCKOPT1 variable has been set to [PRESSURE](#__RefHeading___Toc135627_1317547213) on the [ROCKOPTS](#__RefHeading___Toc111814_2939291539) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section, then PRESS should be a columnar vector of real monotonically *increasing* down the column values, that define the reference pressure for which the other parameters correspond to.<br>If ROCKOPT1 has been set to STRESS, then PRESS should be a columnar vector of real monotonically *de*creasing down the column values. | None |
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

Table 8.130: ROCKTABH Keyword Description

Each data set consists of columnar vectors of pore volume and transmissibility multipliers versus pressure that specify the elastic contraction and expansion and of the reservoir rock. The deflation curve is derived from the first data elements on each elastic curve. If the ROCKOPT parameter on the [ROCKCOMP](#__RefHeading___Toc55593_1778172979) keyword has been set to HYSTER, then the dilation curves are extrapolated to infinite pressure, that is the curves are unbounded. However, if [ROCKCOMP](#__RefHeading___Toc55593_1778172979) is set to BOBERG the last points of each elastic curve are used as the dilation curves.

#### Example

The example below defines two rock compaction tables, assuming NTROCC is equal to two on the [ROCKCOMP](#__RefHeading___Toc55593_1778172979) keyword and NPPVT is greater than or equal to four on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword and that the [RKTRMDIR](#__RefHeading___Toc111812_2939291539) keyword is not present in the input deck.

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
