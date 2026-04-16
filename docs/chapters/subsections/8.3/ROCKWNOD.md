### ROCKWNOD -- Water Saturation Values for Compaction Pressure-Sw Tables

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [ROCK2D](#__RefHeading___Toc174483_4194303431) and the [ROCK2DTR](#__RefHeading___Toc180656_4194303431) keywords in the [PROPS](#__RefHeading___Toc39329_784232322) section define rock compressibility pore volume and transmissibility multipliers as a function of pressure and water saturation ("Sw"), for when the rock compaction option has been invoked by the [ROCKCOMP](#__RefHeading___Toc55593_1778172979) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The pressure values are defined on [ROCK2D](#__RefHeading___Toc174483_4194303431) and the [ROCK2DTR](#__RefHeading___Toc180656_4194303431) keywords together with the multipliers. This keyword [ROCKWNOD](#__RefHeading___Toc189921_4194303431), defines the water saturations that are used in conjunction with the [ROCK2D](#__RefHeading___Toc174483_4194303431) and the [ROCK2DTR](#__RefHeading___Toc180656_4194303431) keywords.

This keyword should only be used if compaction option has been enabled.

| 1 | [SWAT](#__RefHeading___Toc137373_1317547213) | A columnar vector of real monotonically increasing down the column values that defines the water saturations to be associated with the data on the [ROCK2D](#__RefHeading___Toc174483_4194303431) and the ROCKTR keywords. | None |
| --- | --- | --- | --- |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by NTROCC tables as declared on the [ROCKCOMP](#__RefHeading___Toc55593_1778172979) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each table must contain a minimum of two rows and a maximum of NSSFUN rows as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.131: ROCKWNOD Keyword Description

See also the [OVERBURD](#__RefHeading___Toc162159_4194303431), [ROCKTAB](#__RefHeading___Toc107256_3812137098), [ROCK2D](#__RefHeading___Toc174483_4194303431) and [ROCK2DTR](#__RefHeading___Toc180656_4194303431) keywords in the [PROPS](#__RefHeading___Toc39329_784232322) section.

#### Example

The following example defines two [ROCKWNOD](#__RefHeading___Toc189921_4194303431) tables for the pore volume and transmissibility compaction tables, assuming NTROCC is equal to two on the [ROCKCOMP](#__RefHeading___Toc55593_1778172979) keyword and NSSFUN is greater than or equal to four on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword.

\--

\-- WATER SATURATION VALUES FOR COMPACTION PRESSURE-SW TABLES

\--

ROCKWNOD

\-- COMPACT

\-- SWAT

\-- \-\-\-\-\--

0.000

0.200

0.400

1.000 / P-SW SET TABLE NO. 01

\-- COMPACT

\-- SWAT

\-- \-\-\-\-\--

0.000

0.250

0.750

1.000 / P-SW SET TABLE NO. 02

Note that there must be exactly NTROCC tables entered for this keyword, otherwise an error will occur.
