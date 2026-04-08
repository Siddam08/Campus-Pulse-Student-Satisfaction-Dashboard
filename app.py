# # # # # import streamlit as st
# # # # # import pandas as pd
# # # # # import matplotlib.pyplot as plt
# # # # # import seaborn as sns

# # # # # # Page config
# # # # # st.set_page_config(page_title="Campus Pulse Dashboard", layout="wide")

# # # # # # Load data
# # # # # df = pd.read_csv("campus_pulse_data.csv")

# # # # # # Title
# # # # # st.title("🎓 Campus Pulse - Student Satisfaction Dashboard")
# # # # # st.markdown("Developed by Sri Teja")

# # # # # # ---------------- FILTERS ----------------
# # # # # st.sidebar.header("🔎 Filters")

# # # # # dept = st.sidebar.multiselect("Select Department", df["Department"].unique(), default=df["Department"].unique())
# # # # # year = st.sidebar.multiselect("Select Year", df["Year"].unique(), default=df["Year"].unique())
# # # # # facility = st.sidebar.multiselect("Select Facility", df["Facility"].unique(), default=df["Facility"].unique())

# # # # # filtered_df = df[
# # # # #     (df["Department"].isin(dept)) &
# # # # #     (df["Year"].isin(year)) &
# # # # #     (df["Facility"].isin(facility))
# # # # # ]

# # # # # # ---------------- KPI ----------------
# # # # # col1, col2, col3 = st.columns(3)

# # # # # col1.metric("Total Responses", len(filtered_df))
# # # # # col2.metric("Average Rating", round(filtered_df["Rating"].mean(), 2))
# # # # # col3.metric("Max Rating", filtered_df["Rating"].max())

# # # # # # ---------------- CHARTS ----------------
# # # # # st.subheader("📊 Average Rating by Department")

# # # # # dept_avg = df.groupby("Department")["Rating"].mean()  # FIXED HERE
# # # # # st.bar_chart(dept_avg)

# # # # # # ---------------- FACILITY ANALYSIS ----------------
# # # # # st.subheader("🏫 Average Rating by Facility")

# # # # # facility_avg = df.groupby("Facility")["Rating"].mean()
# # # # # st.bar_chart(facility_avg)

# # # # # # ---------------- PIE CHART ----------------
# # # # # st.subheader("📌 Department Distribution")

# # # # # fig1, ax1 = plt.subplots()
# # # # # df["Department"].value_counts().plot.pie(autopct='%1.1f%%', ax=ax1)
# # # # # st.pyplot(fig1)

# # # # # # ---------------- TREND ----------------
# # # # # st.subheader("📈 Rating Trend Over Time")

# # # # # df["Feedback_Date"] = pd.to_datetime(df["Feedback_Date"])
# # # # # trend = df.groupby("Feedback_Date")["Rating"].mean()

# # # # # st.line_chart(trend)

# # # # # # ---------------- SCATTER ----------------
# # # # # st.subheader("🔍 Year vs Rating Analysis")

# # # # # fig2, ax2 = plt.subplots()
# # # # # sns.scatterplot(data=df, x="Year", y="Rating", hue="Department", ax=ax2)
# # # # # st.pyplot(fig2)

# # # # # # ---------------- TABLE ----------------
# # # # # st.subheader("📋 Data Table")
# # # # # st.dataframe(filtered_df)

# # # # # # ---------------- DOWNLOAD ----------------
# # # # # st.download_button(
# # # # #     label="📥 Download Filtered Data",
# # # # #     data=filtered_df.to_csv(index=False),
# # # # #     file_name="filtered_data.csv",
# # # # #     mime="text/csv"
# # # # # )

# # # # import streamlit as st
# # # # import pandas as pd
# # # # import matplotlib.pyplot as plt
# # # # import seaborn as sns
# # # # import sqlite3

# # # # st.set_page_config(page_title="Campus Pulse Dashboard", layout="wide")

# # # # # Load CSV
# # # # df = pd.read_csv("campus_pulse_data.csv")

# # # # # ---------------- SQL PART ----------------
# # # # conn = sqlite3.connect("campus.db")

# # # # # Store data into SQL
# # # # df.to_sql("students", conn, if_exists="replace", index=False)

