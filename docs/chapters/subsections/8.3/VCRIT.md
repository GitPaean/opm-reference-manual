### VCRIT -- Critical Volumes

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The VCRIT keyword defines the critical volumes for each of the compositional components active in the model and for each equation of state. The keyword should only be used if the compositional mode has been requested using the COMPS keyword in the RUNSPEC section.

OPM Flow does not currently support the general compositional modeling formulation.

This keyword is not supported by OPM Flow but it will be parsed and its data ignored.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | VCRIT | A series of real numbers that define the critical volumes for each of the compositional components active in the model. | None |
| ft^3^/lb-M | m^3^/kg-M | m^3^/kg-M |  |
| Notes:<br>1)  The keyword is followed by NMEOSR records as specified by the TABDIMS keyword in the RUNSPEC section.<br>2)  Each record must contain COMPS values as specified by the COMPS keyword in the RUNSPEC section.<br>3)  Each record is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.3.359.1: VCRIT Keyword Description

#### Examples

The following example defines the critical volumes for each component in a single three-component equation of state model.

\--

\-- Critical Volumes

\--

VCRIT

1.505 1.585 3.250 /

The following example defines the critical volumes for each component in two three-component equation of state models.

\--

\-- Critical Volumes

\--

VCRIT

1.505 1.585 3.250 /

1.505 1.585 3.250 /
