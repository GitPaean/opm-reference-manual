### MULTFLT -- Multiply the Transmissibility of a Defined Fault by a Constant

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

MULTFLT enables the transmissibilities across defined faults, as declared by the FAULTS keyword, to be modified. They keyword allows for the re-scaling of the existing fault transmissibilities calculated by OPM Flow, for example setting a fault to be completely sealing by setting the multiplier to zero.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | FLTNAME | FLTNAME is a character string enclosed in quotes with a maximum length of eight characters, that defines the name of the fault that FLTMULT will be applied to. FLTNAME must have previously been defined using the FAULTS keyword in GRID section | None |
| 2 | FLT-TRS | A positive real number that sets the transmissible multiplier to be applied to the FLTNAME transmissibilities positive real number that sets the transmissible multiplier to be applied to the FLTNAME transmissibilities. | 1.0 |
| 3 | FLT-DIF | A positive real number that sets the diffusivity multiplier to be applied to the FLTNAME diffusivities.<br>This option should only be used if the Diffusion option has been made activate by the DIFFUSE keyword in the RUNSPEC section.<br>OPM Flow does not support this Diffusion option. | 1.0 |
| Notes:<br>1)  Repeated entries of the same FLTNAME will result in all but the last entry being overwritten.<br>2)  Each record must be terminated by a "/" and the keyword is terminated by a "/". |  |  |  |

Table 6.67: MULTFLT Keyword Description

#### Example

\--

\-- MODIFY THE TRANSMISSIBILITES ACROSS DEFINED FAULTS

\--

\-- FAULT TRANS DIFUSS

\-- NAME MULTIPLIER MULTIPLIER

MULTFLT

\'FAULT01\' 0.0 / FAULT MULTIPLIERS

\'FAULT02\' 0.0 / FAULT MULTIPLIERS

\'FAULT03\' 0.0 / FAULT MULTIPLIERS

/

The above example sets the fault transmissibility multiplier for defined faults named FAULT01, FAULT02, and FAULT03 to zero making the faults sealing in the model.