# # # # # SQL Query
# # # # query = """
# # # # SELECT Department, AVG(Rating) as Avg_Rating
# # # # FROM students
# # # # GROUP BY Department
# # # # """
# # # # sql_result = pd.read_sql(query, conn)

# # # # # ---------------- UI ----------------
# # # # st.title("🎓 Campus Pulse - Student Satisfaction Dashboard")
# # # # st.markdown("Developed by Sri Teja")
# # # # st.markdown("---")

# # # # # Sidebar Filters
# # # # st.sidebar.header("🔎 Filters")

# # # # dept = st.sidebar.multiselect("Department", df["Department"].unique(), default=df["Department"].unique())
# # # # year = st.sidebar.multiselect("Year", df["Year"].unique(), default=df["Year"].unique())
# # # # facility = st.sidebar.multiselect("Facility", df["Facility"].unique(), default=df["Facility"].unique())

# # # # filtered_df = df[
# # # #     (df["Department"].isin(dept)) &
# # # #     (df["Year"].isin(year)) &
# # # #     (df["Facility"].isin(facility))
# # # # ]

# # # # # ---------------- KPI ----------------
# # # # col1, col2, col3 = st.columns(3)

# # # # col1.metric("Total Responses", len(filtered_df))
# # # # col2.metric("Average Rating", round(filtered_df["Rating"].mean(), 2))
# # # # col3.metric("Max Rating", filtered_df["Rating"].max())

# # # # # ---------------- SQL OUTPUT ----------------
# # # # st.subheader("🗄️ SQL Analysis: Avg Rating by Department")
# # # # st.dataframe(sql_result)

# # # # # ---------------- CHARTS ----------------
# # # # st.subheader("📊 Average Rating by Department")

# # # # dept_avg = df.groupby("Department")["Rating"].mean()
# # # # st.bar_chart(dept_avg)

# # # # # Facility Chart
# # # # st.subheader("🏫 Average Rating by Facility")
# # # # facility_avg = df.groupby("Facility")["Rating"].mean()
# # # # st.bar_chart(facility_avg)

# # # # # Pie Chart
# # # # st.subheader("📌 Department Distribution")
# # # # fig1, ax1 = plt.subplots()
# # # # df["Department"].value_counts().plot.pie(autopct='%1.1f%%', ax=ax1)
# # # # st.pyplot(fig1)

# # # # # Trend
# # # # st.subheader("📈 Rating Trend Over Time")
# # # # df["Feedback_Date"] = pd.to_datetime(df["Feedback_Date"])
# # # # trend = df.groupby("Feedback_Date")["Rating"].mean()
# # # # st.line_chart(trend)

# # # # # Scatter
# # # # st.subheader("🔍 Year vs Rating Analysis")
# # # # fig2, ax2 = plt.subplots()
# # # # sns.scatterplot(data=df, x="Year", y="Rating", hue="Department", ax=ax2)
# # # # st.pyplot(fig2)

# # # # # Table
# # # # st.subheader("📋 Filtered Data")
# # # # st.dataframe(filtered_df)

# # # # # Download
# # # # st.download_button(
# # # #     label="📥 Download Data",
# # # #     data=filtered_df.to_csv(index=False),
# # # #     file_name="filtered_data.csv",
# # # #     mime="text/csv"
# # # # )


# # # import streamlit as st
# # # import pandas as pd
# # # import matplotlib.pyplot as plt
# # # import seaborn as sns
# # # import sqlite3

# # # st.set_page_config(page_title="Campus Pulse Dashboard", layout="wide")

# # # # ---------------- LOAD DATA ----------------
# # # df = pd.read_csv("campus_pulse_data.csv")

# # # # ---------------- SQL ----------------
# # # conn = sqlite3.connect("campus.db")
# # # df.to_sql("students", conn, if_exists="replace", index=False)

# # # query = """
# # # SELECT Department, AVG(Rating) as Avg_Rating
# # # FROM students
# # # GROUP BY Department
# # # """
# # # sql_result = pd.read_sql(query, conn)

# # # # ---------------- TITLE ----------------
# # # st.title("🎓 Campus Pulse - Student Satisfaction Dashboard")
# # # st.markdown("### 📊 Real-time analysis of campus facilities")
# # # st.markdown("Developed by Sri Teja")
# # # st.markdown("---")

