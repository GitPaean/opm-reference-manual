### ROCK2D -- Pore Volume Compaction versus Pressure and Sw Tables

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [ROCK2D](#__RefHeading___Toc174483_4194303431) keyword defines rock compressibility pore volume multipliers as a function of pressure and water saturation ("Sw") for when the rock compaction option has been invoked by the [ROCKCOMP](#__RefHeading___Toc55593_1778172979) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The pressure values are defined on this keyword and the water saturations are declared on the associated [ROCKWNOD](#__RefHeading___Toc189921_4194303431) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section

The rock compaction pore volume and transmissibility multipliers, entered via the [ROCKTAB](#__RefHeading___Toc107256_3812137098), [ROCK2D](#__RefHeading___Toc174483_4194303431) and [ROCK2DTR](#__RefHeading___Toc180656_4194303431) keywords, are applied to the pore pressure, unless the [OVERBURD](#__RefHeading___Toc162159_4194303431) keyword in [PROPS](#__RefHeading___Toc39329_784232322) section is included in the input deck. When the [OVERBURD](#__RefHeading___Toc162159_4194303431) keyword is present the multipliers are applied to the effective pore volume pressure, that is. If the keyword is not present in the input deck then the overburden pressure is set to zero.

This keyword should only be used if compaction option has been enabled.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 1                                                                                                                                                                                                                      | > PRESS         | > A columnar vector of real monotonically increasing down the column values that defines the corresponding overburden pressure for the subsequent MULT columnar vector.                                                                                                                               | > None |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > psia                                                                                                                                                                                                                   | > bars          | > atm                                                                                                                                                                                                                                                                                                 |        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 2                                                                                                                                                                                                                      | > MULT          | > A columnar vector of real equal or decreasing down the column values that are less than or equal to one, that defines the rock compressibility pore volume multipliers corresponding to PRESS and for each water saturation entry in the [ROCKWNOD](#__RefHeading___Toc189921_4194303431) keyword.  | > None |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > dimensionless                                                                                                                                                                                                          | > dimensionless | > dimensionless                                                                                                                                                                                                                                                                                       |        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > Notes:                                                                                                                                                                                                                 |                 |                                                                                                                                                                                                                                                                                                       |        |
|                                                                                                                                                                                                                          |                 |                                                                                                                                                                                                                                                                                                       |        |
| 1)  The keyword is followed by NTROCC tables as declared on the [ROCKCOMP](#__RefHeading___Toc55593_1778172979) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.                                   |                 |                                                                                                                                                                                                                                                                                                       |        |
|                                                                                                                                                                                                                          |                 |                                                                                                                                                                                                                                                                                                       |        |
| 2)  Each table must contain a minimum of two rows and a maximum of NSSFUN rows as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.   |                 |                                                                                                                                                                                                                                                                                                       |        |
|                                                                                                                                                                                                                          |                 |                                                                                                                                                                                                                                                                                                       |        |
| 3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword.                                                                                                                                    |                 |                                                                                                                                                                                                                                                                                                       |        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+

Table 8.126: ROCK2D Keyword Description

See also the [OVERBURD](#__RefHeading___Toc162159_4194303431), [ROCKTAB](#__RefHeading___Toc107256_3812137098), [ROCK2DTR](#__RefHeading___Toc180656_4194303431), and [ROCKWNOD](#__RefHeading___Toc189921_4194303431) keywords in the [PROPS](#__RefHeading___Toc39329_784232322) section.

#### Example

The following example defines two pore volume compaction tables, assuming NTROCC is equal to two on the [ROCKCOMP](#__RefHeading___Toc55593_1778172979) keyword and NSSFUN is greater than or equal to four on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword.

\--

\-- ROCK COMPACTION VERSUS PRESSURE AND SW TABLES

\--

ROCK2D

\-- PRESS PORV FIRST ROCK2D TABLE DATA

\-- PSIA MULTIPLER

\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-\--

0.0 0.850

0.850

0.850

0.085 / P-SW SET TABLE NO. 01

\-- PRESS PORV

\-- PSIA MULTIPLER

\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-\--

1000.0 0.900

0.900

0.900

0.900 / P-SW SET TABLE NO. 01

\-- PRESS PORV

\-- PSIA MULTIPLER

\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-\--

2500.0 0.950

0.950

0.950

0.950 / P-SW SET TABLE NO. 01

\-- PRESS PORV

\-- PSIA MULTIPLER

\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-\--

5000.0 1.000

1.000

1.000

1.000 / P-SW SET TABLE NO. 01

\--

\-- PRESS PORV SECOND ROCK2D TABLE DATA

\-- PSIA MULTIPLER

\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-\--

0.0 0.800

0.800

0.800

0.800 / P-SW SET TABLE NO. 02

\-- PRESS PORV

\-- PSIA MULTIPLER

\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-\--

1000.0 0.880

0.880

0.880

0.880 / P-SW SET TABLE NO. 02

\-- PRESS PORV

\-- PSIA MULTIPLER

\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-\--

2500.0 0.950

0.950

0.950

0.950 / P-SW SET TABLE NO. 02

\-- PRESS PORV

\-- PSIA MULTIPLER

\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-\--

5000.0 1.000

1.000

1.000

1.000 / P-SW SET TABLE NO. 02

Note that there must be exactly NTROCC tables entered for this keyword, otherwise an error will occur.
