import ParameterClasses as P
import MarkovModelClasses as MarkovCls
import SupportMarkovModel as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs

# create a cohort
cohort = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NoTherapy)

# simulate the cohort
simOutputs = cohort.simulate()

# graph survival curve
PathCls.graph_sample_path(
    sample_path=simOutputs.get_survival_curve(),
    title='Survival curve',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )

Figs.graph_histogram(
    data=simOutputs.get_strokes(),
    title='Number of patients with Stroke',
    x_label='Stroke',
    y_label='Counts',
    bin_width=1
)

# print the outcomes of this simulated cohort
SupportMarkov.print_outcomes(simOutputs, 'No Therapy:')
simOutputs.get_mean_strokes()


# create a cohort
cohort1 = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.Anti)

# simulate the cohort
simOutputs1 = cohort1.simulate()

# graph survival curve
PathCls.graph_sample_path(
    sample_path=simOutputs1.get_survival_curve(),
    title='Survival curve',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )


Figs.graph_histogram(
    data=simOutputs1.get_strokes(),
    title='Number of patients with Stroke',
    x_label='Stroke',
    y_label='Counts',
    bin_width=1
)


# print the outcomes of this simulated cohort
SupportMarkov.print_outcomes(simOutputs1, 'Anticoagulation:')
simOutputs1.get_mean_strokes()

