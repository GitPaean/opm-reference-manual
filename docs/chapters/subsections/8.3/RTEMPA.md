### RTEMPA -- Define the Initial Reservoir Temperature for the Model

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the initial reservoir temperature for the model. Note that the [RTEMPA](#__RefHeading___Toc111818_2939291539) keyword is an alias for [RTEMP](#__RefHeading___Toc111816_2939291539), and that both keywords are supported by OPM Flow, in both the [PROPS](#__RefHeading___Toc39329_784232322) and [SOLUTION](#__RefHeading___Toc43947_784232322) sections, but are treated as being mutually exclusive.

The initial reservoir temperature must be defined when OPM Flow's thermal option has been activated by the [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Note this is different to the commercial simulator that uses the [TEMP](#__RefHeading___Toc146397_3544483072) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section to activate the black-oil temperature model, and the [THERMAL](#__RefHeading___Toc137276_650382403) keyword to activate the compositional thermal model.

The initial reservoir temperature should be defined when OPM Flow's CO~2~ or H~2~ storage option has been activated by the [CO2STORE](#__RefHeading___Toc387968_1616145207) or [H2STORE](#REF_HEADING_KEYWORD_H2STORE) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [RTEMPA](#__RefHeading___Toc111818_2939291539) | Single real positive value that define the reservoir temperature for the model. | None |
| ^o^F | ^o^C | ^o^C |  |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 8.136: RTEMPA Keyword Description

See also the [RTEMPVD](#__RefHeading___Toc108628_29392915391) keyword in [SOLUTION](#__RefHeading___Toc43947_784232322) section to define the reservoir temperature as a function of depth.

#### Example

\--

\-- RESERVOIR

\-- TEMPERATURE

\-- \-\-\-\-\-\-\-\-\-\--

RTEMPA

190.0 / RESERVOIR TEMPERATURE

The above example defines the reservoir temperature to be 190 oF.
