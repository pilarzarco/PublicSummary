import streamlit as st

st.set_page_config(page_title="Predicting Cosmologies", page_icon="🌌")

# Title of the page
st.title("How Cosmologists Use Technology to Study the Universe")

# Section 1: Overview
st.header("Introduction")
st.write("""
Cosmologists study the universe to answer some of its biggest questions: How did it begin? What is it made of? And how will it change over time? 
To solve these mysteries, they use **advanced technology**, **data analysis**, and **computer tools**.
""")



# Section 2: What Do Cosmologists Do?
st.header("What Do Cosmologists Do?")
st.write("""
Cosmologists gather **data** from telescopes and satellites and use **mathematical models** and **computer simulations** to test ideas about how the universe works. 
These tools help them understand the formation of galaxies, the behavior of dark matter, and the expansion of the universe.

Cosmologists analyze data and test theories to predict how the universe will behave under different conditions.
""")

# Add an image for the universe view
st.image('Assets/hubble.png', caption="Image of the Universe taken by the Hubble Space Telescope")

st.markdown("""
<sub><br> 
📸 <i>Image Credit: NASA, ESA, and Hubble Heritage Team (STScI/AURA).<br> 
Visit the official Hubble site for more details: <a href="https://hubblesite.org/" target="_blank">Hubble Space Telescope</a>
</i>
</sub>
""", unsafe_allow_html=True)


# Section 3: Data
st.header("Understanding the Data")
st.write("""
Cosmologists rely on data collected from space telescopes, satellites, and detectors. This data comes from everything from star positions to cosmic radiation, and **statistics** help cosmologists make sense of it. By analyzing patterns in the data, they can predict how the universe works.

The universe provides a vast amount of data, and cosmologists use **statistics** to search for patterns. Similar to how weather scientists predict the weather, cosmologists use data to understand the behavior of galaxies and stars.
""")

# Add a final image of a cosmologist or observatory
st.image('Assets/euclid.jpeg', caption="Euclid Mission, designed to explore the composition and evolution of the universe.")

# Add credits using HTML tags
st.markdown("""
<sub><br> 
📸 <i>Image Credit: ESA/Euclid Consortium. Image credit for visual and scientific design.<br> 
Visit the official Euclid site for more details: <a href="https://www.esa.int/Science_Exploration/Space_Science/Euclid" target="_blank">Euclid Mission</a>
</i>
</sub>
""", unsafe_allow_html=True)

# Section 5: Simulating the Universe
st.header("Simulating the Universe")
st.write("""
Simulations help cosmologists understand how the universe works. For example, they can simulate how matter behaves under gravity, how galaxies form, or how dark energy might affect the expansion of the universe. 
These simulations are crucial for testing different theories, but they can be **time-consuming** and **computationally expensive**.

Running a simulation of the universe is like building a detailed model of a city. Cosmologists create simulations to test different scenarios, like how galaxies form or how the universe's expansion affects cosmic structures. 
But because these simulations take so much computing power, cosmologists often need faster, more efficient ways to make predictions.
""")

st.write("""
To make predictions faster, cosmologists use **emulators**. An emulator is like a shortcut—it learns from previous simulations and uses that knowledge to make quick predictions without needing to run the simulation from scratch each time.

Instead of running a full simulation every time, emulators predict the outcome based on past data. This saves time and allows scientists to explore many more possibilities, making it easier to test different theories and ideas about how the universe works.
""")


# Section 7: Real-World Example
st.header("Real-World Application: Predicting the Universe's Evolution")
st.write("""
In this project, the goal was to predict how the universe evolves under different conditions. By using an **emulator** trained on data from earlier simulations, we can predict how **matter** is distributed across galaxies and how it might change in the future. This helps cosmologists understand the large-scale structure of the universe.

The emulator in my project helped predict how matter clusters in the universe without having to run a new simulation for each scenario. This allows scientists to test different models more efficiently and get answers faster.
""")

# Add an image of matter distribution or a galaxy simulation
st.image('Assets/millenium_image.jpg', caption="Image taken from the Millenium simulation, showing the structure of the universe")

st.markdown("""
<sub><br>
📸 <i>Image Credit: Millennium Simulation Project. Simulation by the Virgo Consortium. Visualization by the Max Planck Institute for Astrophysics.<br>
Springel et al., Nature 435, 629–636 (2005). <a href="https://doi.org/10.1038/nature03597" target="_blank">DOI: 10.1038/nature03597</a></i>
</sub>
""", unsafe_allow_html=True)

#### Why This Matters: Understanding the Universe
st.header("Why It Matters")
st.write("""
The work done by cosmologists using **Python**, **emulators**, **statistics**, and **simulations** is crucial for solving some of the universe’s biggest mysteries. By testing different theories, cosmologists can better understand **dark matter**, **dark energy**, and **how gravity works**. These tools help make **predictions** about the future of the universe and guide future space missions and experiments.

Cosmology is more than just looking at stars through a telescope. It’s about using the best tools available to **solve the mysteries of the universe**. And **Python**, **emulators**, **statistics**, and **simulations** are the **key** to unlocking those mysteries.
""")



