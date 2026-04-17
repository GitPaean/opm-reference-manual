### PLYTRRFA -- Define Polymer Rock Permeability Reduction versus Temperature Option

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The PLYTRRFA keyword defines the how the polymer rock permeability reduction factor to the water phase as a function of temperature data, entered via the PLYTRRA keyword in the PROPS section, should be used. This keyword should only be used if the Polymer option has been activated by the POLYMER keyword in the RUNSPEC section. See the PERMFAC parameter on the PLYROCK keyword in the PROPS section for setting the property for the whole grid for a constant temperature.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
