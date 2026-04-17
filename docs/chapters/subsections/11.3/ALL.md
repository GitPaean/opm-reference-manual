### ALL -- Export Standard Summary Variable Vectors to File

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword activates the writing out of a standard set of summary production and injection data vectors for the field, group and well objects to the SUMMARY (\*.SMSPEC and \*.UNSMRY) and RSM (\*.RSM) files. lists the production, injection, pressure and volume summary variables written out by the ALL keyword, and list the aquifer variables.

| Variable | Root | Field | Group | Well | Comment |
| --- | --- | --- | --- | --- | --- |
| Gas Injection Rate | GIR | FGIR | GGIR | WGIR |  |
| Gas Injection Total | GIT | FGIT | GGIT | WGIT |  |
| Gas Production Rate | GPR | FGPR | GGPR | WGPR | Produced reservoir gas only, gas lift gas is excluded. |
| Gas Production Total | GPT | FGPT | GGPT | WGPT |  |
| Oil Injection Rate | OIR | FOIR | GOIR | WOIR |  |
| Oil Injection Total | OIT | FOIT | GOIT | WOIT |  |
| Oil Production Rate | OPR | FOPR | GOPR | WOPR |  |
| Oil Production Total | OPT | FOPT | GOPT | WOPT |  |
| Res. Vol. Injection Rate | VIR | FVIR | GVIR | WVIR |  |
| Res. Vol. Injection Total | VIT | FVIT | GVIT | WVIT |  |
| Res. Vol. Production Rate | VPR | FVPR | GVPR | WVPR |  |
| Res. Vol. Production Total | VPT | FVPT | GVPT | WVPT |  |
| Water Injection Rate | WIR | FWIR | GWIR | WWIR |  |
| Water Injection Total | WIT | FWIT | GWIT | WWIT |  |
| Water Production Rate | WPR | FWPR | GWPR | WWPR |  |
| Water Production Total | WPT | FWPT | GWPT | WWPT |  |
| Bottom-Hole Pressure | BHP |  |  | WBHP |  |
| Productivity | PI |  |  | WPI | Preferred Phase |
| Tubing Head Pressure | THP |  |  | WTHP |  |
| Gas-Oil Ratio | GOR | FGOR | GGOR | WGOR |  |
| Water -Gas Ratio | WGR | FWGR | GWGR | WWGR |  |
| Water Cut | WCT | FWCT | GWCT | WWCT |  |
| Pressures and Volumes |  |  |  |  |  |
| Variable | Root | Field | Group | Well | Comment |
| Oil Phase Pressure | PR | FPR |  |  | Field and Region HCPV weighted |
| Gas In-Place | GIP | FGIP |  |  | Liquid and gas phases |
| Gas In-Place (Gas Phase) | GIPG | FGIPG |  |  |  |
| Gas In-Place (Liquid Phase) | GIPL | FGIPL |  |  | Only for cases that have dissolved gas in the water phase |
| Oil In-Place | OIP | FOIP |  |  | Liquid and gas phases |
| Oil In-Place (Gas Phase) | OIPG | FOIPG |  |  |  |
| Oil In-Place (Liquid Phase) | OIPL | FOIPL |  |  |  |
| Water In-Place | WIP | FWIP |  |  |  |
| Notes:<br>1)  Cells colored in gray indicate that the summary variable is not available for this combination.<br>2)  Cells colored orange under the Type column indicate that this set of summary variables are not available in OPM Flow because the underlying feature is not available in OPM Flow. |  |  |  |  |  |

*Table 11.26: Standard Production, Injection, and Pressure Summary Variables*
| Standard Aquifer Summary Variables |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Variable | Root | Field | Analytical\ Aquifer | Analytical\ Aquifer\ List | Numerical\ Aquifer | Comment |
| Aquifer Influx Rate (Water Aquifers) | QR | FAQR | AAQR |  |  |  |
| Aquifer Influx Total (Water Aquifers) | QT | FAQT | AAQT |  |  |  |
| Aquifer Influx Rate (Gas Aquifers) | QRG | FAQRG | AAQRG |  |  |  |
| Aquifer Influx Total (Gas Aquifers) | QTG | FAQTG | AAQTG |  |  |  |
| Notes:<br>3)  Cells colored in gray with a mnemonic indicate that the summary variable is not available in OPM Flow.<br>4)  Cells colored in gray with no mnemonic indicate that the summary variable is not available for this combination.<br>5)  Cells colored orange show combinations that are not available in OPM Flow because the underlying feature is not available. |  |  |  |  |  |  |

*Table 11.27: Standard Aquifer Summary Variables*
There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Examples

\-- ==============================================================================

\--

\-- SUMMARY SECTION

\--

\-- ==============================================================================

SUMMARY

\--

\-- EXPORT STANDARD SUMMARY VARIABLE VECTORS TO FILE

\--

ALL

\--

\-- ACTIVATE COLUMNAR SUMMARY DATA REPORTING OPTION

\--

RUNSUM

\--

\-- ACTIVATE SUMMARY DATA RSM FILE OUTPUT OPTION

\--

SEPARATE

Note the SEPARATE keyword is not required for OPM Flow as this is the default behavior; however, it is probably good practice to include it if the same input decks are being run with commercial simulator.
