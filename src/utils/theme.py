custom_palette = [
    "#636EFA",  # Blue
    "#EF553B",  # Red
    "#00CC96",  # Green
    "#AB63FA",  # Purple
    "#FFA15A",  # Orange
    "#19D3F3",  # Cyan
    "#FF6692",  # Pink
    "#B6E880",  # Light Green
    "#FF97FF",  # Magenta
    "#FECB52",  # Yellow
]


def apply_custom_palette():
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Set globally for matplotlib and seaborn
    plt.rcParams["axes.prop_cycle"] = plt.cycler(color=custom_palette)
    sns.set_palette(custom_palette)
