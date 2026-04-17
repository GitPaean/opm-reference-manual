### SWOF -- Water-Oil Saturation Tables (Format Type 1)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SWOF keyword defines the water and oil relative permeability and water-oil capillary pressure data versus water saturation tables for when water and oil are present in the input deck. This keyword should only be used if water and oil are present in the run.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SWAT | A columnar vector of real monotonically increasing down the column values starting from zero and terminating at one, that defines the water saturation.<br>The first entry is the connate water saturation Swc and the last entry should be 1.0. | None |
| dimensionless | dimensionless | dimensionless |  |
| 2 | KRW | A columnar vector of real values that are either equal or increasing down the column and that are greater than or equal to zero and less than or equal to one that defines the water relative permeability with respect to gas saturation.<br>The first value in the column should be zero. | None |
| dimensionless | dimensionless | dimensionless |  |
| 3 | KRO | A columnar vector of real values that are either equal or decreasing down the column and that are greater than or equal to zero and less than or equal to one that defines the oil relative permeability with respect to oil and water saturation.<br>When gas is active in the run, the first entry the column, that is at krow(So = 1-Swc), must be the same as the first entry in the corresponding SGOF or SLGOF table, that is at krog(Sg = 0).<br>The first value in the column should be one. | None |
| dimensionless | dimensionless | dimensionless |  |
| 4 | PCWO | A columnar vector of real values that are either equal or decreasing down the column that defines the water-oil relative capillary pressure.<br>If the SWATINIT keyword has been used to initialize the model then columnar vector has to be strictly monotonically increasing. | None |
| psia | bars | atm |  |
| Notes:<br>1)  The keyword is followed by NTSFUN tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NSSFUN rows as declared on the TABDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.189: SWOF Keyword Description

#### Example

The following example is based on NTSFUN equals two on the TABDIMS keyword in the RUNSPEC section.

\--

\-- WATER-OIL RELATIVE PERMEABILITY TABLES (SWOF)

\--

SWOF

\-- SWAT KRW KROW PCOW

\-- FRAC PSIA

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\--

0.200000 0.0000 0.9000 0.000000

0.238616 0.0002 0.7664 0.000000

0.245309 0.0004 0.7443 0.000000

0.261989 0.0010 0.6907 0.000000

0.303091 0.0044 0.5671 0.000000

0.368269 0.0191 0.3962 0.000000

0.435026 0.0519 0.2528 0.000000

0.486387 0.0940 0.1643 0.000000

0.550683 0.1725 0.0803 0.000000

0.575342 0.2115 0.0559 0.000000

0.599076 0.2542 0.0367 0.000000

0.621294 0.2991 0.0223 0.000000

0.642171 0.3458 0.0120 0.000000

0.658984 0.3868 0.0061 0.000000

0.671123 0.4183 0.0030 0.000000

0.679268 0.4403 0.0015 0.000000

0.684963 0.4562 0.0008 0.000000

0.688893 0.4674 0.0004 0.000000

0.692025 0.4765 0.0002 0.000000

0.694641 0.4841 0.0001 0.000000

0.696976 0.4910 0.0000 0.000000

0.699099 0.4973 0.0000 0.000000

0.700000 0.5000 0.0000 0.000000

1.000000 0.9000 0.0000 0.000000 / TABLE NO. 01

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\--

0.200000 0.0000 0.9000 0.000000

0.238616 0.0002 0.7664 0.000000

0.245309 0.0004 0.7443 0.000000

0.261989 0.0010 0.6907 0.000000

0.303091 0.0044 0.5671 0.000000

0.368269 0.0191 0.3962 0.000000

0.435026 0.0519 0.2528 0.000000

0.486387 0.0940 0.1643 0.000000

0.550683 0.1725 0.0803 0.000000

0.575342 0.2115 0.0559 0.000000

0.599076 0.2542 0.0367 0.000000

0.621294 0.2991 0.0223 0.000000

0.642171 0.3458 0.0120 0.000000

0.658984 0.3868 0.0061 0.000000

0.671123 0.4183 0.0030 0.000000

0.679268 0.4403 0.0015 0.000000

0.684963 0.4562 0.0008 0.000000

0.688893 0.4674 0.0004 0.000000

0.692025 0.4765 0.0002 0.000000

0.694641 0.4841 0.0001 0.000000

0.696976 0.4910 0.0000 0.000000

0.699099 0.4973 0.0000 0.000000

0.700000 0.5000 0.0000 0.000000

1.000000 0.9000 0.0000 0.000000 / TABLE NO. 01

The example defines two SWOF tables for use when water and oil are present in the run. In the tables the water-oil capillary pressure data has been set to zero.
