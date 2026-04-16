<a id="__RefHeading___Toc268463_1366622701"></a>

### WELSPECS -- Define Well Specifications

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword defines the general well specification data for all well types, and must be used for all wells before any other well specification keywords are used in the input file. The keyword declares the well, the name of the well, the group the well initial belongs to, the wellhead location and other key parameters.

OPM Flow also supports the use of the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword to change the properties of one or more wells previously specified using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword. In particular, this supports changing the controlling group (GRPNAME) without affecting any other well properties such as the location of the well head (I, J) or the well reference depth (BHPREF), since defaulted properties are not changed in this case. However, the well reference depth can be re-defaulted by specifying a negative value for BHPREF. The wells to be changed can be specified using a well name, well name pattern or well list (WELNAME).

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well specification data are being defined. | None |
| --- | --- | --- | --- |
| 2 | GRPNAME | A character string of up to eight characters in length that defines the group name for which the well is assigned to.<br>The group named FIELD is the top most group. GRPNAME can be set to FIELD although this is discouraged and a warning message will be issued. This is allowed in the commercial compositional simulator but not the commercial black-oil simulator. The FIELD group cannot contain both groups and wells.<br>Note that the group hierarchy should be defined by the [GRUPTREE](#__RefHeading___Toc118321_1596574740) keyword when there is more than one level of groups, otherwise all the groups will sit directly under the FIELD group in the group tree hierarchy.<br>Secondly, groups defined by the [GRUPTREE](#__RefHeading___Toc118321_1596574740) keyword cannot contain other groups and wells; that is, groups must either contain other groups or wells but not both.<br>If necessary, wells can be re-allocated to a different group by re-entering a well\'s [WELSPECS](#__RefHeading___Toc268463_1366622701) data together with a new value for GRPNAME. | None |
| 3 | I | A positive integer greater than or equal to zero and less than or equal to NX that defines the wellhead location for a vertical or deviated well, or the heel for a horizontal well in the I-direction.<br>For wells being specified with the [COMPTRAJ](#__RefHeading___Toc97651_32617439171) and [WELTRAJ](#__RefHeading___Toc268463_13666227011) keywords in [SCHEDULE](#__RefHeading___Toc43945_784232322) section, that allow for an alternative manner to define the well connections to the simulation grid blocks, this parameter should be defaulted with 1\*. Since the simulator will calculate the wellhead location from the trajectory data on the [WELTRAJ](#__RefHeading___Toc268463_13666227011) keyword.<br>Note that the [COMPTRAJ](#__RefHeading___Toc97651_32617439171) and [WELTRAJ](#__RefHeading___Toc268463_13666227011) keywords are OPM Flow specific keywords, and will cause an error in the commercial simulator. | None |
| 4 | J | A positive integer greater than or equal to zero and less than or equal to NY that defines the wellhead location for a vertical or deviated well, or the heel for a horizontal well in the J-direction.<br>For wells being specified with the [COMPTRAJ](#__RefHeading___Toc97651_32617439171) and [WELTRAJ](#__RefHeading___Toc268463_13666227011) keywords in [SCHEDULE](#__RefHeading___Toc43945_784232322) section, that allows for an alternative manner to define the well connections to the simulation grid blocks, this parameter should be defaulted with 1\*. Since the simulator will calculate the wellhead location from the trajectory data on the [WELTRAJ](#__RefHeading___Toc268463_13666227011) keyword.<br>Note that the [COMPTRAJ](#__RefHeading___Toc97651_32617439171) and [WELTRAJ](#__RefHeading___Toc268463_13666227011) keywords are OPM Flow specific keywords, and will cause an error in the commercial simulator. | None |
| 5 | BHPREF | A real value that defines the reference depth for reporting the bottom-hole pressure for the well. Ideally this value should be set to the midpoint of the perforations as defined by the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.<br>If defaulted by 1\* or set to a value less than or equal to zero, then the mid-point of shallowest connection defined by the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword will be used. | Mid-point of shallowest connection defined by the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword |
| feet | m | cm |  |
| 6 | TYPE | A defined character string that defines the "main" phase for the well, and should be set to one of the following character strings:<br>1)  GAS: for a gas well.<br>2)  OIL: for an oil well.<br>3)  WAT: for a water injection well.<br>4)  LIQ: for an oil well when the liquid productivity index is required for the well.<br>This parameter defines the phase used to calculate a well's productivity or injectivity index and the type of well, or a well's connection, to close when a group's production constraints, as defined on the [GCONPROD](#__RefHeading___Toc146746_4203985108) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, have been violated. For example, if the well is declared as an oil well, then excessive gas and water connections will be subject to closure.<br>Note OPM Flow only currently supports options one to three, that is option four (LIQ) is not supported. For producing wells this mostly matters if one plots the WPI summary vector (productivity index for well\'s preferred phase). In the current treatment WPI will not have contributions from the water phase if the declared preferred phase is LIQ. For injecting wells WELSPECS\'s preferred phase does not matter, since the preferred phase is (typically) reset to the injected phase via the [WCONINJE](#__RefHeading___Toc146750_4203985108) and [WCONINJH](#__RefHeading___Toc146752_4203985108) keywords. | None |
| 7 | DRADIUS | A real value that defines the well drainage radius for the well used to calculate a well's productivity or injectivity index.<br>A default of zero results in the pressure equivalent radius of the grid blocks containing the well connections are used. | 0.0 |
| feet | m | cm |  |
| 8 | INFLOW | A defined character string that defines the inflow equation to be used for the well in calculating the well's flow rates. INFLOW should be set to one of the following character strings:<br>1)  STD: the standard inflow equation will be used. This is normally used for wells that are primary oil or water wells.<br>2)  NO: an alias for STD.<br>3)  R-G: the Russell Goodrich[^1] pressure square inflow equation will used. This option can be used for dry gas wells.<br>4)  YES: an alias for R-G.<br>5)  P-P: the general dry gas pseudo pressure inflow equation will be used. Normally used for dry gas wells.<br>6)  GPP: the generalized gas pseudo pressure inflow equation used with wet gas wells, that is condensate gas wells. This inflow equation is based on the formulation of Whitson et al.[^2]<br>For oil and water wells the INFLOW should be set to STD, whereas for dry gas wells INFLOW can be set to either R-G or P-P; however, the P-P option is preferred for dry gas wells due to the more rigorous treatment of gas flow. For wet gas wells, that is gas condensate wells, INFLOW should be set to GPP.<br>Only INFLOW equal to STD and NO are currently implemented in OPM Flow. | STD |
| 9 | AUTO | A defined character string that specifies the action to be taken if the well is automatically closed/shut by the simulator, and should be set to one of the following:<br>1)  STOP: the well is "stopped" at the surface and will not produce any fluids to surface; however, if there any open connections then flow may occur within the wellbore and between the open connections depending on a connection's potential with respect to all the other connections. Inter-connection flow (cross flow) can be prevented by setting the XFLOW variable to NO. In this case the well's behavior will be similar to the SHUT option described below.<br>2)  SHUT: the well is shut at the surface and downhole, this results in no flow at the surface and no cross flow downhole.<br>The corrective action takes places at the end of the time step in which the constraint is violated. | SHUT |
| 10 | XFLOW | A defined character string that defines the if cross flow should occur within the wellbore, and should be set to either:<br>1)  YES: to allow cross flow in the wellbore through well connections.<br>2)  NO: to disallow cross flow within the wellbore, even if the flow potentials in the well connections would allow such flow to occur.<br>In some cases numerical issues can occur if this variable is set to YES, and resetting it to NO may resolve the issue; however, the results may not represent the physical down hole process in this case. | YES |
| 11 | [PVTNUM](#__RefHeading___Toc68366_2752266063) | A positive integer greater than or equal to zero that defines the PVT table used to calculate the wellbore fluid properties that define the relationship between reservoir and surface volume rates.<br>The default value of zero sets [PVTNUM](#__RefHeading___Toc68366_2752266063) to be the PVT table of the deepest connection in the well. | 0 |
| 12 | DENOPT | A defined character string that sets the type of density calculation used in calculating the wellbore hydrostatic head, and should be set to one of the following character strings:<br>1)  SEG: sets the hydrostatic head density calculation to segmented. In this cases the density is calculated between neighboring well connections and the volumes flowing from the connections. This is the more accurate calculation if the fluid properties flowing from the well connections are variable. The density calculation itself is explicit, i.e. uses the flowing volumes of the last time step.<br>2)  AVG: sets the hydrostatic head density calculation to the average density calculation. Here the density is considered uniform across a given reservoir and is dependent on total inflow rates of each phase and the well's bottom-hole pressure<br>The default option of 1\* invokes the SEG option and is the only option implemented in OPM Flow. | SEG |
| 13 | [FIPNUM](#__RefHeading___Toc77229_2752266063) | An integer value defines the [FIPNUM](#__RefHeading___Toc77229_2752266063) region used to determine the reservoir conditions in calculating the well's reservoir volumes and is determined by:<br>1)  If set to a negative integer value then the [FIPNUM](#__RefHeading___Toc77229_2752266063) region of the deepest connection in the well will be used.<br>2)  If set to zero, the default value, then the average properties for the field will be used.<br>3)  If set to an integer value greater than zero, then the [FIPNUM](#__RefHeading___Toc77229_2752266063) indicated by this value will be used. | 0 |
| 14 | STRMLIN1 | Not used and should be defaulted with 1\*. | 1\* |
| 15 | STRMLIN2 | Not used and should be defaulted with 1\*. | 1\* |
| 16 | TYPECOMP | Commercial compositional simulator well type model option that is not used and should be defaulted with either STD or 1\*. | STD |
| 17 | POLYTAB | A positive integer greater than or equal to zero that defines the polymer mixing table, as defined by the [PLMIXPAR](#__RefHeading___Toc93833_3812137098) and [PLYMAX](#__RefHeading___Toc110214_2939291539) keywords, to be used in calculating the well's well bore properties. The default value of zero means the table allocated via the [PLMIXNUM](#__RefHeading___Toc107258_3812137098) array for the deepest connection in the well bore is utilized.<br>Only the default value of zero is supported by OPM Flow. | 0 |
| Notes:<br>1)  The keyword is followed by any number records with each record terminated by a "/" and the keyword should be terminated by a "/".<br>2)  Note that the total number of individual wells declared by the [WELSPECS](#__RefHeading___Toc268463_1366622701) cannot exceed the valued entered via the MXWELS variable on the [WELLDIMS](#__RefHeading___Toc82886_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. |  |  |  |

Table 12.3.281.1: WELSPECS Keyword Description

See also the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword to define a well's connections, the [WCONPROD](#__RefHeading___Toc146754_4203985108) and [WCONINJE](#__RefHeading___Toc146750_4203985108) keywords to define a well's production and injection targets and constraints. All the aforementioned keywords are described in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Example

The following example defines three wells using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword

\--

\-- WELL SPECIFICATION DATA

\--

\-- WELL GROUP LOCATION BHP PHASE DRAIN INFLOW OPEN CROSS PVT

\-- NAME NAME I J DEPTH FLUID AREA EQUANS SHUT FLOW TABLE

WELSPECS

GI01 PLATFORM 14 13 1\* GAS 1\* P-P SHUT NO 1\* /

GP01 PLATFORM 64 80 1\* GAS 1\* GPP SHUT NO 1\* /

OP01 PLATFORM 24 110 1\* OIL 1\* STD SHUT NO 1\* /

/

Here, well GI01 is a dry gas injection well that uses the dry gas pseudo inflow equation, GP01 is a gas condensate well that uses the generalized gas pseudo pressure inflow equation, and finally, OP01 is an oil well that uses the standard inflow equation. All wells will be shut if they are required to cease production, all wells disallow cross flow, and the hydrostatic head calculation is defaulted to the segment option for all wells.

If the same three wells are using the [COMPTRAJ](#__RefHeading___Toc97651_32617439171) and [WELTRAJ](#__RefHeading___Toc268463_13666227011) keywords to specify the connections to the simulation grid, then the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword should be;

\--

\-- WELL SPECIFICATION DATA

\--

\-- WELL GROUP LOCATION BHP PHASE DRAIN INFLOW OPEN CROSS PVT

\-- NAME NAME I J DEPTH FLUID AREA EQUANS SHUT FLOW TABLE

WELSPECS

GI01 PLATFORM 1\* 1\* 1\* GAS 1\* P-P SHUT NO 1\* /

GP01 PLATFORM 1\* 1\* 1\* GAS 1\* GPP SHUT NO 1\* /

OP01 PLATFORM 1\* 1\* 1\* OIL 1\* STD SHUT NO 1\* /

/

Notice how the well location parameters have been defaulted with 1\* in this case.

The following example illustrates how the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword can be used to change the controlling group for oil production wells previously specified by the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword that have an oil production rate less than 100.

\--

\-- ACTIONX BLOCK

\--

ACTIONX

ACT01 1 /

WOPR \'OP\*\' \< 100.0 /

/

WELSPECS

\'?\' \'LOWPRESS\' /

/

ENDACTIO

[^1]: Russell, D.G., Goodrich, J.H., Perry, G.E and Bruskotter, J.F \"Methods of Predicting Gas Well Performance\", Transactions of the ASME, Journal of Petroleum Technology (1966) 99-108.

[^2]: Whitson, C. H. and Fevang, Ø. "Generalised Pseudopressure Well Treatment in Reservoir Simulation," Presented at the IBC Technical Services Conference on Optimisation of Gas Condensate Fields, Aberdeen, UK (June 26-27, 1997).
