### GDIMS -- Activate Instantaneous Gradient Option and Define Dimensions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The GDIMS keyword activates the Instantaneous Gradient option and defines the maximum dimensions as used by the GWRTWCV keyword in the SCHEDULE section. The Instantaneous Gradient option calculates derivatives of solution quantities at the current time step with respect to variations in the variables at the *current time step*. This is different to Gradient option that calculates the derivatives of solution quantities at the current time step with respect to variations in the variables at the initial* time step*, that is a time equal to zero. Consequently, the Instantaneous Gradient option can be switched on and off by the GUPFREQ keyword in the SCHEDULE section, whereas the Gradient option cannot.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
