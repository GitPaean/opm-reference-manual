### DISGASW -- Activate Dissolved Gas in the Water Phase in the Model

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword indicates that dissolved gas is present in the water phase in the model. The keyword may only be used for gas-water input decks that contain just the gas and the water phases, which must also be declared. The keyword will also invoke data input file checking to ensure that all the required gas and water phase input parameters are defined in the input deck.

The activation of this phase may be used for modeling the production of gas from the water in gas fields, where gas has dissolved into the in situ water phase. Although this is always the case, the volumes are usually insignificant compared with the volumes in the hydrocarbon zones, and therefore in nearly all cases the dissolved gas volumes are usually ignored in terms of resource volumes. For gas fields, the interest is normally the amount of water in the gas phase, as this influences the liquid loading rate as the water is liberated from the gas as the fluid transverses up the wellbore.

The second, and primary, application of this black-oil formulation is for CO~2~ storage, where injection of CO~2~ injection is being conducted in either depleted gas fields or in water filled aquifer zones. Activating the dissolved gas in the water phase under these circumstances will allow the CO~2~ to dissolve into the water phase based on the entered PVT properties in the [PROPS](#__RefHeading___Toc39329_784232322) section. In this case the [CO2STORE](#__RefHeading___Toc387968_1616145207) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section should also be present in the deck.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- GAS PHASE IS PRESENT IN THE RUN

\--

GAS

\--

\-- WATER PHASE IS PRESENT IN THE RUN

\--

WATER

\--

\-- DISSOLVED GAS IN WATER IS PRESENT IN THE RUN (OPM FLOW KEYWORD)

\--

DISGASW

\--

\-- ACTIVATE CO2 STORAGE IN THE MODEL (OPM FLOW CO2 STORAGE KEYWORD)

\--

CO2STORE

The above example declares that the gas and water phases are present, and that the dissolved gas in the water phase is also active in the model, for modeling CO2 storage.
