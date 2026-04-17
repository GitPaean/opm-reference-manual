### PLYVISCS -- Define Polymer-Salt Viscosity Scaling Factors

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

PLYSVISCS defines the polymer-salt viscosity scaling factor tables applied to pure water that are used to determine the viscosity of a polymer-salt mixture with respect to increasing polymer concentration within a grid block. The polymer option must be activated by the POLYMER keyword, as well as the brine phase declared by the BRINE keyword in the RUNSPEC section in order to use this keyword. However the ECLM keyword in the RUNSPEC must not be used with this keyword.

See also the PLYVSCST keyword in the PROPS section to enter polymer viscosity scaling factor data that is dependent on both salt and reservoir temperature.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
