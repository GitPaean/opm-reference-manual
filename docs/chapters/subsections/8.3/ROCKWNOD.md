### ROCKWNOD -- Water Saturation Values for Compaction Pressure-Sw Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The ROCK2D and the ROCK2DTR keywords in the PROPS section define rock compressibility pore volume and transmissibility multipliers as a function of pressure and water saturation ("Sw"), for when the rock compaction option has been invoked by the ROCKCOMP keyword in the RUNSPEC section. The pressure values are defined on ROCK2D and the ROCK2DTR keywords together with the multipliers. This keyword ROCKWNOD, defines the water saturations that are used in conjunction with the ROCK2D and the ROCK2DTR keywords.

This keyword should only be used if compaction option has been enabled.

| 1 | SWAT | A columnar vector of real monotonically increasing down the column values that defines the water saturations to be associated with the data on the ROCK2D and the ROCKTR keywords. | None |
| --- | --- | --- | --- |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by NTROCC tables as declared on the ROCKCOMP keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NSSFUN rows as declared on the TABDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.131: ROCKWNOD Keyword Description

See also the OVERBURD, ROCKTAB, ROCK2D and ROCK2DTR keywords in the PROPS section.

#### Example

The following example defines two ROCKWNOD tables for the pore volume and transmissibility compaction tables, assuming NTROCC is equal to two on the ROCKCOMP keyword and NSSFUN is greater than or equal to four on the TABDIMS keyword.

\--

\-- WATER SATURATION VALUES FOR COMPACTION PRESSURE-SW TABLES

\--

ROCKWNOD

\-- COMPACT

\-- SWAT

\-- \-\-\-\-\--

0.000

0.200

0.400

1.000 / P-SW SET TABLE NO. 01

\-- COMPACT

\-- SWAT

\-- \-\-\-\-\--

0.000

0.250

0.750

1.000 / P-SW SET TABLE NO. 02

Note that there must be exactly NTROCC tables entered for this keyword, otherwise an error will occur.
