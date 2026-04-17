### THERMAL -- Activate the Thermal Modeling Option

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword activates the thermal modeling option.

In OPM Flow\'s thermal model (THERMAL keyword) enthalpy is conserved and the energy equations are solved fully implicitly with the black-oil equations. Whereas, in OPM Flow\'s temperature model (TEMP keyword) internal energy is conserved (the work term is neglected and internal energy is equal to enthalpy) and the energy equations are solved sequentially after the black-oil equations. Note that the thermal model can be modified so that internal energy rather than enthalpy is conserved by setting the command line option \--conserve-inner-energy-thermal=true (the default is false). If properties like density or viscosity \"strongly\" depend on temperature, the thermal model is recommended.

There is no data required for this keyword and there is no terminating "/" for this keyword.

The temperature option (TEMP keyword) and the thermal option (THERMAL keyword) are two separate modeling facilities in the commercial simulator, although some keywords can be used by both options, for example the RTEMP keyword. OPM Flow's thermal model is not directly equivalent to either the commercial simulator's black-oil TEMP or compositional THERMAL formulation.

The energy black-oil implementation in OPM Flow uses a mixture of the commercial simulators black-oil and the commercial simulators "compositional thermal" keywords, as well as some OPM Flow specific keywords. Keywords specifically associated with both OPM Flow's THERMAL and the commercial simulators TEMP and THERMAL options are listed in for ease of reference.

| RUNSPEC | ROCKDIMS | Thermal Rock Dimensions of Over and Underburden Rock Types |  |  |  |
| --- | --- | --- | --- | --- | --- |
| TEMP | Activate the Temperature Modeling Option |  |  | Black-Oil |  |
| THERMAL | Activate the Thermal Modeling Option |  |  |  |  |
| GRID | ROCKCON | Thermal Rock Over and Underburden Connection Data |  |  |  |
| ROCKPROP | Thermal Rock Over and Underburden Property Data |  |  |  |  |
| HEATCR | Rock Heat Capacity. |  |  |  |  |
| HEATCRT | Rock Heat Capacity Temperature. |  |  |  |  |
| THCGAS | Gas Phase Thermal Conductivity. |  |  |  |  |
| THCOIL | Oil Phase Thermal Conductivity. |  |  |  |  |
| THCONR | Thermal Conductivity of liquids and reservoir rock. |  |  |  |  |
| THCONSF | Thermal Conductivity of liquids and reservoir rock scaling factor applied to THCONR to account for gas saturation. |  |  |  |  |
| THCROCK | Rock Thermal Conductivity. |  |  |  |  |
| THCSOLID | Solid Phase Thermal Conductivity. |  |  |  |  |
| THCWATER | Water Thermal Conductivity. |  |  |  |  |
| PROPS | HEATVAP | Thermal Oil Component Heat of Vaporization |  |  |  |
| GASDENT | Gas Density Temperature Coefficients (OPM Flow keyword). |  |  |  |  |
| GASJT | Gas Joule-Thomson Coefficient (OPM Flow keyword). |  |  |  |  |
| GASVISCT | Gas Viscosity versus Temperature Functions (OPM Flow black-oil keyword). |  |  |  |  |
| OILDENT | Oil Density Temperature Coefficients (OPM Flow keyword). |  |  |  |  |
| OILJT | Oil Joule-Thomson Coefficient (OPM Flow keyword). |  |  |  |  |
| OILVISCT | Oil Viscosity versus Temperature Functions (OPM Flow black-oil keyword). |  |  |  |  |
| RTEMP | Constant Initial Reservoir Temperature. |  |  |  |  |
| RTEMPA | Constant Initial Reservoir Temperature. |  |  |  |  |
| RTEMPVD | Initial Reservoir Temperature versus Depth. |  |  |  |  |
| SPECHA | Thermal Specific Heat of Oil Component |  |  |  |  |
| SPECHEAT | Specific Heat of Oil, Water and Gas |  |  |  |  |
| SPECROCK | Specific Heat of the Reservoir Rock |  |  |  |  |
| TEMPVD | Initial Reservoir Temperature versus Depth. |  |  |  |  |
| THANALB | Activate Thermal Analytic Water Density Option |  |  |  |  |
| THERMEX1 | Liquid Components Thermal Expansion Coefficient |  |  |  |  |
| WATDENT | Oil Density Temperature Coefficients. |  |  |  |  |
| WATJT | Water Joule-Thomson Coefficient (OPM Flow keyword). |  |  |  |  |
| WATVISCT | Oil Viscosity versus Temperature Function. |  |  |  |  |
| REGIONS | THERMNUM | Thermal Region Numbers. |  |  |  |
| SOLUTION | RTEMP | Constant Initial Reservoir Temperature. |  |  |  |
| RTEMPA | Constant Initial Reservoir Temperature. |  |  |  |  |
| RTEMPVD | Initial Reservoir Temperature versus Depth. |  |  |  |  |
| TEMPI | Initial Reservoir Temperature for All Cells. |  |  |  |  |
| TEMPVD | Initial Reservoir Temperature versus Depth. |  |  |  |  |
| SCHEDULE | WTEMP | Set An Injection Well's Fluid Temperature |  |  |  |
| WINJTEMP | Define Injection Fluid Thermal Properties |  |  |  |  |
| Notes:<br>1)  Cells colored green implies the keyword can be used with this model formulation.<br>2)  Cells colored orange means the keyword is recognized by OPM Flow's parser but is ignored and not used by OPM Flow.<br>3)  Cells colored red should not be used with this model formulation.<br>4)  The list is focused on the OPM Flow implementation of the energy and black-oil formulation and therefore does not necessary include all the commercial simulator's compositional keywords. |  |  |  |  |  |

Table 5.46: OPM Flow's THERMAL Option Associated Keywords

In thermal runs a producing well's bottom-hole temperature is calculated based on a weighted average of the temperature in the grid cell connections open to flow in the producing well, that is the reported bottom-hole temperature, *TBHT*, is calculated as:

with

The term is the energy rate density (J/(K s)) of phase *p*,

where:

= number of phases,

= number of open connections in the well,

= the open connection index,

= the phase index, oil, water and gas.

= indicating that the parameter is evaluated at reservoir conditions,

= temperature (K),

= connection flow rate (m^3^/s),

= fluid density (kg/m^3^), and

= specific heat capacity (J/(K kg))

(see the SPECHEAT keyword in the PROPS section).

The current implementation makes use of the specific internal energy:

derived from the specific enthalpy, *h~*pi*~*

where is connection grid block pressure of phase *p*.

The phase rates at surface conditionsare converted to reservoir in situ ratesusing the phase formation volume factor, *B~*pi*~*, via:

And thus equation can be simplified to:

#### Example

\--

\-- ACTIVATE THE THERMAL MODELING OPTION (OPM FLOW THERMAL OPTION ONLY)

\--

THERMAL

The above example activates the thermal modeling option.
