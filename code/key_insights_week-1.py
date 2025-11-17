import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ============================================================
# 1️⃣ Competitive Differentiation Radar Chart
# ============================================================

# Categories
categories = ['AI-Powered Matching', 'Trust & Verification', 'SME Focus',
              'Global Reach', 'User Experience', 'Value-Added Services']

# Values for each platform
pep_values = [4, 4, 5, 3, 4, 4]
indiamart_values = [2, 3, 5, 3, 3, 3]
alibaba_values = [5, 4, 3, 5, 4, 5]
globalsources_values = [3, 3, 4, 4, 3, 4]

# Repeat first value to close radar
values = [pep_values, indiamart_values, alibaba_values, globalsources_values]
for v in values:
    v += v[:1]

# Radar chart setup
N = len(categories)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

plt.figure(figsize=(10, 10))
ax = plt.subplot(111, polar=True)
plt.xticks(angles[:-1], categories, color='grey', size=10)

ax.set_rlabel_position(30)
plt.yticks([1, 2, 3, 4, 5], ["1", "2", "3", "4", "5"], color="grey", size=8)
plt.ylim(0, 5)

labels = ['Pepagora', 'IndiaMART', 'Alibaba', 'Global Sources']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

for i, v in enumerate(values):
    ax.plot(angles, v, linewidth=2, linestyle='solid', label=labels[i], color=colors[i])
    ax.fill(angles, v, alpha=0.1, color=colors[i])

plt.title('Competitive Differentiation Radar Chart', size=14, pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
plt.tight_layout()
plt.show()


# ============================================================
# 2️⃣ Strategic Opportunity Bar Chart
# ============================================================

data = {
    'Opportunity Area': [
        'AI Analytics Integration',
        'Mobile-First Experience',
        'Cross-Border Partnerships',
        'Regional Localization',
        'Sustainability & Green Trade'
    ],
    'Growth Potential Score': [9, 8, 7, 6, 5]
}

df = pd.DataFrame(data)

plt.figure(figsize=(9, 5))
colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(df)))

bars = plt.barh(df['Opportunity Area'], df['Growth Potential Score'], color=colors)

for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.1,
             bar.get_y() + bar.get_height() / 2,
             f'{width:.0f}', va='center', fontsize=10,
             fontweight='bold', color='black')

plt.xlabel('Growth Potential Score (1–10)', fontsize=11)
plt.title('Strategic Opportunity Potential for Pepagora', fontsize=13, fontweight='bold', pad=15)
plt.xlim(0, 10)
plt.gca().invert_yaxis()
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


# ============================================================
# 3️⃣ Pepagora Value Proposition Table
# ============================================================

data = {
    "Functional Value": [
        "AI Matching, Verified Leads",
        "RFQ Tools, Transparent Pricing",
        "API Access, Co-Branding"
    ],
    "Strategic Value": [
        "Brand Growth, Export Access",
        "Reliable Supply & Quality",
        "Shared Market Expansion"
    ]
}

stakeholders = ["SME Sellers", "Buyers", "Partners"]
df = pd.DataFrame(data, index=stakeholders)

fig, ax = plt.subplots(figsize=(8, 3))
ax.axis('tight')
ax.axis('off')

table = ax.table(
    cellText=df.values,
    rowLabels=df.index,
    colLabels=df.columns,
    cellLoc='center',
    rowLoc='center',
    loc='center'
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.5)

# Header styling
for (row, col), cell in table.get_celld().items():
    if row == 0:
        cell.set_text_props(weight='bold', color='white')
        cell.set_facecolor('#4c72b0')
    elif col == -1:
        cell.set_text_props(weight='bold')
        cell.set_facecolor('#f0f0f0')

plt.title('Pepagora – Value Proposition Matrix', fontsize=13, fontweight='bold', pad=12)
plt.tight_layout()
plt.show()