# # # # ---------------- SIDEBAR ----------------
# # # st.sidebar.header("🔎 Filters")

# # # dept = st.sidebar.multiselect("Department", df["Department"].unique(), default=df["Department"].unique())
# # # year = st.sidebar.multiselect("Year", df["Year"].unique(), default=df["Year"].unique())
# # # facility = st.sidebar.multiselect("Facility", df["Facility"].unique(), default=df["Facility"].unique())

# # # filtered_df = df[
# # #     (df["Department"].isin(dept)) &
# # #     (df["Year"].isin(year)) &
# # #     (df["Facility"].isin(facility))
# # # ]

# # # # ---------------- STATUS LOGIC ----------------
# # # def get_status(rating):
# # #     if rating <= 2:
# # #         return "Critical 🔴"
# # #     elif rating == 3:
# # #         return "Average 🟡"
# # #     else:
# # #         return "Good 🟢"

# # # filtered_df["Status"] = filtered_df["Rating"].apply(get_status)

# # # # ---------------- KPI ----------------
# # # col1, col2, col3 = st.columns(3)

# # # col1.metric("Total Responses", len(filtered_df))
# # # col2.metric("Average Rating", round(filtered_df["Rating"].mean(), 2))
# # # col3.metric("Max Rating", filtered_df["Rating"].max())

# # # st.markdown("---")

# # # # ---------------- MAIN LAYOUT ----------------
# # # left, right = st.columns(2)

# # # # LEFT SIDE
# # # with left:
# # #     st.subheader("📊 Avg Rating by Department (SQL)")
# # #     st.dataframe(sql_result)

# # #     st.subheader("🏫 Facility Performance")
# # #     facility_avg = df.groupby("Facility")["Rating"].mean()
# # #     st.bar_chart(facility_avg)

# # # # RIGHT SIDE
# # # with right:
# # #     st.subheader("📈 Trend Over Time")
# # #     df["Feedback_Date"] = pd.to_datetime(df["Feedback_Date"])
# # #     trend = df.groupby("Feedback_Date")["Rating"].mean()
# # #     st.line_chart(trend)

# # #     st.subheader("📌 Department Distribution")
# # #     fig1, ax1 = plt.subplots()
# # #     df["Department"].value_counts().plot.pie(autopct='%1.1f%%', ax=ax1)
# # #     st.pyplot(fig1)

# # # # ---------------- SCATTER ----------------
# # # st.subheader("🔍 Year vs Rating Analysis")
# # # fig2, ax2 = plt.subplots()
# # # sns.scatterplot(data=df, x="Year", y="Rating", hue="Department", ax=ax2)
# # # st.pyplot(fig2)

# # # # ---------------- INSIGHTS ----------------
# # # st.subheader("📢 Key Insights")

# # # st.success(f"⭐ Overall Average Rating: {round(df['Rating'].mean(),2)}")

# # # st.info(f"🏆 Best Department: {df.groupby('Department')['Rating'].mean().idxmax()}")

# # # st.warning(f"⚠️ Lowest Performing Facility: {df.groupby('Facility')['Rating'].mean().idxmin()}")

# # # # ---------------- TABLE ----------------
# # # st.subheader("📋 Filtered Data with Status")
# # # st.dataframe(filtered_df)

# # # # ---------------- DOWNLOAD ----------------
# # # st.download_button(
# # #     label="📥 Download Filtered Data",
# # #     data=filtered_df.to_csv(index=False),
# # #     file_name="filtered_data.csv",
# # #     mime="text/csv"
# # # )

# # # # ---------------- FOOTER ----------------
# # # st.markdown("---")
# # # st.markdown("📌 Project: Campus Pulse Dashboard | Built using Python, SQL & Streamlit")


# # import streamlit as st
# # import pandas as pd
# # import matplotlib.pyplot as plt
# # import seaborn as sns
# # import sqlite3

# # st.set_page_config(page_title="Campus Pulse Dashboard", layout="wide")

# # # ---------------- LOAD DATA ----------------
# # df = pd.read_csv("campus_pulse_data.csv")

# # # ---------------- SQL ----------------
# # conn = sqlite3.connect("campus.db")
# # df.to_sql("students", conn, if_exists="replace", index=False)

