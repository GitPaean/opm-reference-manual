### WCONINJE -- Well Injection Targets and Constraints

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WCONINJE](#__RefHeading___Toc146750_4203985108) keyword defines injection targets and constraints for wells that have previously been defined by the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. Note that wells can be allocated to a group when they are specified by the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword. Wells defined to be under group control will have their injection rates controlled by the group to which they belong, in addition to any well constraints defined for the wells using this keyword.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well injection targets and constraints data are being defined.<br>Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | TYPE | A defined character string that defines the type of injection well. TYPE should be set to one of the following character strings:<br>1)  [GAS](#__RefHeading___Toc38607_2267116897): for a gas injection well.<br>2)  [OIL](#__RefHeading___Toc97439_1778172979): for an oil injection well.<br>3)  WAT: for a water injection well. | None |
| 3 | STATUS | A defined character string that declares the status of the well. STATUS should be set to one of the following character strings:<br>1)  OPEN: the well is open for injection and will attempt to inject the required injection volumes.<br>2)  STOP: the well is "stopped" at the surface and will not inject any fluids; however, if there any open connections then flow may occur within the wellbore and between the open connections depending on a connection's potential with respect to all the other connections. Inter-connection flow (cross flow) can be prevented by setting the XFLOW variable on the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword to NO. In this case the well's behavior will be similar to the SHUT option described below.<br>3)  SHUT: the well is shut at the surface and downhole, this results in no injection and no cross flow downhole.<br>4)  AUTO: the well is initially SHUT, but may be opened automatically if an economic limit is violated. This option is currently not supported by OPM Flow.<br>Note a well's STATUS should always be set either STOP or SHUT if the well's injection is to be set to zero. Just setting a well's injection rate to zero means that the well is open for injection with a zero rate, this will cause numerical issues especially for wells under THP control. | OPEN |
| 4 | TARGET | A defined character string that sets the target injection control mode for the well. TARGET should be set to one of the following character strings:<br>1)  RATE: the injection phase will be controlled by the surface fluid rate for the given well type as defined by the TYPE variable. For example, if TYPE has been set to WAT then this would mean the surface water injection rate as defined by item (5).<br>2)  RESV: the injection phase will be controlled by the in situ reservoir volume fluid rate for the given well type as defined by the TYPE variable. For example, if TYPE has been set to [GAS](#__RefHeading___Toc38607_2267116897) then this would mean the gas reservoir volume injection rate as defined by item (6).<br>3)  BHP: the target rate is set according to the bottom-hole pressure as defined by item (7).<br>4)  THP: the target rate is set according to the tubing head pressure as defined by item (8). If this option is selected then the vertical lift performance tables must be entered via the [VFPINJ](#__RefHeading___Toc121917_2556401936) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section and allocated to the well via item (9).<br>5)  GRUP: the well is under group control and injects its share of the group\'s target as set using the [GCONINJE](#__RefHeading___Toc134874_2055188184) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. | None |
| 5 | RATE | A real positive value that defines the maximum surface injection rate target or constraint.<br>This value may be specified using a User Defined Argument (UDA). | None |
| Liquid stb/d<br>Gas Mscf/d | Liquid sm^3^/day<br>Gas sm3/day | Liquid scc/hour<br>Gas scc/hour |  |
| 6 | RESV | A real positive value that defines the maximum reservoir volume injection rate target or constraint.<br>This value may be specified using a User Defined Argument (UDA). | None |
| rb/d | rm^3^/day | rcc/hour |  |
| 7 | BHP | A real positive value that defines the maximum bottom-hole pressure target or constraint.<br>This value may be specified using a User Defined Argument (UDA).<br>Note the default value basically means unlimited injection or no constraint and should therefore be avoided as the BHP will result in unrealistic well potentials as well as optimistic injection forecasts for the well. | Defined |
| psia<br>10,0000 | barsa<br>6,895 | atma<br>6,803 |  |
| 8 | THP | A real positive value that defines the maximum tubing head pressure target or constraint.<br>This value may be specified using a User Defined Argument (UDA). | None |
| psia | barsa | atma |  |
| 9 | VFPTAB | A positive integer greater than or equal to zero that defines the vertical lift performance tables to be used for calculating the tubing head pressure for the well.<br>If a non-zero value is entered then the vertical lift performance tables must be entered via the [VFPINJ](#__RefHeading___Toc121917_2556401936) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section and allocated to the well via this item.<br>The default value of zero implies no vertical lift performance tables and in this case TARGET cannot be set to THP and in addition item (10) should be defaulted or set to zero. | 0 |
| 10 | RSRVINJ | The dissolved gas-oil ratio in the injected oil, or the vaporized oil-gas ratio in the injected gas. | 0.0 |
| Gas Injection: stb/Mscf<br>Oil Injection: Mscf/stb | Gas Injection: sm^3^/sm^3^<br>Oil Injection: sm^3^/sm^3^ | Gas Injection: scc/scc<br>Oil Injection: scc/scc |  |
| 11 | RSSTEAM | Thermal/Temperature gas-steam ratio for steam-gas injectors.<br>The parameter is ignored by OPM Flow and should be defaulted or set to the default value of zero. | 0.0 |
| 12 | OILFRAC | Surface oil fraction in a multi-phase injector.<br>The parameter is ignored by OPM Flow and should be defaulted or set to the default value of zero. | 0.0 |
| 13 | WATFRAC | Surface water fraction in a multi-phase injector.<br>The parameter is ignored by OPM Flow and should be defaulted or set to the default value of zero. | 0.0 |
| 14 | GASFRAC | Surface gas fraction in a multi-phase injector.<br>The parameter is ignored by OPM Flow and should be defaulted or set to the default value of zero. | 0.0 |
| 15 | OILSTEAM | Surface oil volume to steam volume ratio in a steam-oil injector.<br>The parameter is ignored by OPM Flow and should be defaulted or set to the default value of zero. | 0.0 |
| Notes:<br>1)  User Defined Quantities (\"UDQ\") can be used as User Defined Arguments (\"UDA\") for various group, well, and connection keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. User Defined Arguments are activated using the [UDADIMS](#__RefHeading___Toc65914_1778172979) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, and defined by the [UDQ](#__RefHeading___Toc161095_2932703077) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.<br>2)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.78: WCONINJE Keyword Description

See also the [GCONPROD](#__RefHeading___Toc146746_4203985108) and the [GCONINJE](#__RefHeading___Toc134874_2055188184) keywords to define a group's production and injection targets and constraints, and the [WCONPROD](#__RefHeading___Toc146754_4203985108) keyword to define a production well's targets and constraints. All the aforementioned keywords are described in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Example

The following example defines the injection targets and constraints for one gas injection well and one water injection well as follows:

\--

\-- WELL INJECTION CONTROLS

\--

\-- WELL FLUID OPEN/ CNTL SURF RESV BHP THP VFP

\-- NAME TYPE SHUT MODE RATE RATE PRSES PRES TABLE

WCONINJE

GI01 GAS OPEN GRUP 50E3 1\* 1\* 1\* 1\* /

WI01 WAT OPEN RATE 25E3 1\* 5000. 1\* 1\* /

/

Well GI01 is a gas injection well directly under group control constrained by a maximum surface gas injection rate of 50 MMscf/d and well WI01 is an open water injection well with a surface water injection rate target of 25,000 stb/d, subject to a maximum bottom-hole pressure constraint 5,000 psia.
