### WCONINJH -- Well Historical Observed Injection Rates and Pressures

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WCONINJH keyword defines injection rates and pressures for wells that have been declared history matching wells by the use of this keyword. History matching wells are handled differently then ordinary wells that use the WCONINJE keyword for controlling their injection targets and constraints. However, the wells still need to be defined like ordinary injection wells using the WELSPECS keyword in the SCHEDULE section.

Note that although wells can be allocated to a group when they are specified by the WELSPECS keyword, history matching wells cannot operate under group control. Field and group reporting is still consistent for all wells allocated to a group, but history matching wells cannot be under group control.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the wells observed injection rates and pressures are being defined.<br>Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | TYPE | A defined character string that defines the type of injection well. TYPE should be set to one of the following character strings:<br>1)  GAS: for a gas injection well.<br>2)  OIL: for an oil injection well.<br>3)  WAT: for a water injection well. | None |
| 3 | STATUS | A defined character string that declares the status of the well. STATUS should be set to one of the following character strings:<br>1)  OPEN: the well is open for injection and will attempt to inject the observed injection volumes.<br>2)  STOP: the well is "stopped" at the surface and will not inject fluids; however, if there any open connections then flow may occur within the wellbore and between the open connections depending on a connection's potential with respect to all the other connections. Inter-connection flow (cross flow) can be prevented by setting the XFLOW variable on the WELSPECS keyword to NO. In this case the well's behavior will be similar to the SHUT option described below.<br>3)  SHUT: the well is shut at the surface and downhole, this results in no injection and no cross flow downhole.<br>Note a well's STATUS should always be set either STOP or SHUT if the well's injection is to be set to zero. Just setting a well's injection rate to zero means that the well is open to flow with a zero injection rate, this may cause numerical issues. | OPEN |
| 4 | RATE | A real positive value that defines the observed surface injection rate. | 0.0 |
| Liquid stb/d<br>Gas Mscf/d | Liquid sm^3^/day<br>Gas sm3/day | Liquid scc/hour<br>Gas scc/hour |  |
| 5 | BHP | A real positive value that defines the observed bottom-hole pressure. | 0.0 |
| psia | barsa | atma |  |
| 6 | THP | A real positive value that defines the observed tubing head pressure.<br>This parameter is only used for comparing the actual tubing head pressure given here with those calculated by the simulator, that is history matching wells can only be controlled by either the surface injection rate or their bottom-hole pressure. | None |
| psia | barsa | atma |  |
| 7 | VFPTAB | A positive integer greater than or equal to zero that defines the vertical lift performance tables to be used for calculating the tubing head pressure for the well.<br>If a non-zero value is entered then the vertical lift performance tables must be entered via the VFPINJ keyword in the SCHEDULE section and allocated to the well via this item.<br>The default value of zero implies no vertical lift performance table initially. If this value is then reset to be greater than zero then the table will be used to calculate the well's tubing head pressure. Subsequently, the default is to use the previously declared table number. | 0 |
| 8 | RSRVINJ | Dissolved gas fraction in injected oil or vaporized oil fraction in injected gas.<br>The parameter is ignored by OPM Flow and should be defaulted or set to the default value of zero. | 0.0 |
| 9 | OILFRAC | Surface oil fraction in a multi-phase injector.<br>The parameter is ignored by OPM Flow and should be defaulted or set to the default value of zero. | 0.0 |
| 10 | WATFRAC | Surface water fraction in a multi-phase injector.<br>The parameter is ignored by OPM Flow and should be defaulted or set to the default value of zero. | 0.0 |
| 11 | GASFRAC | Surface gas fraction in a multi-phase injector.<br>The parameter is ignored by OPM Flow and should be defaulted or set to the default value of zero. | 0.0 |
| 12 | TARGET | A defined character string that sets the target injection control mode for the well. TARGET should be set to one of the following character strings:<br>1)  RATE: the injection well will be controlled by the surface injection rate for the given well type as defined by the TYPE variable. For example, if TYPE has been set to WAT then this would mean the surface water injection rate as defined by item (4).<br>2)  BHP: the injection well will be controlled by the bottom-hole pressure as defined by item (5). | RATE |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.79: WCONINJH Keyword Description

This keyword should be repeated at various time steps to fully describe the historical injection performance of the wells. For example, as most production and injection data is reconciled on a monthly basis, then monthly time steps covering the injection history of the wells should be used with WCONINJH keyword entered on a monthly basis.

History matching well are converted to ordinary wells by restating a well's control mode using either the WCONINJE or WELTARG keywords in the SCHEDULE section.

#### Example

The following example below shows the observed gas rates for the GI01 gas injector for the first quarter of 2000.

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\-- 01 JAN 2000 START OF SCHEDULE SECTION

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\--

\-- WELL HISTORICAL INJECTION CONTROLS

\--

\-- WELL FLUID OPEN/ SURF BHP THP VFP NOT CNTL

\-- NAME TYPE SHUT RATE PRES PRES TABLE USED MODE

WCONINJH

GI01 GAS OPEN 15.5E3 1\* 5462 12 4\* 1\* /

/ DATES

01 FEB 2000 /

/

\--

\-- WELL HISTORICAL INJECTION CONTROLS

\--

\-- WELL FLUID OPEN/ SURF BHP THP VFP NOT CNTL

\-- NAME TYPE SHUT RATE PRES PRES TABLE USED MODE

WCONINJH

GI01 GAS OPEN 15.9E3 1\* 5468 1\* 4\* 1\* /

/ DATES

01 MAR 2000 /

/

\--

\-- WELL HISTORICAL INJECTION CONTROLS

\--

\-- WELL FLUID OPEN/ SURF BHP THP VFP NOT CNTL

\-- NAME TYPE SHUT RATE PRES PRES TABLE USED MODE

WCONINJH

GI01 GAS OPEN 17.2E3 1\* 5489 1\* 4\* 1\* /

/

Well GI01is declared as a gas injection well under gas rate control as TARGET variable is defaulted to rate control by using 1\* (the last entry on the record). In addition, the well uses vertical lift table VFPINJ number 12 (as shown at January 1, 2000) to calculate the tubing head pressures for the well. Note that it is not necessary to declare the VFPINJ table number if it remains the same for subsequent time steps and thus the default 1\* is used to indicate the last entry should be used.
