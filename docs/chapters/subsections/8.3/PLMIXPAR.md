### PLMIXPAR -- Define the Polymer Todd-Longstaff Mixing Parameters

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The PLMIXPAR keyword defines the Todd-Longstaff[^1] mixing parameters for when the polymer option has been activated by the POLYMER keyword in the RUNSPEC section. This keyword must be present in the input deck if the POLYMER keyword has been activated.

Note that this keyword is used only for the polymer option, if the MISCIBLE keyword in the RUNSPEC section has been invoked then in addition the TLMIXPAR keyword is also required to define the Todd-Longstaff mixing parameters for the MISCIBLE option.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | PLMVIS | A real positive value that is greater than or equal to zero and less than or equal to one, that defines the viscosity Todd-Longstaff mixing parameter for each polymer region. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by NPLMIX tables as declared on the REGDIMS keyword in the RUNSPEC section, for each rock region. There should be only one row per table.<br>2)  Each entry is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.98: PLMIXPAR Keyword Description

#### Example

\--

\-- POLYMER TODD-LONGSTAFF MIXING PARAMETERS

\--

PLMIXPAR

\-- PLM

\-- VISCOS

\-- \-\-\-\-\-\--

0.3500 / TABLE NO. 01

0.2500 / TABLE NO. 02

0.6500 / TABLE NO. 03

The above example defines three polymer Todd-Longstaff mixing parameter data sets, based on the NPLMIX variable on the REGDIMS keyword in the RUNSPEC section being equal to three.

[^1]: Todd, M. and Longstaff, W. "The Development, Testing and Application of a Numerical Simulator for Predicting Miscible Flood Performance," paper SPE 3484, Journal of Canadian Petroleum Technology (1972) 24, No. 7, 874-882.
