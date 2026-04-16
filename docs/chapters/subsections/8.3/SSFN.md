### SSFN -- Solvent and Gas Relative Permeability Tables

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [SSFN](#__RefHeading___Toc106880_335817223) keyword defines the miscible normalized relative permeability tables for when the [SOLVENT](#__RefHeading___Toc62787_1778172979) option has been activated in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section using the respective keyword. The [SOLVENT](#__RefHeading___Toc62787_1778172979) keyword results in a four component model (oil, water and gas, plus a solvent). This keyword should only be used if the [SOLVENT](#__RefHeading___Toc62787_1778172979) option has been activated.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [SGAS](#__RefHeading___Toc137369_1317547213) | A columnar vector of real monotonically increasing down the column values starting from zero and terminating at one, that defines the gas plus solvent saturation ration which is defined as either:<br>or<br>Where Sg is the gas saturation and Ss is the solvent saturation. | None |
| dimensionless | dimensionless | dimensionless |  |
| 2 | KRGt | A columnar vector of real values that are either equal or increasing down the column and that are greater than or equal to zero and less than or equal to one that defines the gas relative permeability. The resulting gas relative permeability is calculated from:<br>where krg^t\ ^is the data in this column and krgt is the gas relative permeability from the [SGFN](#__RefHeading___Toc106868_335817223) keyword. | None |
| dimensionless | dimensionless | dimensionless |  |
| 3 | KRSt | A columnar vector of real values that are either equal or increasing down the column and that are greater than or equal to zero and less than or equal to one that defines the solvent relative permeability. The resulting solvent relative permeability is calculated from:<br>where krS^t\ ^is the data in this column and krgt is the gas relative permeability from the [SGFN](#__RefHeading___Toc106868_335817223) keyword. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by NTSFUN tables as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each table must contain a minimum of two rows and a maximum of NSSFUN rows as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.172: SSFN Keyword Description

#### Example

\--

\-- SOLVENT RELATIVE PERMEABILITY TABLES

\--

SSFN

\-- SGAS KRGT KRST

\-- FRAC

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

0.0000 0.0000 0.0000

1.0000 1.0000 1.0000 / TABLE NO. 01

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

0.0000 0.0000 0.0000

0.2000 0.2000 0.3000

0.4000 0.3000 0.5000

0.6000 0.4000 0.7000

0.8000 0.5000 0.7500

1.0000 1.0000 1.0000 / TABLE NO. 02

The above example defines two [SSFN](#__RefHeading___Toc106880_335817223) tables for use with the [SOLVENT](#__RefHeading___Toc62787_1778172979) option.
