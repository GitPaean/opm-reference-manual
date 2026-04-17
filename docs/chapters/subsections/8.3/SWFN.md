### SWFN -- Water Saturation Tables (Format Type 2)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SWFN keyword defines the water relative permeability and water-oil capillary pressure data versus water saturation tables for when water is present in the input deck. This keyword should only be used if water is present in the run.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SWAT | A columnar vector of real monotonically increasing down the column values starting from zero and terminating at one, that defines the water saturation. | None |
| dimensionless | dimensionless | dimensionless |  |
| 2 | KRW | A columnar vector of real values that are either equal or increasing down the column and that are greater than or equal to zero and less than or equal to one that defines the water relative permeability with respect to gas saturation.<br>The first value in the column should be zero. | None |
| dimensionless | dimensionless | dimensionless |  |
| 3 | PCWO | A columnar vector of real values that are either equal or increasing down the column that defines the water-oil relative capillary pressure.<br>If the SWATINIT keyword has been used to initialize the model then columnar vector has to be strictly monotonically increasing. | None |
| psia | bars | atm |  |
| Notes:<br>1)  The keyword is followed by NTSFUN tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NSSFUN rows as declared on the TABDIMS keyword in the RUNSPEC section.<br>3)  Items (2) and (3) may be defaulted, in which case linear interpolation or constant extrapolation will be used to calculate the missing values. At least two values must be entered for item (2), and at least one value must be entered for item (3).<br>4)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.3.332.1: SWFN Keyword Description

#### Example

\--

\-- WATER RELATIVE PERMEABILITY TABLES (SWFN)

\--

SWFN

\-- SWAT KRW PCOW

\-- FRAC FRAC PSIA

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\--

0.15 0.00000 0.0

0.20 6.25e-6 0.0

0.25 0.00010 0.0

0.30 0.00050 0.0

0.35 0.00160 0.0

0.40 0.00390 0.0

0.45 0.00810 0.0

0.50 0.01500 0.0

0.55 0.02560 0.0

0.60 0.04100 0.0

0.65 0.06250 0.0

0.70 0.09150 0.0

0.75 0.12960 0.0

0.80 0.17850 0.0

0.85 0.24010 0.0

0.90 0.31640 0.0

0.95 0.40960 0.0

1.00 0.52200 0.0 / TABLE NO. 1

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\--

0.15 0.00000 0.0

0.20 6.25e-6 0.0

0.25 0.00010 0.0

0.30 0.00050 0.0

0.35 0.00160 0.0

0.40 0.00390 0.0

0.45 0.00810 0.0

0.50 0.01500 0.0

0.55 0.02560 0.0

0.60 0.04100 0.0

0.65 0.06250 0.0

0.70 0.09150 0.0

0.75 0.12960 0.0

0.80 0.17850 0.0

0.85 0.24010 0.0

0.90 0.31640 0.0

0.95 0.40960 0.0

1.00 0.52200 0.0 / TABLE NO. 2

The example defines two SWFN tables for use when water is present in the run.
