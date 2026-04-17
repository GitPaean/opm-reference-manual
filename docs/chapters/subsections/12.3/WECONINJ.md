### WECONINJ -- Well Economic Criteria for Injection Wells

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WECONINJ keyword defines economic criteria for injection wells that have previously been defined by the WELSPECS and WCONINJE keywords in the SCHEDULE section.

Note that wells can be allocated to a group when they are specified by the WELSPECS keyword and groups can also have economic controls. Wells under group control are therefore subject to the economic criteria set via the GCONINJE keyword in the SCHEDULE section and the controls specified by this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well economic injection criteria data is being defined.<br>Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | MINVALUE | A real positive value that defines the minimum economic injection value, below which an economic action will take place, as defined by the AUTO parameter on the WELSPECS keyword (SHUT or STOP). Note that TYPE determines if the minimum value is applied to the well's actual injection rate or the well's potential.<br>A value less than or equal to zero switches off this criterion. | 0.0 |
| Liquid stb/d<br>Gas Mscf/d | Liquid sm^3^/day<br>Gas sm3/day | Liquid scc/hour<br>Gas scc/hour |  |
| 3 | TYPE | A defined character string that determines if MINVALUE is applied to a well's actual rate or potential, and should be set to one of the following:<br>1)  RATE: In this case the MINVALUE is applied to a well's actual rate.<br>2)  POTN: Here, MINVALUE is applied to the well's potential with only the BHP and THP constraints applied.<br>The default value is RATE. | RATE |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.82: WECONINJ Keyword Description

See also the WELSPECS keyword to define a wells shut-in or stop options and GCONINJE for group controls in the SCHEDULE section.

#### Example

The following example defines the economic injection parameters for all gas and water injection wells.

\--

\-- WELL ECONOMIC LIMIT DATA FOR INJECTION WELLS

\--

\-- WELL MIN RATE

\-- NAME VALUE POTN

WECONINJ

GI\* 2.0E3 RATE /

WI\* 5.0E3 POTN /

/

Here all the gas injection wells have a minimum economic gas injection rate of 2 MMscf/d and the water injection wells have a minimum water potential rate of 5,000 stb/d. The AUTO parameter on the WELSPECS keyword will determine if the wells will be shut-in or stopped.
