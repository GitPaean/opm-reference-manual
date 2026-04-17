### WSKPTAB -- Assign Well Polymer Molecular Model Skin Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WSKPTAB keyword assigns the well polymer molecular water and polymer skin tables to water injection wells in OPM Flow\'s Polymer Molecular Weight Transport option, that uses the polymer molecular weight in calculating the polymer viscosity, as well as accounting for formation damage due to the water and polymer injection, by adjusting the wellbore skin pressure. This keyword should only be used if the POLYMER and POLYMW keywords in the RUNSPEC section are also activated. The keyword assigns the water SKPRWAT tables, that are defined via the SKPRWAT keyword in the PROPS section, that are used to calculable the wellbore skin pressure during water injection. As well as the polymer SKPRPOLY tables, that are defined via the SKPRPOLY keyword in the PROPS section, that are used to calculable the wellbore skin pressure during polymer injection.

| 1 | WELNAME | A character string of up to eight characters in length, that defines the water injection well name, for which the well water injection skin table, SKKPRWAT, and the polymer skin injection table, SKPRPOLY, are to be assigned.<br>Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | SKPRWAT | A positive integer value that defines the corresponding SKPRWAT table to be allocated to the water injection well.<br>A value less than or equal to zero means that no SKPRWAT table is allocated to the well | 0 |
| 3 | SKPRPOLY | A positive integer value that defines the corresponding SKPRPOLY table to be allocated to the water injection well.<br>A value less than or equal to zero means that no SKPRPOLY table is allocated to the well | 0 |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.123: WSKPTAB Keyword Description

See also the SKPRWAT and SKPRPOLY keywords in the PROPS section, that describe the relationship of the wellbore skin pressure with respect to the injected water and polymer throughput and fluid velocity, for the simulator\'s Polymer Molecular Weight Transport option. As well as the PLYMWINJ and PLYVMH keywords, also in the PROPS section, that are the additional keywords required for the Polymer Molecular Weight Transport option.

The WPMITAB keyword in the SCHEDULE section may be used to assign the PLYMWINJ keyword in the PROPS section. Where PLYMWINJ, describes the relationship of the injected polymer molecular weight as a function of polymer throughput and polymer velocity, for the simulator\'s Polymer Molecular Weight Transport option

Note that the standard polymer property data keywords: PLYROCK, PLYADS, PLYMAX, etc., are still required to fully describe the polymer fluid.

#### Example

Given NTSKWAT equals two and NTSKPOLY equals three on the PINTDIMS keyword in the RUNSPEC section, then:

\--

\-- ASSIGN WELL POLYMER MOLECULAR MODEL SKIN TABLES

\--

\-- WELL SKPRWAT SKPRPOLY

\-- NAME TABLE TABLE

WSKPTAB

WI01 1 1 /

WI02 1 3 /

WI03 2 2 /

/

Assigns SKPRWAT table one to wells WI01 and WI02 and table two to WI03, and SKPRPOLY tables one, two and three to wells WI01, WI03, and WI02, respectively.
