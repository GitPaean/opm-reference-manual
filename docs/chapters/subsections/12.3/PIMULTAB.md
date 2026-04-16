### PIMULTAB -- Define Well Productivity Index versus Water Cut Tables

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[PIMULTAB](#__RefHeading___Toc121637_2412586160) defines productivity index multiplier versus water cut tables that are used to scaled a well's connection factors based on connection's current producing water cut. The tables are used for modeling the productivity decline due to increasing water cut. Allocation of the tables to a well is via the [WPITAB](#__RefHeading___Toc121649_2412586160) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | WCUT | A real monotonically increasing positive columnar vector that defines the maximum surface water cut for the corresponding PIMULT vector. Water cut is defined as. | None |
| dimensionless | dimensionless | dimensionless |  |
| 2 | PIMULT | A real positive decreasing columnar vector that defines the productivity index multiplier used to scale a well's connection factors, for the corresponding WCUT vector. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by NTPIMT tables as stated on the [PIMTDIMS](#__RefHeading___Toc31215_1640804870) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each table must contain a minimum of two rows and a maximum of NRPIMT rows as declared on the [PIMTDIMS](#__RefHeading___Toc31215_1640804870) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 12.58: PIMULTAB Keyword Description

See also the [WPITAB](#__RefHeading___Toc121649_2412586160) keyword that allocates the tables to the wells, and also the [WPIMULT](#__RefHeading___Toc121645_2412586160) keyword that scales a well's productivity index by a constant value, both of which are in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Examples

Given NTPIMT equals two and NRPIMT equals four on [PIMTDIMS](#__RefHeading___Toc31215_1640804870) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, then:

\-- DEFINE WELL PRODUCTIVITY INDEX VERSUS WATER CUT TABLES

\--

\-- MAX PI

\-- WCUT MULT

\-- \-\-\-\-\-- \-\-\-\-\--

PIMULTAB

0.0000 1.0000

0.2500 0.9500

0.5000 0.8500

0.7500 0.7500 /

\--

\--

0.0000 1.0000

0.2500 0.9500

0.5000 0.8500

0.7500 0.7500 /

The next example is summarized from the Norne model with NTPIMT equals one and NRPIMT equals to 51 on the [PIMTDIMS](#__RefHeading___Toc31215_1640804870) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

\--

\-- DEFINE WELL PRODUCTIVITY INDEX VERSUS WATER CUT TABLES

\-- The following is the reviewed model in Aug-2006, low-high case

\-- a=0.25, b=0.1; PIMULT=(1-a)/exp(fw/b)+a

\--

\-- MAX PI

\-- WCUT MULT

\-- \-\-\-\-\-- \-\-\-\-\--

PIMULTAB

0.000 1.0000

0.025 0.8341

0.050 0.7049

0.075 0.6043

0.100 0.5259

0.125 0.4649

0.150 0.4173

0.175 0.3803

0.200 0.3515

0.225 0.3290

0.250 0.3116

0.275 0.2979

0.300 0.2873

0.325 0.2791

0.350 0.2726

0.375 0.2676

0.400 0.2637

0.425 0.2607

0.450 0.2583

0.475 0.2565

0.500 0.2551

0.525 0.2539

0.550 0.2531

0.575 0.2524

0.600 0.2519

0.625 0.2514

0.650 0.2511

0.675 0.2509

0.700 0.2507

0.725 0.2505

0.750 0.2504

0.775 0.2503

0.800 0.2503

0.825 0.2502

0.850 0.2502

0.875 0.2501

0.900 0.2501

0.925 0.2501

0.950 0.2501

0.975 0.2500

1.000 0.2500 /
