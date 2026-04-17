### ACTCO2S -- Activity Model for CO2

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The keyword ACTCO2S specifies the activity model for salting-out effects when calculating mutual solubility in the CO2 storage module which is activated by the CO2STORE keyword in the RUNSPEC section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | ACTMODEL | A positive integer value selecting the activity model for the salting-out effect. The choices are:<br>1)  The Rumpf et al.[^1] model as detailed in the paper by Spycher and Pruess[^2]. The model was calibrated in the P-T range 5 to 96 bar and 40 to 160°C, and was shown in Spycher and Pruess^^ to be accurate in the P-T range 1 to 600 bar and 12 to 100°C. Note that this model requires a (fixed-point) iteration procedure to compute solubility, but usually converges within few iterations.<br>2)  The Duan and Sun[^3] model as detailed in the paper by Spycher and Pruess[^4]. The model was recalibrated to the P-T range 1 to 600 bar and 12 to 300°C, and was shown to be accurate within the same range. Note that above 99°C a (fixed-point) iteration procedure is required to compute solubility, while below 99°C the computations are done in a direct manner without needing iterations.<br>3)  The Duan and Sun^^ model as detailed in the paper by Spycher and Pruess^^. The model was calibrated to the P-T range 0 to 2000 bar and 0 to 260°C, and was shown in Spycher and Pruess^^ to be accurate in the P-T range 1 to 600 bar and 12 to 100°C. Note that no iterations are required to compute the solubility. | 3 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 8.3.1.1: ACTCO2S Keyword Description

#### Example

The following example activates activity model number 1.

\--

\-- ACTIVITY MODEL FOR SALTING-OUT EFFECTS IN CO2

\--

ACTCO2S

1 /

[^1]: Rumpf, B.,Nicolaisen, H., Ocal, C., and Maurer, G., 1994. Solubility of carbon dioxide in aqueous solutions of sodium chloride: experimental results and correlation. J. Sol. Chem. 23, 431-448.

[^2]: Spycher, N., and Pruess, K., 2005. CO2-H2O mixtures in the geological sequestration of CO2. II. Partitioning in chloride brines at 12--100°C and up to 600 bar. Geochimica Et Cosmochimica Acta 69, 3309--3320.

[^3]: Duan Z., and Sun R., 2003. An improved model calculating CO2 solubility in pure water and aqueous NaCl solutions from 257 to 533 K and from 0 to 2000 bar. Chem. Geol. 193, 257--271.

[^4]: Spycher, N., and Pruess, K., 2009. A Phase-Partitioning Model for CO2--Brine Mixtures at Elevated Temperatures and Pressures: Application to CO2-Enhanced Geothermal Systems. Transp Porous Med 82, 173--196.
