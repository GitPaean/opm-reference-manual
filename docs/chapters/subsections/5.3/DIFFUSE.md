### DIFFUSE -- Activate Molecular Diffusion Option

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The DIFFUSE keyword activates OPM Flow's Molecular Diffusion option based on fluid and grid data (Sandve et al.[^1]), similar to the commercial simulator. For field-scale simulations diffusion is a sub-grid phenomenon and is typically not explicitly represented in the flow equations. However, for simulations on the laboratory scale diffusion plays a direct role and therefore needs to be explicitly represented in the flow equations. Diffusion coefficients that control the diffusion depend on temperature, pressure, and salinity. In OPM Flow, the diffusion coefficients are computed internally for pure water using McLachlan and Danckwerts[^2] and modified to account for salinity using Ratcliff and Holdcroft[^3]. The effect of the porous media on the diffusion is modeled using the relation suggested by Millington and Quirk[^4]. The coefficients can also be given for each PVT region as an input parameter using the DIFFC keyword in the PROPS section.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- ACTIVATE MOLECULAR DIFFUSION OPTION

\--

DIFFUSE

The above example switches on the molecular diffusion facility.

[^1]: Tor Harald Sandve1, Sarah E. Gasda, Atgeirr Rasmussen, and Alf Birger Rustad. Convective dissolution in field scale CO~2~ storage simulation using the OPM Flow simulator. Submitted to TCCS 11 -- Trondheim Conference on CO~2~ Capture, Transport and Storage Trondheim, Norway -- June 21-23, 2021.

[^2]: McLachlan, C. N. S., & Danckwerts, P. V. (1972). Desorption of carbon dioxide from aqueous potash solutions with and without the addition of arsenite as a catalyst. Trans. Inst. Chem. Eng, 50, 300-309.

[^3]: Ratcliff, G. A., & Holdcroft, J. G. (1963). Diffusivities of gases in aqueous electrolyte solutions. Trans. Inst. Chem. Eng, 41(10), 315-319.

[^4]: Millington, R. J., & Quirk, J. P. (1961). Permeability of porous solids. Transactions of the Faraday Society, 57, 1200-1207
