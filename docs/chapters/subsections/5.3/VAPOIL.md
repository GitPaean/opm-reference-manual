### VAPOIL -- Activate the Vaporized Oil in Wet Gas Phase in the Model

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword indicates that vaporized oil (more commonly referred to as condensate) is present in wet[^1] gas in the model and the keyword should only be used if the there is both oil and gas phases in the model. The keyword may be used for gas-water and oil-water-gas input decks that contain the oil and gas phases. The keyword will also invoke data input file checking to ensure that all the required oil and gas phase input parameters are defined in the input deck.

If the gas has a constant and uniform vaporized oil concentration, Condensate-Gas Ratio ("CGR"), and if the reservoir pressure never drops below the saturation pressure (dew point pressure), then the model can be run more efficiently by omitting the [OIL](#__RefHeading___Toc97439_1778172979) and [VAPOIL](#__RefHeading___Toc56610_2267116897) keywords from the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, treating the gas as a dry gas[^2], and defining a constant Rv (CGR) value with keyword [RVCONST](#__RefHeading___Toc329587_516898843) or [RVCONSTT](#__RefHeading___Toc138400_3326918171) in the [PROPS](#__RefHeading___Toc39329_784232322) section. This results in the model being run with as a dry gas problem with no active oil (condensate) phase. However, OPM Flow takes into account the constant Rv in the calculations and reporting.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- VAPORIZED OIL IN WET GAS IS PRESENT IN THE RUN

\--

VAPOIL

The above example declares that the vaporized oil, i.e. condensate, in the gas phase is active in the model.

[^1]: Natural gas that contains significant heavy hydrocarbons such as propane, butane and other liquid hydrocarbons is known as wet gas or rich gas. The general rule of thumb is if the gas contains less methane (typically less than 85% methane) and more ethane, and other more complex hydrocarbons, it is labeled as wet gas. Wet gas normally has GOR\'s less than 100,000 scf/stb or 18,000 Sm3/m3, with the condensate having a gravity greater than 50 ^o^[API](#__RefHeading___Toc4422_421927891).

[^2]: Natural gas that occurs in the absence of condensate or liquid hydrocarbons, or gas that had condensable hydrocarbons removed, is called dry gas. It is primarily methane with some intermediates. The hydrocarbon mixture is solely gas in the reservoir and there is no liquid (condensate surface liquid) formed either in the reservoir or at surface. The term dry indicates that the gas does not contain heavier hydrocarbons to form liquids at the surface conditions. Dry gas typically has GOR\'s greater than 100,000 scf/stb or 18,000 Sm3/m3.
