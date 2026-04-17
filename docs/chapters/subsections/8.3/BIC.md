### BIC -- Binary Interaction Coefficients

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The BIC keyword defines the binary interaction coefficients for each pair of compositional components active in the model and for each equation of state. The keyword should only be used if the compositional mode has been requested using the COMPS keyword in the RUNSPEC section.

OPM Flow does not currently support the general compositional modeling formulation.

This keyword is not supported by OPM Flow but it will be parsed and its data ignored.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | BIC | A series of real numbers that define the binary interaction coefficients for each pair (*i*, *j*) of compositional components active in the model. The matrix is symmetrical with zeroes on the diagonal so only the portion of the matrix below the diagonal is required (i.e., *i* = {2, \... COMPS} and *j* \< *i*), where COMPS is specified by the COMPS keyword in the RUNSPEC section. The values are ordered with *j* cycling fastest (i.e. , , , , , , \...). | 0 |
| Notes:<br>1)  The keyword is followed by NMEOSR records as specified by the TABDIMS keyword in the RUNSPEC section.<br>2)  Each record must contain COMPS × (COMPS - 1) / 2 values as specified by the COMPS keyword in the RUNSPEC section.<br>3)  Each record is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.3.17.1: BIC Keyword Description

#### Examples

The following example defines the binary interaction coefficients for each pair of compositional components in a single three-component equation of state model.

\--

\-- Binary Interaction Coefficients

\--

BIC

0.1209

0.1310 0.0339 /

The following example defines the binary interaction coefficients for each component in two three-component equation of state models.

\--

\-- Binary Interaction Coefficients

\--

BIC

0.1209

0.1310 0.0339 /

0.1209

0.1310 0.0339 /
