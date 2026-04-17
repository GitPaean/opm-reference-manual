### WSEGDFMD -- Define Multi-Segment Well Drift Flux Slip Model

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WSEGDFMD keyword defines a multi-segment well's drift flux slip model definition that sets the type of slip model to be used. A slip model[^1] and [^2] enables the different phases in the wellbore to flow at different velocities, for example gas will flow up the tubing at a higher velocity than oil and water. The option is activated by the FLOWOPT parameter on the WELSEGS keyword in the SCHEDULE section; however, the slip model flow calculation is not available in OPM Flow.

See also the WSEGDFIN keyword that sets the slip model's input parameters and the WSEGDFPA keyword that allows the model default values employed by WSEGDFMD to be modified..

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

[^1]: Shi, H., Holmes, J.A., Durlofsky, L. J., Aziz, K., Diaz, L. R., Alkaya, B., and Oddie, G. "Drift-Flux Modeling of Two-Phase Flow in Wellbores," paper SPE 84228, Society of Petroleum Engineers Journal (2005) 10, No. 1, 24-33; also presented as "Drift-Flux Modeling of Multiphase Flow in Wellbores," at the SPE Annual Technical Conference and Exhibition, Denver, Colorado, USA(October 5-8, 2003).

[^2]: Shi, H., Holmes, J.A., Diaz, L. R., Durlofsky, L. J., and Aziz, K. "Drift-Flux Parameters for Three-Phase Steady-State Flow in Wellbores," paper SPE 89836, Society of Petroleum Engineers Journal(2005) 10, No. 2, 130-137; also presented at the SPE Annual Technical Conference and Exhibition, Houston, Texas, USA (September 26-29, 2004).
