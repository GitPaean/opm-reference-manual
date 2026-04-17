### SGWFN -- Gas-Water Saturation Tables (Format Type 2)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SGWFN keyword defines the gas and water relative permeability and gas-water capillary pressure data versus gas saturation tables for when gas and water are present in the input deck. This keyword should only be used if gas and water are present in the run.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SGAS | A columnar vector of real monotonically increasing down the column values starting from zero and terminating at one, that defines the gas saturation. | None |
| dimensionless | dimensionless | dimensionless |  |
| 2 | KRG | A columnar vector of real values that are either equal or increasing down the column and that are greater than or equal to zero and less than or equal to one that defines the gas relative permeability.<br>Note that the first entry in the column must be zero. | None |
| dimensionless | dimensionless | dimensionless |  |
| 3 | KRW | A columnar vector of real values that are either equal or decreasing down the column and that are greater than or equal to zero and less than or equal to one that defines the water relative permeability with respect to gas saturation.<br>The last value in the column should be zero. | None |
| dimensionless | dimensionless | dimensionless |  |
| 4 | PCGW | A columnar vector of real values that are either equal or increasing down the column that defines the gas-water relative capillary pressure. | None |
| psia | bars | atm |  |
| Notes:<br>1)  The keyword is followed by NTSFUN tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NSSFUN rows as declared on the TABDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.155: SGWFN Keyword Description

#### Example

\--

\-- GAS-WATER RELATIVE PERMEABILITY TABLES (SGWFN)

SGWFN

\-- SG KRG KRW PCOW

\-- FRAC PSIA

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\--

0.000000 0.0000 0.9000 0.000000

0.200000 0.0002 0.7664 0.000000

0.699099 0.4973 0.0000 0.000000

0.700000 1.0000 0.0000 0.000000 / TABLE NO. 01

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\--

0.000000 0.0000 0.9000 0.000000

0.200000 0.0002 0.7664 0.000000

0.245309 0.0004 0.7443 0.000000

0.261989 0.0010 0.6907 0.000000

0.303091 0.0044 0.5671 0.000000

0.368269 0.0191 0.3962 0.000000

0.435026 0.0519 0.2528 0.000000

0.486387 0.0940 0.1643 0.000000

0.522283 0.1339 0.1137 0.000000

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

0.700000 1.0000 0.0000 0.000000 / TABLE NO. 02

The example defines two SGWFN tables for use when gas and water are present in the run.
