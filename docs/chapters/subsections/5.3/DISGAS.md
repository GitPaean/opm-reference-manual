### DISGAS -- Activate the Dissolved Gas Phase in the Model

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword indicates that dissolved gas is present in live[^1] oil in the model and the keyword should only be used if the there is both oil and gas phases in the model. The keyword may be used for oil-water and oil-water-gas input decks that contain the oil and gas phases. The keyword will also invoke data input file checking to ensure that all the required oil and gas phase input parameters are defined in the input deck.

If the oil has a constant and uniform dissolved gas concentration, Gas-Oil Ratio ("GOR"), and if the reservoir pressure never drops below the saturation pressure (bubble point pressure), then the model can be run more efficiently by omitting the [GAS](#__RefHeading___Toc38607_2267116897) and [DISGAS](#__RefHeading___Toc39767_2267116897) keywords from the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, treating the oil as a dead oil[^2], and defining a constant Rs (GOR) value with keyword [RSCONST](#__RefHeading___Toc138398_332691817) or [RSCONSTT](#__RefHeading___Toc138400_332691817) in the [PROPS](#__RefHeading___Toc39329_784232322) section. This results in the model being run with as a dead oil problem with no active gas phase. However, OPM Flow takes into account the constant Rs in the calculations and reporting.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- DISSOLVED GAS IN LIVE OIL IS PRESENT IN THE RUN

\--

DISGAS

The above example declares that the dissolved gas in the oil phase is active in the model.

[^1]: "Live" oil is oil that contains gas in solution, which is normally the case for most conventional oil reservoirs. However, for oil reservoirs classified as heavy oil reservoirs, the in situ dissolved gas may be negligible and oil would then be classified as gas-free oil which is commonly referred to as "dead" oil.

[^2]: "Dead" oil is oil that it contains no dissolved gas or a relatively thick oil or residue that has lost its volatile components.
