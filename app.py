"""
       MOODIFY0  ·  Pastel Music Recommender  v1.          
 Bollywood & Hollywood · 9 Moods · Global Hits · Pastel UI   
             Run: streamlit run app.py      
"""

import streamlit as st
import webbrowser

# setting up page
st.set_page_config(page_title="Moodify 🎼", page_icon="🎵", layout="centered")

# check session state variables
if "now_playing" not in st.session_state:
    st.session_state["now_playing"] = None
    
if "active_tab" not in st.session_state:
    st.session_state["active_tab"] = "moods"
    
if "dark_mode" not in st.session_state:
    st.session_state["dark_mode"] = False

# load theme colors based on dark mode toggle
if st.session_state["dark_mode"] == True:
    theme = dict(
        bg="#0F0B1A", surface="#1A1428", surface_glass="#1A1428B3",
        surface2="#221A36", surface3="#2E2248",
        lavender="#2A2040", lavender_glass="#2A2040CC", 
        lavender_mid="#443468", lavender_deep="#C4A8FF",
        lilac="#1A1428", lilac_glass="#1A1428CC", lilac_mid="#352860",
        border="rgba(196,168,255,0.12)", border_mid="rgba(196,168,255,0.25)",
        text="#F0EAFF", text2="#C0AEED", text3="#8878B0",
        text_on_accent="#0F0B1A", accent="#C4A8FF", step_label="#C4A8FF",
        badge_bw_bg="#3D2E00", badge_bw_fg="#FFD966",
        badge_hw_bg="#002B44", badge_hw_fg="#7ED4FF",
        shadow_soft="0 4px 24px rgba(0,0,0,0.40)",
        shadow_hover="0 16px 56px rgba(0,0,0,0.65)",
        dot_color="rgba(196,168,255,0.07)", scheme="dark",
    )
else:
    theme = dict(
        bg="#FBF8FF", surface="#FFFFFF", surface_glass="#FFFFFFB3",
        surface2="#F5F0FF", surface3="#EDE6FF",
        lavender="#E8E0F7", lavender_glass="#E8E0F7CC",
        lavender_mid="#C9B8EF", lavender_deep="#9B7ED4",
        lilac="#F0E6FF", lilac_glass="#F0E6FFCC", lilac_mid="#D4B8FF",
        border="rgba(155,126,212,0.15)", border_mid="rgba(155,126,212,0.30)",
        text="#3D2F5A", text2="#6B5A8A", text3="#9C88BF",
        text_on_accent="#FFFFFF", accent="#9B7ED4", step_label="#9B7ED4",
        badge_bw_bg="#FFF3CC", badge_bw_fg="#7A5800",
        badge_hw_bg="#D6EEFF", badge_hw_fg="#1A5F8A",
        shadow_soft="0 4px 24px rgba(155,126,212,0.12)",
        shadow_hover="0 16px 56px rgba(155,126,212,0.28)",
        dot_color="rgba(155,126,212,0.12)", scheme="light",
    )

# background animation
st.markdown("""
<div class="ambient-bg">
    <div class="note" style="left: 10%; animation-duration: 15s; animation-delay: 0s; font-size: 1.5rem;">♪</div>
    <div class="note" style="left: 25%; animation-duration: 25s; animation-delay: -5s; font-size: 2.5rem;">♫</div>
    <div class="note" style="left: 40%; animation-duration: 20s; animation-delay: -12s; font-size: 1.8rem;">♬</div>
    <div class="note" style="left: 60%; animation-duration: 18s; animation-delay: -3s; font-size: 2.2rem;">♪</div>
    <div class="note" style="left: 75%; animation-duration: 28s; animation-delay: -18s; font-size: 1.2rem;">♫</div>
    <div class="note" style="left: 90%; animation-duration: 22s; animation-delay: -8s; font-size: 2.0rem;">♬</div>
    <div class="note" style="left: 15%; animation-duration: 19s; animation-delay: -15s; font-size: 1.6rem;">♪</div>
    <div class="note" style="left: 85%; animation-duration: 26s; animation-delay: -7s; font-size: 2.8rem;">♫</div>
</div>
""", unsafe_allow_html=True)

# custom styles using our theme dictionary
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,300;0,400;0,600;1,300;1,400&family=DM+Sans:wght@300;400;500;600&family=Space+Mono:wght@400;700&display=swap');

:root, [data-theme="light"], [data-theme="dark"] {{
  color-scheme: {theme['scheme']};
  --background-color:           {theme['bg']};
  --secondary-background-color: {theme['surface2']};
  --text-color:                 {theme['text']};
}}

*, *::before, *::after {{ box-sizing: border-box; }}

.ambient-bg {{
  position: fixed; inset: 0; pointer-events: none; z-index: 0; overflow: hidden;
  background: radial-gradient(circle at 15% 50%, {theme['dot_color']}, transparent 50%),
              radial-gradient(circle at 85% 30%, {theme['border_mid']}, transparent 50%);
}}
.note {{
  position: absolute; bottom: -10%; color: {theme['text']}; opacity: 0;
  animation: rise linear infinite; pointer-events: none;
}}
@keyframes rise {{
  0%   {{ transform: translateY(0) rotate(-15deg) scale(0.8); opacity: 0; }}
  15%  {{ opacity: 0.12; }}
  85%  {{ opacity: 0.12; }}
  100% {{ transform: translateY(-110vh) rotate(25deg) scale(1.2); opacity: 0; }}
}}

html, body,
[data-testid="stAppViewContainer"],
[data-testid="block-container"] {{
  background: {theme['bg']} !important;
  background-color: {theme['bg']} !important;
  color: {theme['text']} !important;
  font-family: 'DM Sans', sans-serif !important;
}}

[data-testid="stMain"] {{
  background: transparent !important;
  position: relative;
  z-index: 10;
}}

#MainMenu, footer, header,
[data-testid="stDecoration"],
[data-testid="stToolbar"] {{ visibility:hidden; display:none; }}

p, li, span, div, label {{
  font-family:'DM Sans',sans-serif !important;
  color:{theme['text']} !important;
}}
h1,h2,h3 {{ font-family:'Fraunces',serif !important; color:{theme['text']} !important; }}

[data-testid="stSidebar"] {{
  background: linear-gradient(180deg,{theme['lavender_glass']} 0%,{theme['lilac_glass']} 100%) !important;
  backdrop-filter: blur(16px) !important;
  -webkit-backdrop-filter: blur(16px) !important;
  border-right: 1px solid {theme['border_mid']} !important;
  z-index: 100;
}}
[data-testid="stSidebar"] * {{
  color:{theme['text2']} !important; font-family:'DM Sans',sans-serif !important;
}}
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {{
  color:{theme['lavender_deep']} !important; font-family:'Fraunces',serif !important;
}}
[data-testid="stSidebar"] hr {{ border-color:{theme['border_mid']} !important; }}

[data-testid="stSelectbox"] > div > div {{
  background:{theme['surface_glass']} !important;
  backdrop-filter: blur(8px) !important;
  -webkit-backdrop-filter: blur(8px) !important;
  border: 1.5px solid {theme['border_mid']} !important;
  border-radius:14px !important;
  color:{theme['text']} !important;
}}

[data-testid="stRadio"] > div {{
  display:flex !important; gap:0 !important;
  background:rgba(255,255,255,0.02) !important;
  backdrop-filter: blur(8px) !important;
  -webkit-backdrop-filter: blur(8px) !important;
  border: 1.5px solid {theme['border_mid']} !important;
  border-radius:50px !important; padding:4px !important; width:fit-content;
}}
[data-testid="stRadio"] > div > label {{
  font-family:'DM Sans',sans-serif !important;
  font-size:0.92rem !important; font-weight:500 !important;
  color:{theme['text2']} !important;
  padding:8px 28px !important; border-radius:50px !important;
  cursor:pointer !important; transition:all 0.25s ease !important;
  letter-spacing:0 !important; text-transform:none !important;
}}
[data-testid="stRadio"] > div > label:has(input:checked) {{
  background:{theme['lavender_deep']} !important;
  color:{theme['text_on_accent']} !important;
  box-shadow:0 4px 14px {theme['border_mid']} !important;
}}
[data-testid="stRadio"] input[type="radio"] {{ display:none !important; }}

