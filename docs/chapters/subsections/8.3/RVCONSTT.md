### RVCONSTT -- Define Constant CGR (Rv) for Each Dry Gas PVT Fluid

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[RVCONSTT](#__RefHeading___Toc138400_3326918171) defines a constant Condensate-Gas Ratio ("CGR" or Rv), for each dry gas[^1] PVT fluid. If the gas has a constant and uniform dissolved condensate concentration, and if the reservoir pressure never drops below the saturation pressure (dew point pressure), then the model can be run more efficiently by omitting the [OIL](#__RefHeading___Toc97439_1778172979) and VAPGAS keywords from the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, treating the gas as a dry gas, and defining a constant Rv (CGR) value with keywords [RVCONST](#__RefHeading___Toc329587_516898843) or [RVCONSTT](#__RefHeading___Toc138400_3326918171) in the [PROPS](#__RefHeading___Toc39329_784232322) section. This results in the model being run as a dry gas problem with no active oil phase. However, OPM Flow takes into account the constant Rv in the calculations and reporting.

This keyword is ignored by OPM Flow but is documented here for completeness.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [RS](#__RefHeading___Toc137361_1317547213) | A real positive value that defines the dry gas CGR for each dry gas PVT table in the model | None |
| stb/Mscf | sm^3^/sm^3^ | scc/scc |  |
| 2 | PRESS | A real positive value that defines that saturation pressure (dew point pressure) for each dry gas PVT table in the model. | 0.0 |
| psia | barsa | atma |  |
| Notes:<br>1)  The keyword is followed by NTPVT rows as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each row must contain two values representing the [RV](#__RefHeading___Toc137365_1317547213) and PRESS variables.<br>3)  Each row is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.138: RVCONSTT Keyword Description

See also the [RVCONST](#__RefHeading___Toc329587_516898843) keyword to define a constant Rv to all the various dry gas PVT tables and the [PVDG](#__RefHeading___Toc104056_57619843) keyword to enter the dry gas properties. All of the aforementioned keywords are in the [PROPS](#__RefHeading___Toc39329_784232322) section.

#### Example

The example sets the dry gas CGR to 5, 6.5 and 8.0 stb/MMscf for PVT tables one, two and three, respectively and the bubble point pressure to 14.7 psia for all three tables.

\--

\-- DRY GAS PVT CONSTANT GCR AND SATURATION PRESSURE

\--

RVCONSTT

\-- RV PSAT

\-- STB/MSCF PSIA

\-- \-\-\-\-\-\-\-- \-\-\-\-\--

0.0050 14.7 / TABLE NO. 01

0.0065 14.7 / TABLE NO. 02

0.0080 14.7 / TABLE NO. 03

[^1]: Natural gas that occurs in the absence of condensate or liquid hydrocarbons, or gas that had condensable hydrocarbons removed, is called dry gas. It is primarily methane with some intermediates. The hydrocarbon mixture is solely gas in the reservoir and there is no liquid (condensate surface liquid) formed either in the reservoir or at surface. The term dry indicates that the gas does not contain heavier hydrocarbons to form liquids at the surface conditions. Dry gas typically has GOR\'s greater than 100,000 scf/stb or 18,000 Sm3/m3.
