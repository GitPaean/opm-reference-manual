### ACF -- Define Acentric Factors

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The ACF keyword defines the acentric factors for each of the compositional components active in the model and for each equation of state. The keyword should only be used if the compositional mode has been requested using the COMPS keyword in the RUNSPEC section.

OPM Flow does not currently support the general compositional modeling formulation.

This keyword is not supported by OPM Flow but it will be parsed and its data ignored.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | ACF | A series of real numbers that define the acentric factors for each of the compositional components active in the model. | None |
| Notes:<br>1)  The keyword is followed by NMEOSR records as specified by the TABDIMS keyword in the RUNSPEC section.<br>2)  Each record must contain COMPS values as specified by the COMPS keyword in the RUNSPEC section.<br>3)  Each record is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.3.1.1: ACF Keyword Description

#### Examples

The following example defines the acentric factors for each component in a single three-component equation of state model.

\--

\-- Acentric Factors

\--

ACF

0.0108 0.2273 0.3434 /

The following example defines the acentric factors for each component in two three-component equation of state models.

\--

\-- Acentric Factors

\--

ACF

0.0108 0.2273 0.3434 /

0.0110 0.2281 0.3428 /
