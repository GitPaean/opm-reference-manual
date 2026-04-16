### SORWMIS -- Miscible Residual Oil versus Water Saturation Functions

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[SORWMIS](#__RefHeading___Toc121477_83452205) defines the dependency between the miscible residual oil saturation and the water saturation, for when the [MISCIBLE](#__RefHeading___Toc61978_4106839650) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section has been activated. The keyword can only be used with the [MISCIBLE](#__RefHeading___Toc61978_4106839650) option and for when the oil, water and gas phases are active in the model.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [SWAT](#__RefHeading___Toc137373_1317547213) | A columnar vector of real monotonically increasing down the column values starting from zero and terminating at one, that defines the water saturation. | None |
| dimensionless | dimensionless | dimensionless |  |
| 2 | SORMIS | A columnar vector of real equal or increasing down the column values that are greater than or equal to zero and less than one, that define the corresponding miscible residual oil saturation for the corresponding water saturation [SWAT](#__RefHeading___Toc137373_1317547213). | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by NTMISC tables as declared on the [MISCIBLE](#__RefHeading___Toc61978_4106839650) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each table must contain a minimum of two rows and a maximum of NSMISC rows as declared on the [MISCIBLE](#__RefHeading___Toc61978_4106839650) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.168: SORWMIS Keyword Description

#### Example

\--

\-- MISCIBLE RESIDUAL OIL VERSUS WATER SATURATION TABLE

\--

SORWMIS

\-- SWAT SORWMIS

\-- FRAC FRAC

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.0000 0.0000

0.2000 0.0000

1.0000 0.0000 / TABLE NO. 01

\-- SWAT SORWMIS

\-- FRAC FRAC

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.0000 0.0000

0.3000 0.1000

0.7500 0.1500 / TABLE NO. 02

The above example defines two miscible residual oil versus water saturation tables assuming NTMISC equals two and NSMISC is greater than or equal to three on the [MISCIBLE](#__RefHeading___Toc61978_4106839650) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.
