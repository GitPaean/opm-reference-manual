### BC -- Define Boundary Conditions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The BC keyword defines the boundary conditions for the model, and can be used to set boundary conditions for when external influx or efflux volumes are influencing the reservoir pressure and production history. For example, when the average reservoir pressure remains constant throughout the production period due to water influx, or gas migration from an external source.

The BC keyword has been replaced by the BCCON keyword in the GRID section that defines the boundary condition connections and the BCPROP keyword in the SCHEDULE section that defines the boundary condition properties.

| 1 | I1 | A positive integer that defines the lower bound of the grid in the I-direction for which the boundary conditions are to be applied, must be greater than or equal 1 and less than or equal to I2 and NX. | 1 |
| --- | --- | --- | --- |
| 2 | I2 | A positive integer that defines the upper bound of the grid in the I-direction for which the boundary conditions are to be applied, must be greater than or equal to II and less than or equal to NX | NX |
| 3 | J1 | A positive integer that defines the lower bound of the grid in the J-direction for which the boundary conditions are to be applied, must be greater than or equal 1 and less than or equal to J2 and NY. | 1 |
| 4 | J2 | A positive integer that defines the upper bound of the grid in the J-direction for which the boundary conditions are to be applied, must be greater than or equal to JI and less than or equal to NY. | NY |
| 5 | K1 | A positive integer that defines the lower bound of the grid in the K-direction for which the boundary conditions are to be applied, must be greater than or equal to one and less than or equal to K2 and NZ. | 1 |
| 6 | K2 | A positive integer that defines the upper bound of the grid in the K-direction for which the boundary conditions are to be applied, must be greater than or equal to KI and less than or equal to NZ. | NZ |
| 7 | DIRECT | A character string that defines the direction to apply the boundary conditions, and should be set to one of the following X, Y, or Z for the positive direction, or X-, Y- or Z- for the negative direction. | None |
| 8 | TYPE | A defined character string that defines the type of boundary condition to be applied, and should be set to one of the following character strings:<br>1)  DIRICHLET: for a user defined boundary conditions. In this case, items (1) through (7) must be set, together with PHASE for the fluid type, and PRESS and TEMP for the constant pressure and temperature boundary conditions.<br>This option is currently not supported but will be available in the next release.<br>2)  FREE: for the initial state of the boundary to be kept throughout the simulation, that is a constant boundary condition. For this option only items (1) through (7) need to be defined.<br>3)  RATE: for the boundary to have a constant influx or efflux rate. Again items (1) through (7) are required, plus PHASE for the fluid type, and RATE to set the PHASE rate.<br>Only the FREE and RATE options are currently supported; however the next release will support the DIRICHLET option. | None |
| 9 | PHASE | A defined character string that sets fluid type used in the boundary calculations, and should be set to one of the following character strings:<br>1)  GAS: the gas phase will be used to control the boundary conditions for when the TYPE has been set to DIRICHLET or RATE.<br>2)  OIL: the oil phase will be used to control the boundary conditions for when the TYPE has been set to DIRICHLET or RATE.<br>3)  WATER or WAT: the water phase will be used to control the boundary conditions for when the TYPE has been set to DIRICHLET or RATE. | None |
| 10 | RATE | A real value that defines the constant surface oil, gas or water rate to be injected or withdrawn at the boundary, for when TYPE has been set to RATE.<br>Note a negative value implies an injection rate, whereas, a positive value indicates a withdrawal rate. | 0,0 |
| Liquid: stb/day<br>Gas: Mscf/day | Liquid: sm^3^/day<br>Gas: sm^3^/day | Liquid: scc/hr<br>Gas: scc/hr |  |
| 11 | PRESS | PRESS is a real positive value that defines the constant pressure boundary condition. PRESS should only be entered if TYPE has been set to DIRICHLET. If the pressure at the boundary is less than PRESS, then the fluid type declared via PHASE will flow across the boundary.<br>The default value of 1\* will use the simulator\'s calculated value based on data entered via the EQUIL keyword in the SOLUTION section. | 1\* |
| psia | barsa | atma |  |
| 12 | TEMP | TEMP is a real positive number that defines the constant temperature boundary condition. TEMP should only be entered if TYPE has been set to DIRICHLET.<br>The default value of 1\* will use the simulator\'s calculated value based on data entered via one of the following reservoir temperature keywords: RTEMP, RTEMPA, RTEMPVD, TEMPI, or TEMPVD, in the SOLUTION section. Note that all of the aforementioned reservoir temperature keywords, except for TEMPI, may also be used in the PROPS section as well. | 1\* |
| ^o^F | ^o^C | ^o^C |  |
| Notes:<br>1)  Where NX, NY and NZ are the dimensions of the model as defined on the DIMENS keyword in the RUNSPEC section.<br>2)  Each record must be terminated by a "/" and the keyword is terminated by a "/\". |  |  |  |

Table 10.10: BC Keyword Description

See also the [AQUFLUX - Define Constant Flux Analytical Aquifer](#anchor-2) keyword that is supported by OPM Flow in both the SOLUTION and SCHEDULE sections, to define the aquifer influx with greater flexibility.

If the BC keyword is not present in the input deck, then the boundary conditions for the model are set to be no flow, which is the normal behavior in both OPM Flow and the commercial simulator.

#### Examples

The first example shows how to set a constant pressure boundary using TYPE equal to FREE:

\--

\-- DEFINE MODEL BOUNDARY CONDITIONS (OPM FLOW SOLUTION GRID KEYWORD)

\--

\-- \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\-- BC BC BC BC BC BC

\-- I1 I2 J1 J2 K1 K2 DIRC TYPE PHASE RATE PRESS TEMP

BC

1 1 1 1\* 1 1\* X- FREE 1\* 1\* 1\* 1\* /

1 1\* 1 1 1 1\* Y FREE /

/

With this option it is only necessary to define the boundary cells and all the other parameters (PHASE, RATE, PRESS, and TEMP) can be defaulted, as they are ignored for when TYPE equals FREE.

The next example is based on NX, NY and NZ equal to 20, 1, 10 respectively, on the DIMENS keyword in the RUNSPEC section, and shows how different boundary types can be assigned to different parts of the model.

\--

\-- DEFINE MODEL BOUNDARY CONDITIONS (OPM FLOW SOLUTION GRID KEYWORD)

\--

\-- \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\-- BC BC BC BC BC BC

\-- I1 I2 J1 J2 K1 K2 DIRC TYPE PHASE RATE PRESS TEMP

BC

1 1 1 1 1 10 X- RATE GAS 1\* 256.0 100.0 /

20 20 1 1 1 10 X FREE 4\* /

/

The last example shows how the DIRICHLET boundary condition option may be used:

\--

\-- DEFINE MODEL BOUNDARY CONDITIONS (OPM FLOW SOLUTION GRID KEYWORD)

\--

\-- \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\-- BC BC BC BC BC BC

\-- I1 I2 J1 J2 K1 K2 DIRC TYPE PHASE RATE PRESS TEMP

BC

1 1 1 1\* 1 1\* X- DIRICHLET WAT 1\* 256.0 100.0 /

1 1\* 1 1 1 1\* Y DIRICHLET WAT 1\* 1\* 100.0 /

/

Here, the first line sets both the pressure and temperature at the boundary, and the second line defaults the pressure entry, so that the simulator calculated initial boundary pressure will be used.