[data-testid="stHorizontalBlock"] > div {{
  background:{theme['surface_glass']} !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  border: 1.5px solid {theme['border']} !important;
  border-radius:22px !important; padding:0 !important; overflow:hidden !important;
  transition:transform 0.3s cubic-bezier(0.34,1.56,0.64,1), box-shadow 0.3s ease !important;
  box-shadow:{theme['shadow_soft']} !important;
}}
[data-testid="stHorizontalBlock"] > div:hover {{
  transform:translateY(-6px) scale(1.02) !important;
  box-shadow:{theme['shadow_hover']} !important;
}}

[data-testid="stExpander"] {{
  background:{theme['lilac_glass']} !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  border: 1.5px solid {theme['lavender_mid']} !important;
  border-radius:18px !important; overflow:hidden !important;
}}
[data-testid="stExpander"] summary {{
  font-family:'DM Sans',sans-serif !important; font-size:0.92rem !important;
  font-weight:600 !important; color:{theme['lavender_deep']} !important;
  padding:14px 20px !important; background:transparent !important;
}}
[data-testid="stExpander"] > div > div {{ background:transparent !important; }}

.stButton > button {{
  font-family:'DM Sans',sans-serif !important; font-weight:600 !important;
  font-size:0.82rem !important; border-radius:50px !important;
  padding:0.45rem 1rem !important; width:100% !important;
  border: 2px solid {theme['lavender_deep']} !important;
  background:rgba(255,255,255,0.05) !important; color:{theme['lavender_deep']} !important;
  transition:all 0.2s ease !important;
}}
.stButton > button:hover {{
  background:{theme['lavender_deep']} !important;
  color:{theme['text_on_accent']} !important;
  transform:translateY(-2px) !important;
  box-shadow:{theme['shadow_soft']} !important;
}}

hr {{ border-color:{theme['border_mid']} !important; }}
::-webkit-scrollbar {{ width:5px; }}
::-webkit-scrollbar-track {{ background:{theme['surface2']}; }}
::-webkit-scrollbar-thumb {{ background:{theme['lavender_mid']}; border-radius:5px; }}

@keyframes moodpulse {{
  0%   {{ box-shadow:0 0 0 0 {theme['border_mid']}; }}
  70%  {{ box-shadow:0 0 0 10px transparent; }}
  100% {{ box-shadow:0 0 0 0 transparent; }}
}}
@keyframes floatNote {{
  0%,100% {{ transform:translateY(0) rotate(-3deg); }}
  50%     {{ transform:translateY(-8px) rotate(3deg); }}
}}

