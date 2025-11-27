import streamlit as st
import pandas as pd
import pickle

# ----------------------------------------
# 1. Load Model
# ----------------------------------------
MODEL_PATH = r"C:\Users\yuvra\OneDrive\Desktop\Projects\movie_recomandation_app\revenue_model.pkl"
model = pickle.load(open(MODEL_PATH, "rb"))

# ----------------------------------------
# 2. Load Dataset
# ----------------------------------------
CSV_PATH = r"C:\Users\yuvra\OneDrive\Desktop\Projects\movie_recomandation_app\reco_df.csv"
reco_df = pd.read_csv(CSV_PATH)

if "status" not in reco_df.columns:
    reco_df["status"] = "Released"

# ----------------------------------------
# 3. PAGE SETTINGS + CSS
# ----------------------------------------
st.set_page_config(page_title="Movie Recommender", layout="wide")

# Dark UI CSS
st.markdown("""
    <style>
        body {
            background-color: #0d0f12;
        }
        .movie-card {
            background: #1a1d21;
            padding: 22px;
            border-radius: 14px;
            margin-bottom: 20px;
            color: white !important;
            border: 1px solid #2b2e33;
        }
        .movie-title {
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 10px;
            color: #ff4c4c;
        }
        .movie-detail {
            font-size: 18px;
            margin-bottom: 6px;
            color: #d1d1d1;
        }
    </style>
""", unsafe_allow_html=True)

# ----------------------------------------
# 4. HEADER
# ----------------------------------------
st.markdown(
    "<h1 style='text-align:center;color:#ff4b4b;'>🎬 Movie Recommendation System</h1>",
    unsafe_allow_html=True,
)
st.write("### Select your preferences to get personalized movie suggestions 🎯")


# ----------------------------------------
# 5. FILTERS
# ----------------------------------------
all_genres = [
    'Action','Adventure','Animation','Available','Comedy','Crime','Documentary',
    'Drama','Family','Fantasy','Fiction','Foreign','History','Horror','Movie',
    'Music','Mystery','Not','Romance','Science','TV','Thriller','War','Western'
]

genre = st.selectbox("🎯 Choose Genre", all_genres)

# Language Columns
lang_cols = [col for col in reco_df.columns if col.startswith("lang_")]
pretty_lang = {col: col.replace("lang_", "") for col in lang_cols}

language_select = st.selectbox("🌐 Select Language", list(pretty_lang.values()))
selected_language_col = "lang_" + language_select

top_rated = st.checkbox("⭐ Show Top Rated Movies Only")

year_list = sorted(reco_df["release_year"].unique())
min_year = st.selectbox("📅 Minimum Release Year", year_list)

cast_list = sorted(reco_df["cast"].dropna().unique())
selected_cast = st.selectbox("🧑‍🎤 Filter by Cast (Optional)", ["None"] + cast_list)

st.write("---")

show_btn = st.button("🎥 Show Recommended Movies")


# ----------------------------------------
# 6. RECOMMEND MOVIES
# ----------------------------------------
if show_btn:

    df = reco_df.copy()

    # Genre Filter
    df = df[df[genre] == 1]

    # Language Filter
    df = df[df[selected_language_col] == 1]

    # Year Filter
    df = df[df["release_year"] >= min_year]

    # Cast Filter
    if selected_cast != "None":
        df = df[df["cast"] == selected_cast]

    # Rating Filter
    if top_rated:
        df = df.sort_values(by="vote_average", ascending=False).head(10)
    else:
        df = df.sample(10) if len(df) >= 10 else df

    st.write("## 🔥 Recommended Movies")

    if df.empty:
        st.error("No movies found for your filters 😔")
    else:
        for idx, row in df.iterrows():
            st.markdown(
                f"""
                <div class="movie-card">
                    <div class="movie-title">{row['title']}</div>
                    <div class="movie-detail"><b>📅 Year:</b> {row['release_year']}</div>
                    <div class="movie-detail"><b>⭐ Rating:</b> {row['vote_average']}</div>
                    <div class="movie-detail"><b>⏱ Runtime:</b> {row['runtime']} min</div>
                    <div class="movie-detail"><b>🎭 Cast:</b> {row['cast']}</div>
                    <div class="movie-detail"><b>🎬 Director:</b> {row['director']}</div>
                    <div class="movie-detail"><b>🏁 Status:</b> {row['status']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
