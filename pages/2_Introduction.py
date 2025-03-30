import streamlit as st

st.set_page_config(page_title="Introduction", page_icon="📖")

st.title("📖 Introduction to Cosmology")

st.markdown("""
You’ve just seen a simulation of a universe, one built from a set of numbers.  
Now let’s talk about what those numbers actually mean, and how they help us understand the Universe.

---

### 🌌 What Is Cosmology?

Cosmology is the study of the Universe on the largest scales.  
It’s not just about stars or galaxies, but about space itself. How it began, how it changes, and what it’s made of.

Even though the Universe seems impossibly complex, a lot of its behaviour can be captured by a small set of physical parameters. These include things like how fast the Universe expands, how much matter it contains, and how smooth or bumpy it was at the beginning.

These numbers form the basis of our models, which are simplified but powerful ways of describing how the Universe works.

---

### 🧮 Building a Universe

In physics, when you can describe something with numbers, you can usually predict how it behaves. Cosmology works the same way.

By choosing values for things like the Hubble constant or the amount of matter in the Universe, scientists can simulate how space evolves over time. We use software that takes those values and calculates how structures like galaxies and clusters would form.

Once we have those predictions, we compare them to what we actually see with telescopes. If they match, we might be on the right track. If not, it’s back to the drawing board.

---

### 🎥 What Do These Simulations Look Like?

It’s one thing to talk about structure forming across the Universe, but it’s much easier to understand when you can see it happen.

The video below shows the **Millennium Simulation**, a large-scale computer model of how matter clumps together under gravity over billions of years.
""")

st.video("https://www.youtube.com/watch?v=ClIiUkHPkIE")

st.markdown("""
Each bright thread or cluster in the simulation represents regions of high matter density, where galaxies and clusters are most likely to form.

This is why we build simulations in cosmology. They help us test ideas about dark matter, gravity, and the evolution of the Universe in a way that’s both visual and scientific.

<sub><br>
📽️ <i>Simulation by the Virgo Consortium. Video by the Max Planck Institute for Astrophysics.<br>
Springel et al., Nature 435, 629–636 (2005). <a href="https://doi.org/10.1038/nature03597" target="_blank">DOI: 10.1038/nature03597</a></i>
</sub>
""", unsafe_allow_html=True)

st.markdown("""
---

### 🔭 Why This Matters

Understanding how matter is distributed throughout the Universe helps us figure out what the Universe is made of.

It’s one of the ways we study dark matter and dark energy, things we can't see directly, but that leave a clear imprint on the way galaxies form and move.  
It also helps us test our theories of gravity on the biggest scales possible.

This kind of modelling is one of the main ways we try to figure out how the Universe works and where it might be heading.

---

### 🧠 From Quiz to Cosmology

Earlier, you explored one possible version of the Universe by answering some questions. Each answer was linked to a physical assumption; things like how fast expansion happens or how clumpy matter is.

In real research, scientists vary these assumptions and simulate thousands of different Universes to see which ones match reality best.

The quiz was just a small taste. Next, we’ll break down what that power spectrum plot actually showed, and how it helps us study the cosmos.
""")
