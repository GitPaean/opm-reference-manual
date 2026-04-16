### GASDENT -- Define Gas Density Temperature Coefficients

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[GASDENT](#__RefHeading___Toc123086_2509125675) defines the gas density as a function of temperature coefficients for when OPM Flow's thermal option has been activated by the [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979). Note this is an OPM Flow keyword used with OPM Flow's black-oil thermal model that is not available in the commercial simulator's black-oil thermal formulation.

This keyword can only be used if OPM Flow's thermal option has been activated by the [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Note this is different to the commercial simulator that uses the [TEMP](#__RefHeading___Toc146397_3544483072) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section to activate the black-oil thermal model.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [TEMP](#__RefHeading___Toc146397_3544483072) | [TEMP](#__RefHeading___Toc146397_3544483072) is a real positive value greater than zero that defines the absolute reference temperature used with TEXP1 and TEXP2 to estimate the change in gas density with respect to temperature. | Defined |
| ^o^R<br>527.67 | ^o^K<br>293.15 | ^o^K<br>293.15 |  |
| 2 | TEXP1 | TEXP1 is a real positive value greater than zero that defines the gas thermal expansion coefficient of the first order. | Defined |
| 1/^o^R<br>1.67 x 10^-4^ | 1/^o^K<br>3.0 x 10^-4^ | 1/^o^K<br>3.0 x 10^-4^ |  |
| 3 | TEXP2 | TEXP2 is a real positive value greater than zero that defines the gas thermal expansion coefficient of the second order. | Defined |
| 1/^o^R2<br>9.26 x 10^-7^ | 1/^o^K2<br>3.0 x 10^-6^ | 1/^o^K2<br>3.0 x 10^-6^ |  |
| Notes:<br>1)  The keyword is followed by NTPVT records as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each data set is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.3.73.1: GASDENT Keyword Description

The gas density at a given pressure and temperature is calculated from its value at surface conditions and the gas expansion factor (the reciprocal of the gas formation volume factor) as shown in the following equation:

Where the temperature dependence of the gas expansion factor relative to its value at the reference temperature is calculated as shown in the following equation:

Where:

= gas density

= gas expansion factor

= pressure

= temperature

= thermal expansion coefficients to first and second order

= subscript indicating surface conditions

= subscript indicating reference conditions

#### Example

The following example shows the [GASDENT](#__RefHeading___Toc123086_2509125675) keyword using the default values, for when the thermal option has been activated by the [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section and for when NTPVT on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section is set to two.

\--

\-- GAS DENSITY TEMPERATURE COEFFICIENTS (OPM FLOW THERMAL KEYWORD)

\--

\-- GAS DENSITY DENSITY

\-- TEMP COEFF1 COEFF2

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\--

GASDENT

1\* 1\* 1\* / TABLE NO. 01

1\* 1\* 1\* / TABLE NO. 02

There is no terminating "/" for this keyword.
