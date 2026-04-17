### WMICP -- Define Water Injection Well's Microbial, Oxygen, And Urea Concentrations

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WMICP keyword defines a water injection well\'s microbial, growth, and cementation injection stream solutions, where the rate-limiting components are suspended microbes, oxygen, and urea concentrations respectively. These concentrations are used when the MICP keyword in the RUNSPEC section has been used to activate OPM Flow's Microbially Induced Calcite Precipitation model. See Landa-Marbán et al[^1] and [^2] for a description of the model.

Note the keyword should only be used for wells declared as water injection wells via the WCONINJE keyword in the SCHEDULE section.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well connection data is being defined.<br>Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | MICRCON | MICRCON is a real positive value that defines the microbial concentration of the well's injection stream. | 0.0 |
| lb/stb | kg/sm^3^ | gm/scc |  |
| 3 | OXYGCON | A real positive value that defines the oxygen concentration of the well's injection stream. | 0.0 |
| lb/stb | kg/sm3 | gm/scc |  |
| 4 | UREACON | UREACON is a real positive value that defines the urea concentration of the well's injection stream. | 0.0 |
| lb/stb | kg/sm^3^ | gm/scc |  |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.107: WMICP Keyword Description

Water injection wells that are not declared via this keyword have their concentrations defaulted to zero.

#### Example

\--

\-- DEFINE WATER INJECTION WELL MICROBIAL, OXYGEN, AND UREA CONCENTRATIONS

\--

\-- WELL MICROBIAL OXYGEN UREA

\-- NAME MICRCON OXYGCON UREACON

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

WMICP

WI01 0.01 /

WI02 1\* 0.04 /

WI03 1\* 1\* 60.0 /

WI04 1\* 0.04 60.0 /

/

Here the microbial concentration for well WI01 is set to 0.01, the oxygen concentration for well WI02 is set to 0.04, the urea concentration for well WI03 is set to 60, and the oxygen and urea concentrations for well WI04 are set to 0.04 and 60 respectively.

[^1]: Landa-Marbán, D., Tveit, S., Kumar, K., Gasda, S.E., 2021. Practical approaches to study microbially induced calcite precipitation at the eld scale. Int. J. Greenh. Gas Control 106, 103256. https://doi.org/10.1016/j.ijggc.2021.103256.

[^2]: Landa-Marbán, D., Kumar, K., Tveit, S., Gasda, S.E., 2021. Numerical studies of CO2 leakage remediation by micp-based plugging technology. In: Røkke, N.A. and Knuutila, H.K. (Eds) Short Papers from the 11th International Trondheim CCS conference, ISBN: 978-82-536-1714-5, 284-290.
