<a id="__RefHeading___Toc134880_2055188184"></a>

### WCONHIST -- Define Well Historical Production Rates and Pressures

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WCONHIST keyword defines production rates and pressures for wells that have been declared history matching wells by the use of this keyword. History matching wells are handled differently than ordinary wells that use the WCONPROD keyword for controlling their production targets and constraints. However, the wells still need to be defined like ordinary production wells using the WELSPECS keyword in the SCHEDULE section.

Note that although wells can be allocated to a group when they are specified by the WELSPECS keyword, history matching wells cannot operate under group control. Field and group reporting is still consistent for all wells allocated to a group.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the wells observed production rates and pressures are being defined.<br>Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | STATUS | A defined character string that declares the status of the well. STATUS should be set to one of the following character strings:<br>1)  OPEN: the well is open to flow and will attempt to produce the required production volumes.<br>2)  STOP: the well is "stopped" at the surface and will not produce any fluids to surface; however, if there any open connections then flow may occur within the wellbore and between the open connections depending on a connection's potential with respect to all the other connections. Inter-connection flow (cross flow) can be prevented by setting the XFLOW variable on the WELSPECS keyword to NO. In this case the well's behavior will be similar to the SHUT option described below.<br>3)  SHUT: the well is shut at the surface and downhole, this results in no flow at the surface and no cross flow downhole.<br>Note a well's STATUS should always be set either STOP or SHUT if the well's production is to be set to zero. Just setting a well's production rate to zero means that the well is open to flow with a zero rate. | OPEN |
| 3 | TARGET | A defined character string that sets the observed target production phase for the well, all the other phases are calculated unconstrained and used for reporting only. The simulator will attempt to meet the TARGET based on the phase rate stated in items (4) to (6) and (10) on this keyword. TARGET should be set to one of the following character strings:<br>1)  ORAT: the target is set to the surface oil production rate as defined by item (4).<br>2)  WRAT: the target is set to the surface water production rate as defined by item (5).<br>3)  GRAT: the target is set to the surface gas production rate as defined by item (6).<br>4)  LRAT: the target is set to the surface liquid (oil plus water) production rate and is calculated by the simulator using (4) and (5).<br>5)  RESV: the target is set to the in situ reservoir volume rate and is calculated by the simulator using items (4), (5) and (6).<br>6)  BHP: the target rate is set to the bottom-hole pressure as defined by item (10).<br>```{=html} <!-- --> ``` 1)  Note the TARGET control mode may be reset using the WHISTCTL keyword in the SCHEDULE section, from the time the WHISTCTL is invoked, thus avoiding changing the control mode on all subsequent WCONHIST keywords. | None |
| 4 | ORAT | A real positive value that defines the observed surface oil production rate target or constraint.<br>This value may be specified using a User Defined Argument (UDA). | Defined |
| stb/d<br>0.0 | sm^3^/day<br>0.0 | scc/hour<br>0.0 |  |
| 5 | WRAT | A real positive value that defines the observed surface water production rate target or constraint.<br>This value may be specified using a User Defined Argument (UDA). | Defined |
| stb/d<br>0.0 | sm^3^/day<br>0.0 | scc/hour<br>0.0 |  |
| 6 | GRAT | A real positive value that defines the observed surface gas production rate target or constraint<br>This value may be specified using a User Defined Argument (UDA). | Defined |
| Mscf/d<br>0.0 | sm^3^/day<br>0.0 | scc/hour<br>0.0 |  |
| 7 | VFPTAB | A positive integer greater than or equal to zero that defines the vertical lift performance tables to be used for calculating the tubing head pressure for the well.<br>If a non-zero value is entered then the vertical lift performance tables must be entered via the VFPPROD keyword in the SCHEDULE section and allocated to the well via this item.<br>The default value of zero implies no vertical lift performance table initially. If this value is then reset to be greater than zero then the table will be used to calculate the well's tubing head pressure. Subsequently, the default is to use the previously declared table number. | 0 |
| 8 | ALQ-WELL | A real positive value that defines the artificial lift quantity to be used in conjunction with the VFPPROD assigned to the well via that keyword\'s VFPTAB variable.<br>This value may be specified using a User Defined Argument (UDA).<br>VFPTAB vertical lift performance table and the artificial lift quantity ALQ-WELL are used with the well fluid rates to calculate the well's tubing head pressures values from the bottom-hole pressure.<br>Note that the units for ALQ-WELL is dependent on the associated variable on the VFPPROD keyword. | None |
| 9 | THP | A real positive value that defines the observed tubing head pressure.<br>This value may be specified using a User Defined Argument (UDA).<br>This parameter is only used for comparing the actual tubing head pressure given here with those calculated by the simulator, that is history matching wells can only be controlled by either the surface injection rate or their bottom-hole pressure. | Defined |
| psia<br>0.0 | barsa<br>0.0 | atma<br>0.0 |  |
| 10 | BHP | A real positive value that defines the observed bottom-hole pressure.<br>This value may be specified using a User Defined Argument (UDA). | Defined |
| psia<br>0.0 | barsa<br>0.0 | atma<br>0.0 |  |
| 11 | WGRA | A real positive value that defines the observed wet gas rate in the commercial compositional simulator. The parameter is ignored by OPM Flow and should be defaulted or set to the default value of zero. | 0.0 |
| 12 | NGL | A real positive value that defines the observed Natural Gas Liquid ("NGL") rate in the commercial compositional simulator. The parameter is ignored by OPM Flow and should be defaulted or set to the default value of zero. | 0.0 |
| Notes:<br>1)  User Defined Quantities (\"UDQ\") can be used as User Defined Arguments (\"UDA\") for various group, well, and connection keywords in the SCHEDULE section. User Defined Arguments are activated using the UDADIMS keyword in the RUNSPEC section, and defined by the UDQ keyword in the SCHEDULE section.<br>2)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.77: WCONHIST Keyword Description

See also the WHISTCTL keyword that can be used to reset the TARGET phase, the GCONPROD and GCONINJE keywords to define a group's production and injection targets and constraints, and the WCONPROD keyword to define a production well's targets and constraints. All the aforementioned keywords are described in the SCHEDULE section.

History matching wells are converted to ordinary wells by restating a well's control mode using either the WCONPROD or WELTARG keywords in the SCHEDULE section.

#### Examples

The following example below shows the observed production rates for the OP01 oil producer for the first quarter of 2000.

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\-- 01 JAN 2000 START OF SCHEDULE SECTION

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\--

\-- WELL HISTORICAL PRODUCTION CONTROLS

\--

\-- WELL OPEN/ CNTL OIL WAT GAS VFP VFP THP BHP

\-- NAME SHUT MODE RATE RATE RATE TABLE ALFQ PRES PRES

WCONHIST OP01 OPEN ORAT 15.5E3 100.0 1550 10 1\* 900.0 1\* /

/ DATES

01 FEB 2000 /

/

\--

\-- WELL HISTORICAL PRODUCTION CONTROLS

\--

\-- WELL OPEN/ CNTL OIL WAT GAS VFP VFP THP BHP

\-- NAME SHUT MODE RATE RATE RATE TABLE ALFQ PRES PRES

WCONHIST OP01 OPEN ORAT 15.2E3 150.0 1520 1\* 1\* 875.0 3250.0 /

/ DATES

01 MAR 2000 /

/

\--

\-- WELL HISTORICAL PRODUCTION CONTROLS

\--

\-- WELL OPEN/ CNTL OIL WAT GAS VFP VFP THP BHP

\-- NAME SHUT MODE RATE RATE RATE TABLE ALFQ PRES PRES

WCONHIST OP01 OPEN ORAT 15.0E3 200.0 1500 1\* 1\* 850.0 1\* /

/

From January 1, 2000 well OP01 is open and is on oil rate control, and produces 15,500 stb/d oil, with the observed rates of 100 stb/d of water and 15.5 MMscf/d of gas. The well uses VFPPROD vertical lift table number 10 so that OPM Flow can calculate the tubing head pressures based on the fluids produced and the calculated pressures in the simulator.

The next example illustrates how to convert OP01 from a history match well to a normal production well at the start for the forecast run at August 1, 2017 using the WELTARG keyword.

DATES

01 AUG 2017 /

/

\--

\-- WELL PRODUCTION AND INJECTION TARGETS

\--

\-- WELL WELL TARGET

\-- NAME TARG VALUE

WELTARG

OP01 THP 1\* /

/

Here by defaulting the bottom-hole pressure via 1\* OPM Flow automatically applies the last bottom-hole pressure from the previous time step as the "constraining phase" together with the last historical rates as constraints. This ensures a smooth transition between history and prediction without having to resort to unreasonable changes to the model. This option is currently not implemented in OPM Flow but is expected to be incorporated in a future release.* *
