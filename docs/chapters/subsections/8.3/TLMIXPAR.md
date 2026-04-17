### TLMIXPAR -- Define the Miscible Todd-Longstaff Mixing Parameters

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The TLMIXPAR keyword defines the Todd-Longstaff[^1] mixing parameters, for when either the miscible or solvent options have been activated by the MISCIBLE or SOLVENT keywords in the RUNSPEC section. This keyword must be present in the input deck if the MISCIBLE or SOLVENT keywords have been activated.

Note that If the POLYMER option has been activated by the POLYMER keyword in the RUNSPEC section, then this keyword is ignored and the mixing parameters are taken from the PLMIXPAR keyword instead.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | TLMVIS | A real positive value that is greater than or equal to zero and less than or equal to one, that defines the viscosity Todd-Longstaff mixing parameter for each miscibility region. | None |
| dimensionless | dimensionless | dimensionless |  |
| 2 | TLMDEN | A real positive value that is greater than or equal to zero and less than or equal to one, that defines the density Todd-Longstaff mixing parameter for each miscibility region. | The same value as entered for TLMVIS |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by NTMISC tables as declared on the MISCIBLE keyword in the RUNSPEC section, for each rock region. There should be only one row per table.<br>2)  Each entry is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.192: TLMIXPAR Keyword Description

#### Example

\--

\-- TODD-LONGSTAFF MIXING PARAMETERS

\--

TLMIXPAR

\-- TLM TLM

\-- VISCOS DENSITY

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.3500 0.3500 / TABLE NO. 01

0.2500 1\* / TABLE NO. 02

0.6500 0.7500 / TABLE NO. 03

The above example defines three Todd-Longstaff mixing parameter data sets, based on the NTMISC variable on the MISCIBLE keyword in the RUNSPEC section being equal to three.

[^1]: Todd, M. and Longstaff, W. "The Development, Testing and Application of a Numerical Simulator for Predicting Miscible Flood Performance," paper SPE 3484, Journal of Canadian Petroleum Technology (1972) 24, No. 7, 874-882.
