### GSF -- Gas Saturation Function Tables (Gas-Water Systems)

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [GSF](#__RefHeading___Toc524656_3603161511) keyword defines the gas relative permeability and gas-water capillary pressure data versus gas saturation tables for when only gas and water are present in the input deck. This keyword should only be used if the gas and water phases are present in the run, and can therefore also be used with the [CO2STORE](#__RefHeading___Toc387968_1616145207) and [H2STORE](#REF_HEADING_KEYWORD_H2STORE) models. In addition, the keyword must be used in conjunction with the [WSF](#__RefHeading___Toc524656_3603161511 Copy 1) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section, that defines the water relative permeability versus water saturation for gas-water systems.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [SGAS](#__RefHeading___Toc137369_1317547213) | A columnar vector of real values monotonically increasing down the column starting from zero and terminating at one minus the connate water saturation, that defines the gas saturation. | None |
| dimensionless | dimensionless | dimensionless |  |
| 2 | [KRG](#__RefHeading___Toc97393_621662414) | A columnar vector of real values that are either equal or increasing down the column and that are greater than or equal to zero and less than or equal to one that defines the gas relative permeability.<br>Note that the first entry in the column must be zero. | None |
| dimensionless | dimensionless | dimensionless |  |
| 3 | PCWG | A columnar vector of real values that are either equal or increasing down the column that defines the gas-water capillary pressure. | None |
| psia | bars | atm |  |
| Notes:<br>1)  The keyword is followed by NTSFUN tables as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each table must contain a minimum of two rows and a maximum of NSSFUN rows as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.44: GSF Keyword Description

See also the [[WSF - Water Saturation Tables versus Water Saturation (Gas-Water and CO2STORE Systems)](#anchor-1)](#8.3.365.WSF - Water Saturation Tables versus Water Saturation (Gas-Water and CO2STORE Systems)|outline) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section, that defines the water saturation as a function of water saturation for when only the gas and water phases are present in the model.

#### Example

\--

\-- GAS RELATIVE PERMEABILITY TABLES (OPM FLOW KEYWORD)

\--

GSF

\-- SGAS KRG PCGW

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

\-- SGAS KRG PCGW

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

The example defines two [GSF](#__RefHeading___Toc524656_3603161511) tables for when gas and water are present in the input deck. In the tables the gas-water capillary pressure data has been set to zero.
