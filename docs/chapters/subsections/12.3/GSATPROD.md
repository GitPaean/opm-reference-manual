### GSATPROD -- Define Group Satellite Production Rates

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [GSATPROD](#__RefHeading___Toc202038_870710203) keyword defines a satellite group's oil, water and gas production rates in the model. Satellite groups are not connected to the reservoir model and therefore have no wells or subordinate groups associated with them, they are nevertheless connected to other higher level groups and higher level groups within a network model (if activated). They provide a means to "add-in" outside injection and production to the model without modeling the "add-in" reservoirs.

This keyword is used to import additional fluid streams into the model from other sources (fields, reservoirs, etc.) that are not defined in the current run. For example, if Fields A, B and C are supplying gas to a power plant, but only Field A is being modeled in the current input deck, then production from Fields B and C can be incorporated into model in order to meet the plant demand. Note in this case the import gas rates from Fields B and C are fixed, and therefore Field A acts like a "swing" producer to match the gas demand target.

| 1 | GRPNAME | A character string of up to eight characters in length that defines the satellite group name for which the group production import rates are being defined. The group named FIELD is the top most group and should not be used with this keyword.<br>Note that the group hierarchy should be defined by the [GRUPTREE](#__RefHeading___Toc118321_1596574740) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section when there is more than one level of groups, otherwise all the groups will sit directly under the FIELD group in the group tree hierarchy.<br>Note that a satellite group cannot have subordinate groups or wells. | None |
| --- | --- | --- | --- |
| 2 | ORAT | A real value, greater than or equal to zero, that defines the satellite's surface oil production rate to be imported into the model.<br>This value may be specified using a User Defined Argument (UDA). | 0.0 |
| stb/d | sm^3^/day | scc/hour |  |
| 3 | WRAT | A real value, greater than or equal to zero, that defines the satellite's surface water production rate to be imported into the model.<br>This value may be specified using a User Defined Argument (UDA). | 0.0 |
| stb/d | sm^3^/day | scc/hour |  |
| 4 | GRAT | A real value, greater than or equal to zero, that defines the satellite's surface gas production rate to be imported into the model.<br>This value may be specified using a User Defined Argument (UDA). | 0.0 |
| Mscf/d | sm^3^/day | scc/hour |  |
| 5 | RESV | A real value, greater than or equal to zero, that defines the satellite's reservoir volume production rate to be imported into the model.<br>This item is not supported by OPM Flow and should be defaulted (1\*) or set to zero. | 0.0 |
| rb/d | rm^3^/day | rcc/hour |  |
| 6 | GASLIFT | A real value, greater than or equal to zero, that defines the satellite's gas lift gas to be imported for this group.<br>A value for GASLIFT is only required if externally supplied gas lift is being imported into the model, and:<br>1)  The Network Model is active in the input deck via the [NETWORK](#__RefHeading___Toc311583_1841740821) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Here, GASLIFT is applied to the production network in order to calculate the pressure drop through the network, for branches that have:<br>(1) OPTION2 set to FLO on the [GRUPNET](#__RefHeading___Toc118319_1596574740) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, or<br>(2) the GASLIFT parameter on the [NODEPROP](#__RefHeading___Toc212708_2026549522) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section set to YES, for when the Extended Network Model is being used. as per the [BRANPROP](#__RefHeading___Toc162078_289573908) and [NODEPROP](#__RefHeading___Toc212708_2026549522) keywords, in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.<br>2)  The Gas Lift Optimization Model is active in the deck via the [LIFTOPT](#__RefHeading___Toc118992_332691817) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. In this case GASLIFT is applied to GRPNAME's superordinate group's gas supply constraints based on the [GLIFTOPT](#__RefHeading___Toc111805_332691817) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. For clarity, [GLIFTOPT](#__RefHeading___Toc111805_332691817) constraint violations result in the groups being modeled having their rates adjusted, whereas satellite group rates are not affected.<br>This item is not supported by OPM Flow and should be defaulted (1\*) or set to zero. | 0.0 |
| Mscf/d | sm^3^/day | scc/hour |  |
| 7 | CALRATE | A real value greater than or equal to zero that defines the satellite\'s calorific production rate.<br>This item is not supported by OPM Flow and should be defaulted (1\*) or set to zero. | 0.0 |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

*Table 12.46: GSATPROD Keyword Description*
See also the [GSATINJE](#__RefHeading___Toc116596_332691817) and [GRUPTREE](#__RefHeading___Toc118321_1596574740) keywords to define satellite injection rates and the group hierarchy, respectively. For non-satellite groups see the [GCONINJE](#__RefHeading___Toc134874_2055188184) and [GCONPROD](#__RefHeading___Toc146746_4203985108) keywords. All the aforementioned keywords are in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Example

The example below is based on a dry gas field, with the main field FLD-A being modeled in the input deck with two groups (FLD-A1 and FLD-A2), combined with two satellite gas fields, FLD-B and FLD-C.

\-- ==============================================================================

\--

\-- SCHEDULE SECTION

\--

\-- ==============================================================================

SCHEDULE

\--

\-- DEFINE GROUP TREE HIERARCHY

\-- LOWER HIGHER

\-- GROUP GROUP

GRUPTREE

FLD-A FIELD /

FLD-A1 FLD-A /

FLD-A2 FLD-A /

FLD-B FIELD /

FLD-C FIELD /

/

\--

\-- GROUP PRODUCTION CONTROLS

\--

\-- GRUP CNTL OIL WAT GAS LIQ CNTL GRUP GUIDE GUIDE CNTL

\-- NAME MODE RATE RATE RATE RATE OPT CNTL RATE DEF WAT

GCONPROD

FIELD GRAT 1\* 1\* 450E3 1\* 1\* 1\* /

FLD-A FLD 1\* 1\* 450E3 1\* 1\* 1\* /

/

\--

\-- LOAD INCLUDE FILE - LOAD ALL WELLS AND VFP TABLES

\--

INCLUDE

\'FLD-A-P50-WELLS.INC\' /

\--

\-- SATELLITE GROUP PRODUCTION CONTROLS

\--

\-- GRUP OIL WAT GAS RESV GAS CALORIFIC

\-- NAME RATE RATE RATE RATE LIFT RATE

GSATPROD

FLD-B 10.0 0.00 30E3 1\* 1\* /

FLD-C 20.0 5.50 20E3 0.0 1\* /

/

\--

\-- ADVANCE SIMULATION BY REPORTING DATE

\--

DATES

1 FEB 2021 /

/

\--

\-- SATELLITE GROUP PRODUCTION CONTROLS

\--

\-- GRUP OIL WAT GAS RESV GAS CALORIFIC

\-- NAME RATE RATE RATE RATE LIFT RATE

GSATPROD

FLD-B 10.0 0.00 30E3 0.0 1\* /

FLD-C 20.0 9.00 20E3 0.0 1\* /

/

Since the field gas rate is set to 450 MMscf/d and the satellite production is 50 MMscf/d, then FLD-A will produce only 400 MMscf/d and not the stipulated 450 MMscf/d on the [GCONPROD](#__RefHeading___Toc146746_4203985108) keyword.
