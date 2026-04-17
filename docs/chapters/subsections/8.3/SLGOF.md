### SLGOF -- Gas-Oil Saturation Tables versus Gas (Format Type 1)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SLGOF keyword defines the oil and gas relative permeability and oil-gas capillary pressure versus liquid saturation tables for when oil and gas are present in the input deck. This keyword should only be used if both oil and gas are present in the run.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SLIQ | A columnar vector of real monotonically increasing down the column values starting from zero and terminating at one, that defines the liquid saturation, that is the connate water saturation (SWL) plus the oil saturation.<br>The first entry should correspond to residual liquid, that is Swc + Sorg and the last entry should be 1.0 to correspond to a gas saturation of zero. | None |
| dimensionless | dimensionless | dimensionless |  |
| 2 | KRG | A columnar vector of real values that are either equal or decreasing down the column and that are greater than or equal to zero and less than or equal to one that defines the gas relative permeability.. | None |
| dimensionless | dimensionless | dimensionless |  |
| 3 | KRO | A columnar vector of real values that are either equal or increasing down the column and that are greater than or equal to zero and less than or equal to one that defines the oil relative permeability with respect to gas and connate water saturation.<br>When water is active in the run, the last entry the column, that is at krog(Sg = 0), must be the same as the first entry in the corresponding SWOF table, that is at krow(So = 1 - Swco).<br>The first value in the column should be zero. | None |
| dimensionless | dimensionless | dimensionless |  |
| 4 | PCOG | A columnar vector of real values that are either equal or decreasing down the column that defines the oil-gas relative capillary pressure. | None |
| psia | bars | atm |  |
| Notes:<br>1)  The keyword is followed by NTSFUN tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NSSFUN rows as declared on the TABDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.163: SLGOF Keyword Description

#### Example

\--

\-- GAS-OIL RELATIVE PERMEABILITY TABLES (SLGOF)

SLGOF

\-- SLIQ KRG KROG PCOG

\-- FRAC PSIA

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\--

0.30060 0.55000 0.0000 0.0000

0.31480 0.42500 0.2848 0.0000

0.32910 0.35000 0.3091 0.0000

0.34330 0.27500 0.4333 0.0000

0.35760 0.25000 0.5576 0.0000

0.37180 0.22500 0.5818 0.0000

0.38610 0.20000 0.6061 0.0000

0.40030 0.17500 0.6303 0.0000

0.41450 0.15000 0.6545 0.0000

0.42880 0.12500 0.6788 0.0000

0.44300 0.10000 0.7030 0.0000

0.45730 0.07500 0.7273 0.0000

0.47150 0.05000 0.7515 0.0000

0.48580 0.02500 0.7758 0.0000

0.50000 0.00000 0.8000 0.0000

0.80000 0.00000 0.9000 0.0000 / TABLE No. 01

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\--

0.30060 0.55000 0.0000 0.0000

0.31480 0.42500 0.2848 0.0000

0.32910 0.35000 0.3091 0.0000

0.34330 0.27500 0.4333 0.0000

0.35760 0.25000 0.5576 0.0000

0.37180 0.22500 0.5818 0.0000

0.38610 0.20000 0.6061 0.0000

0.40030 0.17500 0.6303 0.0000

0.41450 0.15000 0.6545 0.0000

0.42880 0.12500 0.6788 0.0000

0.44300 0.10000 0.7030 0.0000

0.45730 0.07500 0.7273 0.0000

0.47150 0.05000 0.7515 0.0000

0.48580 0.02500 0.7758 0.0000

0.50000 0.00000 0.8000 0.0000

0.80000 0.00000 0.9000 0.0000 / TABLE No. 02

The example defines two SLGOF tables for use when oil, gas and water are present in the run.
