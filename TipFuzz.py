# !pip install scikit-fuzzy
# !pip install networkx

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt


# New Antecedent/Consequent objects hold universe variables
# and membership functions
quality = ctrl.Antecedent(
    np.arange(0, 11, 1),
    'quality'
)

service = ctrl.Antecedent(
    np.arange(0, 11, 1),
    'service'
)

tip = ctrl.Consequent(
    np.arange(0, 26, 1),
    'tip'
)


# Auto-membership function population
quality.automf(3)
service.automf(3)


# Custom membership functions
tip['low'] = fuzz.trimf(
    tip.universe,
    [0, 0, 13]
)

tip['medium'] = fuzz.trimf(
    tip.universe,
    [0, 13, 25]
)

tip['high'] = fuzz.trimf(
    tip.universe,
    [13, 25, 25]
)


# View membership functions
quality.view()
service.view()
tip.view()


# Keep the plots on screen
plt.show()

#tipfuzz is a Python library that provides a simple way to implement fuzzy logic systems. It allows users to define fuzzy variables, membership functions, and rules to model complex systems with uncertainty and imprecision. The library uses the scikit-fuzzy package for fuzzy logic operations and provides a user-friendly interface for creating and visualizing fuzzy systems. It can be used for tasks such as decision-making, control systems, and pattern recognition.