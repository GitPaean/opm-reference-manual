### WLISTARG -- Modify Well List Target and Constraint Values (Static)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WLISTARG keyword modifies the target and constraint values of both rates and pressures for wells previously defined in a well list by the WLIST or WLISTNAM keywords. WLISTARG is similar to the WELTARG keyword in it that allows for modifying targets and constraints without having to define all the variables on the well control keywords: WCONPROD, WCONHIST, WCONINJE, or WCONINJH keywords. Variables not changed by the WLISTARG keyword remain the same as those previously entered via the well control keywords or previously entered WLISTARG keywords. Note that the well must still be initially be fully defined using the WCONPROD or WCONINJE keywords. All the aforementioned keywords are described in the SCHEDULE section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | WLIST | A character string of up to eight characters in length, enclosed in quotes, that defines the well list name declared by the WLIST keyword.<br>Note the first character must be asterisk ("\*") and the second character must be a letter, for example, \*PROD. | None |
| --- | --- | --- | --- |
| 2 | TARGET | A defined character string that sets the item to be changed for the well the value of the item is set by item (3).<br>1)  ORAT: reset the surface oil production rate value as defined by item (3).<br>2)  WRAT: reset the surface water production rate value as defined by item (3).<br>3)  GRAT: reset the surface gas production rate value as defined by item (3).<br>4)  LRAT: reset the surface liquid (oil plus water) production rate value as defined by (3).<br>5)  RESV: reset the in situ reservoir volume rate value as defined by (3).<br>6)  BHP: reset the bottom-hole pressure value as defined by item (3).<br>7)  THP: reset the tubing head pressure value for the well as defined by item (3).<br>8)  VFP: reset the vertical lift performance table number as defined by (3).<br>9)  LIFT: reset the artificial lift quantity for use with vertical lift performance tables.<br>10) GUID: reset the guide rate value for wells operating under group control.<br>```{=html} <!-- --> ``` 1)  Note TARGET only defines the variable to be changed, it does not change how a well is controlled. For example, if a well is operating on ORAT control, as defined by the previously entered WCONPROD keyword, entering TARGET equal to LRAT with a value, changes the liquid constraint but the well still remains on ORAT control. Use the WELCNTL keyword in the SCHEDULE section to change the control mode of a well. | None |
| 3 | VALUE<br>Liquid<br>Gas<br>Res Vol<br>Pressure<br>VFP<br>LIFT | A real positive vector of values that defines the value of the variable declared by TARGET for all the wells contained in WLIST. For example if there are four wells in WLIST then there must four real numbers for VALUE. The vector should be terminated by a "/" as indicated in the notes below. | None |
| stb/d<br>Mscf/d<br>rb/d<br>psia<br>dimensionless<br>same as<br>VFPPROD or VFPINJ | sm^3^/day<br>sm3/day<br>rm^3^/day<br>barsa<br>dimensionless<br>same as<br>VFPPROD or VFPINJ | scc/hour<br>scc/hour<br>rcc/hour<br>atma<br>dimensionless<br>same as<br>VFPPROD or VFPINJ |  |
| Notes:<br>1)  The keyword is followed by any number records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.105: WLISTARG Keyword Description

If a well is currently a history matching well, then WLISELTARG should only be used to change a wells bottom-hole pressure limit, vertical flow performance table number or the artificial lift quantity.

See also the WELCNTL keyword, in the SCHEDULE section that can be used to reset the control mode, as well as a well's target and constraints of both rates and pressures.

#### Example

The following example defines two named well lists using the WLIST keyword.

\--

\-- WELL LIST SPECIFICATION

\--

\-- LIST OPER WELL NAME LIST

\-- NAME

WLIST

\'\*BLK-1\' NEW WEL-01M WEL-02M WEL-03M /

\'\*BLK-2\' NEW WEL-03U WEL-05U WEL-06U WEL-10U /

/

\--

\-- WELL PRODUCTION AND INJECTION TARGETS

\--

\-- WELL WELL TARGET

\-- NAME TARG VALUE

WLISTARG

'\*BLK-1' ORAT 2000.0 2000.00 2000.0 /

'\*BLK-2' ORAT 3000.0 3500.00 4000.0 2000.0 /

/

The wells in the \'\*BLK-1\' well list are all given an oil rate of 2,000 stb/d and wells in the \'\*BLK-2\' well list are given rates of 3,000, 3,500, 4,000 and 2,000 stb/d.
