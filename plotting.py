import matplotlib.pyplot as plt
import numpy as np
import io
import base64

def run_plot(df):
    fig, ax = plt.subplots()
    x = df["Rank"]
    y = df["Peak"]
    ax.scatter(x, y)
    m, b = np.polyfit(x, y, 1)
    ax.plot(x, m*x + b, linestyle="dotted", color="red")
    ax.set_xlabel("Rank")
    ax.set_ylabel("Peak")
    plt.tight_layout()

    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode()
    return f"data:image/png;base64,{img_base64}"