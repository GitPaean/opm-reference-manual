### PLYADS -- Define Polymer Rock Adsorption Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The PLYADS keyword defines the rock polymer adsorption tables for when the polymer option has been activated by the POLYMER keyword in the RUNSPEC section. Alternatively, the functions can be entered via the PLYADSS keyword in the PROPS section for when salt sensitivity is to be considered.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | POLCON | A columnar vector of real monotonically increasing down the column values that defines the polymer concentration in the solution surrounding the rock.<br>The first entry should be zero to define a no polymer concentration. | None |
| lb/stb | kg/sm^3^ | gm/scc |  |
| 2 | POLRATIO | A columnar vector of real increasing down the column values that defines the mass of adsorbed polymer per unit mass of rock.<br>The first entry should be zero to define a zero ratio of polymer concentration. | None |
| lb/lb | kg/kg | gm/gm |  |
| Notes:<br>1)  The keyword is followed by NTSFUN tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NSSFUN rows as declared on the TABDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.99: PLYADS Keyword Description

See also the PLYADSS keyword in the PROPS section to also define rock polymer adsorption tables when the polymer concentration is a function of salinity.

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

The above example defines two polymer rock adsorption tables assuming NTSFUN equals two and NSSFUN is greater than or equal to eight on the TABDIMS keyword in the RUNSPEC section.

There is no terminating "/" for this keyword.
