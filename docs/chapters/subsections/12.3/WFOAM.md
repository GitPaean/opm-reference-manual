### WFOAM -- Define Well Foam Injection Concentrations

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WFOAM keyword defines an injection wells foam concentration. The foam option must be activated by the FOAM keyword in the RUNSPEC section in order to use this keyword. Note if a well's foam concentration is not set with this keyword then default value of zero is assigned to a well.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well injection foam concentration is being defined. | None |
| --- | --- | --- | --- |
| 2 | FOAMCON | A real positive value that defines the well's injection foam concentration.<br>This value may be specified using a User Defined Argument (UDA).<br>Units are dependent on the transport phase specified via the FOAMOPT1 variable on the FOAMOPTS keyword in the PROPS section. FOAMOPT1 should be set to either GAS or WATER.<br>Currently OPM Flow only supports injecting foam via the GAS phase. | None |
| Gas: lb/Mscf<br>Water: lb/stb | Gas: kg/sm^3^<br>Water: kg/sm^3^ | Gas: gm/scc<br>Water: gm/scc |  |
| Notes:<br>1)  User Defined Quantities (\"UDQ\") can be used as User Defined Arguments (\"UDA\") for various group, well, and connection keywords in the SCHEDULE section. User Defined Arguments are activated using the UDADIMS keyword in the RUNSPEC section, and defined by the UDQ keyword in the SCHEDULE section.<br>2)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.95: WFOAM Keyword Description

See also the FOAM keyword in the RUNSPEC section, the FOAMADS, FOAMOPTS and FOAMROCK keywords in the PROPS section.

#### Example

\--

\-- WELL INJECTION FOAM CONCENTRATION

\--

\-- WELL FOAM

\-- NAME FOAMCON

WFOAM

GI01 0.020 /

GI02 0.020 /

GI03 0.020 /

/

Here three gas wells are given an injection foam concentration of 0.020 lb/Mscf, assuming field units.
