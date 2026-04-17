### WBOREVOL -- Define Effective Wellbore Storage Volume

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WBOREVOL defines a well's effective wellbore storage volume. The primary purpose of the keyword is to enable matching of the wellbore storage effects in well tests and the corresponding pressure response observed in the test. Normally, as part of well test interpretation, the pressure, permeability, effective wellbore storage, etc., are derived from the analytical interpretation of the test. This keyword therefore allows the engineer to enter the analytical derived effective wellbore storage.

Wellbore storage, in terms of well testing, is an important variable when the well is shut-in at the surface, as the well continues to flow down-hole until the fluids obtain equilibrium. Most well tests are now conducted using specialized tools that shut-in the well down-hole, thus eliminating, or mostly eliminating, wellbore storage effects.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
