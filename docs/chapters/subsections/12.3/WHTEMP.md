### WHTEMP -- Define Well Tubing Head Temperature Parameters

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, WHTEMP, sets the parameters for the Tubing Head Temperature calculation, which can either be a constant value, or from a table lookup using a VFPPROD table, via the VFPPROD keyword in the SCHEDULE section, containing tubing head temperature data.

This keyword can only be used if the thermal option has been activated by the THERMAL keyword in the RUNSPEC section. Note this is different to the commercial simulator that uses the TEMP keyword in the RUNSPEC section to activate the black-oil thermal model.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well production targets and constraints data are being defined.<br>Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | VFPTAB | A positive integer greater than or equal to zero that references the production vertical lift performance table (VFPPROD), containing the tubing head temperature data for the well.<br>Note, a well must have both a VFPPROD pressure and a VFPPROD temperature table, if the tubing head temperatures are to be calculated.<br>Alternatively, if a constant tubing head temperature for a production well is to be defined via the TEMP parameter, then VFPTAB should be defaulted with 1\* instead. | None |
| dimensionless | dimensionless | dimensionless |  |
| 3 | TEMP | A real positive value greater than zero that defines a constant tubing head temperature for a production well.<br>In this case the VFPTAB parameter should be defaulted with 1\* if a constant tubing head temperature for a production well. | None |
| ^o^F | ^o^C | ^o^C |  |
| Notes:<br>1)  Note either VFPTAB or TEMP must be supplies, that is one can specify both.<br>2)  The keyword is followed by any number records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.99: WHTEMP Keyword Description

See also the VFPPROD keyword in the SCHEDULE section.

#### Example

The following example defines three wells tubing head temperature parameters using the WHTEMP keyword

\--

\-- DEFINE WELL TUBING HEAD TEMPERATURE PARAMETERS

\--

\-- WELL VFP TUB

\-- NAME TABLE TEMP

WHTEMP

OP01 5 /

OP02 1\* 150 /

OP03 5 /

/

Here, well OP01 and OP03 used VFPPROD table number five to calculate the tubing head temperature, and well OP02's uses a constant 150o tubing head temperature.