# # query = """
# # SELECT Department, AVG(Rating) as Avg_Rating
# # FROM students
# # GROUP BY Department
# # """
# # sql_result = pd.read_sql(query, conn)

# # # ---------------- TITLE ----------------
# # st.title("🎓 Campus Pulse - Student Satisfaction Dashboard")
# # st.markdown("### 📊 Real-time analysis of campus facilities")
# # st.markdown("Developed by Sri Teja")
# # st.markdown("---")

# # # ---------------- SIDEBAR ----------------
# # st.sidebar.header("🔎 Filters")

# # dept = st.sidebar.multiselect("Department", df["Department"].unique(), default=df["Department"].unique())
# # year = st.sidebar.multiselect("Year", df["Year"].unique(), default=df["Year"].unique())
# # facility = st.sidebar.multiselect("Facility", df["Facility"].unique(), default=df["Facility"].unique())

# # filtered_df = df[
# #     (df["Department"].isin(dept)) &
# #     (df["Year"].isin(year)) &
# #     (df["Facility"].isin(facility))
# # ]

# # # ---------------- STATUS LOGIC ----------------
# # def get_status(rating):
# #     if rating <= 2:
# #         return "Critical 🔴"
# #     elif rating == 3:
# #         return "Average 🟡"
# #     else:
# #         return "Good 🟢"

# # filtered_df["Status"] = filtered_df["Rating"].apply(get_status)

# # # ---------------- KPI ----------------
# # col1, col2, col3 = st.columns(3)

# # col1.metric("Total Responses", len(filtered_df))
# # col2.metric("Average Rating", round(filtered_df["Rating"].mean(), 2))
# # col3.metric("Max Rating", filtered_df["Rating"].max())

# # st.markdown("---")

# # # ---------------- MAIN LAYOUT ----------------
# # left, right = st.columns(2)

# # # LEFT SIDE
# # with left:
# #     st.subheader("📊 Avg Rating by Department (SQL)")
# #     st.dataframe(sql_result)

# #     st.subheader("🏫 Facility Performance")
# #     facility_avg = df.groupby("Facility")["Rating"].mean()
# #     st.bar_chart(facility_avg)

# # # RIGHT SIDE
# # with right:
# #     st.subheader("📈 Trend Over Time")
# #     df["Feedback_Date"] = pd.to_datetime(df["Feedback_Date"])
# #     trend = df.groupby("Feedback_Date")["Rating"].mean()
# #     st.line_chart(trend)

# #     st.subheader("📌 Department Distribution")
# #     fig1, ax1 = plt.subplots()
# #     df["Department"].value_counts().plot.pie(autopct='%1.1f%%', ax=ax1)
# #     st.pyplot(fig1)

# # # ---------------- SCATTER ----------------
# # st.subheader("🔍 Year vs Rating Analysis")
# # fig2, ax2 = plt.subplots()
# # sns.scatterplot(data=df, x="Year", y="Rating", hue="Department", ax=ax2)
# # st.pyplot(fig2)

# # # ---------------- INSIGHTS ----------------
# # st.subheader("📢 Key Insights")

# # st.success(f"⭐ Overall Average Rating: {round(df['Rating'].mean(),2)}")

# # st.info(f"🏆 Best Department: {df.groupby('Department')['Rating'].mean().idxmax()}")

# # st.warning(f"⚠️ Lowest Performing Facility: {df.groupby('Facility')['Rating'].mean().idxmin()}")

# # # ---------------- TABLE ----------------
# # st.subheader("📋 Filtered Data with Status")
# # st.dataframe(filtered_df)

# # # ---------------- DOWNLOAD ----------------
# # st.download_button(
# #     label="📥 Download Filtered Data",
# #     data=filtered_df.to_csv(index=False),
# #     file_name="filtered_data.csv",
# #     mime="text/csv"
# # )

# # # ---------------- FOOTER ----------------
# # st.markdown("---")
# # st.markdown("📌 Project: Campus Pulse Dashboard | Built using Python, SQL & Streamlit")




# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(page_title="Campus Pulse Dashboard", layout="wide")

# # ---------------- LOAD DATA ----------------
# df = pd.read_csv("campus_pulse_data.csv")

# # Convert date
# df["Feedback_Date"] = pd.to_datetime(df["Feedback_Date"])

