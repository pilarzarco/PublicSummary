import streamlit as st

st.set_page_config(page_title="Introduction", page_icon="📖")

st.markdown("""
You've just seen an example of how we can study the structure and evolution of the universe, and it is all built entirely from a set of numbers!
Tiny differences in these numbers can change our picture of the cosmos, and finding accurate values for these numbers can help us understand the world we live in. Let's look at what these numbers mean and why they are at the heart of my research!

---

### 🌌 What Is Cosmology?

Cosmology is the study of the structure, history and evolution of the universe.  
It isn’t just about stars or galaxies; it’s about the very fabric of spacetime, how it began, how it changes, and what it’s made of.  
Even though the Universe appears overwhelmingly complex, much of its behaviour can be described using a handful of physical parameters, such as the rate of expansion, the amount of matter, and the initial conditions of cosmic structure.

These key numbers form the foundation of our computational and mathematical models; simplified but powerful representations that help us understand and predict the evolution of the cosmos.

---

### 🧮 Building a Universe

In physics, if you can describe something with numbers, you can usually predict how it behaves. Cosmology works in much the same way.  
By selecting values for parameters like the Hubble constant or the matter density, scientists can use simulations to study how the Universe evolves over time. However, these simulations are extremely computationally expensive, which means we need a faster method to be able to study the universe. 

In my project, I experimented with different sampling techniques to determine the most effective way of choosing these parameters. Instead of relying on full, computationally expensive simulations, I used something called an emulator to predict the outcome of these simulations. By comparing different sampling strategies, I identified the most optimal method for achieving high accuracy predictions of the universe's structure.

---

### 🎥 Visualizing Cosmic Evolution

It’s one thing to describe cosmic structure in words, but it’s quite another to see it unfold. The video below showcases the **Millennium Simulation**, a large-scale computer model that illustrates how gravity pulls matter together to form galaxies and clusters over billions of years.
""")

st.video("https://www.youtube.com/watch?v=ClIiUkHPkIE")

st.markdown("""
Each bright thread or cluster in the simulation represents regions where matter is densely packed, where galaxies and clusters are likely to form.

<sub>
📽️ <i>Simulation by the Virgo Consortium. Video by the Max Planck Institute for Astrophysics.<br>
Springel et al., Nature 435, 629–636 (2005). <a href="https://doi.org/10.1038/nature03597" target="_blank">DOI: 10.1038/nature03597</a></i>
</sub>
""", unsafe_allow_html=True)

st.markdown("""
To complement the video, here’s a striking image capturing a snapshot of the cosmic web – the intricate network of matter that threads through the Universe.
""")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Cosmic_web_simulation.jpg/640px-Cosmic_web_simulation.jpg", 
         caption="Visualization of the Cosmic Web – a network of galaxies and dark matter. (Image credit: Wikimedia Commons)")

st.markdown("""
---

### 🧠 From Quiz to Cosmology: Connecting the Dots

After exploring your cosmic personality quiz, where your responses translated into a unique matter power spectrum, you’ve seen firsthand how subtle variations in key parameters can dramatically alter our understanding of the Universe.  
Now, building on that foundation, this page introduces you to the broader topic and the research behind it. We’ll unpack how these numerical models are constructed, why they matter, and how they help us test and refine our ideas about the cosmos.

Enjoy this journey into the heart of cosmology, where every number tells a story and every simulation brings us one step closer to understanding the Universe!
""")
