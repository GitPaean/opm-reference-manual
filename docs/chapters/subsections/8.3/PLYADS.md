### PLYADS -- Define Polymer Rock Adsorption Tables

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [PLYADS](#__RefHeading___Toc121087_57619843) keyword defines the rock polymer adsorption tables for when the polymer option has been activated by the [POLYMER](#__RefHeading___Toc38609_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Alternatively, the functions can be entered via the [PLYADSS](#__RefHeading___Toc121089_57619843) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section for when salt sensitivity is to be considered.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | POLCON | A columnar vector of real monotonically increasing down the column values that defines the polymer concentration in the solution surrounding the rock.<br>The first entry should be zero to define a no polymer concentration. | None |
| lb/stb | kg/sm^3^ | gm/scc |  |
| 2 | POLRATIO | A columnar vector of real increasing down the column values that defines the mass of adsorbed polymer per unit mass of rock.<br>The first entry should be zero to define a zero ratio of polymer concentration. | None |
| lb/lb | kg/kg | gm/gm |  |
| Notes:<br>1)  The keyword is followed by NTSFUN tables as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each table must contain a minimum of two rows and a maximum of NSSFUN rows as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.99: PLYADS Keyword Description

See also the [PLYADSS](#__RefHeading___Toc121089_57619843) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section to also define rock polymer adsorption tables when the polymer concentration is a function of salinity.

#### Example

\--

\-- POLYMER ROCK ADSORPTION TABLE

\--

PLYADS

\-- POLYMER POLYMER

\-- POLCON POLRATIO

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.0 0.00000

2.0 0.00003

4.0 0.00005

6.0 0.00007

8.0 0.00009

10.0 0.00011

12.0 0.00012

14.0 0.00015 / TABLE NO. 01

\-- POLYMER POLYMER

\-- POLCON POLRATIO

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.0 0.00000

3.0 0.00004

5.0 0.00006

7.0 0.00008

8.0 0.00009

10.0 0.00011 / TABLE NO. 02

The above example defines two polymer rock adsorption tables assuming NTSFUN equals two and NSSFUN is greater than or equal to eight on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

There is no terminating "/" for this keyword.
