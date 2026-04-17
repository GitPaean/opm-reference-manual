### SGFN -- Gas Saturation Tables (Format Type 2)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SGFN keyword defines the gas relative permeability and oil-gas capillary pressure data versus gas saturation tables for when gas is present in the input deck. This keyword should only be used if the gas is present in the run.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SGAS | A columnar vector of real monotonically increasing down the column values starting from zero and terminating at one, that defines the gas saturation. | None |
| dimensionless | dimensionless | dimensionless |  |
| 2 | KRG | A columnar vector of real values that are either equal or increasing down the column and that are greater than or equal to zero and less than or equal to one that defines the gas relative permeability. | None |
| dimensionless | dimensionless | dimensionless |  |
| 3 | PCOG | A columnar vector of real values that are either equal or increasing down the column that defines the oil-gas capillary pressure. | None |
| psia | bars | atm |  |
| Notes:<br>1)  The keyword is followed by NTSFUN tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NSSFUN rows as declared on the TABDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.148: SGFN Keyword Description

See also the [GSF - Gas Saturation Tables versus Gas Saturation (Gas-Water and CO2STORE Systems)](#anchor-2) keyword in the PROPS section, that defines the gas relative permeability and gas-water capillary pressure data as a function of gas saturation, for when only the gas and water phases are present in the model. Note that the GSF keyword must be used in conjunction with the [WSF - Water Saturation Tables versus Water Saturation (Gas-Water and CO2STORE Systems)](#anchor-3) keyword, also in the PROPS section. WSF defines the water saturation as a function of water saturation for when only the gas and water phases are present in the model.

#### Example

\--

\-- GAS RELATIVE PERMEABILITY TABLES (SGFN)

\--

SGFN

\-- SGAS KRG PCGO

\-- FRAC PSIA

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\--

0.00 0.0000 0.0

0.05 0.0000 0.0

0.10 0.0000 0.0

0.15 0.0000 0.0

0.20 0.0002 0.0

0.25 0.0010 0.0

0.30 0.0062 0.0

0.35 0.0140 0.0

0.40 0.0273 0.0

0.45 0.0450 0.0

0.50 0.0707 0.0

0.55 0.1020 0.0

0.60 0.1412 0.0

0.65 0.1870 0.0

0.70 0.2412 0.0

0.77 0.3288 0.0

0.82 0.4000 0.0

0.85 0.4450 0.0 / TABLE NO. 01

\-- SGAS KRG PCGO

\-- FRAC PSIA

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\--

0.00 0.0000 0.0

0.05 0.0000 0.0

0.10 0.0000 0.0

0.15 0.0000 0.0

0.20 0.0002 0.0

0.25 0.0010 0.0

0.30 0.0062 0.0

0.35 0.0140 0.0

0.40 0.0273 0.0

0.45 0.0450 0.0

0.50 0.0707 0.0

0.55 0.1020 0.0

0.60 0.1412 0.0

0.65 0.1870 0.0

0.70 0.2412 0.0

0.77 0.3288 0.0

0.82 0.4000 0.0

0.85 0.4450 0.0 / TABLE NO. 02

The example defines two SGFN tables for when gas is present in the input deck.
