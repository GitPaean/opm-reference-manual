### TEMPI -- Define the Initial Temperature Values for All Cells

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the initial reservoir temperature for each cell in the model. The keyword is used to explicitly define the initial reservoir temperature via the Enumeration Initialization method rather than defining a uniform initial temperature or defining temperature versus depth tables.

The initial reservoir temperature must be defined when OPM Flow's thermal option has been activated by the [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Note this is different to the commercial simulator that uses the [TEMP](#__RefHeading___Toc146397_3544483072) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section to activate the black-oil temperature model, and the [THERMAL](#__RefHeading___Toc137276_650382403) keyword to activate the compositional thermal model.

The initial reservoir temperature should be defined when OPM Flow's CO~2~ or H~2~ storage option has been activated by the [CO2STORE](#__RefHeading___Toc387968_1616145207) or [H2STORE](#REF_HEADING_KEYWORD_H2STORE) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [TEMPI](#__RefHeading___Toc117385_650382403) | [TEMPI](#__RefHeading___Toc117385_650382403) is an array of real positive numbers assigning the initial temperature to each cell in the model.<br>Repeat counts may be used, for example 20\*100.0. | None |
| ^o^F | ^o^C | ^o^C |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 10.58: TEMPI Keyword Description

See also the [RTEMP](#__RefHeading___Toc111816_2939291539) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section and the [RTEMPVD](#__RefHeading___Toc108628_29392915391) keyword in the [SOLUTION](#__RefHeading___Toc43947_784232322) section for alternative ways to initialize the model's initial temperature.

#### Example

\--

\-- DEFINE GRID BLOCK TEMPERATURE FOR ALL CELLS

-- (BASED ON NX x NY x NZ = 300)

\--

TEMPI

100\*212.0 100\*215.0 100\*220.0 /

The above example defines the initial temperature to be 212.0, 215.0, and 220.0 oF for the first, second and third layers in the model for all 300 cells, as defined by the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.
