### FOAMADS -- Define Foam Rock Adsorption Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The FOAMADS keyword defines the foam rock adsorption tables for when the Foam option has been activated by the FOAM keyword in the RUNSPEC section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | FOAMCON | A columnar vector of real monotonically increasing down the column values that defines the foam concentration in the solution surrounding the rock.<br>The first entry should be zero to define a no foam concentration data set.<br>Units are dependent on the transport phase specified via the FOAMOPT1 variable on the FOAMOPTS keywod in the PROPS section. | None |
| Gas: lb/Mscf<br>Water: lb/stb | Gas: kg/sm^3^<br>Water: kg/sm^3^ | Gas: gm/scc<br>Water: gm/scc |  |
| 2 | FOAMRATI | A columnar vector of real increasing down the column values that defines the mass of adsorbed foam per unit mass of rock for a given FOAMCON.<br>The first table data set entry should be zero to define a no foam concentration data set. | None |
| lb/lb | kg/kg | gm/gm |  |
| Notes:<br>1)  The keyword is followed by NTSFUN tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NSSFUN rows as declared on the TABDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.3.58.1: FOAMADS Keyword Description

#### Example

\--

\-- FOAM ROCK ADSORPTION TABLE

\--

FOAMADS

\-- FOAM FOAM

\-- FOAMCON FOAMRATI

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.0 0.00000

2.0 0.00003

4.0 0.00005

6.0 0.00007

8.0 0.00009

10.0 0.00011

12.0 0.00012

14.0 0.00015 / TABLE NO. 01

\-- FOAM FOAM

\-- FOAMCON FOAMRATI

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.0 0.00000

3.0 0.00004

5.0 0.00006

7.0 0.00008

8.0 0.00009

10.0 0.00011 / TABLE NO. 02

The above example defines two foam rock adsorption tables assuming NTSFUN equals two and NSSFUN is greater than or equal to eight on the TABDIMS keyword in the RUNSPEC section.