[data-testid="stButton"] > [data-testid="stWidgetLabel"],
[data-testid="stButton"] > div > [data-testid="stWidgetLabel"] {{
  display:none !important;
}}
[data-testid="stSidebar"] [data-testid="stWidgetLabel"] {{
  display:none !important;
}}
</style>
""", unsafe_allow_html=True)

# songs and moods database
MOOD_DATA = {
    "😊 Happy": {
        "tagline": "Sunshine in every beat",
        "songs": {
            "Bollywood": {
                "top": [
                    {"name":"Badtameez Dil",      "artist":"Pritam",             "film":"Yeh Jawaani Hai Deewani","emoji":"🌈","url":"https://www.youtube.com/watch?v=II2EO3Nw4m0"},
                    {"name":"Gallan Goodiyaan",    "artist":"Shankar-Ehsaan-Loy", "film":"Dil Dhadakne Do",        "emoji":"🎉","url":"https://www.youtube.com/watch?v=9fxfKaTOAV0"},
                    {"name":"London Thumakda",     "artist":"Labh Janjua",        "film":"Queen",                  "emoji":"💃","url":"https://www.youtube.com/watch?v=gadgFdl8OBI"},
                ],
                "extra": [
                    {"name":"Balam Pichkari",      "artist":"Vishal-Shekhar",     "film":"Yeh Jawaani Hai Deewani","emoji":"🎨","url":"https://www.youtube.com/watch?v=qFkNATtJCrk"},
                    {"name":"Ainvayi Ainvayi",     "artist":"Salim-Sulaiman",     "film":"Band Baaja Baaraat",     "emoji":"🌻","url":"https://www.youtube.com/watch?v=RCqousFnRhk"},
                    {"name":"Nagada Sang Dhol",    "artist":"Shreya Ghoshal",     "film":"Goliyon Ki Raasleela",   "emoji":"🪘","url":"https://www.youtube.com/watch?v=FejuD_EHpig"},
                    {"name":"Aankhon Mein Teri",   "artist":"KK",                 "film":"Om Shanti Om",           "emoji":"✨","url":"https://www.youtube.com/watch?v=nQDxjNEX84Q"},
                ],
            },
            "Hollywood": {
                "top": [
                    {"name":"Happy",               "artist":"Pharrell Williams",  "film":"Despicable Me 2 OST",    "emoji":"☀️","url":"https://www.youtube.com/watch?v=ZbZSe6N_BXs"},
                    {"name":"Can't Stop the Feeling","artist":"Justin Timberlake","film":"Trolls OST",             "emoji":"✨","url":"https://www.youtube.com/watch?v=ru0K8uYEZWw"},
                    {"name":"Walking on Sunshine",  "artist":"Katrina & The Waves","film":"Walking on Sunshine",   "emoji":"🌞","url":"https://www.youtube.com/watch?v=iPUmE-tne5U"},
                ],
                "extra": [
                    {"name":"Good as Hell",         "artist":"Lizzo",             "film":"Coconut Oil (EP)",        "emoji":"💪","url":"https://www.youtube.com/watch?v=SmbmeOgWsqE"},
                    {"name":"I Gotta Feeling",      "artist":"Black Eyed Peas",   "film":"The E.N.D.",             "emoji":"🍾","url":"https://www.youtube.com/watch?v=uSD4vsh1zDA"},
                    {"name":"Shake It Off",         "artist":"Taylor Swift",      "film":"1989 (Album)",           "emoji":"🎀","url":"https://www.youtube.com/watch?v=nfWlot6h_JM"},
                    {"name":"Roar",                 "artist":"Katy Perry",        "film":"PRISM (Album)",          "emoji":"🦁","url":"https://www.youtube.com/watch?v=CevxZvSJLk8"},
                ],
            },
        },
    },
    "😢 Sad": {
        "tagline": "Let the tears flow freely",
        "songs": {
            "Bollywood": {
                "top": [
                    {"name":"Tum Hi Ho",            "artist":"Arijit Singh",       "film":"Aashiqui 2",             "emoji":"💧","url":"https://www.youtube.com/watch?v=Umqb9KENgmk"},
                    {"name":"Channa Mereya",        "artist":"Arijit Singh",       "film":"Ae Dil Hai Mushkil",     "emoji":"🌧️","url":"https://www.youtube.com/watch?v=284Ov7ysmfA"},
                    {"name":"Kal Ho Na Ho",         "artist":"Sonu Nigam",         "film":"Kal Ho Na Ho",           "emoji":"🥀","url":"https://www.youtube.com/watch?v=bFMJszkMFkI"},
                ],
                "extra": [
                    {"name":"Dil Diyan Gallan",     "artist":"Atif Aslam",         "film":"Tiger Zinda Hai",        "emoji":"💙","url":"https://www.youtube.com/watch?v=1UqQSE8Ek2Y"},
                    {"name":"Khairiyat",            "artist":"Arijit Singh",       "film":"Chhichhore",             "emoji":"🌿","url":"https://www.youtube.com/watch?v=t6dxJSxCCso"},
                    {"name":"Hamari Adhuri Kahani", "artist":"Arijit Singh",       "film":"Hamari Adhuri Kahani",   "emoji":"📖","url":"https://www.youtube.com/watch?v=fxVEXoAjFu8"},
                    {"name":"Phir Le Aya Dil",      "artist":"Arijit Singh",       "film":"Barfi!",                 "emoji":"🌊","url":"https://www.youtube.com/watch?v=PqFpIf0RBXY"},
                ],
            },
            "Hollywood": {
                "top": [
                    {"name":"Someone Like You",     "artist":"Adele",              "film":"21 (Album)",             "emoji":"🌊","url":"https://www.youtube.com/watch?v=hLQl3WQQoQ0"},
                    {"name":"Fix You",              "artist":"Coldplay",           "film":"X&Y (Album)",            "emoji":"🕯️","url":"https://www.youtube.com/watch?v=k4V3Mo61fJM"},
                    {"name":"The Night We Met",     "artist":"Lord Huron",         "film":"Strange Trails",         "emoji":"🌙","url":"https://www.youtube.com/watch?v=KtlgYxa6BMU"},
                ],
                "extra": [
                    {"name":"Skinny Love",          "artist":"Bon Iver",           "film":"For Emma, Forever Ago",  "emoji":"🍂","url":"https://www.youtube.com/watch?v=sldE7HgxSsI"},
                    {"name":"Liability",            "artist":"Lorde",              "film":"Melodrama",              "emoji":"🪞","url":"https://www.youtube.com/watch?v=UjKyA-kKHAs"},
                    {"name":"Happier",              "artist":"Olivia Rodrigo",     "film":"SOUR",                   "emoji":"🌧","url":"https://www.youtube.com/watch?v=8tlBxWNp68E"},
                    {"name":"All I Want",           "artist":"Kodaline",           "film":"In a Perfect World",     "emoji":"💔","url":"https://www.youtube.com/watch?v=YoRCEAteKLM"},
                ],
            },
        },
    },
    "💕 Romantic": {
        "tagline": "Love floating in the air",
        "songs": {
            "Bollywood": {
                "top": [
                    {"name":"Tujh Mein Rab Dikhta Hai","artist":"Roop Kumar Rathod","film":"Rab Ne Bana Di Jodi",  "emoji":"💞","url":"https://www.youtube.com/watch?v=V-LMbCbDwMM"},
                    {"name":"Gerua",                "artist":"Arijit Singh",       "film":"Dilwale",                "emoji":"🌹","url":"https://www.youtube.com/watch?v=AEIVhBS6baE"},
                    {"name":"Tere Sang Yaara",      "artist":"Atif Aslam",         "film":"Rustom",                 "emoji":"🌙","url":"https://www.youtube.com/watch?v=MqAGl6r6RNI"},
                ],
                "extra": [
                    {"name":"Pehla Nasha",          "artist":"Udit Narayan",       "film":"Jo Jeeta Wohi Sikandar", "emoji":"🦋","url":"https://www.youtube.com/watch?v=k8nIFpkUMFI"},
                    {"name":"Raabta",               "artist":"Arijit Singh",       "film":"Agent Sai Srinivasa",    "emoji":"🤍","url":"https://www.youtube.com/watch?v=Y0rNVjJasug"},
                    {"name":"Ae Dil Hai Mushkil",   "artist":"Arijit Singh",       "film":"Ae Dil Hai Mushkil",     "emoji":"💔","url":"https://www.youtube.com/watch?v=6FURuLYrR_Q"},
                    {"name":"Lag Ja Gale",          "artist":"Lata Mangeshkar",    "film":"Woh Kaun Thi",           "emoji":"🌸","url":"https://www.youtube.com/watch?v=k7yXUFmLVkk"},
                ],
            },
            "Hollywood": {
                "top": [
                    {"name":"Perfect",              "artist":"Ed Sheeran",         "film":"Divide (Album)",         "emoji":"💎","url":"https://www.youtube.com/watch?v=2Vv-BfVoq4g"},
                    {"name":"All of Me",            "artist":"John Legend",        "film":"Love in the Future",     "emoji":"💓","url":"https://www.youtube.com/watch?v=450p7goxZqg"},
                    {"name":"A Thousand Years",     "artist":"Christina Perri",    "film":"Twilight: Breaking Dawn","emoji":"⏳","url":"https://www.youtube.com/watch?v=rtOvBOTyX00"},
                ],
                "extra": [
                    {"name":"Can't Help Falling in Love","artist":"Elvis Presley","film":"Blue Hawaii",            "emoji":"🌺","url":"https://www.youtube.com/watch?v=vGJTaP6anOU"},
                    {"name":"Make You Feel My Love","artist":"Adele",              "film":"19 (Album)",             "emoji":"🎻","url":"https://www.youtube.com/watch?v=0put0_a--Ng"},
                    {"name":"Lover",                "artist":"Taylor Swift",       "film":"Lover (Album)",          "emoji":"🌈","url":"https://www.youtube.com/watch?v=b8KkRxsqcmY"},
                    {"name":"The Way You Look Tonight","artist":"Frank Sinatra",   "film":"A Swingin' Affair",      "emoji":"🥂","url":"https://www.youtube.com/watch?v=Bfoe4EJA0YY"},
                ],
            },
        },
    },
    "🧊 Chill": {
        "tagline": "Slow down & breathe easy",
        "songs": {
            "Bollywood": {
                "top": [
                    {"name":"Kabira",               "artist":"Rekha Bhardwaj",     "film":"Yeh Jawaani Hai Deewani","emoji":"🌿","url":"https://www.youtube.com/watch?v=5TBDWuMGFpg"},
                    {"name":"Lut Gaye",             "artist":"Jubin Nautiyal",     "film":"Single",                 "emoji":"🍃","url":"https://www.youtube.com/watch?v=nBKNFNumu5Y"},
                    {"name":"O Re Piya",            "artist":"Rahat Fateh Ali Khan","film":"Aaja Nachle",           "emoji":"🌺","url":"https://www.youtube.com/watch?v=PIc3M3h9BJI"},
                ],
                "extra": [
                    {"name":"Agar Tum Saath Ho",    "artist":"Arijit Singh",       "film":"Tamasha",                "emoji":"🌾","url":"https://www.youtube.com/watch?v=sLDyO6SBFQM"},
                    {"name":"Mann Mera",            "artist":"Gajendra Verma",     "film":"Table No 21",            "emoji":"☁️","url":"https://www.youtube.com/watch?v=c3vqX1LyBdI"},
                    {"name":"Ilahi",                "artist":"Mohit Chauhan",      "film":"Yeh Jawaani Hai Deewani","emoji":"🌠","url":"https://www.youtube.com/watch?v=oTKFvMzcLoM"},
                    {"name":"Sooha Saaha",          "artist":"Nooran Sisters",     "film":"Highway",                "emoji":"🏔️","url":"https://www.youtube.com/watch?v=Fxq5y1PYB1w"},
                ],
            },
            "Hollywood": {
                "top": [
                    {"name":"Holocene",             "artist":"Bon Iver",           "film":"Bon Iver (Album)",       "emoji":"🏔️","url":"https://www.youtube.com/watch?v=TWcyIpul8OE"},
                    {"name":"Weightless",           "artist":"Marconi Union",      "film":"Weightless (Single)",    "emoji":"☁️","url":"https://www.youtube.com/watch?v=UfcAVejslrU"},
                    {"name":"Let Her Go",           "artist":"Passenger",          "film":"All the Little Lights",  "emoji":"🍂","url":"https://www.youtube.com/watch?v=RBumgq5yVrA"},
                ],
                "extra": [
                    {"name":"Breathe (2 AM)",       "artist":"Anna Nalick",        "film":"Wreck of the Day",       "emoji":"🌙","url":"https://www.youtube.com/watch?v=FlsBObg-1BQ"},
                    {"name":"Skinny Love",          "artist":"Birdy",              "film":"Birdy (Album)",          "emoji":"🌱","url":"https://www.youtube.com/watch?v=oNbKCpKFkEg"},
                    {"name":"Banana Pancakes",      "artist":"Jack Johnson",       "film":"In Between Dreams",      "emoji":"🌅","url":"https://www.youtube.com/watch?v=OzRRSGTT5OA"},
                    {"name":"Sunset Lover",         "artist":"Petit Biscuit",      "film":"Presence (Album)",       "emoji":"🌇","url":"https://www.youtube.com/watch?v=Nln-oCn3-Bc"},
                ],
            },
        },
    },
    "🎉 Party": {
        "tagline": "Turn the speakers all the way up",
        "songs": {
            "Bollywood": {
                "top": [
                    {"name":"Abhi Toh Party Shuru Hui Hai","artist":"Akriti Kakar","film":"Khoobsurat",            "emoji":"🍾","url":"https://www.youtube.com/watch?v=b4IgCpbKRbA"},
                    {"name":"Subha Hone Na De",     "artist":"Mika Singh",         "film":"Desi Boyz",              "emoji":"🌙","url":"https://www.youtube.com/watch?v=Z4k20e-mIGo"},
                    {"name":"Tattad Tattad",        "artist":"Arijit Singh",       "film":"Goliyon Ki Raasleela",   "emoji":"💫","url":"https://www.youtube.com/watch?v=iDBnCEWABYo"},
                ],
                "extra": [
                    {"name":"Desi Beat",            "artist":"Yo Yo Honey Singh",  "film":"Bodyguard",              "emoji":"🔊","url":"https://www.youtube.com/watch?v=WpHCK7alSRY"},
                    {"name":"Char Baj Gaye",        "artist":"Badshah",            "film":"Single",                 "emoji":"🥳","url":"https://www.youtube.com/watch?v=_WsqIWdXjB4"},
                    {"name":"Ghungroo",             "artist":"Arijit Singh",       "film":"War",                    "emoji":"🔔","url":"https://www.youtube.com/watch?v=qFkNATtJCrk"},
                    {"name":"Cutiepie",             "artist":"Ankit Tiwari",       "film":"Ae Dil Hai Mushkil",     "emoji":"🎊","url":"https://www.youtube.com/watch?v=GZdivaTlTmk"},
                ],
            },
            "Hollywood": {
                "top": [
                    {"name":"Blinding Lights",      "artist":"The Weeknd",         "film":"After Hours (Album)",    "emoji":"🌆","url":"https://www.youtube.com/watch?v=4NRXx6U8ABQ"},
                    {"name":"Levitating",           "artist":"Dua Lipa",           "film":"Future Nostalgia",       "emoji":"🚀","url":"https://www.youtube.com/watch?v=TUVcZfQe-Kw"},
                    {"name":"Don't Start Now",      "artist":"Dua Lipa",           "film":"Future Nostalgia",       "emoji":"⚡","url":"https://www.youtube.com/watch?v=oygrmJFKYZY"},
                ],
                "extra": [
                    {"name":"Save Your Tears",      "artist":"The Weeknd",         "film":"After Hours",            "emoji":"😢","url":"https://www.youtube.com/watch?v=LIIDh-qI9oI"},
                    {"name":"As It Was",            "artist":"Harry Styles",       "film":"Harry's House",          "emoji":"🌀","url":"https://www.youtube.com/watch?v=H5v3kku4y6Q"},
                    {"name":"Cruel Summer",         "artist":"Taylor Swift",       "film":"Lover (Album)",          "emoji":"☀️","url":"https://www.youtube.com/watch?v=ic8j13piAhQ"},
                    {"name":"STAY",                 "artist":"Kid LAROI & Bieber", "film":"F*CK LOVE 3",            "emoji":"🌊","url":"https://www.youtube.com/watch?v=bT7bGKHJFxQ"},
                ],
            },
        },
    },
    "💪 Workout": {
        "tagline": "Push harder, go further",
        "songs": {
            "Bollywood": {
                "top": [
                    {"name":"Zinda",                "artist":"Siddharth Mahadevan","film":"Bhaag Milkha Bhaag",     "emoji":"🔥","url":"https://www.youtube.com/watch?v=3UyFRMJnxZc"},
                    {"name":"Kar Har Maidaan Fateh","artist":"Sukhwinder Singh",   "film":"Sanju",                  "emoji":"⚡","url":"https://www.youtube.com/watch?v=4mONADMBRqA"},
                    {"name":"Dhoom Machale",        "artist":"Sunidhi Chauhan",    "film":"Dhoom",                  "emoji":"🏍️","url":"https://www.youtube.com/watch?v=1IpBmkJRsXA"},
                ],
                "extra": [
                    {"name":"Sultan",               "artist":"Sukhwinder Singh",   "film":"Sultan",                 "emoji":"🥋","url":"https://www.youtube.com/watch?v=2TtaULqRWKk"},
                    {"name":"War Title Track",      "artist":"Vishal-Shekhar",     "film":"War",                    "emoji":"⚔️","url":"https://www.youtube.com/watch?v=kAEPKCKcfA8"},
                    {"name":"Chak De India",        "artist":"Sukhwinder Singh",   "film":"Chak De! India",         "emoji":"🏑","url":"https://www.youtube.com/watch?v=lXCMfLqd4PM"},
                    {"name":"Dangal",               "artist":"Daler Mehndi",       "film":"Dangal",                 "emoji":"🥊","url":"https://www.youtube.com/watch?v=IZ-OoMVkDE4"},
                ],
            },
            "Hollywood": {
                "top": [
                    {"name":"Eye of the Tiger",     "artist":"Survivor",           "film":"Rocky III OST",          "emoji":"🥊","url":"https://www.youtube.com/watch?v=btPJPFnesV4"},
                    {"name":"Lose Yourself",        "artist":"Eminem",             "film":"8 Mile OST",             "emoji":"🎤","url":"https://www.youtube.com/watch?v=_Yhyp-_hX2s"},
                    {"name":"Thunderstruck",        "artist":"AC/DC",              "film":"The Razor's Edge",       "emoji":"🎸","url":"https://www.youtube.com/watch?v=v2AC41dglnM"},
                ],
                "extra": [
                    {"name":"Believer",             "artist":"Imagine Dragons",    "film":"Evolve (Album)",         "emoji":"💥","url":"https://www.youtube.com/watch?v=7wtfhZwyrcc"},
                    {"name":"Till I Collapse",      "artist":"Eminem",             "film":"The Eminem Show",        "emoji":"🏋️","url":"https://www.youtube.com/watch?v=ytQ5ApkBMbA"},
                    {"name":"Can't Hold Us",        "artist":"Macklemore",         "film":"The Heist",              "emoji":"🚩","url":"https://www.youtube.com/watch?v=2zNSgSzhBfM"},
                    {"name":"Stronger",             "artist":"Kanye West",         "film":"Graduation",             "emoji":"⚙️","url":"https://www.youtube.com/watch?v=PsO6ZnUZI0g"},
                ],
            },
        },
    },
    "🧠 Focus": {
        "tagline": "Enter deep flow state",
        "songs": {
            "Bollywood": {
                "top": [
                    {"name":"Kun Faya Kun",         "artist":"A.R. Rahman",        "film":"Rockstar",               "emoji":"🕌","url":"https://www.youtube.com/watch?v=T94PHkuydcw"},
                    {"name":"Khwaja Mere Khwaja",   "artist":"A.R. Rahman",        "film":"Jodhaa Akbar",           "emoji":"🌌","url":"https://www.youtube.com/watch?v=DHUQZV8jqmo"},
                    {"name":"Breathless",           "artist":"Shankar Mahadevan",  "film":"Single",                 "emoji":"🎵","url":"https://www.youtube.com/watch?v=DlGNZH5_pEE"},
                ],
                "extra": [
                    {"name":"Sadda Haq",            "artist":"Mohit Chauhan",      "film":"Rockstar",               "emoji":"✊","url":"https://www.youtube.com/watch?v=z8rMmB3EZx4"},
                    {"name":"Maa",                  "artist":"A.R. Rahman",        "film":"Taare Zameen Par",       "emoji":"🌙","url":"https://www.youtube.com/watch?v=CUBwFvBFsrI"},
                    {"name":"Roja Theme",           "artist":"A.R. Rahman",        "film":"Roja",                   "emoji":"🎹","url":"https://www.youtube.com/watch?v=i1l1I8SBQ08"},
                ],
            },
            "Hollywood": {
                "top": [
                    {"name":"Time (Inception OST)", "artist":"Hans Zimmer",        "film":"Inception OST",          "emoji":"⏱️","url":"https://www.youtube.com/watch?v=RxabLA7UQ9k"},
                    {"name":"Experience",           "artist":"Ludovico Einaudi",   "film":"In a Time Lapse",        "emoji":"🎹","url":"https://www.youtube.com/watch?v=hN_q-_jMQQk"},
                    {"name":"Interstellar Theme",   "artist":"Hans Zimmer",        "film":"Interstellar OST",       "emoji":"🚀","url":"https://www.youtube.com/watch?v=UDVtMYqUAyw"},
                ],
                "extra": [
                    {"name":"Nuvole Bianche",       "artist":"Ludovico Einaudi",   "film":"Una Mattina",            "emoji":"☁️","url":"https://www.youtube.com/watch?v=rnMIh0i9Z-Y"},
                    {"name":"Comptine d'un autre été","artist":"Yann Tiersen",     "film":"Amélie OST",             "emoji":"🎡","url":"https://www.youtube.com/watch?v=jXfrBHOjbHU"},
                    {"name":"On the Nature of Daylight","artist":"Max Richter",    "film":"The Blue Notebooks",     "emoji":"🌅","url":"https://www.youtube.com/watch?v=b_YHE4Sx-08"},
                ],
            },
        },
    },
    "🕰️ Nostalgic": {
        "tagline": "Memories wrapped in melody",
        "songs": {
            "Bollywood": {
                "top": [
                    {"name":"Yeh Dosti",            "artist":"Kishore Kumar",      "film":"Sholay",                 "emoji":"🤝","url":"https://www.youtube.com/watch?v=ql-5EpMIDgA"},
                    {"name":"Purani Jeans",         "artist":"Ali Haider",         "film":"Single",                 "emoji":"👖","url":"https://www.youtube.com/watch?v=9jGiRuMiMcw"},
                    {"name":"Ik Vaari Aa",          "artist":"Arijit Singh",       "film":"Raabta",                 "emoji":"📼","url":"https://www.youtube.com/watch?v=72KZBow8gFo"},
                ],
                "extra": [
                    {"name":"Kabhi Kabhi Mere Dil Mein","artist":"Mukesh",         "film":"Kabhi Kabhi",            "emoji":"📻","url":"https://www.youtube.com/watch?v=5RD7A9j5gPw"},
                    {"name":"Ruk Ja O Dil Deewane", "artist":"Udit Narayan",       "film":"DDLJ",                   "emoji":"🚂","url":"https://www.youtube.com/watch?v=4UE7fM0FX-A"},
                    {"name":"Zindagi Na Milegi Dobara","artist":"Shankar-Ehsaan-Loy","film":"ZNMD",                 "emoji":"🌊","url":"https://www.youtube.com/watch?v=JmkpHRgkWdQ"},
                    {"name":"Ae Mere Humsafar",     "artist":"Alisha Chinai",      "film":"Qayamat Se Qayamat Tak", "emoji":"💌","url":"https://www.youtube.com/watch?v=g7MnlInE6KM"},
                ],
            },
            "Hollywood": {
                "top": [
                    {"name":"Bohemian Rhapsody",    "artist":"Queen",              "film":"A Night at the Opera",   "emoji":"🎸","url":"https://www.youtube.com/watch?v=fJ9rUzIMcZQ"},
                    {"name":"Hotel California",     "artist":"Eagles",             "film":"Hotel California (Album)","emoji":"🌴","url":"https://www.youtube.com/watch?v=BciS5krYL80"},
                    {"name":"Sweet Child O' Mine",  "artist":"Guns N' Roses",      "film":"Appetite for Destruction","emoji":"🎵","url":"https://www.youtube.com/watch?v=1w7OgIMMRc4"},
                ],
                "extra": [
                    {"name":"Don't Stop Believin'", "artist":"Journey",            "film":"Escape",                 "emoji":"🌃","url":"https://www.youtube.com/watch?v=VcjzHMhBtf0"},
                    {"name":"Africa",               "artist":"Toto",               "film":"Toto IV",                "emoji":"🌍","url":"https://www.youtube.com/watch?v=FTQbiNvZqaY"},
                    {"name":"Comfortably Numb",     "artist":"Pink Floyd",         "film":"The Wall",               "emoji":"🧱","url":"https://www.youtube.com/watch?v=_FrOQC-zEog"},
                    {"name":"Yesterday",            "artist":"The Beatles",        "film":"Help! (Soundtrack)",     "emoji":"🌻","url":"https://www.youtube.com/watch?v=NrgmdOz227I"},
                ],
            },
        },
    },
    "🔥 Hype": {
        "tagline": "Maximum energy — zero limits",
        "songs": {
            "Bollywood": {
                "top": [
                    {"name":"Senorita",             "artist":"Vishal-Shekhar",     "film":"Zindagi Na Milegi Dobara","emoji":"🌊","url":"https://www.youtube.com/watch?v=zf4bLQqHMKM"},
                    {"name":"Garmi",                "artist":"Badshah & Neha Kakkar","film":"Street Dancer 3D",    "emoji":"🌡️","url":"https://www.youtube.com/watch?v=IHI0CQTGHVY"},
                    {"name":"Munni Badnaam",        "artist":"Mamta Sharma",       "film":"Dabangg",                "emoji":"💃","url":"https://www.youtube.com/watch?v=V7W5ZCWXBBY"},
                ],
                "extra": [
                    {"name":"Lovely",               "artist":"Kanika Kapoor",      "film":"Happy New Year",         "emoji":"✨","url":"https://www.youtube.com/watch?v=X0s3BSbsXH4"},
                    {"name":"Illegal Weapon 2.0",   "artist":"Garry Sandhu",       "film":"Street Dancer 3D",       "emoji":"⚡","url":"https://www.youtube.com/watch?v=6_bVXbLHbOk"},
                    {"name":"Tattoo",               "artist":"Badshah",            "film":"Single",                 "emoji":"🎯","url":"https://www.youtube.com/watch?v=M0GHxuSEbKw"},
                    {"name":"Kala Chashma",         "artist":"Baar Baar Dekho",    "film":"Baar Baar Dekho",        "emoji":"🕶️","url":"https://www.youtube.com/watch?v=nEDeQJgOCKY"},
                ],
            },
            "Hollywood": {
                "top": [
                    {"name":"HUMBLE.",              "artist":"Kendrick Lamar",     "film":"DAMN.",                  "emoji":"👑","url":"https://www.youtube.com/watch?v=tvTRZJ-4EyI"},
                    {"name":"SICKO MODE",           "artist":"Travis Scott",       "film":"Astroworld",             "emoji":"🌙","url":"https://www.youtube.com/watch?v=6ONRf7h3Mdk"},
                    {"name":"Starboy",              "artist":"The Weeknd",         "film":"Starboy (Album)",        "emoji":"⭐","url":"https://www.youtube.com/watch?v=34Na4j8AVgA"},
                ],
                "extra": [
                    {"name":"God's Plan",           "artist":"Drake",              "film":"Scorpion",               "emoji":"🙏","url":"https://www.youtube.com/watch?v=xpVfcZ0ZcFM"},
                    {"name":"Rockstar",             "artist":"Post Malone",        "film":"Beerbongs & Bentleys",   "emoji":"🤘","url":"https://www.youtube.com/watch?v=UceaB4D0jpo"},
                    {"name":"Bad Guy",              "artist":"Billie Eilish",      "film":"When We All Fall Asleep","emoji":"😈","url":"https://www.youtube.com/watch?v=DyDfgMOUjCI"},
                    {"name":"Power",                "artist":"Kanye West",         "film":"My Beautiful Dark...",   "emoji":"⚡","url":"https://www.youtube.com/watch?v=L53gjP-TtGE"},
                ],
            },
        },
    },
}

MOOD_PALETTE = {
    "😊 Happy":     {"r":212,"g":160,"b":23,  "deep":"#D4A017"},
    "😢 Sad":       {"r":58, "g":155,"b":213, "deep":"#3A9BD5"},
    "💕 Romantic":  {"r":224,"g":96, "b":144, "deep":"#E06090"},
    "🧊 Chill":     {"r":77, "g":191,"b":160, "deep":"#4DBFA0"},
    "🎉 Party":     {"r":232,"g":132,"b":90,  "deep":"#E8845A"},
    "💪 Workout":   {"r":224,"g":96, "b":96,  "deep":"#E06060"},
    "🧠 Focus":     {"r":155,"g":126,"b":212, "deep":"#9B7ED4"},
    "🕰️ Nostalgic": {"r":139,"g":106,"b":196, "deep":"#8B6AC4"},
    "🔥 Hype":      {"r":212,"g":96, "b":10,  "deep":"#D4600A"},
}

GLOBAL_HITS = [
    {"name":"Billie Jean",             "artist":"Michael Jackson",   "film":"Thriller (Album)",        "genre":"Hollywood","emoji":"🕺","url":"https://www.youtube.com/watch?v=Zi_XLOBDo_Y"},
    {"name":"Shape of You",            "artist":"Ed Sheeran",        "film":"Divide (Album)",          "genre":"Hollywood","emoji":"💫","url":"https://www.youtube.com/watch?v=JGwWNGJdvx8"},
    {"name":"Tum Hi Ho",               "artist":"Arijit Singh",      "film":"Aashiqui 2",              "genre":"Bollywood","emoji":"🌟","url":"https://www.youtube.com/watch?v=Umqb9KENgmk"},
    {"name":"One More Time",           "artist":"Daft Punk",         "film":"Discovery (Album)",       "genre":"Hollywood","emoji":"🤖","url":"https://www.youtube.com/watch?v=FGBhQbmPwH8"},
    {"name":"Kal Ho Na Ho",            "artist":"Sonu Nigam",        "film":"Kal Ho Na Ho",            "genre":"Bollywood","emoji":"🌟","url":"https://www.youtube.com/watch?v=bFMJszkMFkI"},
    {"name":"Smells Like Teen Spirit", "artist":"Nirvana",           "film":"Nevermind (Album)",       "genre":"Hollywood","emoji":"⚡","url":"https://www.youtube.com/watch?v=hTWKbfoikeg"},
    {"name":"Gallan Goodiyaan",        "artist":"Shankar-Ehsaan-Loy","film":"Dil Dhadakne Do",         "genre":"Bollywood","emoji":"🎉","url":"https://www.youtube.com/watch?v=9fxfKaTOAV0"},
    {"name":"Rolling in the Deep",     "artist":"Adele",             "film":"21 (Album)",              "genre":"Hollywood","emoji":"🌊","url":"https://www.youtube.com/watch?v=rYEDA3JcQqw"},
    {"name":"Kar Har Maidaan Fateh",   "artist":"Sukhwinder Singh",  "film":"Sanju",                   "genre":"Bollywood","emoji":"⚡","url":"https://www.youtube.com/watch?v=4mONADMBRqA"},
    {"name":"Despacito",               "artist":"Luis Fonsi",        "film":"Vida (Album)",            "genre":"Hollywood","emoji":"🎸","url":"https://www.youtube.com/watch?v=kTJczUoc26U"},
    {"name":"Gerua",                   "artist":"Arijit Singh",      "film":"Dilwale",                 "genre":"Bollywood","emoji":"🌹","url":"https://www.youtube.com/watch?v=AEIVhBS6baE"},
    {"name":"Uptown Funk",             "artist":"Bruno Mars",        "film":"Mark Ronson ft. Bruno",   "genre":"Hollywood","emoji":"🎷","url":"https://www.youtube.com/watch?v=OPf0YbXqDm0"},
]

# toggle function for sidebar
def toggle_theme():
    if st.session_state["dark_mode"] == True:
        st.session_state["dark_mode"] = False
    else:
        st.session_state["dark_mode"] = True

# display sidebar
with st.sidebar:
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"""
        <div style="padding:8px 0 16px;">
          <p style="font-family:'Fraunces',serif;font-size:1.6rem;
             color:{theme['lavender_deep']};margin:0;line-height:1.1;">Moodify</p>
          <p style="font-family:'Space Mono',monospace;font-size:0.58rem;
             color:{theme['text3']};letter-spacing:0.12em;margin:4px 0 0;">
            MUSIC FOR EVERY MOOD · v1.0</p>
        </div>""", unsafe_allow_html=True)
        
    with col2:
        st.markdown("<div style='padding-top:14px'></div>", unsafe_allow_html=True)
        # checking icon to show based on theme
        if st.session_state["dark_mode"] == True:
            theme_icon = "☀️"
            theme_tooltip = "Light mode"
        else:
            theme_icon = "🌙"
            theme_tooltip = "Dark mode"
            
        st.button(theme_icon, help=theme_tooltip, key="dm_button", use_container_width=True, on_click=toggle_theme)

    st.divider()
    st.markdown("### 🎵 How to Use")
    st.markdown("""
