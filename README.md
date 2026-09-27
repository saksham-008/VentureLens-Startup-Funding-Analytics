# VentureLens — Startup Funding Analytics

## 📊 Project Overview

**VentureLens — Startup Funding Analytics** is a data analytics project focused on analyzing startup funding data to answer real-world business questions.

The project follows an analyst-oriented workflow:

**Raw Data → Data Cleaning → Business Questions → Data Analysis → Insights → Visualization**

The goal is to transform raw startup funding records into meaningful insights about **industries, cities, funding patterns, and startup hubs**.

---

## 🎯 Business Objective

Startup funding data can be used to understand where investment is concentrated and which areas of the startup ecosystem attract the most capital.

VentureLens focuses on questions such as:

1. Which industries attract the most funding?
2. Which cities are India's startup hubs?
3. How has funding grown year over year?
4. What investment types are most common?
5. Which startups received the highest funding?
6. Which months see highest funding activity?
7. Who are the most active investors in India?

These questions are answered using data cleaning, aggregation, comparison, and visualization.

---

## 📁 Dataset

The project uses a startup funding dataset containing approximately:

| Stage           | Records |
| --------------- | ------: |
| Raw Dataset     |   3,044 |
| Cleaned Dataset |   2,064 |

The raw dataset required preprocessing before analysis. Cleaning was performed to improve data consistency and ensure that the resulting analysis was based on usable records.

---

## 🔄 Data Analysis Workflow

### 1. Data Collection

The project starts with the raw startup funding dataset.

### 2. Data Cleaning

The raw dataset is examined and cleaned to handle issues such as:

* Missing values
* Duplicate records
* Inconsistent entries
* Invalid or unusable data
* Formatting inconsistencies

After cleaning:

```text
3,044 Raw Records
        ↓
   Data Cleaning
        ↓
2,064 Cleaned Records
```

### 3. Business Question Formulation

Instead of simply exploring columns, the analysis begins with business questions.

For example:

```text
Which industries attract the most funding?
                ↓
          GROUP BY Industry
                ↓
        SUM(Funding Amount)
                ↓
        Compare Industries
                ↓
       Identify Top Industries
```

Another example:

```text
Which cities are startup hubs?
                ↓
            GROUP BY City
                ↓
        SUM(Funding Amount)
                ↓
        Compare Cities
                ↓
       Identify Major Hubs
```

### 4. Analysis

The cleaned dataset is aggregated and compared to answer the defined business questions.

Key analytical operations include:

* Grouping
* Aggregation
* Summation
* Counting
* Sorting
* Comparison
* Trend analysis

### 5. Visualization

The results are presented through visualizations to make funding patterns easier to understand.

---

## 📌 Key Areas of Analysis

### Industry Analysis

Examines funding distribution across different startup industries.

**Business Question:**

> Which industries attract the most funding?

The analysis groups startups by industry and calculates total funding received.

---

### Geographic Analysis

Examines funding across different cities.

**Business Question:**

> Which cities are startup funding hubs?

Cities are grouped and compared based on their total funding.

---

### Startup Funding Analysis

Examines the overall distribution of funding across startups and funding categories.

This helps identify patterns in how investment is distributed within the dataset.

---

## 🛠️ Tools & Technologies

* **Excel** — Data cleaning, analysis, and visualization
* **Pivot Tables** — Aggregation and business-question analysis
* **Charts & Dashboards** — Data visualization
* **Data Cleaning Techniques** — Handling duplicates, missing values, and inconsistent data

---

---

## 📈 Analyst Skills Demonstrated

This project demonstrates practical skills relevant to a **Data Analyst / Business Analyst** role:

* Data Cleaning
* Exploratory Data Analysis
* Business Question Formulation
* Data Aggregation
* Data Interpretation
* Comparative Analysis
* Data Visualization
* Dashboard Development
* Extracting Business Insights from Raw Data

---

## 💡 Project Takeaway

VentureLens demonstrates how raw startup funding data can be converted into structured analysis that helps answer practical business questions.

Rather than focusing only on technical data manipulation, the project follows a **business-first analytical approach**:

> **Ask the right question → Analyze the data → Visualize the result → Derive meaningful insights**
