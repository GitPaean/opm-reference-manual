### MISC -- Define Solvent Miscibility-Immiscibility Transform Functions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

MISC defines the transformation between the miscible and immiscible relative permeability models, for when the MISCIBLE and SOLVENT keywords in the RUNSPEC section have been activated. The keyword can only be used with the MISCIBLE option and for when the oil, water, gas and solvent phases are active in the model.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SSOL | A columnar vector of real monotonically increasing down the column values starting from zero and terminating at one, that defines the solvent fraction with respect to the solvent and gas saturation, and is defined by:<br>Where Sg is the gas saturation and Ss is the solvent saturation.<br>Note that the first entry in the columnar vector should be zero and the last entry should be one to fully define the solvent fraction range. | None |
| dimensionless | dimensionless | dimensionless |  |
| 2 | MISC | A columnar vector of real equal or increasing down the column values that are greater than or equal to zero and less then one, that define the corresponding miscibility for the corresponding solvent fraction SSOL.<br>The first entry in the columnar vector should be zero and the last entry should be one to fully define the miscible-immiscible relationship. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by NTMISC tables as declared on the MISCIBLE keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NSMISC rows as declared on the MISCIBLE keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.88: MISC Keyword Description

#### Example

\--

\-- SOLVENT MISCIBILITY-IMMISCIBLITY TRANSFORM TABLE

\--

MISC

\-- SSOL MISC

\-- FRAC FRAC

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.0000 0.0000

0.2000 0.2500

0.5000 0.7500

1.0000 1.0000 / TABLE NO. 01

\-- SSOL MISC

\-- FRAC FRAC

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.0000 0.0000

0.3000 0.2500

0.6000 1.0000

1.0000 1.0000 / TABLE NO. 02

The above example defines two solvent miscible-immiscible transform tables assuming NTMISC equals two and NSMISC is greater than or equal to four on the MISCIBLE keyword in the RUNSPEC section.
