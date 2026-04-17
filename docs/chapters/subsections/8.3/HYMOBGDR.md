### HYMOBGDR -- Activate Carlson and Killough Alternative Drainage Hysteresis Option

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, HYMOBGDR, activates the Carlson and Killough alternative secondary drainage hysteresis option for when the hysteresis option has been activated by the HYSTER variable on the SATOPTS keyword in the RUNSPEC section, and either the Carlson[^1] or Killough[^2] models have been selected via the EHYSTR keyword in the PROPS section. Due to numerical accuracy, the gas saturation may fall below the critical gas saturation (SGCR), that is the largest gas saturation for which the gas relative permeability is zero, and gas would therefore be immobile until the gas saturation increases above SGCR. This option overcomes this situation by letting the gas become mobile once it starts increasing, effectively setting the SGCR to the current gas saturation.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

\--

\-- ACTIVATE CARLSON AND KILLOUGH ALTERNATIVE DRAINAGE HYSTERESIS OPTION

\--

HYMOBGDR

[^1]: Carlson, F. M. "Simulation of Relative Permeability Hysteresis to the Non-Wetting Phase," paper SPE 10157, presented at the SPE Annual Technical Conference & Exhibition, San Antonio, Texas, USA (October 5-7, 1981).

[^2]: Killough, J. E. "Reservoir Simulation with History-dependent Saturation Functions," paper SPE 5106, Society of Petroleum Engineers Journal (1976) 16, No. 1, 37-48.