1. Pick your **mood** from the dropdown
2. Choose **Bollywood** or **Hollywood**
3. Get **3 top tracks** instantly
4. Tap 🔽 **Discover More** for hidden gems
5. Check **Global Hits** tab for curated classics
6. Click **▶ Play** to open on YouTube
    """)
    st.divider()
    st.markdown("### 🎭 9 Moods")
    
    # list all moods from dictionary
    for m_label in MOOD_DATA:
        m_info = MOOD_DATA[m_label]
        st.markdown(
            f'<div style="padding:3px 0;">'
            f'<span style="font-size:0.88rem;color:{theme["text"]};">{m_label}</span>'
            f'<span style="font-family:\'Space Mono\',monospace;font-size:0.58rem;'
            f'color:{theme["lavender_deep"]};margin-left:8px;font-style:italic;">'
            f'{m_info["tagline"]}</span></div>',
            unsafe_allow_html=True,
        )
    st.divider()
    st.caption("Moodify · Let music find your mood 🎼")

# show main header
st.markdown(f"""
<div style="text-align:center;padding:2.5rem 0 0.5rem;position:relative;">
  <span style="position:absolute;top:10px;left:5%;font-size:1.6rem;
    animation:floatNote 4s ease-in-out infinite;opacity:0.55;">🎼</span>
  <span style="position:absolute;top:20px;right:5%;font-size:1.4rem;
    animation:floatNote 4s ease-in-out infinite 1s;opacity:0.55;">🎵</span>
  <span style="position:absolute;bottom:0;left:12%;font-size:1.2rem;
    animation:floatNote 4s ease-in-out infinite 0.5s;opacity:0.40;">🎶</span>
  <span style="position:absolute;bottom:0;right:12%;font-size:1.2rem;
    animation:floatNote 4s ease-in-out infinite 1.5s;opacity:0.40;">🎸</span>
  <div style="position:absolute;top:-20px;left:50%;transform:translateX(-50%);
    width:500px;height:140px;pointer-events:none;
    background:radial-gradient(ellipse,rgba(201,184,239,0.30) 0%,transparent 70%);"></div>
  <p style="font-family:'Space Mono',monospace;font-size:0.65rem;
     letter-spacing:0.25em;text-transform:uppercase;
     color:{theme['lavender_mid']};margin-bottom:10px;">
     🎼 ✨ Your personal music companion ✨ 🎼</p>
  <h1 style="font-family:'Fraunces',serif;font-size:3.6rem;font-weight:600;
     color:{theme['text']};line-height:1.0;margin-bottom:6px;letter-spacing:-0.02em;">
    <span style="font-style:italic;color:{theme['lavender_deep']};">Moodify</span>
  </h1>
  <p style="font-family:'DM Sans',sans-serif;color:{theme['text2']};
     font-size:1.0rem;margin:0;font-weight:300;">
    Pick a mood · Choose your genre · Let the music find you 🎵</p>
