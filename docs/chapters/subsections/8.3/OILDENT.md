### OILDENT -- Define Oil Density Temperature Coefficients

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

OILDENT defines the oil density as a function of temperature coefficients for when OPM Flow's thermal option has been activated by the THERMAL keyword in the RUNSPEC. Note this is an OPM Flow keyword used with OPM Flow's black-oil thermal model that is not available in the commercial simulator's black-oil thermal formulation.

This keyword can only be used if OPM Flow's thermal option has been activated by the THERMAL keyword in the RUNSPEC section. Note this is different to the commercial simulator that uses the TEMP keyword in the RUNSPEC section to activate the black-oil thermal model.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | TEMP | TEMP is a real positive value greater than zero that defines the absolute reference temperature used with TEXP1 and TEXP2 to estimate the change in oil density with respect to temperature. | Defined |
| ^o^R<br>527.67 | K<br>293.15 | K<br>293.15 |  |
| 2 | TEXP1 | TEXP1 is a real positive value greater than zero that defines the oil thermal expansion coefficient of the first order. | Defined |
| 1/^o^R<br>1.67 x 10^-4^ | 1/K<br>3.0 x 10^-4^ | 1/K<br>3.0 x 10^-4^ |  |
| 3 | TEXP2 | TEXP2 is a real positive value greater than zero that defines the oil thermal expansion coefficient of the second order. | Defined |
| 1/^o^R2<br>9.26 x 10^-7^ | 1/K2<br>3.0 x 10^-6^ | 1/K2<br>3.0 x 10^-6^ |  |
| Notes:<br>1)  The keyword is followed by NTPVT records as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each data set is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.3.186.1: OILDENT Keyword Description

The oil density at a given pressure and temperature is calculated from its value at surface conditions and the oil shrinkage factor (the reciprocal of the oil formation volume factor) as shown in the following equation:

Where the temperature dependence of the oil shrinkage factor relative to its value at the reference temperature is calculated as shown in the following equation:

Where:

= oil density

= oil shrinkage factor

= pressure

= temperature

= thermal expansion coefficients to first and second order

= subscript indicating surface conditions

= subscript indicating reference conditions

#### Example

The following example shows the OILDENT keyword using the default values, for when the thermal option has been activated by the THERMAL keyword in the RUNSPEC section and for when NTPVT on the TABDIMS keyword in the RUNSPEC section is set to two.

\--

\-- OIL DENSITY TEMPERATURE COEFFICIENTS (OPM FLOW THERMAL KEYWORD)

\--

\-- OIL DENSITY DENSITY

\-- TEMP COEFF1 COEFF2

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\--

OILDENT

1\* 1\* 1\* / TABLE NO. 01

1\* 1\* 1\* / TABLE NO. 02

There is no terminating "/" for this keyword.
