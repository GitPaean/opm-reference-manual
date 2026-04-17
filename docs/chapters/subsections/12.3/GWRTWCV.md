### GWRTWCV -- Instantaneous Gradient Option Well Variables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The GWRTWCV keyword defines the wells and instantaneous gradient parameters to be calculated and exported as SUMMARY vectors to the summary file, for when the Instantaneous Gradient option has been activated by the GDIMS keyword in the RUNSPEC section. The Instantaneous Gradient option calculates derivatives of solution quantities at the current time step with respect to variations in the variables at the *current time step*. This is different to Gradient option that calculates the derivatives of solution quantities at the current time step with respect to variations in the variables at the initial* time step*, that is a time equal to zero. Consequently, the Instantaneous Gradient option can be switched on and off by the GUPFREQ keyword in the SCHEDULE section, whereas the Gradient option cannot.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
