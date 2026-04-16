### VAPWAT -- Activate Vaporized Water in the Dry and Wet Gas Phases

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword indicates that vaporized water is present in the gas phase and the keyword should only be used if both water and gas phases are present in the model. [VAPWAT](#__RefHeading___Toc317543_3149455253) should also be used in conjunction with the [PRECSALT](#__RefHeading___Toc332782_3149455253) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section in order to activate OPM Flow's Salt Precipitation model. [VAPWAT](#__RefHeading___Toc317543_3149455253) may be used for gas-water and oil-water-gas input decks that contain the oil, gas and water phases.

Note that if the [VAPWAT](#__RefHeading___Toc317543_3149455253) keyword is in the input deck then either the [PVTGW](#__RefHeading___Toc355649_3149455253) or [PVTGWO](#__RefHeading___Toc356776_4176551521) keywords in [PROPS](#__RefHeading___Toc39329_784232322) section should be used to defined the gas and water PVT properties.

Secondly, if both the [VAPWAT](#__RefHeading___Toc317543_3149455253) keyword and the [PRECSALT](#__RefHeading___Toc332782_3149455253) keyword (used to activate the OPM Flow's Salt Precipitation model) are present in the input deck, then the [RWGSALT](#__RefHeading___Toc304264_1667959253) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section also needs to be present.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- VAPORIZED WATER IN DRY/WET GAS IS PRESENT IN THE RUN (OPM FLOW KEYWORD)

\--

VAPWAT

The above example declares that the vaporized water is present in the gas phase and is active in the model.
