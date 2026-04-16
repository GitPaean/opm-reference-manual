<a id="__RefHeading___Toc179876_3429068809"></a>

### AQUCT -- Define Carter-Tracy Analytical Aquifers

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [AQUCT](#__RefHeading___Toc179876_3429068809) keyword defines Carter-Tracy[^1] [^2] analytical aquifers, the properties of the aquifer, including the Carter-Tracy aquifer influence function associated with the aquifer, defined by the [AQUTAB](#__RefHeading___Toc110746_846947960) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section.

Each row entry in the [AQUCT](#__RefHeading___Toc179876_3429068809) keyword defines one Carter-Tracy aquifer.

| 1 | AQUID | A positive integer greater than or equal to one and less than or equal to NANAQU on the [AQUDIMS](#__RefHeading___Toc10103_3701168388) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, that defines the Carter-Tracy aquifer number. | 1 |
| --- | --- | --- | --- |
| 2 | DATUM | DATUM is a single positive value that defines the Carter-Tracy reference datum depth for PRESS. | None |
| feet | m | cm |  |
| 3 | PRESS | PRESS is a single positive value that defines the aquifer pressure at DATUM.<br>If PRESS is defaulted then the simulator will set the aquifer's initial reservoir pressure to be in equilibrium with the cells the aquifer is contacted to. | 1\* |
| psia | barsa | atma |  |
| 4 | PERM | PERM is a real positive number that assigns the permeability to the aquifer. | None |
| mD | mD | mD |  |
| 5 | PORO | PORO is a real positive number greater than zero and less than or equal to one that assigns the porosity to the aquifer. | None |
| dimensionless | dimensionless | dimensionless |  |
| 6 | RCOMP | RCOMP is a real number defining the total (rock and water) compressibility (Ct) at the DATUM pressure. | None |
| 1/psia | 1/barsa | 1/atma |  |
| 7 | RE | RE is a real positive number that defines the Carter-Tracy aquifer external radius. | None |
| feet | m | cm |  |
| 8 | DZ | DZ is a real positive number that defines the Carter-Tracy aquifer average net thickness. | None |
| feet | m | cm |  |
| 9 | ANGLE | ANGLE is a real positive number that defines the angle of influence, that is the angular connection between the aquifer and the hydrocarbon reservoir. A value of 360^o^ degrees, the default value, indicates that the aquifer completely surrounds the hydrocarbon reservoir. | 360.0 |
| degrees | degrees | degrees |  |
| 10 | PVTNUM | PVTNUM is positive integer greater than zero and less than the NTPVT variable on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, that defines the [PVTW](#__RefHeading___Toc2086106_3315222525) table allocated to the Carter-Tracy aquifer. | 1 |
| 11 | AQUTAB | AQUTAB is positive integer greater than zero and less than the NIFTBL variable as declared on the [AQUDIMS](#__RefHeading___Toc10103_3701168388) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, that defines the AQUTAB table allocated to this Carter-Tracy aquifer.<br>The default value of one sets the internal infinite acting Carter-Tracy aquifer influence table not the first table in the [AQUTAB](#__RefHeading___Toc110746_846947960) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section The first table in the [AQUTAB](#__RefHeading___Toc110746_846947960) keyword is considered to be table number two.<br>The internal table, AQUTAB equal to one, is based on the Radial Flow, Constant Pressure and Constant Terminal Rate Cases for Infinite Reservoirs (Table I) in Van Everdingen and Hurst\'s [^3] paper. | 1 |
| 12 | SALTCON | SALTCON is a real positive number that defines the initial salt concentration in the aquifer, for when with simulator\'s Brine Model has been activated via the [BRINE](#__RefHeading___Toc162083_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>This variable is ignored by OPM Flow. | 0.0 |
| lb/stb | kg/sm^3^ | gm/scc |  |
| 13 | TEMP | TEMP is a real positive number that defines the initial temperature of the aquifer at DATUM for use with OPM Flow\'s thermal option. The [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section must be activated to use this option. | 1\* |
| ^o^F | ^o^C | ^o^C |  |
| Notes:<br>1)  The keyword is followed by up to NANAQ records as defined on the [AQUDIMS](#__RefHeading___Toc10103_3701168388) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section<br>2)  Each record is terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 6.9: AQUCT Keyword Description

In order to full define a Carter-Tracy aquifer one has to define the aquifer properties via the [AQUCT](#__RefHeading___Toc179876_3429068809) keyword, the Carter-Tracy influence function via the [AQUTAB](#__RefHeading___Toc110746_846947960) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section ([[AQUTAB -- Define Carter-Tracy Aquifer Influence Functions](#anchor-2)](#8.3.9.AQUTAB – Define Carter-Tracy Aquifer Influence Functions|outline)), if the default infinite acting table is not being employed, and finally, how the aquifer is connected to the reservoir using the [AQUANCON](#__RefHeading___Toc177536_3429068809) keyword in the [GRID](#__RefHeading___Toc38674_784232322) or [SOLUTION](#__RefHeading___Toc43947_784232322) sections.

#### Example

Given the following grid and aquifer dimensions in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section:

\--

\-- MAX MAX MAX

\-- NDIVIX NDIVIY NDIVIZ

DIMENS

20 1 5 /

\-- AQF AQF AQF AQF AQF AQF AQF AQF

\-- MXAQN MXNAQC NIFTBL NRIFTB NANAQU NCAMAX MXNALI MXAAQL

AQUDIMS

1\* 1\* 5 100 1 1\* 1\* 1\* /

And the [AQUTAB](#__RefHeading___Toc110746_846947960) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section

\--

\-- CARTER-TRACY AQUIFER INFLUENCE TABLES

\-- (STARTS FROM TABLE NO. 2, AS DEFAULT IS TABLE NO. 1)

\--

AQUTAB

\-- DIMLESS DIMLESS

\-- TIME PRESSURE

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\-\--

0.01 0.112

0.05 0.229

0.10 0.315

0.15 0.376

0.20 0.424

0.22 0.443

0.24 0.459

0.26 0.476

0.28 0.492

0.30 0.507

0.32 0.522

0.34 0.536

0.36 0.551

0.38 0.565

0.40 0.579

0.42 0.593

0.44 0.607

0.46 0.621

0.48 0.634

0.50 0.648

0.60 0.715

0.70 0.782

0.80 0.849

0.90 0.915

1.00 0.982

2.00 1.649

3.00 2.316

5.00 3.649

10.00 6.982

20.00 13.649

30.00 20.316

50.00 33.649

100.00 66.982

200.00 133.649

300.00 200.316

500.00 333.649

1000.00 666.982 /

The Carter-Tracy aquifer is defined in the [GRID](#__RefHeading___Toc38674_784232322) or [SOLUTION](#__RefHeading___Toc43947_784232322) sections as:

\-- ==============================================================================

\--

\-- SOLUTION SECTION

\--

\-- ==============================================================================

SOLUTION

\--

\-- CARTER-TRACY AQUIFER DESCRIPTION

\--

\-- ID DATUM AQF AQF AQF AQF AQF AQF INFL PVT AQU

\-- NUM DEPTH PRESS PERM PORO RCOMP RE DZ ANGLE NUM TAB

\--

AQUCT

1 2000.0 269 100.0 0.30 3.0e-5 330 10.0 360.0 1 2 /

/

And the connection of the aquifer is set in the [GRID](#__RefHeading___Toc38674_784232322) or [SOLUTION](#__RefHeading___Toc43947_784232322) sections as:

\--

\-- ANALYTIC AQUIFER CONNECTION

\--

\-- ID \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\-- CONNECT AQF AQF ADJOIN

\-- NUMBER I1 I2 J1 J2 K1 K2 FACE INFLX MULTI CELLS

AQUANCON

1 1 1 1 1 1 1 J- 1.0 1.0 \'NO\' /

/

Here one Carter-Tracy aquifer is connected to a single cell (1, 1, 1) at the J- face (or X- face) of the cell.

[^1]: Carter, R. D. and Tracy, G. W. "An Improved Method for Calculating Water Influx," Transactions of AIME (1960) 219, 215-417.

[^2]: Van Everdingen, A. & Hurst, W.,.The Application of the Laplace Transformation to Flow Problems in Reservoirs. Petroleum Transactions, AIME (December, 1949).

[^3]: Van Everdingen, A. & Hurst, W.,.The Application of the Laplace Transformation to Flow Problems in Reservoirs. Petroleum Transactions, AIME (December, 1949).
