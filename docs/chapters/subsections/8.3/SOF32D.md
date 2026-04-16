### SOF32D -- Oil Saturation Tables with Respect to Water and Gas (Three Phase)

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [SOF32D](#__RefHeading___Toc765497_4250154414) keyword defines the three phase oil relative permeability versus water and gas saturation tables for when oil, gas and water are present in the input deck. The keyword should only be used if oil, gas and water are present in the input deck. Normally the simulator calculates the three-phase oil relative permeabilities based on the entered two phase tables of water-oil and gas-oil, combined with the [STONE1](#__RefHeading___Toc210162_2884651453) and [STONE2](#__RefHeading___Toc210166_2884651453) keywords in the [PROPS](#__RefHeading___Toc39329_784232322) section that determine the method used to generate the thee phase oil relative permeability curves. [SOF32D](#__RefHeading___Toc765497_4250154414) allows for the direct input of the three phase tables, as such the [STONE1](#__RefHeading___Toc210162_2884651453) and [STONE2](#__RefHeading___Toc210166_2884651453) keywords should not be entered if [SOF32D](#__RefHeading___Toc765497_4250154414) is used in the input deck.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
