import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Cosmic Quiz", page_icon="🌌")

st.title("🌀 What Kind of Universe Are You?")

st.markdown("""
Answer these five questions to find out your cosmic personality and see what your universe's structure looks like!
""")

# Set up session state flags
if 'show_result' not in st.session_state:
    st.session_state.show_result = False

if 'retake_quiz' not in st.session_state:
    st.session_state.retake_quiz = False

# Handle full quiz reset before rendering anything
if st.session_state.retake_quiz:
    for key in ["q1", "q2", "q3", "q4", "q5"]:
        st.session_state.pop(key, None)
    st.session_state.show_result = False
    st.session_state.retake_quiz = False
    st.rerun()

# Only show quiz if result isn't being shown
if not st.session_state.show_result:
    q1 = st.radio("1. How do you handle change?", [
        "🏃 I adapt fast — go with the flow, quick to act.",
        "🌊 Change is fine, as long as I can see it coming.",
        "🧘 Slow and steady — I like things to evolve gradually."
    ], index=None, key="q1")

    q2 = st.radio("2. What’s your ideal social setting?", [
        "🎉 Chaotic, exciting — I like when things get intense.",
        "🫱 A bit of structure is nice, but I don’t need too much.",
        "🏝️ Peaceful and uniform. No drama, thanks."
    ], index=None, key="q2")

    q3 = st.radio("3. Where do you feel most at home in your free time?", [
        "🧱 Somewhere solid and grounded — a quiet room, a good book, something dependable.",
        "🏞️ A bit of both — I like comfort, but I need some space and air.",
        "🌬️ Out in the open — anywhere I can roam, explore, and feel light."
    ], index=None, key="q3")

    q4 = st.radio("4. Which kind of story do you like best?", [
        "📜 A classic narrative — order, rules, symmetry.",
        "📘 One with a few surprising twists.",
        "🌀 Experimental, strange, nonlinear plots."
    ], index=None, key="q4")

    q5 = st.radio("5. What’s your vibe in a group project?", [
        "🧱 I’m the one doing the bulk of the work. I carry the structure.",
        "⚖️ I contribute steadily — I’m part of the balance.",
        "🌬️ I’m there, but I float around. I don’t like being pinned down."
    ], index=None, key="q5")

    all_answered = all(st.session_state.get(key) is not None for key in ["q1", "q2", "q3", "q4", "q5"])

    if st.button("Reveal My Cosmic Identity", disabled=not all_answered):
        st.session_state.show_result = True

# Now show the results
if st.session_state.show_result:
    h0_map = {
        "🏃 I adapt fast — go with the flow, quick to act.": "chaotic",
        "🌊 Change is fine, as long as I can see it coming.": "balanced",
        "🧘 Slow and steady — I like things to evolve gradually.": "minimalist"
    }
    lnAs_map = {
        "🎉 Chaotic, exciting — I like when things get intense.": "chaotic",
        "🫱 A bit of structure is nice, but I don’t need too much.": "balanced",
        "🏝️ Peaceful and uniform. No drama, thanks.": "minimalist"
    }
    omega_m_map = {
        "🧱 Somewhere solid and grounded — a quiet room, a good book, something dependable.": "structured",
        "🏞️ A bit of both — I like comfort, but I need some space and air.": "balanced",
        "🌬️ Out in the open — anywhere I can roam, explore, and feel light.": "minimalist"
    }
    ns_map = {
        "📜 A classic narrative — order, rules, symmetry.": "structured",
        "📘 One with a few surprising twists.": "balanced",
        "🌀 Experimental, strange, nonlinear plots.": "chaotic"
    }

    tag1 = h0_map[st.session_state["q1"]]
    tag2 = lnAs_map[st.session_state["q2"]]
    tag3 = omega_m_map[st.session_state["q3"]]
    tag4 = ns_map[st.session_state["q4"]]

    tags = [tag1, tag2, tag3, tag4]
    dominant_tag = max(set(tags), key=tags.count)

    personalities = {
        "chaotic": ("⚡ The Chaotic Sprinter", "You're fast-paced and unpredictable. Your universe evolves quickly, forming dramatic structures in a short time."),
        "balanced": ("🌌 The Structured Explorer", "You're a well-balanced universe — not too fast, not too clumpy. A classic ΛCDM-like cosmos."),
        "minimalist": ("🌬️ The Peaceful Voidwalker", "You prefer calm and simplicity. Your universe evolves slowly and avoids too much structure."),
        "structured": ("🧊 The Deep Thinker", "You’re dense, grounded, and built for forming galaxies. Your universe is rich in matter and strong in structure.")
    }

    name, description = personalities[dominant_tag]

    st.subheader(name)
    st.markdown(description)

    st.markdown("""
---

### 🧬 How does this relate to the Universe?

Each answer you gave maps to a real cosmological parameter, like how fast the universe expands, how much matter it contains, or how smooth or clumpy it started out.

These parameters shape how structure forms in your universe, from huge galaxy clusters to tiny galaxies. The way matter is distributed across different scales is captured by something called the **matter power spectrum**.

---

### 📈 What is the Matter Power Spectrum?

The plot below shows your universe’s **matter power spectrum**, a graph that reveals how matter is spread across the cosmos at different scales.

- The **x-axis** shows the **scale** we’re looking at, using a quantity called the *wavenumber* (k). Smaller values of k correspond to **large cosmic structures** (like superclusters), while larger k means **small-scale structures** (like galaxies).
- The **y-axis** shows **how much structure exists** at each scale — in other words, how strongly matter clumps together at that size.

Together, the shape of this curve tells us how your universe forms structure: does it clump up quickly? Is it more even and spread out? Where are the biggest fluctuations?

Your unique personality result changes the curve, just like different physics would change a real universe.

---
""")

    pk_files = {
        "chaotic": "Assets/chaotic.csv",
        "balanced": "Assets/structured.csv",
        "minimalist": "Assets/voidwalker.csv",
        "structured": "Assets/thinker.csv"
    }

    pk_file = pk_files[dominant_tag]
    df = pd.read_csv(pk_file)

    plt.rcParams.update({
        "text.usetex": False,
        "font.family": "serif",
        "mathtext.fontset": "cm"
    })

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(df["k [1/Mpc]"], df["P(k) [Mpc^3]"], label="Your Universe")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(r"Wavenumber $k\ \left[\mathrm{Mpc}^{-1}\right]$")
    ax.set_ylabel(r"$P(k)\ \left[\mathrm{Mpc}^3\right]$")
    ax.set_title(r"Matter Power Spectrum: $P(k)$ vs $k$")
    ax.grid(True)
    st.pyplot(fig)

    st.markdown("Want to learn more? Head to the sidebar and explore how real cosmologists use these parameters to model the universe!")

    # Reset button
    if st.button("🔁 Retake the Quiz"):
        st.session_state.retake_quiz = True
