### PVDO -- Oil PVT Properties for Dead Oil

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[PVDO](#__RefHeading___Toc45803_719036256) defines the oil PVT properties for dead oil[^1]. If the oil has a constant and uniform dissolved gas concentration, Gas-Oil Ratio ("GOR"), and if the reservoir pressure never drops below the saturation pressure (bubble point pressure), then the model can be run more efficiently by omitting the [GAS](#__RefHeading___Toc38607_2267116897) and [DISGAS](#__RefHeading___Toc39767_2267116897) keywords from the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, treating the oil as a dead oil, and defining a constant Rs (GOR) value with keyword [RSCONST](#__RefHeading___Toc138398_332691817) or [RSCONSTT](#__RefHeading___Toc138400_332691817) in the [PROPS](#__RefHeading___Toc39329_784232322) section. This results in the model being run as a dead oil problem with no active gas phase. However, OPM Flow takes into account the constant Rs in the calculations and reporting.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | PRESS | A columnar vector of real monotonically increasing down the column values that defines the oil phase pressure. | None |
| psia | barsa | atma |  |
| 2 | OFVF | A columnar vector of real decreasing down the column values that defines the corresponding oil phase formation volume factor. | None |
| rb/stb | rm^3^/sm^3^ | rcc/scc |  |
| 3 | OVISC | A columnar vector of real increasing down the column values that defines the corresponding oil phase viscosity. | None |
| cP | cP | cP |  |
| Notes:<br>1)  The keyword is followed by NTPVT tables as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each table must contain a minimum of two rows and a maximum of NPPVT rows as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.115: PVDO Keyword Description

Note that provided the first table has been entered, subsequent tables may be defaulted, in this case the prior table is copied to the current table. See the second example for an illustration on how to use this feature.

See also the [RSCONST](#__RefHeading___Toc138398_332691817) and [RSCONSTT](#__RefHeading___Toc138400_332691817) keywords to define the constant Rs for dead oil and [PVCDO](#__RefHeading___Toc104054_57619843) as an alternative keyword to enter the dead oil properties.

#### Example

The example below defines two dead oil PVT tables with variable viscosity and compressibility with respect to pressure, and assumes that NTPVT equals two and NPPVT is greater than or equal to eight on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

\--

\-- OIL PVT TABLE FOR DEAD OIL

\--

PVDO

\-- PSAT BO VISC

\-- PSIA RB/STB CPOISE

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\--

400 1.0102 1.16

1200 1.0040 1.164

2000 0.9960 1.167

2800 0.9880 1.172

3600 0.9802 1.177

4400 0.9724 1.181

5200 0.9646 1.185

5600 0.9607 1.19 / TABLE NO. 01

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\--

800 1.0255 1.14

1600 1.0172 1.14

2400 1.0091 1.14

3200 1.0011 1.14

4000 0.9931 1.14

4800 0.9852 1.14

5600 0.9774 1.14 / TABLE NO. 02

The second example defines four dead oil PVT tables with variable viscosity and compressibility with respect to pressure, and assumes that NTPVT equals four and NPPVT is greater than or equal to eight on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Here table two defaults to table one, and table four defaults to table three.

\--

\-- OIL PVT TABLE FOR DEAD OIL

\--

PVDO

\-- PSAT BO VISC

\-- PSIA RB/STB CPOISE

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\--

400 1.0102 1.16

1200 1.0040 1.164

2000 0.9960 1.167

2800 0.9880 1.172

3600 0.9802 1.177

4400 0.9724 1.181

5200 0.9646 1.185

5600 0.9607 1.19 / TABLE NO. 01

/ TABLE NO. 02

800 1.0255 1.14

1600 1.0172 1.14

2400 1.0091 1.14

3200 1.0011 1.14

4000 0.9931 1.14

4800 0.9852 1.14

5600 0.9774 1.14 / TABLE NO. 03

/ TABLE NO. 04

There is no terminating "/" for this keyword.

[^1]: "Dead" oil is oil that it contains no dissolved gas or a relatively thick oil or residue that has lost its volatile components.
