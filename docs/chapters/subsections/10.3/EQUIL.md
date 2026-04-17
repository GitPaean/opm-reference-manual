### EQUIL -- Define the Equilibration Initialization Data

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the parameters used to initialize the model for when equilibration is calculated by OPM Flow. This is the standard methodology to initialize a model, the non-standard formulation of entering the pressures and saturations for each grid cell is seldom employed in the industry. The keyword can be used with all grid types.

| 1 | DATUM | DATUM is a single positive value that defines the reference datum depth for PRESS. | 0.0 |
| --- | --- | --- | --- |
| feet | m | cm |  |
| 2 | PRESS | PRESS is a single positive value that defines the pressure at DATUM.<br>If the DATUM depth lies above the GOC then PRESS is the pressure with respect to the gas phase. If the DATUM depth is below OWC then PRESS refers to the water phase pressure. Otherwise, PRESS refers to the oil phase pressure. | 0.0 |
| psia | barsa | atma |  |
| 3 | WATCONT | 1)  For three phase runs containing oil, gas and water WATCONT is the depth of the oil-water contact (OWC).<br>2)  For two phase runs containing oil and water WATCONT is the depth of the oil-water contact (OWC).<br>3)  For two phase runs containing gas and water WATCONT is the depth of the gas-water contact (GWC). | 0.0 |
| feet | m | cm |  |
| 4 | WATCAP | 1)  For three phase runs containing oil, gas and water WATCAP is the oil-water capillary pressure at the OWC.<br>2)  For two phase runs containing oil and water WATCAP is the oil-water capillary pressure at the OWC.<br>3)  For two phase runs containing gas and water WATCAP is the gas-water capillary pressure at the GWC | 0.0 |
| psia | barsa | atma |  |
| 5 | GASCONT | 1)  For three phase runs containing oil, gas and water GASCONT is the depth of the gas-oil contact (GOC).<br>2)  Note in cases where there is no gas cap (or free gas) then GASCONT should be set to a value shallower than the top of the reservoir.<br>3)  In cases where there is initially no oil zone, as for a gas condensate field for example, the GASCONT should be set to the same depth as WATCONT.<br>4)  For two phase runs containing oil and water, or gas and water, GASCONT is ignored. | 0.0 |
| feet | m | cm |  |
| 6 | GASCAP | 1)  For three phase runs containing oil, gas and water GASCAP is the gas-oil capillary pressure at the GWC.<br>2)  For two phase runs containing oil and water, or gas and water, GASCAP is ignored. | 0.0 |
| psia | barsa | atma |  |
| 7 | EQLOPT1 | EQLOPT1 is an integer value that sets the initialization option for when dissolved gas is present in the run, as activated by the DISGAS keyword in the RUNSPEC section.<br>1)  A positive value of EQLOPT1 results in the gas-oil ratio being calculated from data entered on the PBVD (saturation pressure or bubble-point pressure versus depth table) or the RSVD keyword (gas-oil ratio versus depth table). If this option is selected, then either the PBVD or RSVD keywords must be present in the input deck.<br>2)  Note that the allocation of multiple PBVD and RSVD tables to each grid cell is through the EQLNUM keyword and not the PVTNUM keyword.<br>3)  A zero value of EQLOPT1 results in the gas-oil ratio being set to the saturated gas-oil ratio at the GOC. In this case DATUM must be equal GASCONT and the PBVD and RSVD keywords may be omitted.<br>4)  A negative value of EQLOPT1 results in the same option for when EQLOPT1 is zero.<br>EQLOPT1 is ignored if there is no dissolved gas in the run. | 0 |
| dimensionless | dimensionless | dimensionless |  |
| 8 | EQLOPT2 | EQLOPT2 is an integer value that sets the initialization option for when vaporized oil (condensate) is present in the run, as activated by the VAPOIL keyword in the RUNSPEC section.<br>1)  A positive value of EQLOPT2 results in the condensate-gas ratio being calculated from data entered on the PDVD (saturation pressure or dew point pressure versus depth table) or the RVVD keyword (condensate-gas ratio versus depth table). If this option is selected, then either the PDVD or RVVD keywords must be present in the input deck<br>2)  Note that the allocation of multiple PDVD and RVVD tables to each grid cell is through the EQLNUM keyword and not the PVTNUM keyword.<br>3)  A zero value of EQLOPT2 results in the condensate-gas ratio being set to the saturated condensate-gas ratio at the GOC. In this case DATUM must be equal GASCONT and the PDVD and RVVD keywords may be omitted.<br>4)  A negative value of EQLOPT2 results in the same option for when EQLOPT2 is zero.<br>EQLOPT2 is ignored if there is no vaporized oil in the run. | 0 |
| dimensionless | dimensionless | dimensionless |  |
| 9 | EQLOPT3 | EQLOPT3 is an integer value that sets the initialization accuracy options for the equilibration calculation.<br>1)  A zero value of EQLOPT3 results in OPM Flow using the fluid saturations at the center of the grid block in the equilibration calculation. This results in a stable initialization at the expense of a potentially less accurate fluid in-place calculation, especially for large thick grid blocks with a fluid contact in the block.<br>2)  A negative value of EQLOPT3 results in the simulator dividing each grid cell intohorizontal sub-blocks for the equilibration calculation. This results in an accurate fluid in-place calculation at the expense of initialization stability, that is there may be some movement of fluids when there is no production at the start of the run.<br>Increasing the value of N increases the accuracy of the calculation, with the maximum value of N being set to 20 by OPM Flow.<br>1)  A positive value of EQLOPT3 results in the same option for when EQLOPT3 is negative, except that tilted fault blocks are used in the calculation. Again, increasing the value of N increases the accuracy of the calculation, with the maximum value of N being set to 20 by OPM Flow.<br>Note this option should be used with Irregular Corner-Point Grids.<br>EQLOPT3 is ignored for Radial Grids. | 0 |
| dimensionless | dimensionless | dimensionless |  |
| 10 | EQLOPT4 | A positive integer value greater than or equal one and less than or equal to three, that sets the initialization option in the commercial compositional simulator.<br>EQLOPT4 should be defaulted with 1\*, as it is not used by OPM Flow. | None |
| dimensionless | dimensionless | dimensionless |  |
| 11 | EQLOPT5 | A positive integer value that if set to one forces PRESS to be used for the datum pressure in the commercial compositional simulator.<br>EQLOPT5 should be defaulted with either 1\*, as it is not used by OPM Flow. | None |
| dimensionless | dimensionless | dimensionless |  |
| 12 | EQLOPT6 | EQLOPT6 is an integer value that sets the initialization option for when vaporized water is present in the run, as activated by the VAPWAT keyword in the RUNSPEC section. Note this is an OPM Flow specific parameter for use with simulator\'s Vaporized Water Model.<br>1)  A positive value of EQLOPT6 results in the vaporized water-gas ratio being calculated from data entered on the RVWVD keyword (vaporized water-gas ratio versus depth table). If this option is selected, then the RVWVD keyword must be present in the input deck<br>Note that the allocation of multiple RVWVD tables to each grid cell is through the EQLNUM keyword and not the PVTNUM keyword.<br>1)  A zero value of EQLOPT2 results in the vaporized water-gas ratio being set to the saturated vaporized water-gas ratio at the GOC. In this case DATUM must be equal GASCONT and the RVWVD keyword may be omitted.<br>2)  A negative value of EQLOPT6 results in the same option for when EQLOPT6 is zero.<br>EQLOPT6 is ignored if there is no vaporized water in the run. | 0 |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by NTEQUL records as declared on the EQLDIMS keyword in the RUNSPEC section.<br>2)  Each record is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 10.14: EQUIL Keyword Description

See also the PRESSURE, SGAS, SOIL and SWAT keywords in the SOLUTION section to initialize the model using the non-standard formulation of entering the pressures and saturations for each grid cell.

#### Example

\--

\-- DATUM DATUM OWC PCOW GOC PCGO RS RV N E300 RVW

\-- DEPTH PRESS DEPTH \-\-\-- DEPTH \-\-\-- OPT OPT OPT OPTS OPT

EQUIL

3650.0 1560.0 3712.0 0.00 1000.0 0.00 1 0 -5 2\* 1\* /

3650.0 1560.0 3741.0 0.00 1000.0 0.00 1 0 -5 2\* 1\* /

3650.0 1560.0 3741.0 0.00 1000.0 0.00 1 0 -5 2\* 1\* /

The above example defines three equilibration records for when NTEQUL equals three on the EQLDIMS keyword in the RUNSPEC section. Here there is no gas cap and the GOC has been set to a value above the reservoirs (1000.0), and the value of EQLOPT3 (-5) has been explicitly stated.
