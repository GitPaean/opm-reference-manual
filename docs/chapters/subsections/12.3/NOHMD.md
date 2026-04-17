### NOHMD -- Deactivate History Match Gradient Derivative Calculations

The NOHMD deactivates various history match gradient derivative calculations for when the History Match Gradient option has been activated by the HMDIMS keyword in the RUNSPEC section. The keyword consists of a series of character strings that define which derivative should be switch off based on the keyword that requested the derivatives to be calculated, for example HMFAULTS keyword in the GRID section. If an empty list is entered then all the gradient derivative calculations previously requested are switch off. The keyword is useful for changing from history matching runs to predication cases, as the prediction cases will be more computationally efficient without the burden of the gradient derivative calculations.

See [NOHMD -- Deactivate History Match Gradient Derivative Calculations](#anchor-1) in the SOLUTION section for a full description.
