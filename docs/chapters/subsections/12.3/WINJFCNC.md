### WINJFCNC -- Define Injection Well Filtrate Concentration

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WINJFCNC keyword defines the injected filtrate concentration for wells that have previously been defined by the WELSPECS keyword in the SCHEDULE section.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the filter cake properties are being defined.<br>Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | FCONCPPM | A real positive value that defines the volumetric concentration of filtrate in the injected water.<br>This value may be specified using a User Defined Argument (UDA). | 0 |
| ppm | ppm | ppm |  |
| Notes:<br>1)  User Defined Quantities (\"UDQ\") can be used as User Defined Arguments (\"UDA\") for various group, well, and connection keywords in the SCHEDULE section. User Defined Arguments are activated using the UDADIMS keyword in the RUNSPEC section, and defined by the UDQ keyword in the SCHEDULE section.<br>2)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/".<br>3)  New records overwrite previously specified data. |  |  |  |

Table 12.3.296.1: WINJFCNC Keyword Description

See also the WINJDAM keyword to define the filter cake properties and the WINJCLN keyword to signal that a filter cake should be completely or partially cleaned. All the aforementioned keywords are described in the SCHEDULE section.

#### Example

The following example defines the filtrate injection concentration for a water injection well using WINJFCNC:

\--

\-- WELL FILTRATE INJECTION CONCENTRATION

\--

\-- WELL FILTRATE

\-- NAME CONC

WINJFCNC

INJ-A1 10 /

INJ-B\* 30 /

/

Well INJ-A1 has a filtrate concentration of 10 ppm in the injection water, and wells matching INJ-B\* have a concentration of 30 ppm.