</div>
""", unsafe_allow_html=True)
st.markdown("<br/>", unsafe_allow_html=True)

# create tabs
tab_col1, tab_col2 = st.columns(2)
with tab_col1:
    if st.button("🎭  Mood Picks", key="tab_1", use_container_width=True):
        st.session_state["active_tab"] = "moods"
        
with tab_col2:
    if st.button("🌍  Global Hits", key="tab_2", use_container_width=True):
        st.session_state["active_tab"] = "global"

# mark the active tab column for css
if st.session_state["active_tab"] == "moods":
    active_col_num = "1"
else:
    active_col_num = "2"
    
st.markdown(f"""
<style>
div[data-testid="column"]:nth-child({active_col_num}) .stButton > button {{
  background:{theme['lavender_deep']} !important;
  color:{theme['text_on_accent']} !important;
  border-color:{theme['lavender_deep']} !important;
  box-shadow:{theme['shadow_soft']} !important;
}}
</style>""", unsafe_allow_html=True)
st.markdown("<br/>", unsafe_allow_html=True)

# helper function to draw individual song cards
def draw_song_card(col, song, pal, badge_bg, badge_fg, button_key, genre_label):
    r = pal["r"]
    g = pal["g"]
    b = pal["b"]
    deep_color = pal["deep"]
    
    with col:
        st.markdown(f"""
        <div style="background:linear-gradient(145deg,rgba({r},{g},{b},0.22) 0%,
          rgba({r},{g},{b},0.06) 100%);height:110px;border-radius:18px 18px 0 0;
          display:flex;align-items:center;justify-content:center;
          position:relative;overflow:hidden;
          border-bottom:1.5px solid rgba({r},{g},{b},0.15);">
          <div style="position:absolute;width:90px;height:90px;border-radius:50%;
            border:1.5px solid rgba({r},{g},{b},0.20);"></div>
          <div style="position:absolute;width:58px;height:58px;border-radius:50%;
            border:1.5px solid rgba({r},{g},{b},0.28);"></div>
          <div style="position:absolute;width:18px;height:18px;border-radius:50%;
            background:{deep_color};box-shadow:0 0 16px rgba({r},{g},{b},0.50);"></div>
          <span style="position:absolute;top:9px;left:10px;
            font-family:'Space Mono',monospace;font-size:0.52rem;
            background:{badge_bg};color:{badge_fg};padding:2px 9px;border-radius:20px;
            font-weight:700;letter-spacing:0.05em;
            border:1.5px solid rgba({r},{g},{b},0.25);">{genre_label}</span>
          <span style="position:absolute;top:8px;right:10px;
            font-size:1.15rem;opacity:0.9;">{song['emoji']}</span>
        </div>
        <div style="padding:11px 13px 5px;background:transparent;">
          <p style="font-family:'Fraunces',serif;font-size:0.92rem;
             color:{theme['text']};margin:0 0 3px;line-height:1.2;
             white-space:nowrap;overflow:hidden;text-overflow:ellipsis;"
             title="{song['name']}">{song['name']}</p>
          <p style="font-family:'DM Sans',sans-serif;font-size:0.72rem;
             color:{theme['text2']};margin:0 0 2px;">{song['artist']}</p>
          <p style="font-family:'DM Sans',sans-serif;font-size:0.63rem;
             color:{theme['text3']};margin:0 0 10px;font-style:italic;
             white-space:nowrap;overflow:hidden;text-overflow:ellipsis;"
             title="{song['film']}">{song['film']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # handling button click to open youtube link
        if st.button("▶  Play", key=button_key, use_container_width=True):
            # saving song details for the currently playing banner
            selected_song = song.copy()
            selected_song["mood_color"] = deep_color
            selected_song["mood_r"] = r
            selected_song["mood_g"] = g
            selected_song["mood_b"] = b
            selected_song["genre"] = genre_label
            
            st.session_state["now_playing"] = selected_song
            webbrowser.open(song["url"])

# logic for the moods tab
if st.session_state["active_tab"] == "moods":

    st.markdown(f"""<p style="font-family:'Space Mono',monospace;font-size:0.60rem;
      letter-spacing:0.18em;text-transform:uppercase;color:{theme['step_label']};
      margin-bottom:4px;">01 &nbsp;/&nbsp; Choose Your Mood</p>""",
      unsafe_allow_html=True)

    # get user input for mood
    selected_mood_name = st.selectbox("Mood", list(MOOD_DATA.keys()), label_visibility="collapsed")
    mood_dictionary = MOOD_DATA[selected_mood_name]
    mood_palette = MOOD_PALETTE[selected_mood_name]

    st.markdown(f"""<p style="font-family:'Space Mono',monospace;font-size:0.60rem;
      letter-spacing:0.18em;text-transform:uppercase;color:{theme['step_label']};
      margin:16px 0 6px;">02 &nbsp;/&nbsp; Pick Your Genre</p>""",
      unsafe_allow_html=True)

    # get user input for genre
    selected_genre = st.radio("Genre", ["Bollywood", "Hollywood"], horizontal=True, label_visibility="collapsed")

    # get lists from data
    all_songs_in_genre = mood_dictionary["songs"][selected_genre]
    top_3_songs = all_songs_in_genre["top"]
    extra_songs_list = all_songs_in_genre["extra"]
    
    # checking colors for tags
    if selected_genre == "Bollywood":
        badge_bg = theme["badge_bw_bg"]
        badge_fg = theme["badge_bw_fg"]
    else:
        badge_bg = theme["badge_hw_bg"]
        badge_fg = theme["badge_hw_fg"]

    st.markdown("<div style='margin:20px 0 10px'></div>", unsafe_allow_html=True)

    # display mood title block
    r = mood_palette["r"]
    g = mood_palette["g"]
    b = mood_palette["b"]
    
    # split emoji and name
    mood_parts = selected_mood_name.split(" ")
    mood_emoji = mood_parts[0]
    mood_text = mood_parts[1]
    
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,rgba({r},{g},{b},0.15) 0%,
      rgba({r},{g},{b},0.05) 100%);border:1.5px solid rgba({r},{g},{b},0.20);
      border-radius:20px;padding:16px 22px;margin-bottom:18px;
      display:flex;align-items:center;gap:16px;
      backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);">
      <div style="font-size:2.2rem;filter:drop-shadow(0 2px 8px rgba({r},{g},{b},0.4));">
        {mood_emoji}</div>
      <div>
        <p style="font-family:'Fraunces',serif;font-size:1.35rem;
           color:{theme['text']};margin:0;font-style:italic;">{mood_text}</p>
        <p style="font-family:'DM Sans',sans-serif;font-size:0.82rem;
           color:{theme['text2']};margin:0;font-style:italic;font-weight:300;">
          {mood_dictionary['tagline']}</p>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""<p style="font-family:'Space Mono',monospace;font-size:0.60rem;
      letter-spacing:0.18em;text-transform:uppercase;color:{theme['step_label']};
      margin-bottom:12px;">03 &nbsp;/&nbsp; Top 3 Tracks</p>""",
      unsafe_allow_html=True)

    # layout for top 3 songs
    top_cols = st.columns(3)
    for i in range(len(top_3_songs)):
        col = top_cols[i]
        song = top_3_songs[i]
        b_key = "top_btn_" + selected_mood_name + "_" + selected_genre + "_" + str(i)
        draw_song_card(col, song, mood_palette, badge_bg, badge_fg, b_key, selected_genre)

    st.markdown("<div style='margin-top:20px'></div>", unsafe_allow_html=True)
    
    # hidden extra songs section
    with st.expander(f"🔽  Discover More {selected_genre} Tracks  —  {len(extra_songs_list)} hidden gems"):
        st.markdown(f"""<p style="font-family:'DM Sans',sans-serif;font-size:0.84rem;
          color:{theme['text2']};margin:4px 0 16px;font-style:italic;">
          More vibes to keep the feeling alive ✨</p>""", unsafe_allow_html=True)
          
        extra_cols = st.columns(min(len(extra_songs_list), 4))
        for i in range(len(extra_songs_list)):
            # avoiding index out of range if more than 4 songs
            if i < 4:
                e_col = extra_cols[i]
                e_song = extra_songs_list[i]
                b_key = "extra_btn_" + selected_mood_name + "_" + selected_genre + "_" + str(i)
                draw_song_card(e_col, e_song, mood_palette, badge_bg, badge_fg, b_key, selected_genre)

