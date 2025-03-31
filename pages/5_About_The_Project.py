import streamlit as st

st.set_page_config(page_title="About My Project", page_icon="🔭")
st.title("🔭 About My Project")

st.header("Introduction")
st.write("""
As you have seen earlier, in cosmology, the **matter power spectrum** is our key tool for understanding how matter is distributed across the Universe. 
A closely related concept is the **boost factor**, which compares the clumping of matter in non-linear simulations to that in linear models, essentially showing how gravity enhances the clustering of matter.

This project sets out to predict the boost factor quickly using a **Gaussian Process emulator**. Instead of running full, time-consuming simulations for every set of cosmological parameters, the emulator learns from a carefully chosen dataset. The main goal is to determine which sampling method yields the most predictions with less than $1%$ error.
""")

st.header("The Challenge")
st.write("""
Running full cosmological simulations is like solving a giant, complex puzzle, it demands enormous computing power and time. 
To overcome this, the project explores different ways to choose the best input parameters using something called **Latin Hypercube Sampling (LHS)**.
This approach allows us to efficiently cover the wide range of cosmological parameters and train our emulator to predict the boost factor accurately without needing to simulate every possibility.
""")

st.header("Exploring Different Sampling Techniques")
st.write("""
Imagine you have several strategies for picking the right pieces of a puzzle:
- **Uniform LHS:** Spreads the parameter values evenly across the full range.
- **Gaussian LHS:** Focuses the values near the center, where the models are more stable.
- **Hybrid LHS:** Combines both uniform and Gaussian methods to balance wide coverage with precision.

The goal is to discover which strategy leads to the most accurate boost factor predictions, meaning most of the predictions have less than $1%$ error.
""")

st.image('Assets/GaussianNodes.png', caption="Latin Hypercube Sampling (LHS) Architecture")

st.header("Training and Testing the Emulator")
st.write("""
After selecting the parameter sets with LHS, each set was fed into the CAMB simulation tool to compute the boost factor. 
These simulation results formed the training data for the **Gaussian Process emulator**, which learned the relationship between the input parameters and the boost factor.
To validate the emulator’s accuracy, it was tested on 49 independent datasets, ensuring its predictions consistently stayed within a $1%$ error margin.
""")

st.header("Results and Findings")
st.write("""
The evaluation revealed that the **Gaussian LHS** method consistently outperformed the other strategies, delivering the highest fraction of predictions with less than $1%$ error. 
This indicates that focusing on the central region of the parameter space, where the models are more reliable, leads to more accurate boost factor predictions.
""")

st.image('Assets/gaussian_training.png', caption="Emulator Accuracy for one of our LHS methods")

st.header("Impact and Future Directions")
st.write("""
By refining the way we choose input parameters, this project shows that we can greatly reduce the computational cost of simulations while still achieving high accuracy. 
This efficient approach makes it easier to explore different cosmological models and enhances our understanding of key processes in the Universe.

Looking ahead, there is potential to further improve the sampling techniques or incorporate adaptive methods like Bayesian Optimization to boost the emulator’s performance even more.
""")

