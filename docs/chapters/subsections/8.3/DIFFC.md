### DIFFC -- Define PVT Region Molecular Diffusion Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The DIFFC keyword defines the molecular weight of the fluids and diffusion coefficients between phases for each PVT region, for when the Molecular Diffusion option has been activated by the DIFFUSE keyword in the RUNSPEC section. This keyword is optional as OPM Flow will automatically calculate the coefficients, as described by Sandve et al.[^1], if the DIFFC keyword is absent from the input deck. The keyword thus allows one to overwrite the automatically calculated values.

| 1 | OILMW | OILMW is a real positive number that specifies the molecular weight of the oil in the given PVT region. | None |
| --- | --- | --- | --- |
| lb/lb-M | kg/kg-M | gm/gm-M |  |
| 2 | GASMW | GASMW is a real positive number that defines the molecular weight of the gas in the given PVT region. | None |
| lb/lb-M | kg/kg-M | gm/gm-M |  |
| 3 | GASGASDF | A real positive number that defines the gas in gas diffusion coefficient in the given PVT region. | None |
| ft^2^/day | m^2^/day | cm^2^/hour |  |
| 4 | OILGASDF | A real positive number that declares the oil in gas diffusion coefficient in the given PVT region. | None |
| ft^2^/day | m^2^/day | cm^2^/hour |  |
| 5 | GASOILDF | A real positive number that specifies the gas in oil diffusion coefficient in the given PVT region. | None |
| ft^2^/day | m^2^/day | cm^2^/hour |  |
| 6 | OILOILDF | A real positive number that defines the oil in oil diffusion coefficient in the given PVT region. | None |
| ft^2^/day | m^2^/day | cm^2^/hour |  |
| 7 | GASOILCD | A real positive number that defines the gas in oil cross phase diffusion coefficient in the given PVT region.<br>This parameter is ignored by OPM Flow and should be defaulted or set equal to zero. | 0.0 |
| ft^2^/day | m^2^/day | cm^2^/hour |  |
| 8 | OILOILCD | A real positive number that defines the oil in oil cross phase diffusion coefficient in the given PVT region.<br>This parameter is ignored by OPM Flow and should be defaulted or set equal to zero. | 0.0 |
| ft^2^/day | m^2^/day | cm^2^/hour |  |
| Notes:<br>1)  The keyword is followed by NTPVT tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each record is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.27: DIFFC Keyword Description

See also the DIFFUSE keyword in the RUNSPEC section to activate the Molecular Diffusion option.

#### Example

The example below is based on field units, with NTPVT equal to three on the TABDIMS keyword.

\--

\-- PVT REGION MOLECULAR DIFFUSION TABLES

\--

DIFFC

\-- OIL GAS GAS IN OIL IN GAS IN OIL IN GAS IN OIL IN

\-- MW MW GAS DF GAS DF OIL DF OIL DF OIL CD OIL CD

\-- \-\-\-\-\-- \-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\--

103.20 1.120 1.35E-6 1.05E-7 4.50E-7 1.05E-8 /TAB-1

102.00 1.130 1.25E-6 1.25E-7 4.80E-7 1.05E-8 /TAB-2

100.00 1.250 1.22E-6 /TAB-3

Here the third PVT region has no values for the various oil related diffusion coefficients.

[^1]: Tor Harald Sandve1, Sarah E. Gasda, Atgeirr Rasmussen, and Alf Birger Rustad. Convective dissolution in field scale CO~2~ storage simulation using the OPM Flow simulator. Submitted to TCCS 11 -- Trondheim Conference on CO~2~ Capture, Transport and Storage Trondheim, Norway -- June 21-23, 2021.
