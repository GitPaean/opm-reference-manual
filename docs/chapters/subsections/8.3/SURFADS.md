### SURFADS -- Define Surfactant Rock Adsorption Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SURFADS keyword defines the rock surfactant adsorption tables for when the surfactant option has been activated by the SURFACT keyword in the RUNSPEC section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SURCON | A columnar vector of real monotonically increasing down the column values that defines the surfactant concentration in the solution surrounding the rock.<br>The first entry should be zero to define a no surfactant concentration. | None |
| lb/stb | kg/sm^3^ | gm/scc |  |
| 2 | SURRATIO | A columnar vector of real increasing down the column values that defines the mass of adsorbed surfactant per unit mass of rock of the saturated concentration of surfactant adsorbed by the rock.<br>The first entry should be zero to define a zero ratio of surfactant concentration. | None |
| lb/lb | kg/kg | gm/gm |  |
| Notes:<br>1)  The keyword is followed by NTSFUN tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NSSFUN rows as declared on the TABDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.181: SURFADS Keyword Description

See also the ADSORP keyword in the PROPS section that employs adsorption functions, as oppose to adsorption tables, to define rock surfactant adsorption behavior.

#### Example

\--

\-- SURFACTANT ROCK ADSORPTION TABLE

\--

SURFADS

\-- SURF SURF

\-- SURCON SURRATIO

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.0 0.00000

2.0 0.00003

4.0 0.00005

6.0 0.00007

8.0 0.00009

10.0 0.00011

12.0 0.00012

14.0 0.00015 / TABLE NO. 01

\-- SURF SURF

\-- SURCON SURRATIO

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.0 0.00000

3.0 0.00004

5.0 0.00006

7.0 0.00008

8.0 0.00009

10.0 0.00011 / TABLE NO. 02

The above example defines two surfactant rock adsorption tables assuming NTSFUN equals two and NSSFUN is greater than or equal to eight on the TABDIMS keyword in the RUNSPEC section.

There is no terminating "/" for this keyword.
