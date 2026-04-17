### WGRUPCON -- Define Well Guide Rates for Group Control

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WGRUPCON keyword defines a well's production or injection guide rate for when a well is under group control. The guide rate is used to determine a well's production target under group control in order to satisfy a group's targets and constraints, including any higher level related groups as well as the FIELD group.

Wells must have been previously defined and allocated to a group by the WELSPECS keyword in the SCHEDULE section. Wells defined to be under group control will have their production rates controlled by the group to which they belong, in addition to any well constraints defined for the wells via the WCONPROD and WCONINJE keywords in the SCHEDULE section.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well production targets and constraints data are being defined.<br>Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | STATUS | A defined character string that declares the status of the well to be under group control or not under group control. STATUS should be set to one of the following character strings:<br>1)  YES: the well is under group control and its production behavior will be influenced by its assigned group, including connecting higher level groups as well as the FIELD group.<br>2)  NO: the well is NOT under group control and its production behavior will only be influenced by its own targets and constraints.<br>Note the default value of YES puts all wells under group control unless specified otherwise by the STATUS variable, or the TARGET variable on the WCONPROD and WCONINJE keywords in the SCHEDULE section. | YES |
| 3 | GUIDERAT | A dimensionless real number that determines the well's share of its group production (or injection) target rate.<br>If GUIDERAT is a positive number then the guide rate for the well is fixed until modified by this keyword at a subsequent time. If TARGET variable on this keyword is not equal to the group's controlling phase, then the GUIDERAT is converted into the groups' controlling phase and is updated every time step.<br>If GUIDERAT is less than or equal to zero then the well's guide rate is based on the well's potential (unrestricted flow) and the potential is calculated every time step. | -1.0 |
| dimensionless | dimensionless | dimensionless |  |
| 4 | TARGET | A defined character string that sets the well's guide rate phase that the GUIDERAT value should be applied to. TARGET should be set to one of the following character strings:<br>1)  OIL: the well\'s guide rate applies to the surface oil production rate.<br>2)  WAT: the well\'s guide rate applies to the surface water production rate.<br>3)  GAS: the well\'s guide rate applies to the surface gas production rate.<br>4)  LIQ: the well\'s guide rate applies to the surface liquid (oil plus water) production rate.<br>5)  RES: the well\'s guide rate applies to the in situ reservoir volume rate.<br>6)  RAT: the well's guide rate applies to the surface rate of the injection phase. This should only be used if the well has been declared an injection well via the WCONINJE keyword in the SCHEDULE section.<br>7)  COMB: the well's guide rate applies to the linearly combined calculated rate. This option is not supported by OPM Flow.<br>TARGET may be defaulted if GUIDERAT has been defaulted, either by 1\* or a value less than or equal to zero. | None |
| 5 | SCALE | A real value that is used to multiple the GUIDERAT or the calculated well potentials to determine the final GUIDERAT for the well. | 1.0 |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.96: WGRUPCON Keyword Description

See also the GCONPROD the GCONINJE keywords to define a group's production and injection targets and constraints, and the WCONPROD and WCONINJE keyword to define a well's production and injection characteristics. All the aforementioned keywords are described in the SCHEDULE section.

#### Example

The following example defines the guides rates for all oil and gas producers and the gas injectors as follows:

\--

\-- DEFINE WELL GUIDES FOR GROUP CONTROL

\--

\-- WELL GRUP GUIDE GUIDE SCALE

\-- NAME CNTL RATE PHASE FACT

WGRUPCON

\'GI\*\' YES 0 RAT 1.0 /

\'GP\*\' YES 0 GAS 1.0 /

\'OP\*\' NO 2 OIL 1.0 /

/

Both the gas producers ('GP\*') and injectors ('GI'\*) are under group control with their guide rates based on their potentials. The gas injectors are controlled based on their potential surface gas injection rates and the gas producers on their potential surface gas production rates. In comparison, the oil wells (OP\*) are controlled by their own targets and constraints.