# logic for the global hits tab
else:
    st.markdown(f"""
    <div style="text-align:center;padding:0.5rem 0 1.5rem;">
      <h2 style="font-family:'Fraunces',serif;font-size:2rem;
         color:{theme['text']};margin:0 0 6px;font-weight:400;">🌍 Popular Global Hits</h2>
      <p style="font-family:'DM Sans',sans-serif;font-size:0.90rem;
         color:{theme['text2']};margin:0;font-style:italic;font-weight:300;">
        A handpicked playlist of timeless Bollywood &amp; Hollywood favourites</p>
    </div>""", unsafe_allow_html=True)

    accent_colors = ["#9B7ED4","#E06090","#4DBFA0","#E8845A","#3A9BD5",
                     "#D4A017","#E06060","#8B6AC4","#D4600A","#4DBFA0","#9B7ED4","#E06090"]

    # loop to display global hits row by row
    for index in range(len(GLOBAL_HITS)):
        hit_data = GLOBAL_HITS[index]
        accent = accent_colors[index % len(accent_colors)]
        
        # checking genre to set correct badge color
        if hit_data["genre"] == "Bollywood":
            bg_color = theme["badge_bw_bg"]
            fg_color = theme["badge_bw_fg"]
        else:
            bg_color = theme["badge_hw_bg"]
            fg_color = theme["badge_hw_fg"]
            
        # highlight row if song is playing right now
        if st.session_state["now_playing"] != None and st.session_state["now_playing"]["name"] == hit_data["name"]:
            is_active = True
        else:
            is_active = False
            
        if is_active == True:
            pill_text = f'&nbsp;<span style="color:{theme["lavender_deep"]};font-family:\'Space Mono\',monospace;font-size:0.58rem;">▶ now playing</span>'
            border_color = theme["lavender_deep"]
        else:
            pill_text = ""
            border_color = theme["border"]

        # layout columns for the row
        row_col, btn_col = st.columns([5, 1])
        
        with row_col:
            st.markdown(f"""
            <div style="background:{theme['surface_glass']};border:1.5px solid {border_color};
              border-left:4px solid {accent};border-radius:14px;padding:12px 18px;
              display:flex;align-items:center;gap:14px;margin-bottom:2px;
              box-shadow:{theme['shadow_soft']};
              backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);">
              <span style="font-family:'Space Mono',monospace;font-size:0.64rem;
                color:{theme['text3']};min-width:24px;flex-shrink:0;">{str(index+1).zfill(2)}</span>
              <span style="font-size:1.1rem;flex-shrink:0;">{hit_data['emoji']}</span>
              <div style="flex:1;min-width:0;">
                <p style="font-family:'Fraunces',serif;font-size:0.94rem;
                   color:{theme['text']};margin:0;white-space:nowrap;
                   overflow:hidden;text-overflow:ellipsis;">{hit_data['name']}{pill_text}</p>
                <p style="font-family:'DM Sans',sans-serif;font-size:0.72rem;
                   color:{theme['text2']};margin:0;white-space:nowrap;
                   overflow:hidden;text-overflow:ellipsis;">
                  {hit_data['artist']} &nbsp;·&nbsp;
                  <span style="color:{theme['text3']};font-style:italic;">{hit_data['film']}</span>
                </p>
              </div>
              <span style="background:{bg_color};color:{fg_color};
                font-family:'Space Mono',monospace;font-size:0.56rem;
                font-weight:700;padding:3px 10px;border-radius:20px;
                white-space:nowrap;flex-shrink:0;border:1.5px solid {theme['border']};">
                {hit_data['genre']}</span>
            </div>""", unsafe_allow_html=True)
            
        with btn_col:
            button_k = "global_btn_" + str(index)
            if st.button("▶  Play", key=button_k, use_container_width=True):
                # mock a color palette for global hits so the banner doesn't crash
                playing_data = hit_data.copy()
                playing_data["mood_color"] = accent
                playing_data["mood_r"] = 155
                playing_data["mood_g"] = 126
                playing_data["mood_b"] = 212
                
                st.session_state["now_playing"] = playing_data
                webbrowser.open(hit_data["url"])
                
        st.markdown("<div style='margin-bottom:4px'></div>", unsafe_allow_html=True)

