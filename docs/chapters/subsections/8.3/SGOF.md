### SGOF -- Gas-Oil Saturation Tables versus Gas (Format Type 1)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SGOF keyword defines the oil and gas relative permeability and oil-gas capillary versus gas saturation tables for when oil and gas are present in the input deck. This keyword should only be used if both oil and gas are present in the run.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SGAS | A columnar vector of real monotonically increasing down the column values starting from zero and terminating at one, that defines the gas saturation. | None |
| dimensionless | dimensionless | dimensionless |  |
| 2 | KRG | A columnar vector of real values that are either equal or increasing down the column and that are greater than or equal to zero and less than or equal to one that defines the gas relative permeability. | None |
| dimensionless | dimensionless | dimensionless |  |
| 3 | KRO | A columnar vector of real values that are either equal or decreasing down the column and that are greater than or equal to zero and less than or equal to one that defines the oil relative permeability with respect to gas and connate water saturation.<br>When water is active in the run, the first entry the column, that is at krog(Sg = 0), must be the same as the first entry in the corresponding SWOF table, that is at krow(So = 1 - Swco).<br>The last value in the column should be zero. | None |
| dimensionless | dimensionless | dimensionless |  |
| 4 | PCOG | A columnar vector of real values that are either equal or increasing down the column that defines the oil-gas relative capillary pressure. | None |
| psia | bars | atm |  |
| Notes:<br>1)  The keyword is followed by NTSFUN tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NSSFUN rows as declared on the TABDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.151: SGOF Keyword Description

#### Example

The following example is based on NTSFUN equals two on the TABDIMS keyword in the RUNSPEC section.

\--

\-- GAS-OIL RELATIVE PERMEABILITY TABLES (SGOF)

SGOF

\-- SG KRG KROG PCOG

\-- FRAC PSIA

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\--

0.00000 0.000000 0.90000 0.0000

0.03000 0.000000 0.82500 0.0000

0.80000 0.900000 0.00000 0.0000 / TABLE No. 01

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\--

0.00000 0.000000 0.90000 0.0000

0.03000 0.000000 0.82500 0.0000

0.04420 0.024200 0.80000 0.0000

0.05850 0.048500 0.77500 0.0000

0.07270 0.072700 0.75000 0.0000

0.08700 0.097000 0.72500 0.0000

0.10120 0.121200 0.70000 0.0000

0.11550 0.145500 0.67500 0.0000

0.12970 0.169700 0.65000 0.0000

0.14390 0.193900 0.62500 0.0000

0.15820 0.218200 0.60000 0.0000

0.17240 0.242400 0.57500 0.0000

0.18670 0.266700 0.55000 0.0000

0.20090 0.290900 0.52500 0.0000

0.21520 0.315200 0.50000 0.0000

0.22940 0.339400 0.47500 0.0000

0.24360 0.363600 0.45000 0.0000

0.25790 0.387900 0.42500 0.0000

0.27210 0.412100 0.40000 0.0000

0.28640 0.436400 0.37500 0.0000

0.30060 0.460600 0.35000 0.0000

0.31480 0.484800 0.32500 0.0000

0.32910 0.509100 0.30000 0.0000

0.34330 0.533300 0.27500 0.0000

0.35760 0.557600 0.25000 0.0000

0.37180 0.581800 0.22500 0.0000

0.38610 0.606100 0.20000 0.0000

0.40030 0.630300 0.17500 0.0000

0.41450 0.654500 0.15000 0.0000

0.42880 0.678800 0.12500 0.0000

0.44300 0.703000 0.10000 0.0000

0.45730 0.727300 0.07500 0.0000

0.47150 0.751500 0.05000 0.0000

0.48580 0.775800 0.02500 0.0000

0.50000 0.800000 0.00000 0.0000

0.80000 0.900000 0.00000 0.0000 / TABLE No. 02

The example defines two SGOF tables for use when oil, gas and water are present in the run.
