### SOURCE -- Define Source Term

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [SOURCE](#REF_HEADING_KEYWORD_SOURCE_12_3) keyword defines a mass and heat source term for a given pseudo component in the specified grid block.

One source term can be added to each grid block for each pseudo component active in the model. If the source term for a given pseudo component is later redefined in the same block this will replace the previous source term.

This is an OPM Flow specific keyword that is not supported by the commercial simulator.

| 1 | I | A positive integer greater than zero and less than or equal to NX that defines the location of the source term in the I-direction. | None |
| --- | --- | --- | --- |
| 2 | J | A positive integer greater than zero and less than or equal to NY that defines the location of the source term in the J-direction. | None |
| 3 | K | A positive integer greater than zero and less than or equal to NZ that defines the location of the source term in the K-direction. | None |
| 4 | COMP | A defined character string that defines the pseudo component to be injected by the source term, COMP should be set to one of the following character strings:<br>1)  [OIL](#__RefHeading___Toc97439_1778172979): the source term will inject oil.<br>2)  [GAS](#__RefHeading___Toc38607_2267116897): the source term will inject gas.<br>3)  [WATER](#__RefHeading___Toc38611_2267116897): the source term will inject water.<br>4)  [SOLVENT](#__RefHeading___Toc62787_1778172979): the source term will inject solvent.<br>5)  [POLYMER](#__RefHeading___Toc38609_2267116897): the source term will inject polymer.<br>6)  MICR: the source term will inject microbes.<br>7)  OXYG: the source term will inject oxygen.<br>8)  UREA: the source term will inject urea.<br>9)  NONE: no pseudo component specified.<br>The [SOLVENT](#__RefHeading___Toc62787_1778172979) or [POLYMER](#__RefHeading___Toc38609_2267116897) option should only be specified if the solvent or polymer model has been activated by the [SOLVENT](#__RefHeading___Toc62787_1778172979) or [POLYMER](#__RefHeading___Toc38609_2267116897) keyword respectively in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. MICR, OXYG, or UREA requires the [MICP](#__RefHeading___Toc383375_111689907) keyword.<br>A pseudo component must be specified if the mass injection rate is non-zero. | NONE |
| 5 | RATE | A real value that defines the source term's mass injection rate of the specified component COMP. | 0.0 |
| lb/day | kg/day | gm/hour |  |
| 6 | HRATE | A real value that defines the source term's heat injection rate^1^.<br>The heat injection rate should only be specified if the thermal model has been activated by the [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | 0.0 |
| Btu/day | kJ/day | J/hour |  |
| 7 | [TEMP](#__RefHeading___Toc146397_3544483072) | A real value that defines the temperature of the injected component^1^.<br>The temperature of the source term should only be specified if the thermal model has been activated by the [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | None |
| °F | °C | °C |  |
| Notes:<br>1)  The heat injection rate HRATE and the temperature of the injected component [TEMP](#__RefHeading___Toc146397_3544483072) cannot be specified in the same record, if one of these has been specified the other should be defaulted.<br>2)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.3.223.1: SOURCE Keyword Description

See also the [BCCON](#REF_HEADING_KEYWORD_BCCON) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section and the [BCPROP](#REF_HEADING_KEYWORD_BCPROP) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section that can be used to specify boundary conditions.

#### Example

The first example adds two source terms to block (I=2, J=4, K=6) that inject gas at a mass flow rate of 25,000 lb/day and inject water at a mass flow rate of 1,000 lb/day respectively.

\--

\-- DEFINE SOURCE TERM

\--

\-- I J K COMP MASS HEAT TEMP

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-- RATE RATE

SOURCE

2 4 6 GAS 25000 1\* 1\* /

2 4 6 WATER 1000 1\* 1\* /

/

The second example adds a source term to block (I=2, J=4, K=6) that injects gas at a mass flow rate of 25,000 lb/day and a heat injection rate of 1.25 × 10^6^ Btu/day in a thermal black-oil simulation.

\--

\-- DEFINE SOURCE TERM

\--

\-- I J K COMP MASS HEAT TEMP

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-- RATE RATE

SOURCE

2 4 6 GAS 25000 1.25E6 1\* /

/

The third example adds a source term to block (I=2, J=4, K=6) that injects gas at a mass flow rate of 25,000 lb/day and a temperature of 200°F in a thermal black-oil simulation.

\--

\-- DEFINE SOURCE TERM

\--

\-- I J K COMP MASS HEAT TEMP

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-- RATE RATE

SOURCE

2 4 6 GAS 25000 1\* 200 /

/
