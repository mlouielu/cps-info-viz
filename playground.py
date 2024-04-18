import pickle
import pathlib

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


PICKLE_DIR = pathlib.Path("data")

asecs = {}
for asec_pkl in sorted(PICKLE_DIR.glob("asec_*.pkl")):
    yrs = asec_pkl.stem[5:9]
    asecs[yrs] = pickle.load(open(asec_pkl, "rb"))


weminds = [
    (-1, "All"),
    (4, "Manufacturing"),
    (6, "Transportation"),
    (7, "Information"),
    (10, "Education_and_Health"),
]


def main():
    for yrs in asecs:
        asec = asecs[yrs]
        print(len(asec["a_wkstat"]))
        print((asec["a_wkstat"] == 2).sum())

        full_time = asec[asec["a_wkstat"] == 2]
        mean = full_time["wsal_val"].mean()
        std = full_time["wsal_val"].std()

        lower_bound = 1
        upper_bound = mean + 2 * std  # adjust multiplier as needed

        for wemind, label in weminds:
            fig, ax = plt.subplots()
            filtered_data = asec[
                (asec["wsal_val"] >= lower_bound) & (asec["wsal_val"] <= upper_bound)
            ]

            if wemind != -1:
                filtered_data = asec[asec["wemind"] == wemind]

            male = filtered_data[filtered_data["a_sex"] == 1]
            female = filtered_data[filtered_data["a_sex"] == 2]

            sns.kdeplot(
                male["wsal_val"]/1000,
                ax=ax,
                alpha=0.5,
                label=f"{yrs} - Male",
                color="blue"
            )
            sns.kdeplot(
                female["wsal_val"]/1000,
                ax=ax,
                alpha=0.5,
                label=f"{yrs} - Female",
                color="#DE5D83"
            )

            ax.set_title(
                f"Full-time workers' salary distribution - by gender/{label} ({yrs})"
            )
            ax.set_xlabel("Salary in thousands (USD)")
            ax.set_ylabel("Density")
            ax.set_xlim(0, 220)
            ax.legend()

            plt.savefig(f"figs/full_time_salary_by_gender_{label}_{yrs}.png")
            plt.close()

        # deciles = np.percentile(filtered_data["wsal_val"], np.arange(10, 100, 10))
        # for decile in deciles:
        #     ax.axvline(decile, color="k", linestyle="-", alpha=0.5)


if __name__ == "__main__":
    main()
