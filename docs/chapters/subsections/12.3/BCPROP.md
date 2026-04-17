### BCPROP -- Define Boundary Conditions Properties

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The BCPROP keyword defines the type and properties of the boundary conditions.

Together the BCCON and BCPROP keywords define the boundary conditions for the model, and can be used to set boundary conditions for when external influx or efflux volumes are influencing the reservoir pressure and production history. For example, when the average reservoir pressure remains constant throughout the production period due to water influx, or gas migration from an external source.

| 1 | INDEX | A positive integer that identifies the boundary condition. | None |
| --- | --- | --- | --- |
| 2 | TYPE | A defined character string that defines the type of boundary condition to be applied, and should be set to one of the following character strings:<br>1)  DIRICHLET: for user defined boundary conditions. In this case, COMPONENT for the fluid type, and PRESS and TEMP for the constant pressure and temperature boundary conditions must be specified.<br>2)  FREE: for the initial state of the boundary to be kept throughout the simulation, that is a constant boundary condition. The remaining items should be defaulted.<br>3)  RATE: for the boundary to have a constant influx or efflux rate. In this case, COMPONENT for the fluid type, and RATE to set the mass rate per unit area must be specified.<br>4)  THERMAL: Constant temperature boundary condition (no-flow of mass).<br>5)  NONE: No flow boundary condition. | None |
| 3 | COMPONENT | A defined character string that sets fluid type used in the boundary calculations, and should be set to one of the following character strings:<br>1)  GAS: the gas phase will be used to control the boundary conditions for when the TYPE has been set to DIRICHLET or RATE.<br>2)  OIL: the oil phase will be used to control the boundary conditions for when the TYPE has been set to DIRICHLET or RATE .<br>3)  WATER or WAT: the water phase will be used to control the boundary conditions for when the TYPE has been set to DIRICHLET or RATE.<br>4)  SOLVENT: the solvent component will be used to control the boundary conditions for when the TYPE has been set to RATE.<br>5)  POLYMER: the polymer component will be used to control the boundary conditions for when the TYPE has been set to RATE.<br>6)  MICR: the microbial component will be used to control the boundary conditions for when the TYPE has been set to RATE.<br>7)  OXYG: the oxygen component will be used to control the boundary conditions for when the TYPE has been set to RATE.<br>8)  UREA: the urea component will be used to control the boundary conditions for when the TYPE has been set to RATE.<br>9)  NONE: the fluid type is undefined.<br>COMPONENT must be declared and not equal to NONE if TYPE has been set to either DIRICHLET or RATE. MICR requires the BIOFILM or MICP keyword, and OXYG or UREA requires the MICP keyword. | NONE |
| 4 | RATE | A real value that defines the constant mass rate per unit area of the specified COMPONENT to be injected or withdrawn at the boundary, when TYPE has been set to RATE.<br>Note a negative value implies an influx rate, whereas, a positive value indicates an efflux. | 0.0 |
| lb/day/ft^2^ | kg/day/m^2^ | gm/hour/cm^2^ |  |
| 5 | PRESS | PRESS is a real positive value that defines the constant pressure boundary condition. PRESS should only be entered if TYPE has been set to DIRICHLET. If the pressure at the boundary is less than PRESS, then the fluid type declared via COMPONENT will flow across the boundary.<br>The default value of 1\* will use the simulator\'s calculated value based on data entered via the EQUIL keyword in the SOLUTION section. | 1\* |
| psia | barsa | atma |  |
| 6 | TEMP | TEMP is a real positive number that defines the constant temperature boundary condition. TEMP should only be entered if TYPE has been set to DIRICHLET or THERMAL.<br>The default value of 1\* will use the simulator\'s calculated value based on data entered via one of the following reservoir temperature keywords: RTEMP, RTEMPA, RTEMPVD, TEMPI, or TEMPVD, in the SOLUTION section. Note that all of the aforementioned reservoir temperature keywords, except for TEMPI, may also be used in the PROPS section as well. | 1\* |
| ^o^F | ^o^C | ^o^C |  |
| 7 | MECHTYPE | A defined character string that defines the type of geo-mechanical boundary condition to be applied, and should be set to one of the following character strings:<br>1)  FREE: Surface is free to move with no external stress.<br>2)  FIXED: Surface is fixed in the x/y/z-directions if FIXEDX / FIXEDY / FIXEDZ \> 0. The displacement in each direction defined by DISPX / DISPY / DISPZ. The external stess is defined by STRESSXX / STRESSYY / STRESSZZ.<br>3)  NONE: No geo-mechanical boundary condition. | NONE |
| 8 | FIXEDX | A positive integer that identifies the whether the boundary is free or fixed in the x-direction.<br>A value of 0 implies the boundary is free to move in the x-direction. A value \> 0 implies the boundary is fixed in the x-direction with displacement defined by DISPX, | 1 |
| 9 | FIXEDY | A positive integer that identifies the whether the boundary is free or fixed in the y-direction.<br>A value of 0 implies the boundary is free to move in the y-direction. A value \> 0 implies the boundary is fixed in the y-direction with displacement defined by DISPY, | 1 |
| 10 | FIXEDZ | A positive integer that identifies the whether the boundary is free or fixed in the z-direction.<br>A value of 0 implies the boundary is free to move in the z-direction. A value \> 0 implies the boundary is fixed in the z-direction with displacement defined by DISPZ, | 1 |
|  | STRESSXX | A real value that defines the diagonal component of the stress tensor. | 0 |
| psia | barsa | atma |  |
|  | STRESSYY | A real value that defines the diagonal component of the stress tensor. | 0 |
| psia | barsa | atma |  |
|  | STRESSZZ | A real value that defines the diagonal component of the stress tensor. | 0 |
| psia | barsa | atma |  |
|  | DISPX | A real value that defines the x-direction displacement boundary condition. | 0 |
| feet | m | cm |  |
|  | DISPY | A real value that defines the y-direction displacement boundary condition. | 0 |
| feet | m | cm |  |
|  | DISPZ | A real value that defines the z-direction displacement boundary condition. | 0 |
| feet | m | cm |  |
| Notes:<br>1)  The boundary condition connections must have been specified using the BCCON keyword.<br>2)  Cells colored orange indicate parameters for the geo-mechanical boundary conditions that are only supported by the experimental geo-mechanical simulator.<br>3)  Each record must be terminated by a "/" and the keyword is terminated by a "/\". |  |  |  |

