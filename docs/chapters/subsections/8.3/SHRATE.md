### SHRATE -- Activate Log-based Polymer Shearing and Define the Shear Rate Constant

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword activates the logarithm-based polymer shear thinning/thickening option and defines the shear rate constant. This keyword can only be used in conjunction with the PLYSHLOG in the PROPS section

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SHRATE | A positive real value that defines the shear rate constant. | 4.8 |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  This keyword is followed by NTPVT values as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each value is terminated by a \"/\" and there is no \"/\" terminator for the keyword. |  |  |  |

*Table 8.3.283.1: SHRATE Keyword Description*
#### Example

The following example activates the logarithm-based polymer shear thinning/thickening option and defines the shear rate constants for a run with two PVT regions.

\--

\-- ACTIVATE LOG-BASED POLYMER SHEAR THINNING-THICKENING OPTION

\-- AND DEFINE THE SHEAR RATE CONSTANT

\--

SHRATE

\-- SHEAR RATE

\-- CONSTANT

4.8 /

4.8 /
