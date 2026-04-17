### WSF -- Water Saturation Function Tables (Gas-Water Systems)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WSF keyword defines the water relative permeability data versus water saturation tables for when only gas and water are present in the input deck. This keyword should only be used if the gas and water phases are present in the run, and can therefore also be used with the CO2STORE and H2STORE models. In addition, the keyword must be used in conjunction with the GSF keyword in the PROPS section, that defines the gas relative permeability and gas-water capillary pressure data versus gas saturation for gas-water systems.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SWAT | A columnar vector of real values monotonically increasing down the column starting from the connate water saturation and terminating at one, that defines the water saturation. | None |
| dimensionless | dimensionless | dimensionless |  |
| 2 | KRW | A columnar vector of real values that are either equal or increasing down the column and that are greater than or equal to zero and less than or equal to one that defines the water relative permeability with respect to water saturation.<br>Note that the first entry in the column must be zero. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by NTSFUN tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NSSFUN rows as declared on the TABDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.200: WSF Keyword Description

See also the [GSF - Gas Saturation Tables versus Gas Saturation (Gas-Water and CO2STORE Systems)](#anchor-1) keyword in the PROPS section, that defines the gas relative permeability and gas-water capillary pressure data as a function of gas saturation, for when only the gas and water water phases are present in the model.

#### Example

\--

\-- WATER RELATIVE PERMEABILITY TABLES (OPM FLOW KEYWORD)

\--

WSF

\-- SWAT KRW

\-- FRAC

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

0.200000 0.0000

0.238616 0.0002

0.245309 0.0004

0.261989 0.0010

0.303091 0.0044

0.368269 0.0191

0.435026 0.0519

0.486387 0.0940

0.550683 0.1725

0.575342 0.2115

0.599076 0.2542

0.621294 0.2991

0.642171 0.3458

0.658984 0.3868

0.671123 0.4183

0.679268 0.4403

0.684963 0.4562

0.688893 0.4674

0.692025 0.4765

0.694641 0.4841

0.696976 0.4910

0.699099 0.4973

0.700000 0.5000

1.000000 0.9000 / TABLE NO. 01

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

0.200000 0.0000

0.238616 0.0002

0.245309 0.0004

0.261989 0.0010

0.303091 0.0044

0.368269 0.0191

0.435026 0.0519

0.486387 0.0940

0.550683 0.1725

0.575342 0.2115

0.599076 0.2542

0.621294 0.2991

0.642171 0.3458

0.658984 0.3868

0.671123 0.4183

0.679268 0.4403

0.684963 0.4562

0.688893 0.4674

0.692025 0.4765

0.694641 0.4841

0.696976 0.4910

0.699099 0.4973

0.700000 0.5000

1.000000 0.9000 / TABLE NO. 01

The example defines two WSF tables for use when only gas and water are present in the run.
