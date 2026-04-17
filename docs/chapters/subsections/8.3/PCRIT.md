### PCRIT -- Critical Pressures

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The PCRIT keyword defines the critical pressures for each of the compositional components active in the model and for each equation of state. The keyword should only be used if the compositional mode has been requested using the COMPS keyword in the RUNSPEC section.

OPM Flow does not currently support the general compositional modeling formulation.

This keyword is not supported by OPM Flow but it will be parsed and its data ignored.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | PCRIT | A series of real numbers that define the critical pressures for each of the compositional components active in the model. | None |
| psia | barsa | atma |  |
| Notes:<br>1)  The keyword is followed by NMEOSR records as specified by the TABDIMS keyword in the RUNSPEC section.<br>2)  Each record must contain COMPS values as specified by the COMPS keyword in the RUNSPEC section.<br>3)  Each record is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.3.196.1: PCRIT Keyword Description

#### Examples

The following example defines the critical pressures for each component in a single three-component equation of state model.

\--

\-- Critical Pressures

\--

PCRIT

1070.132 667.0576 616.5844 /

The following example defines the critical pressures for each component in two three-component equation of state models.

\--

\-- Critical Pressures

\--

PCRIT

1070.132 667.0576 616.5844 /

1070.132 667.0576 616.5844 /