# sticky banner to show currently playing song
if st.session_state["now_playing"] != None:
    current_song = st.session_state["now_playing"]
    
    # get the colors saved from the button click
    np_color = current_song.get("mood_color","#9B7ED4")
    np_r = current_song.get("mood_r",155)
    np_g = current_song.get("mood_g",126)
    np_b = current_song.get("mood_b",212)
    np_genre = current_song.get("genre","")
    
    # checking genre again for banner tag
    if np_genre == "Bollywood":
        np_bg = theme["badge_bw_bg"]
        np_fg = theme["badge_bw_fg"]
    else:
        np_bg = theme["badge_hw_bg"]
        np_fg = theme["badge_hw_fg"]
        
    st.markdown("<br/>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,rgba({np_r},{np_g},{np_b},0.13),{theme['surface_glass']});
      border:1.5px solid rgba({np_r},{np_g},{np_b},0.25);border-radius:20px;
      padding:18px 22px;display:flex;align-items:center;gap:18px;
      box-shadow:0 8px 40px rgba({np_r},{np_g},{np_b},0.12);
      backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);">
      <div style="position:relative;width:14px;height:14px;flex-shrink:0;">
        <div style="position:absolute;inset:0;background:{np_color};border-radius:50%;
          animation:moodpulse 1.8s ease-in-out infinite;"></div>
      </div>
      <div style="flex:1;min-width:0;">
        <p style="font-family:'Space Mono',monospace;font-size:0.56rem;
           letter-spacing:0.22em;text-transform:uppercase;color:{np_color};margin:0 0 3px;">
          ♫ &nbsp; NOW PLAYING</p>
        <p style="font-family:'Fraunces',serif;font-size:1.1rem;
           color:{theme['text']};margin:0 0 3px;font-style:italic;
           white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{current_song['name']}</p>
        <p style="font-family:'DM Sans',sans-serif;font-size:0.76rem;
           color:{theme['text2']};margin:0;">
          {current_song['artist']} &nbsp;·&nbsp;
          <span style="color:{theme['text3']};font-style:italic;">{current_song.get('film','')}</span>
          &nbsp;&nbsp;
          <span style="background:{np_bg};color:{np_fg};
            font-family:'Space Mono',monospace;font-size:0.56rem;
            padding:2px 10px;border-radius:20px;font-weight:700;
            border:1.5px solid rgba({np_r},{np_g},{np_b},0.20);">{np_genre}</span>
        </p>
      </div>
      <a href="{current_song['url']}" target="_blank" style="
        font-family:'DM Sans',sans-serif;font-size:0.76rem;font-weight:600;
        color:{np_color};text-decoration:none;flex-shrink:0;
        border:1.5px solid rgba({np_r},{np_g},{np_b},0.30);
        padding:8px 18px;border-radius:50px;
        background:rgba({np_r},{np_g},{np_b},0.08);">Open ↗</a>
    </div>""", unsafe_allow_html=True)

# bottom footer element
st.markdown("<br/><br/>", unsafe_allow_html=True)
st.divider()
st.markdown(f"""
<p style="text-align:center;font-family:'Space Mono',monospace;
   font-size:0.56rem;letter-spacing:0.14em;color:{theme['text3']};">
  🎼 &nbsp; MOODIFY &nbsp;·&nbsp; MUSIC FOR EVERY MOOD
  &nbsp;·&nbsp; PYTHON + STREAMLIT &nbsp; 🎵
</p>""", unsafe_allow_html=True)