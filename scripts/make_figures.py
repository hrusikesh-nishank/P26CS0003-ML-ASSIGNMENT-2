from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


Path("figures").mkdir(exist_ok=True)


# Q1c: bagging diagnostics

q1c = pd.read_csv("results/q1c_bagging_diagnostics.csv")

fig, ax = plt.subplots(1, 3, figsize=(12, 3.5))

ax[0].plot(q1c["B"], q1c["oob_accuracy"], marker="o")
ax[0].set_xlabel("Number of trees (B)")
ax[0].set_ylabel("OOB accuracy")
ax[0].set_title("OOB Accuracy")
ax[0].grid(alpha=0.3)

ax[1].plot(q1c["B"], q1c["pairwise_disagreement"], marker="o")
ax[1].set_xlabel("Number of trees (B)")
ax[1].set_ylabel("Average disagreement")
ax[1].set_title("Pairwise Disagreement")
ax[1].grid(alpha=0.3)

ax[2].plot(q1c["B"], q1c["mean_vote_margin"], marker="o")
ax[2].set_xlabel("Number of trees (B)")
ax[2].set_ylabel("Mean vote margin")
ax[2].set_title("Vote Margin")
ax[2].grid(alpha=0.3)

plt.tight_layout()
plt.savefig(
    "figures/q1c_bagging_metrics.png",
    dpi=200,
    bbox_inches="tight"
)
plt.close()


# Q2b: SAMME training history

q2b = pd.read_csv("results/q2b_samme_history.csv")

fig, ax = plt.subplots(2, 2, figsize=(9, 6))

ax[0, 0].plot(q2b["round"], q2b["weighted_error"])
ax[0, 0].set_title("Weighted Training Error")
ax[0, 0].set_xlabel("Round")
ax[0, 0].set_ylabel("Error")

ax[0, 1].plot(q2b["round"], q2b["alpha"])
ax[0, 1].set_title("Learner Weight")
ax[0, 1].set_xlabel("Round")
ax[0, 1].set_ylabel("Alpha")

ax[1, 0].plot(q2b["round"], q2b["max_sample_weight"])
ax[1, 0].set_title("Maximum Sample Weight")
ax[1, 0].set_xlabel("Round")
ax[1, 0].set_ylabel("Weight")

ax[1, 1].plot(q2b["round"], q2b["top10_total_weight"])
ax[1, 1].set_title("Weight of 10 Heaviest Images")
ax[1, 1].set_xlabel("Round")
ax[1, 1].set_ylabel("Total Weight")

plt.tight_layout()
plt.savefig(
    "figures/q2b_samme_training.png",
    dpi=200,
    bbox_inches="tight"
)
plt.close()


print("Figures regenerated successfully.")