### PLYVISCT -- Define Polymer-Temperature Viscosity Scaling Factors

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

PLYSVISCT defines the polymer-temperature viscosity scaling factor tables applied to pure water that are used to determine the viscosity of the polymer at a given temperature with respect to increasing polymer concentration within a grid block. Both the polymer option must be activated by the POLYMER keyword and the temperature option invoked by the TEMP keyword in the RUNSPEC section in order to use this keyword. However the BRINE keyword in the RUNSPEC must not be used with this keyword, that is the salt sensitivity options should be deactivated.

See also the PLYVSCST keyword in the PROPS section to enter polymer viscosity scaling factor data that is dependent on both salt and reservoir temperature.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
