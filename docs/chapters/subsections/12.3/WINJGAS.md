### WINJGAS -- Define Gas Injection Properties for a Well

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WINJGAS](#__RefHeading___Toc27871_3671211675 Copy 1 Copy 1 Copy 1 Copy 2 Copy 1) keyword defines the properties of the injection gas stream, for a given well. Once a gas well stream has been defined via the [WELLSTRE](#__RefHeading___Toc27871_3671211675 Copy 1 Copy 1 Copy 1 Copy 2) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, it can be used with either the [WINJGAS](#__RefHeading___Toc27871_3671211675 Copy 1 Copy 1 Copy 1 Copy 2 Copy 1) or GINJGAS keywords, to set the injected gas composition. Similarly, if an oil well stream has been defined by [WELLSTRE](#__RefHeading___Toc27871_3671211675 Copy 1 Copy 1 Copy 1 Copy 2), then the well stream can be used with the WINJOIL keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, to specify the injected oil composition. Note that, it is unnecessary to use [WINJGAS](#__RefHeading___Toc27871_3671211675 Copy 1 Copy 1 Copy 1 Copy 2 Copy 1) for wells subordinate to a group having gas injection control, with the gas properties set by GINJGAS keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. In this case the injection stream is defined by the GINJGAS keyword. However, if a gas injection well under group control users the [WINJGAS](#__RefHeading___Toc27871_3671211675 Copy 1 Copy 1 Copy 1 Copy 2 Copy 1) keyword, then this fluid, and not the group\'s fluid will be injected instead, at a rate controlled by the group.

The keyword should only be used if the [CO2STORE](#__RefHeading___Toc387968_1616145207) and [GASWAT](#__RefHeading___Toc38607_2267116897 Copy 1) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section have also be activated for the gas-water two component model.

| 1 | WELNAME | A character string of up to eight characters in length that defines the injection well name, for which the gas injection properties are being specified.<br>Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | STREAM | A defined character string that determines the properties of the injection gas, and as should be set to one of the following values:<br>1)  [GAS](#__RefHeading___Toc38607_2267116897): The field separator gas composition is used as the injected gas.<br>2)  GRUP: The well\'s group or upstream group injection fluid is used as the injected gas.<br>3)  GV: This option enables the vapor production of a group, as declared via the [SOURCE](#REF_HEADING_KEYWORD_SOURCE_12_3) parameter on this record, to be used as the injected gas composition.<br>4)  MIX: In this case, the gas injection composition is taken from either the WINJMIX or WINJORD keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, with the name of injected fluid given by the [SOURCE](#REF_HEADING_KEYWORD_SOURCE_12_3) parameter on this record.<br>5)  STREAM: Here the gas injection composition is given by the [WELLSTRE](#__RefHeading___Toc27871_3671211675 Copy 1 Copy 1 Copy 1 Copy 2) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, with the name of injected fluid given by the [SOURCE](#REF_HEADING_KEYWORD_SOURCE_12_3) parameter on this record.<br>6)  WV: This option enables the vapor production from a given well to be used as the injected gas, with the name of the well given by the [SOURCE](#REF_HEADING_KEYWORD_SOURCE_12_3) parameter on this record.<br>*Only the STREAM option is supported by OPM Flow*. | GRUP |
| 3 | [SOURCE](#REF_HEADING_KEYWORD_SOURCE_12_3) | A character string of up to eight characters in length, that defines the source of the gas injection stream, based on the value of STREAM. If STREAM equals GV, then source should be set to a group name. For STREAM equal to MIX or STREAM, then [SOURCE](#REF_HEADING_KEYWORD_SOURCE_12_3) should be set to the name of the gas stream, as defined by the WINJMIX, WINJORD, or [WELLSTRE](#__RefHeading___Toc27871_3671211675 Copy 1 Copy 1 Copy 1 Copy 2) keywords. | None |
| 4 | MAKEUP | The name of the well stream used for the make-up gas, if make-up gas is required for WELNAME to match the injection target for the well.<br>This option is not supported by OPM Flow. | None |
| 5 | STAGE | STAGE defines the separator stage from which the injection gas should be taken from. In this case, the vapor phase from any stage may be used, and the default value of zero users the total vapor phase from the separator.<br>This option is not supported by OPM Flow. | 0 |
| Notes:<br>1)  The keyword is followed by any number records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.100: WINJGAS Keyword Description

#### Example

The following example defines how to specify a two component formulation, together with defining the names of the composition components, to be used with the [CO2STORE](#__RefHeading___Toc387968_1616145207) and [GASWAT](#__RefHeading___Toc38607_2267116897 Copy 1) options.

\-- ==============================================================================

\--

\-- PROPS SECTION

\--

\-- ==============================================================================

PROPS \--

\-- CONFIRM NUMBER OF COMPOSITIONAL COMPONENTS (OPM FLOW KEYWORD)

\--

NCOMPS

2 /

\--

\-- DEFINE COMPOSITIONAL COMPONENTS NAMES (OPM FLOW KEYWORD)

\--

CNAMES

\'CO2\'

\'H2O\' /

The second part of the example, defines the well stream for the above two component CO~2~ water system.

\-- ==============================================================================

\--

\-- SCHEDULE SECTION

\--

\-- ==============================================================================

SCHEDULE

\--

\-- WELL STREAM INJECTION COMPOSITION (OPM FLOW Keyword)

\--

\-- WELL \-- WELL STREAM COMPOSITIONAL COMPONENT \--

\-- STREAM \-- MOLE FRACTIONS \--

WELLSTRE

\'C02STREAM\' 1.000 0.000 /

/

\--

\-- WELL GAS INJECTION PROPERTIES

\--

\-- WELL STREAM SOURCE MAKEUP SEP

\-- NAME OPTION DEPTH GAS STAGE

WINJGAS

GI01 STREAM C02STREAM 1\* 1\* /

/

Here the well stream consists of 100% CO2 and zero water, with well GI01 using the gas injection properties as defined by the [WELLSTRE](#__RefHeading___Toc27871_3671211675 Copy 1 Copy 1 Copy 1 Copy 2) keyword and allocated via the [WINJGAS](#__RefHeading___Toc27871_3671211675 Copy 1 Copy 1 Copy 1 Copy 2 Copy 1) keyword.

Finally, the gas injection rate is set via the [WCONINJE](#__RefHeading___Toc146750_4203985108) keyword as shown below.

\--

\-- WELL INJECTION CONTROLS

\--

\-- WELL FLUID OPEN/ CNTL SURF RESV BHP THP VFP

\-- NAME TYPE SHUT MODE RATE RATE PRES PRES TABLE

WCONINJE

GI01 GAS OPEN RATE 10E4 1\* 300 1\* 1\* /

/

Thus, gas injector GI01 will inject 10 x 10^4^ m^3^ of CO~2~ per day, assuming metric units.
