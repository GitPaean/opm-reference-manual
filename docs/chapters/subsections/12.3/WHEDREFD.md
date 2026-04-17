### WHEDREFD -- Define Well Hydraulic Head Reference Depth

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WHEDREFD keyword sets the hydraulic head reference depth for reporting the hydraulic head pressure for the well, for wells that have previously been defined by the WELSPECS keyword in the SCHEDULE section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well hydraulic head reference depth data is being defined. | None |
| --- | --- | --- | --- |
| 2 | HYDREF | A real value that defines the hydraulic head reference depth for reporting the hydraulic head pressure for the well.<br>HYDREF cannot be defaulted on the keyword; however if a well has not been set by this keyword HYDREF is set equal to the value on the HYDRHEAD keyword. | None |
| feet | m | cm |  |
| Notes:<br>1)  The keyword is followed by any number records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.97: WHEDREFD Keyword Description

See also the HYDRHEAD keyword in the PROPS section.

#### Example

The following example defines three wells hydraulic head reference depths for reporting, using the WHEDREFD keyword

\--

\-- WELL HYDRAULIC HEAD REFERENCE DEPTH

\--

\-- WELL HYDREF

\-- NAME DEPTH

WHEDREFD

OP01 150.0 /

OP02 175.0 /

OP03 150.0 /

/

Here, well OP01 and OP03 have their hydraulic head reference depths set to 150.0 ft and well OP02's hydraulic head reference depth is set to 175.0 ft.
