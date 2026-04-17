### PLYADSS -- Define Polymer Rock Adsorption with Salt Dependence Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The PLYADSS keyword defines the rock polymer adsorption tables for when the polymer and the salt options has been activated by the POLYMER and BRINE keywords in the RUNSPEC section.

Note that the BRINE option is not currently supported by OPM Flow; however, the polymer rock adsorption functions without salt dependence may be entered via the PLYADS keyword in the PROPS section, for when salt sensitivity is not to be considered.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | POLCON | A columnar vector of real monotonically increasing down the column values that defines the polymer concentration in the solution surrounding the rock.<br>The first entry should be zero to define a no polymer and no salt concentration data set.<br>POLCON should only be given for the first entry of the POLCON/POLRATIO set and skipped until another POLCON/POLRATIO table is entered. | None |
| lb/stb | kg/sm^3^ | gm/scc |  |
| 2 | POLRATIO | A columnar vector of real increasing down the column values that defines the mass of adsorbed polymer per unit mass of rock of the saturated concentration of polymer adsorbed by the rock for a given POLCON and the salt concentration given by SALTCON on the ADSALNOD keyword in the PROPS section.<br>The first table data set entry should be zero to define a no polymer and no salt concentration data set.<br>Subsequent POLRATIO values define the POLCON/POLRATIO combinations for a given salt concentration as listed (and in the same order) by the SALTCON variable on the ADSALNOD keyword in the PROPS section.<br>Each POLCON/POLRATIO/SALT data sets should be terminated by a "/" | None |
| lb/lb | kg/kg | gm/gm |  |
| Notes:<br>1)  The keyword is followed by NTSFUN tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NSSFUN rows as declared on the TABDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.100: PLYADSS Keyword Description

See also the PLYADS keyword in the PROPS section to also define rock polymer adsorption tables when the polymer concentration is not a function of salinity.

#### Example

\--

\-- SETS SALT CONCENTRATION FOR POLYMER SOLUTION ADSORPTION

\-- VIA SATNUM ARRAY ALLOCATION

\--

\-- SALT

\--

ADSALNOD

1.0

5.0

10.5

25.0 / SATNUM TABLE NO. 01

\--

\-- POLYMER ROCK ADSORPTION WITH SALT *DEPENDENCY* TABLE

\--

PLYADSS

\-- POLYMER POLYMER

\-- POLCON POLRATIO

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.0 0.00000

0.00000

0.00000

0.00000 / TABLE NO. 01

\-- POLYMER POLYMER

\-- POLCON POLRATIO

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

1.0 0.00002

0.00003

0.00004

0.00005 / TABLE NO. 02

\-- POLYMER POLYMER

\-- POLCON POLRATIO

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

2.0 0.00003

0.00004

0.00005

0.00006 / TABLE NO. 03

\-- POLYMER POLYMER

\-- POLCON POLRATIO

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

3.0 0.00004

0.00005

0.00006

0.00007 / TABLE NO. 04

The above example defines four polymer rock adsorption tables for four salt concentration on the ADSALNOD keyword, assuming NTSFUN equals one and NSSFUN is greater than or equal to four on the TABDIMS keyword in the RUNSPEC section.

There is no terminating "/" for this keyword.
