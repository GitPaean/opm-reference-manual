### VAPWAT -- Activate Vaporized Water in the Dry and Wet Gas Phases

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword indicates that vaporized water is present in the gas phase and the keyword should only be used if both water and gas phases are present in the model. VAPWAT should also be used in conjunction with the PRECSALT keyword in the RUNSPEC section in order to activate OPM Flow's Salt Precipitation model. VAPWAT may be used for gas-water and oil-water-gas input decks that contain the oil, gas and water phases.

Note that if the VAPWAT keyword is in the input deck then either the PVTGW or PVTGWO keywords in PROPS section should be used to defined the gas and water PVT properties.

Secondly, if both the VAPWAT keyword and the PRECSALT keyword (used to activate the OPM Flow's Salt Precipitation model) are present in the input deck, then the RWGSALT keyword in the PROPS section also needs to be present.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- VAPORIZED WATER IN DRY/WET GAS IS PRESENT IN THE RUN (OPM FLOW KEYWORD)

\--

VAPWAT

The above example declares that the vaporized water is present in the gas phase and is active in the model.
