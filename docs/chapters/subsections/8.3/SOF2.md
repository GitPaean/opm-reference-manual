### SOF2 -- Oil Saturation Tables with Respect to Gas or Water (Format Type 2)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SOF2 keyword defines the oil relative permeability versus oil saturation tables for when oil and gas or oil and water are present in the input deck. The keyword is also used to define the relative permeability of the miscible hydrocarbon phase in SOLVENT runs. This keyword should only be used if oil is present in the run.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SOIL | A columnar vector of real monotonically increasing down the column values starting from zero and terminating at one, that defines the oil or the hydrocarbon solvent saturation.<br>For two phase runs the oil saturation should be entered and for when the SOLVENT option has been activated in the RUNSPEC section the total hydrocarbon phase (including the solvent) should be entered, that is SOIL = So + Sg + Ss. | None |
| dimensionless | dimensionless | dimensionless |  |
| 3 | KRO | A columnar vector of real values that are either equal or increasing down the column and that are greater than or equal to zero and less than or equal to one that defines the oil relative permeability with respect to gas and connate water saturation.<br>For two phase runs the oil relative permeability should be entered and for when the SOLVENT option has been activated in the RUNSPEC section the relative permeability of the miscible hydrocarbon phase with respect to water.<br>The last value in the column should be zero. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by NTSFUN tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NSSFUN rows as declared on the TABDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.165: SOF2 Keyword Description

Note this keyword should only be used for when the SOLVENT keyword in the RUNSPEC section has been activated. It should not be use for two-phase oil-water runs.

#### Example

\--

\-- OIL RELATIVE PERMEABILITY TABLES (SOF2)

\--

SOF2

\-- SOIL KRO

\-- FRAC FRAC

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

0.00 0.000000

0.05 1.197e-5

0.10 0.000191

0.15 0.000969

0.20 0.003065

0.25 0.007483

0.30 0.015517

0.35 0.028747

0.40 0.049041

0.45 0.078555

0.50 0.119730

0.55 0.175297

0.60 0.248272

0.65 0.341961

0.70 0.459956

0.75 0.606134

0.80 0.784664

0.85 1.000000 / TABLE NO. 01

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

0.00 0.000000

0.05 1.197e-5

0.10 0.000191

0.15 0.000969

0.20 0.003065

0.25 0.007483

0.30 0.015517

0.35 0.028747

0.40 0.049041

0.45 0.078555

0.50 0.119730

0.55 0.175297

0.60 0.248272

0.65 0.341961

0.70 0.459956

0.75 0.606134

0.80 0.784664

0.85 1.000000 / TABLE NO. 02

The example defines two SOF2 tables for when oil and gas or oil and water are present in the input deck.