Table 12.3.16.1: BCPROP Keyword Description

See also the AQUFLUX keyword that is supported by OPM Flow in both the SOLUTION and SCHEDULE sections, to define a constant flux analytical aquifer.

If the BCCON and BCPROP keywords are not present in the input deck, then the boundary conditions for the model are set to be no flow, which is the normal behavior in both OPM Flow and the commercial simulator.

The BC keyword has been replaced by the BCCON and BCPROP keywords.

#### Examples

The first example shows how to set a constant pressure boundary using TYPE equal to FREE:

\--

\-- DEFINE BOUNDARY CONDITIONS CONNECTION (OPM FLOW GRID KEYWORD)

\--

\--INDEX \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\-- BC

\-- I1 I2 J1 J2 K1 K2 DIRC

BCCON

1 1 1 1 1\* 1 1\* X- /

2 1 1\* 1 1 1 1\* Y /

/

\--

\-- DEFINE BOUNDARY CONDITIONS PROPERTIES (OPM FLOW SCHEDULE KEYWORD)

\--

\--INDEX BC BC BC BC BC

\-- TYPE COMPT RATE PRESS TEMP

BCPROP

1 FREE 1\* 1\* 1\* 1\* /

2 FREE /

/

With this option it is only necessary to define the boundary cells and all the other parameters (COMPONENT, RATE, PRESS, and TEMP) can be defaulted, as they are ignored when TYPE equals FREE.

The next example is based on NX, NY and NZ equal to 20, 1, 10 respectively, on the DIMENS keyword in the RUNSPEC section, and shows how different boundary types can be assigned to different parts of the model.

\--

\-- DEFINE BOUNDARY CONDITIONS CONNECTION (OPM FLOW GRID KEYWORD)

\--

\--INDEX \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\-- BC

\-- I1 I2 J1 J2 K1 K2 DIRC

BCCON

1 1 1 1 1 1 10 X- /

2 20 20 1 1 1 10 X /

/

\--

\-- DEFINE BOUNDARY CONDITIONS PROPERTIES (OPM FLOW SCHEDULE KEYWORD)

\--

\--INDEX BC BC BC BC BC

\-- TYPE COMPT RATE PRESS TEMP

BCPROP

1 DIRICHLET GAS 1\* 256.0 100.0 /

2 FREE 4\* /

/

The last example shows how the DIRICHLET boundary condition option may be used:

\--

\-- DEFINE BOUNDARY CONDITIONS CONNECTION (OPM FLOW GRID KEYWORD)

\--

\--INDEX \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\-- BC

\-- I1 I2 J1 J2 K1 K2 DIRC

BCCON

1 1 1 1 1\* 1 1\* X- /

2 1 1\* 1 1 1 1\* Y /

/

\--

\-- DEFINE BOUNDARY CONDITIONS PROPERTIES (OPM FLOW SCHEDULE KEYWORD)

\--

\--INDEX BC BC BC BC BC

\-- TYPE COMPT RATE PRESS TEMP

BCPROP

1 DIRICHLET WAT 1\* 256.0 100.0 /

2 DIRICHLET WAT 1\* 1\* 100.0 /

/

Here, the first line sets both the pressure and temperature at the boundary, and the second line defaults the pressure entry, so that the simulator calculated initial boundary pressure will be used.
