### WTRACER -- Define An Injection Well's Tracer Concentration

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WTRACER](#__RefHeading___Toc97665_3261743917) keyword defines the tracer concentration of the injection fluid being injected by an injection well. This keyword should only be used if the Tracer option has been invoked by the [TRACERS](#__RefHeading___Toc76509_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section and the tracers have be declared via the [TRACER](#__RefHeading___Toc121485_83452205) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name of an injection well for which the tracer fraction data is being defined.<br>Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | NAME | A three letter character string defining the tracer's name which has previously been defined via the [TRACER](#__RefHeading___Toc121485_83452205) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section.<br>Note it is best to avoid names beginning with the letters F, S, and T as these names may create naming issues in post-processing software. | None |
| 3 | TRCON | A real positive value that defines the tracer concentration of the well's injection stream.<br>This value may be specified using a User Defined Argument (UDA). | None |
| Liquid: 1/stb<br>Gas: 1/Mscf | Liquid: 1/sm^3^<br>Gas: 1/sm^3^ | Liquid: 1/scc<br>Gas: 1/scc |  |
| 4 | TRCUM | A real positive value that defines the cumulative tracer concentration factor of the well's injection stream.<br>This value may be specified using a User Defined Argument (UDA).<br>This feature is currently not supported by OPM Flow. | None |
| Liquid: 1/stb<br>Gas: 1/Mscf | Liquid: 1/sm^3^<br>Gas: 1/sm^3^ | Liquid: 1/scc<br>Gas: 1/scc |  |
| 5 | GRPNAME | A character string of up to eight characters in length that defines the group from which the produced tracer concentration should be used for the well's injection stream.<br>GRPNAME must have been previously defined via the [GCONPROD](#__RefHeading___Toc146746_4203985108) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, unless the FIELD group has been specified here.<br>Note if GRPNAME is not defined then TRCON will be used for the tracer concentration of the well's injection stream.<br>This feature is currently not supported by OPM Flow. | None |
| Notes:<br>1)  User Defined Quantities (\"UDQ\") can be used as User Defined Arguments (\"UDA\") for various group, well, and connection keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. User Defined Arguments are activated using the [UDADIMS](#__RefHeading___Toc65914_1778172979) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, and defined by the [UDQ](#__RefHeading___Toc161095_2932703077) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.<br>2)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.129: WTRACER Keyword Description

Injection wells that are not declared via this keyword have their tracer concentrations set to zero.

See also the [GCONINJE](#__RefHeading___Toc134874_2055188184) keyword to define a group's injection targets and constraints, and the [WCONINJE](#__RefHeading___Toc146750_4203985108) keyword to define an injection well's targets and constraints. All the aforementioned keywords are described in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Example

The following example defines the tracer concentrations for two gas injectors and three water injection wells, with water injection well WI02 having no 'WAT' tracer injected in the water phase.

\--

\-- DEFINE CONCENTRATION OF TRACERS IN THE INJECTION STREAMS,

\-- INJECTION TRACER CONCENTRATIONS NOT DEFINED USING THE WTRACER

\-- KEYWORD ARE ASSUMED TO BE ZERO.

\--

\-- WELL NAME TRACER TRACER TRACER

\-- NAME TRACER CONC CUM GROUP

WTRACER

GI01 \'GAS\' 1.0 /

GI02 \'GAS\' 1.0 /

WI01 \'WAT\' 1.0 /

WI02 \'WAT\' 0.0 /

WI03 \'WAT\' 1.0 /

/

Note the terminating "/" for the keyword.
