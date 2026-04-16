### MISCIBLE -- Define Miscibility Todd-Longstaff Parameters

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [MISCIBLE](#__RefHeading___Toc61978_4106839650) keyword defines the options associated with the Todd-Longstaff[^1] mixing parameters used for when polymer flooding or CO2 EOR simulation cases are being run.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | NTMISC | A positive integer value that declares the number miscible residual oil saturations versus water saturations tables for [SORWMIS](#__RefHeading___Toc121477_83452205) keyword and the number Todd-Longstaff mixing parameters entries on the [TLMIXPAR](#__RefHeading___Toc121483_83452205) keyword. | 1 |
| 2 | NSMISC | A positive integer value that sets the maximum number of entries (or rows) for each [SORWMIS](#__RefHeading___Toc121477_83452205) table defined by the [SORWMIS](#__RefHeading___Toc121477_83452205) keyword. | 20 |
| 3 | MISOPT | A character string that defines the numerical dispersion control options for the oil and gas relative permeability curves, set to either NONE or TWOPOINT:<br>1)  NONE -- standard single point up streaming, that is using the immediate neighbor<br>2)  TWOPOINT -- two-point up streaming, that is using the immediate neighbor plus one cell for better numerical dispersion control but with a higher computational cost.<br>Only the default value of NONE is supported. | NONE |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.21: MISCIBLE Keyword Description

#### Example

\--

\-- NTAB MAX UPSTRM

\-- NTMISC NSMISC MISOPT

MISCIBLE

1 20 NONE /

The above example defines the default values for the [MISCIBLE](#__RefHeading___Toc61978_4106839650) keyword, that is one table with a maximum of 20 rows per table using the standard one cell upstream option.

[^1]: M. R. Todd and W. J Longstaff, The Development, Testing, and Application Of a Numerical Simulator for Predicting Miscible Flood Performance\". In: J. Petrol. Tech. 24.7 (1972), pages 874-882.
