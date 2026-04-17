### WINJDAM -- Define Well Filter Cake Properties

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WINJDAM keyword defines filter cake properties for wells that have previously been defined by the WELSPECS keyword in the SCHEDULE section. This keyword must be accompanied by the WINJFCNC keyword to define the injected filtrate concentration.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the filter cake properties are being defined.<br>Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | GEOMETRY | A defined character string that the filter cake geometry of the well. GEOMETRY must be set to one of the following character strings:<br>1)  LINEAR: the filter cake model will assume a linear geometry.<br>2)  RADIAL: the filter cake model will assume a radial geometry. | None |
| 3 | FCPERM | A real positive value that defines the filter cake permeability. | None |
| mD | mD | mD |  |
| 4 | FCPORO | A real positive value that defines the filter cake porosity. | 0.3 |
| dimensionless | dimensionless | dimensionless |  |
| 5 | FCRADIUS | Well radius to use in skin factor calculations.<br>If FCRADIUS is defaulted then half the diameter from the COMPDAT keyword item 9 will be used if it is defined otherwise 0.5 feet will be used. | 0.5 feet |
| feet | m | cm |  |
| 6 | FCAOF | A real positive value that defines the flow area for each connection.<br>If FCAOF is defaulted then the value will be evaluated as 2π*r*~*w*~*h*, where *r*~*w*~ is equal to FCRADIUS, and *h* is evaluated using the permeability thickness *kh* value from the COMPDAT keyword item 10 and the permeability FCPERM item 3 above. | 2π*r*~*w*~*h* |
| ft^2^ | m^2^ | cm^2^ |  |
| 7 | I | An integer that defines the matching connection location in the I-direction.<br>If set to \< 1 then all connections in the I-direction that also satisfy J and K criteria are selected. | -1 |
| 8 | J | An integer that defines the matching connection location in the J-direction.<br>If set to \< 1 then all connections in the J-direction that also satisfy I and K criteria are selected. | -1 |
| 9 | K | An integer that defines the matching connection location in the K-direction.<br>If set to \< 1 then all connections in the K-direction that also satisfy I and J criteria are selected. | -1 |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/".<br>2)  New records overwrite previously specified data for matching connections. |  |  |  |

Table 12.3.295.1: WINJDAM Keyword Description

See also the WINJFCNC keyword to define a well's injected filtrate concentration and the WINJCLN keyword to signal that a filter cake should be completely or partially cleaned. All the aforementioned keywords are described in the SCHEDULE section.

#### Example

The following example defines the filter cake properties for a water injection well using WINJDAM:

\--

\-- WELL FILTER CAKE PROPERTIES

\--

\-- WELL LINEAR/ PERM PORO WELL FLOW \--LOCATION\--

\-- NAME RADIAL RAD AREA II JJ KK

WINJDAM

INJ LINEAR 10 0.32 /

INJ RADIAL 1 0.25 1\* 1\* 0 0 3 /

/

Well INJ initially has a linear filter cake model for all completions with permeability of 10 mD, porosity of 0.32, and default well radius and flow area based on data from the COMPDAT keyword. This is then overwritten for completions in layer 3 with a radial filter cake model with permeability of 1 mD and porosity of 0.25 (again with default well radius and flow area).
