### GCONSALE -- Define Group Sales Gas Production Targets and Constraints

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[GCONSALE](#__RefHeading___Toc178287_2026549522) defines group sales gas production targets and constraints for when the gas production from an oil field group is exported under a Gas Sales Agreement ("GSA") and the oil field group also has oil production targets and constraints.

Note that the keyword should not be used to control sales gas for a gas field group, as the gas injection rate is used to control the sales gas production with this keyword, that is:

Thus, surplus gas that cannot be sold is re-injected, which requires that there are active gas injectors in the model that are subordinate to groups with gas sales targets. Note that the surplus gas re-injection rates are automatically calculated by OPM Flow at each time step.

| 1 | GRPNAME | A character string of up to eight characters in length that defines the group name for which the group gas sales target and constraints are being defined. The group named FIELD is the top most group and should be used to set the gas sales targets and constraints for the field.<br>Note that the group hierarchy should be defined by the [GRUPTREE](#__RefHeading___Toc118321_1596574740) keyword when there is more than one level of groups, otherwise all the groups will sit directly under the FIELD group in the group tree hierarchy. | None |
| --- | --- | --- | --- |
| 2 | GSALE | GSALE should either be set to:<br>1)  A real positive value that defines the gas sales rate for the group, or,<br>2)  A real negative value that switches off both gas sales and gas re-injection for the group.<br>This value may be specified using a User Defined Argument (UDA).<br>Note that if GSALE has been set to switch off both gas sales and gas re-injection, then the [GCONINJE](#__RefHeading___Toc134874_2055188184) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section may be used to re-enable gas re-injection again. | None |
| Mscf/d | sm^3^/day | scc/hour |  |
| 3 | GSALEMAX | A real positive value that must be greater than GSALE that defines the maximum allowed gas sales rate. If GSALE exceeds GSALEMAX then the action defined by the [ACTION](#__RefHeading___Toc148342_63720426) variable on this keyword is implemented at the end of the current time step.<br>This value may be specified using a User Defined Argument (UDA). | 1 x 10^20^ |
| Mscf/d | sm^3^/day | scc/hour |  |
| 4 | GSALEMIN | A real positive value that must be less than GSALE that defines the minimum allowed gas sales rate. If GSALE is less than GSALEMIN then one of the following actions will be implemented at the end of the current time step:<br>1)  If the group's maximum gas production rate constraint is constraining the gas rate, then reset the constraint to satisfy the group's minimum gas sales rate (GSALEMIN), else:<br>2)  If the group has active subordinate dedicated gas producers, as defined by the [WGASPROD](#__RefHeading___Toc121396_332691817) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, then reset their gas target rates to satisfy GSALEMIN, else:<br>3)  If there are subordinate dedicated gas producers for the group in a drilling queue, open the next dedicated well and set the well's gas rate to satisfy GSALEMIN. Note that only wells that are subordinate to the group and are not under gas rate control or group prioritization are considered for opening.<br>4)  If there are no appropriate subordinate dedicated gas producers for the group in a drilling queue, open the next non-dedicated well and set the well's gas rate to satisfy GSALEMIN. Again, note that only wells that are subordinate to the group and are not under gas rate control or group prioritization are considered for opening.<br>If none of the above actions can be implemented then the minimum gas sales rate will not be satisfied.<br>This value may be specified using a User Defined Argument (UDA). | -1 x 10^20^ |
| 5 | [ACTION](#__RefHeading___Toc148342_63720426) | A defined character string that defines the action to be taken if the maximum gas sales rate, GSALEMAX, is violated. [ACTION](#__RefHeading___Toc148342_63720426) should be set to one of the following character strings:<br>1)  NONE: no action is taken.<br>2)  CON: close the worst offending connection in the worst offending well. If connections have been grouped as completions then the worst offending completion in the worst offending well will be closed.<br>3)  +CON: close the worst offending connection and all below it in the worst offending well. If connections have been grouped as completions then the worst offending completion and all below it in the worst offending well will be closed.<br>4)  WELL: close the worst offending well.<br>5)  PLUG: plug back the worst offending well. This option is not implemented in OPM Flow.<br>6)  RATE: the group's production rate target is reduced to equal GSALEMAX, after accounting for fuel gas ([GCONSUMP](#__RefHeading___Toc188037_2026549522) keyword) and the current rate of re-injection. This will also place the group on gas production control.<br>7)  [END](#__RefHeading___Toc46631_2479612490): stop the simulation at the end of the report step.<br>The corrective action takes places at the end of the time step in which the constraint is violated. | None |
| Notes:<br>1)  User Defined Quantities (\"UDQ\") can be used as User Defined Arguments (\"UDA\") for various group, well, and connection keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. User Defined Arguments are activated using the [UDADIMS](#__RefHeading___Toc65914_1778172979) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, and defined by the [UDQ](#__RefHeading___Toc161095_2932703077) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.<br>2)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

*Table 12.32: GCONSALE Keyword Description*
[GCONSALE](#__RefHeading___Toc178287_2026549522) can also be used with the [GCONINJE](#__RefHeading___Toc134874_2055188184) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section in order to apply additional limits, for example by applying a maximum group injection rate. In this scenario, the TARGET variable on the [GCONINJE](#__RefHeading___Toc134874_2055188184) keyword must be set to "REIN", and if desired, a re-injection fraction (REIN on the [GCONINJE](#__RefHeading___Toc134874_2055188184) keyword), or any other constraint.

See also the [GCONSUMP](#__RefHeading___Toc188037_2026549522) in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section that defines the fuel gas requirements for groups.

#### Example

The following examples sets the field gas sales target rate:

\--

\-- GROUP GAS SALES FOR OIL FIELDS

\--

\-- GRUP GAS MAX MIN CNTL

\-- NAME SALES RATE RATE ACTN

GCONSALE

FIELD 40E3 50E3 20E3 RATE /

/

Here the field has a gas sales target of 40 MMscf/d, with a maximum rate of 50 MMscf/d and a minimum of 20 MMscf/d. If the maximum gas sales rate is exceeded then the group's gas production rate target is reduced to equal GSALEMAX, after accounting for fuel gas and the current rate of re-injection. This will also place the group on gas production control.
