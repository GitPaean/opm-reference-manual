### PLYATEMP -- Define Polymer Adsorption Table Temperature

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the polymer adsorption temperature for subsequent polymer adsorption tables entered via the [PLYADS](#__RefHeading___Toc121087_57619843) and [PLYADSS](#__RefHeading___Toc121089_57619843) keywords in the [PROPS](#__RefHeading___Toc39329_784232322) section. The Polymer option must have been activated by the [POLYMER](#__RefHeading___Toc38609_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section and the Thermal option invoked by the [THERMAL](#__RefHeading___Toc137276_650382403) keyword, also in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [PLYATEMP](#__RefHeading___Toc787898_2928331029) | Single real positive value that defines polymer adsorption temperature for subsequent polymer adsorption tables. | None |
| ^o^F | ^o^C | ^o^C |  |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 8.101: PLYATEMP Keyword Description

#### Example

The example shows how to enter the polymer adsorption data using the [PLYADS](#__RefHeading___Toc121087_57619843) keyword for two different temperatures.

\--

\-- RESERVOIR

\-- TEMPERATURE

\-- \-\-\-\-\-\-\-\-\-\--

PLYATEMP

60.0 / TEMPERATURE

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

\--

\-- POLYMER POLYMER

\-- POLCON POLRATIO

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.0 0.00000

3.0 0.00004

5.0 0.00006

7.0 0.00008

8.0 0.00009

10.0 0.00011 / TABLE NO. 02

\--

\-- RESERVOIR

\-- TEMPERATURE

\-- \-\-\-\-\-\-\-\-\-\--

PLYATEMP

120.0 / TEMPERATURE

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

\--

\-- POLYMER POLYMER

\-- POLCON POLRATIO

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.0 0.00000

3.0 0.00004

5.0 0.00006

7.0 0.00008

8.0 0.00009

10.0 0.00011 / TABLE NO. 02

Here the first [PLYATEMP](#__RefHeading___Toc787898_2928331029) keyword defines the temperature to be 60 oF for the subsequent two polymer rock adsorption tables, assuming NTSFUN equals four and NSSFUN is greater than or equal to eight on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The next [PLYATEMP](#__RefHeading___Toc787898_2928331029) keyword defines the temperature to be 120 oF for the subsequent two polymer rock adsorption tables.
