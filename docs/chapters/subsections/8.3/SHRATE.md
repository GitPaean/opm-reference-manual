### SHRATE -- Activate Log-based Polymer Shearing and Define the Shear Rate Constant

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword activates the logarithm-based polymer shear thinning/thickening option and defines the shear rate constant. This keyword can only be used in conjunction with the [PLYSHLOG](#__RefHeading___Toc110220_2939291539) in the [PROPS](#__RefHeading___Toc39329_784232322) section

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [SHRATE](#__RefHeading___Toc121475_83452205) | A positive real value that defines the shear rate constant. | 4.8 |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  This keyword is followed by NTPVT values as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each value is terminated by a \"/\" and there is no \"/\" terminator for the keyword. |  |  |  |

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
