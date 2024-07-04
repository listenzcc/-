"""
File: update-topics.py
Author: Chuncheng Zhang
Date: 2024-07-04
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Update the project by the '话题管理.xlsx'

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2024-07-04 ------------------------
# Requirements and constants
import pandas as pd

from pathlib import Path

cwd = Path(__file__).parent
root = cwd.parent

# %% ---- 2024-07-04 ------------------------
# Function and class


class NeedUpdate:
    asset = root.joinpath("asset")
    doc = root.joinpath("doc")
    pdf = root.joinpath("pdf")
    sql = root.joinpath("sql")
    web = root.joinpath("web")


def read_topics():
    path = cwd.joinpath('话题管理.xlsx')
    df = pd.read_excel(path, sheet_name='话题表')
    return df


# %% ---- 2024-07-04 ------------------------
# Play ground
if __name__ == "__main__":
    df = read_topics()
    print(df)
    for i, row in df.iterrows():
        for k in dir(NeedUpdate):
            if k.startswith("_"):
                continue
            parent = getattr(NeedUpdate, k)
            p: Path = parent.joinpath(row['Class'], row['Subclass'])
            p.mkdir(exist_ok=True, parents=True)
            print(f'Made {p}')

            with open(p.joinpath('readme.md'), 'w', encoding="utf-8") as f:
                f.writelines(f'''
# {row['Class']} - {row['Subclass']}

EN: {row['Class']} - {row['Subclass']}
CN: {row['大类']} - {row['子类']}

---

{row['备注']}

''')


# %% ---- 2024-07-04 ------------------------
# Pending


# %% ---- 2024-07-04 ------------------------
# Pending
