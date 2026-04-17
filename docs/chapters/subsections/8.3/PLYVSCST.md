### PLYVSCST -- Define Polymer-Salt-Temperature Viscosity Scaling Factors

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

PLYVSCST defines the polymer-salt-temperature viscosity scaling factor tables applied to pure water that are used to determine the viscosity of the polymer at a given salt concentration and for a given temperature, with respect to increasing polymer concentration within a grid block. Both the polymer option must be activated by the POLYMER keyword and the temperature option invoked by the TEMP keyword in the RUNSPEC section in order to use this keyword. In addition, the BRINE keyword in the RUNSPEC must also be invoked. The keyword is used in conjunction with the SALTNODE keyword to define the various salt concentrations and the TEMPNODE keyword to define the various reservoir temperatures. Both keywords are in the PROPS section.

See also the PLYVISCS keyword in the PROPS section to enter polymer viscosity scaling factor data that is dependent just salt concentration and the PLYVISCT keyword in the PROPS section to enter polymer viscosity scaling factor data that is dependent just on reservoir temperature.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