# # ---------------- TITLE ----------------
# st.title("🎓 Campus Pulse - Student Satisfaction Dashboard")
# st.markdown("### 📊 Real-time Analysis of Student Feedback Across Campus Facilities")
# st.markdown("Developed by Sri Teja")
# st.markdown("---")

# # ---------------- FILTERS ----------------
# st.sidebar.header("🔎 Filters")

# dept = st.sidebar.multiselect(
#     "Select Department",
#     df["Department"].unique(),
#     default=df["Department"].unique()
# )

# year = st.sidebar.multiselect(
#     "Select Year",
#     df["Year"].unique(),
#     default=df["Year"].unique()
# )

# facility = st.sidebar.multiselect(
#     "Select Facility",
#     df["Facility"].unique(),
#     default=df["Facility"].unique()
# )

# # Buttons
# apply_filter = st.sidebar.button("🔍 Apply Filters")
# reset_filter = st.sidebar.button("♻ Reset Filters")

# # Session state
# if "filtered_df" not in st.session_state:
#     st.session_state.filtered_df = df

# # Apply filter
# if apply_filter:
#     st.session_state.filtered_df = df[
#         (df["Department"].isin(dept)) &
#         (df["Year"].isin(year)) &
#         (df["Facility"].isin(facility))
#     ]

# # Reset filter
# if reset_filter:
#     st.session_state.filtered_df = df

# filtered_df = st.session_state.filtered_df

# # ---------------- FILTER SUMMARY ----------------
# st.write("### 🔍 Selected Filters")
# st.write("Departments:", dept)
# st.write("Years:", year)
# st.write("Facilities:", facility)

# # ---------------- KPI ----------------
# col1, col2, col3 = st.columns(3)

# col1.metric("Total Responses", len(filtered_df))
# col2.metric("Average Rating", round(filtered_df["Rating"].mean(), 2))
# col3.metric("Max Rating", filtered_df["Rating"].max())

# # ---------------- CHARTS ----------------
# st.subheader("📊 Average Rating by Department")
# dept_avg = filtered_df.groupby("Department")["Rating"].mean()
# st.bar_chart(dept_avg)

# # ---------------- FACILITY ANALYSIS ----------------
# st.subheader("🏫 Average Rating by Facility")
# facility_avg = filtered_df.groupby("Facility")["Rating"].mean()
# st.bar_chart(facility_avg)

# # ---------------- PIE CHART ----------------
# st.subheader("📌 Department Distribution")
# fig1, ax1 = plt.subplots()
# filtered_df["Department"].value_counts().plot.pie(autopct='%1.1f%%', ax=ax1)
# st.pyplot(fig1)

# # ---------------- TREND ----------------
# st.subheader("📈 Rating Trend Over Time")
# trend = filtered_df.groupby("Feedback_Date")["Rating"].mean()
# st.line_chart(trend)

# # ---------------- SCATTER ----------------
# st.subheader("🔍 Year vs Rating Analysis")
# fig2, ax2 = plt.subplots()
# sns.scatterplot(data=filtered_df, x="Year", y="Rating", hue="Department", ax=ax2)
# st.pyplot(fig2)

# # ---------------- TABLE ----------------
# st.subheader("📋 Data Table")
# st.dataframe(filtered_df)

# # ---------------- DOWNLOAD ----------------
# st.download_button(
#     label="📥 Download Filtered Data",
#     data=filtered_df.to_csv(index=False),
#     file_name="filtered_data.csv",
#     mime="text/csv"
# )

# # ---------------- INSIGHTS ----------------
# st.subheader("📢 Key Insights")

# if len(filtered_df) > 0:
#     st.write(f"""
#     - Overall average satisfaction rating is **{round(filtered_df['Rating'].mean(),2)}**
#     - Most active department is **{filtered_df['Department'].value_counts().idxmax()}**
#     - Highest rated facility is **{filtered_df.groupby('Facility')['Rating'].mean().idxmax()}**
#     - Some facilities may need improvement based on lower ratings
#     """)
# else:
#     st.warning("No data available for selected filters.")



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Campus Pulse Dashboard", layout="wide")

