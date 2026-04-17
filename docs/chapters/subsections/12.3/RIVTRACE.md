### RIVTRACE -- Define River Upstream Flow Tracer Concentrations

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The RIVTRACE keyword defines the injected tracer concentration in individual river branches in a previously characterized river system using the RIVERSYS and the REACHES keywords in the SCHEDULE section. The River option must be activated via the RIVRDIMS keyword in the RUNSPEC section in order to use this keyword. In addition, the Tracer option must also be enabled by the TRACER keyword in the RUNSPEC section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
