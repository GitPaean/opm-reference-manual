### WPMITAB -- Assign Well Polymer Molecular Model Injection Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WPMITAB keyword assigns the well polymer molecular injection tables to water injection wells in OPM Flow\'s Polymer Molecular Weight Transport option, that uses the polymer molecular weight in calculating the polymer viscosity, as well as accounting for formation damage due to the water and polymer injection, by adjusting the wellbore skin pressure. This keyword should only be used if the POLYMER and POLYMW keywords in the RUNSPEC section are also activated. The keyword assigns the PLYMWINJ tables that are defined via the PLYMWINJ keyword in the PROPS section.

| 1 | WELNAME | A character string of up to eight characters in length, that defines the water injection well name, for which the well polymer molecular injection table, PLYMWINJ, is to be assigned.<br>Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | PLYMWINJ | A positive integer value that defines the corresponding PLYMWINJ table to be allocated to the water injection well.<br>A value less than or equal to zero means that no PLYMWIN table is allocated to the well | 0 |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.113: WPMITAB Keyword Description

See also the PLYMWINJ keyword in the PROPS section, that describes the relationship of the injected polymer molecular weight as a function of polymer throughput and polymer velocity, for the simulator\'s Polymer Molecular Weight Transport option, as well as the SKPRWAT, SKPRPOLY, and PLYVMH keywords, also in the PROPS section, that are the additional keywords required for the Polymer Molecular Weight Transport option.

The WSKPTAB keyword in the SCHEDULE section may be used to assign the SKPRWAT and SKPRPOL tables to water injections wells, that enable the calculation of the wellbore skin pressure based on the fluids being injected.

Note that the standard polymer property data keywords: PLYROCK, PLYADS, PLYMAX, etc., are still required to fully describe the polymer fluid.

#### Example

Given NTPMWINJ equals two on the PINTDIMS keyword in the RUNSPEC section, then:

\--

\-- ASSIGN WELL POLYMER MOLECULAR MODEL INJECTION TABLES

\--

\-- WELL PLYMWINJ

\-- NAME TABLE

WPMITAB

WI01 1 /

WI02 1 /

WI03 2 /

/

Assigns PLYMWINJ table one to wells WI01 and WI02 and table two to WI03.
