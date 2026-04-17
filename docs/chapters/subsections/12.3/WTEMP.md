### WTEMP -- Define An Injection Well's Fluid Temperature

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WTEMP keyword defines the temperature of the injection fluid being injected by an injection well.

This keyword can only be used if OPM Flow's thermal option has been activated by the THERMAL keyword in the RUNSPEC section. Note this is different to the commercial simulator that uses the TEMP keyword in the RUNSPEC section to activate the black-oil thermal model.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for an injection well for which the injection well fluid's temperature data is being defined.<br>Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | TEMP | A real positive value greater than zero that defines the temperature of the injected fluid. | None |
| ^o^F | ^o^C | ^o^C |  |
| Notes:<br>1)  Injection wells that are not declared via this keyword have their injection fluid temperatures set to zero degrees in the run's units.<br>2)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.126: WTEMP Keyword Description

See also the GCONINJE keyword to define a group's injection targets and constraints, and the WCONINJE keyword to define an injection well's targets and constraints. All the aforementioned keywords are described in the SCHEDULE section.

#### Example

The following example defines the injected fluid temperatures for three water injection wells for when the thermal option has been activated by the THERMAL keyword in the RUNSPEC section.

\--

\-- DEFINE INJECTION WELL FLUID TEMPERATURE

\--

\-- WELL FLUID

\-- NAME TEMP.

\-- \-\-\-\-\-\-\--

WTEMP

WI01 39.00 /

WI02 37.00 /

WI03 39.00 /

/

Here wells WI01 and WI03 inject water with a water temperature of 39 oF and well WI02's injection water temperature is 37 oF.
