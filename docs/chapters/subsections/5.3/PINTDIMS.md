### PINTDIMS -- Define Polymer Molecular Weight Model Table Dimensions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The PINTDIMS keyword defines the number of property tables used in the OPM Flow\'s Polymer Molecular Weight Transport option, that uses the polymer molecular weight in calculating the polymer viscosity, as well as accounting for formation damage due to the water and polymer injection, by adjusting the wellbore skin pressure. This keyword should only be used if the POLYMER and POLYMW keywords in the RUNSPEC section are also activated. The PINTDIMS keyword defines the maximum number of tables for the SKPRWAT, SKPRPOLY, and PLYMWINJ keywords, and the number of entries in the PLYVMH keyword. All the aforementioned keywords are in the PROPS section.

| 1 | NTSKWAT | NTSKWAT is a positive integer that defines the number of SKPRWAT tables in the PROPS section, used to describe the relationship of wellbore skin pressure as a function of water throughput and water velocity, for the simulator\'s Polymer Molecular Weight Transport option. | 1 |
| --- | --- | --- | --- |
| 2 | NTSKPOLY | NTSKPOLY is a positive integer that defines the number of SKPRPOLY tables in the PROPS section, used to describe the relationship of wellbore skin pressure as a function of polymer throughput and polymer velocity, for the simulator\'s Polymer Molecular Weight Transport option. | 1 |
| 3 | NTPMWINJ | NTPMWINJ is a positive integer that defines the number of PLYMWINJ tables in the PROPS section, used to describe the relationship of the injected polymer molecular weight as a function of polymer throughput and polymer velocity, for the simulator\'s Polymer Molecular Weight Transport option. | 1 |
| 4 | NPLYVMH | NPLYVMH is a positive integer that defines the maximum number of entries (rows) in the PLYVMH table in the PROPS section, used to describe the relationship of the injected polymer viscosity as a function of polymer molecular weight and polymer concentration, for the simulator\'s Polymer Molecular Weight Transport option. | 1 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.36: PINTDIMS Keyword Description

The SKPRWAT, SKPRPOLY, PLYMWINJ, and PLYVMH keywords in the PROPS section, are the additional keywords required for the Polymer Molecular Weight Transport option. Note that the standard polymer property data keywords: PLYROCK, PLYADS, PLYMAX, etc., are still required to fully describe the polymer fluid.

#### Example

\--

\-- POLYMER MOLECULAR WEIGHT TRANSPORT TABLES (OPM FLOW RUNSPEC KEYWORD)

\--

\-- NO. NO. NO. NO.

\-- NTSKWAT NTSKPOLY NTPMWINJ NPLYVMH

PINTDIMS

2 2 2 1 /

The above example declares two SKPRWAT, SKPRPOLY, and PLYMWINJ keywords in the PROPS section will be used, as well as the default value of one for the number of rows in the PLYVMH keyword.
