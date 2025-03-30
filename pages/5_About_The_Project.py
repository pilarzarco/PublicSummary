import streamlit as st

st.set_page_config(page_title="About My Project", page_icon="🔭")
# Title for the page
st.title("🔭 About My Project")

# Introduction Section
st.header("Introduction")
st.write("""
This project focuses on using **Gaussian Process (GP) emulators** to predict the **boost factor**, a key element in understanding the distribution of matter in the universe. The **boost factor** describes how the matter power spectrum behaves in the non-linear regime, which is important for studying the clustering of galaxies and large-scale cosmic structures.

The goal is to predict the boost factor efficiently without the need to rerun complex simulations every time, using techniques like **Latin Hypercube Sampling (LHS)** to sample cosmological parameters and **Gaussian Process emulators** to make predictions.
""")

# Image of LHS sampling
st.image('Assets/GaussianNodes.png', caption="Latin Hypercube Sampling (LHS) Architecture")

# Section on the Challenge in Cosmology
st.header("The Challenge in Cosmology")
st.write("""
Cosmological simulations model the evolution of the universe, solving complex equations that describe how matter, energy, and gravity interact. However, running these simulations for each possible set of cosmological parameters is **computationally expensive** and time-consuming. The goal of this project is to use **Gaussian Process emulators** as a tool to **predict the boost factor** much faster by training on a set of previously generated data.
""")

# Section on Emulator Training
st.header("Training the Emulator with Data")
st.write("""
To train the emulator, we first use **Latin Hypercube Sampling (LHS)** to explore the parameter space efficiently. LHS helps us sample a wide range of cosmological parameters (like the **Hubble constant**, **dark matter density**, and **matter distribution**) and cover the space without over-sampling certain regions.

Once we have the **LHS-generated samples**, we run cosmological simulations for each parameter set to generate data, which is then used to train the **Gaussian Process emulator**. The emulator learns the relationship between the parameters and the resulting **boost factor**, allowing it to make quick predictions without the need for repeated simulations.
""")

# Section on Boost Factor Emulation
st.header("Boost Factor Emulation")
st.write("""
The **boost factor** is a crucial component in cosmology as it tells us how matter is distributed on different scales, particularly in the non-linear regime where galaxies and large-scale structures form. By using an emulator, we can make accurate predictions about the boost factor for new cosmological models, without having to rerun the entire simulation each time.

The **Gaussian Process emulator** is trained on the data from the simulations and then used to predict how the **boost factor** behaves for different sets of cosmological parameters. This is much faster than running full simulations, making it possible to explore more models and test new theories efficiently.
""")

# Testing the Emulator
st.header("Testing the Emulator's Accuracy")
st.write("""
After training the emulator, we need to test its ability to make reliable predictions. We do this by comparing its output for **independent datasets**—new parameter sets that were not part of the training data. The emulator’s predictions are compared to **real-world data** and **theoretical models** to assess how well it generalizes to new situations.

The emulator's performance is a key factor in ensuring that predictions made about the **boost factor** are accurate, and the results from this testing phase ensure that the emulator can be confidently used for cosmological predictions.
""")

# Image of Emulator Testing and Results
st.image('Assets/gaussian_training.png', caption="Emulator Accuracy for one of our LHS architectures")

# Section on the Impact of the Project
st.header("The Impact of This Project")
st.write("""
The key outcome of this project is the ability to **predict the boost factor** quickly and efficiently using **Gaussian Process emulators**. This approach significantly reduces the time and computational resources needed for cosmological simulations, allowing scientists to explore more models and test a wider range of cosmological theories. By using emulators, cosmologists can make predictions about the universe more efficiently, leading to faster discoveries and deeper insights into cosmic phenomena.

This methodology can be extended to other areas of cosmology, such as **dark energy**, **galaxy formation**, and **high-energy physics**, where efficient and accurate predictions are crucial for advancing our understanding of the universe.
""")