# ---------------- DARK THEME ----------------
st.markdown("""
<style>
body {
    background-color: #0E1117;
    color: white;
}
.sidebar .sidebar-content {
    background-color: #111827;
}
</style>
""", unsafe_allow_html=True)

sns.set_style("darkgrid")

# ---------------- LOGIN SYSTEM ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 Login - Campus Pulse Dashboard")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.success("Login Successful ✅")
            st.rerun()
        else:
            st.error("Invalid Credentials ❌")

    st.stop()

# ---------------- LOAD DATA ----------------
df = pd.read_csv("campus_pulse_data.csv")
df["Feedback_Date"] = pd.to_datetime(df["Feedback_Date"])

# ---------------- TITLE ----------------
st.title("🎓 Campus Pulse - Student Satisfaction Dashboard")
st.markdown("### 📊 Advanced Data Analytics Dashboard")
st.markdown("---")

# ---------------- FILTERS ----------------
st.sidebar.header("🔎 Filters")

dept = st.sidebar.multiselect("Department", df["Department"].unique(), df["Department"].unique())
year = st.sidebar.multiselect("Year", df["Year"].unique(), df["Year"].unique())
facility = st.sidebar.multiselect("Facility", df["Facility"].unique(), df["Facility"].unique())

apply_filter = st.sidebar.button("🔍 Apply Filters")
reset_filter = st.sidebar.button("♻ Reset")

if "filtered_df" not in st.session_state:
    st.session_state.filtered_df = df

if apply_filter:
    st.session_state.filtered_df = df[
        (df["Department"].isin(dept)) &
        (df["Year"].isin(year)) &
        (df["Facility"].isin(facility))
    ]

if reset_filter:
    st.session_state.filtered_df = df

filtered_df = st.session_state.filtered_df

# ---------------- KPI ----------------
col1, col2, col3 = st.columns(3)

col1.metric("📌 Total Responses", len(filtered_df))
col2.metric("⭐ Avg Rating", round(filtered_df["Rating"].mean(), 2))
col3.metric("🏆 Max Rating", filtered_df["Rating"].max())

# ---------------- BAR ----------------
st.subheader("📊 Department Performance")
dept_avg = filtered_df.groupby("Department")["Rating"].mean()
st.bar_chart(dept_avg)

# ---------------- FACILITY ----------------
st.subheader("🏫 Facility Ratings")
facility_avg = filtered_df.groupby("Facility")["Rating"].mean()
st.bar_chart(facility_avg)

# ---------------- PIE ----------------
st.subheader("📌 Department Distribution")
fig1, ax1 = plt.subplots()
filtered_df["Department"].value_counts().plot.pie(autopct='%1.1f%%', ax=ax1)
ax1.set_ylabel("")
st.pyplot(fig1)

# ---------------- TREND ----------------
st.subheader("📈 Rating Trend")
trend = filtered_df.groupby("Feedback_Date")["Rating"].mean()
st.line_chart(trend)

# ---------------- ADVANCED GRAPH ----------------
st.subheader("📊 Satisfaction Analysis (Year vs Department)")

year_map = {1:"1st Year",2:"2nd Year",3:"3rd Year",4:"4th Year"}
filtered_df["Year_Label"] = filtered_df["Year"].map(year_map)

fig2, ax2 = plt.subplots(figsize=(10,6))

sns.boxplot(data=filtered_df, x="Year_Label", y="Rating", hue="Department")
sns.stripplot(data=filtered_df, x="Year_Label", y="Rating", hue="Department", dodge=True, alpha=0.4)

handles, labels = ax2.get_legend_handles_labels()
ax2.legend(handles[:5], labels[:5])

st.pyplot(fig2)

# ---------------- TABLE ----------------
st.subheader("📋 Data Table")
st.dataframe(filtered_df)

# ---------------- DOWNLOAD ----------------
st.download_button(
    "📥 Download Data",
    filtered_df.to_csv(index=False),
    "filtered_data.csv"
)

# ---------------- INSIGHTS ----------------
st.subheader("📢 Insights")

st.write(f"""
✔ Average Rating: {round(filtered_df['Rating'].mean(),2)}  
✔ Top Department: {filtered_df['Department'].value_counts().idxmax()}  
✔ Best Facility: {filtered_df.groupby('Facility')['Rating'].mean().idxmax()}  
""")



