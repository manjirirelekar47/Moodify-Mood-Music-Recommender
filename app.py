import streamlit as st

# setup page
st.set_page_config(page_title="Moodify 🎼", page_icon="🎵", layout="centered")

# initialize session state
for k, v in [("now_playing", None), ("active_tab", "moods"), ("dark_mode", False)]:
    if k not in st.session_state:
        st.session_state[k] = v

# set theme variables
if st.session_state.dark_mode:
    T = dict(
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
    T = dict(
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

# background html
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

# global css overrides
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,300;0,400;0,600;1,300;1,400&family=DM+Sans:wght@300;400;500;600&family=Space+Mono:wght@400;700&display=swap');

:root, [data-theme="light"], [data-theme="dark"] {{
  color-scheme: {T['scheme']};
  --background-color:           {T['bg']};
  --secondary-background-color: {T['surface2']};
  --text-color:                 {T['text']};
}}

*, *::before, *::after {{ box-sizing: border-box; }}

.ambient-bg {{
  position: fixed; inset: 0; pointer-events: none; z-index: 0; overflow: hidden;
  background: radial-gradient(circle at 15% 50%, {T['dot_color']}, transparent 50%),
              radial-gradient(circle at 85% 30%, {T['border_mid']}, transparent 50%);
}}
.note {{
  position: absolute; bottom: -10%; color: {T['text']}; opacity: 0;
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
  background: {T['bg']} !important;
  background-color: {T['bg']} !important;
  color: {T['text']} !important;
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
  color:{T['text']} !important;
}}
h1,h2,h3 {{ font-family:'Fraunces',serif !important; color:{T['text']} !important; }}

[data-testid="stSidebar"] {{
  background: linear-gradient(180deg,{T['lavender_glass']} 0%,{T['lilac_glass']} 100%) !important;
  backdrop-filter: blur(16px) !important;
  -webkit-backdrop-filter: blur(16px) !important;
  border-right: 1px solid {T['border_mid']} !important;
  z-index: 100;
}}
[data-testid="stSidebar"] * {{
  color:{T['text2']} !important; font-family:'DM Sans',sans-serif !important;
}}
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {{
  color:{T['lavender_deep']} !important; font-family:'Fraunces',serif !important;
}}
[data-testid="stSidebar"] hr {{ border-color:{T['border_mid']} !important; }}

[data-testid="stSelectbox"] > div > div {{
  background:{T['surface_glass']} !important;
  backdrop-filter: blur(8px) !important;
  -webkit-backdrop-filter: blur(8px) !important;
  border: 1.5px solid {T['border_mid']} !important;
  border-radius:14px !important;
  color:{T['text']} !important;
}}

[data-testid="stRadio"] > div {{
  display:flex !important; gap:0 !important;
  background:rgba(255,255,255,0.02) !important;
  backdrop-filter: blur(8px) !important;
  -webkit-backdrop-filter: blur(8px) !important;
  border: 1.5px solid {T['border_mid']} !important;
  border-radius:50px !important; padding:4px !important; width:fit-content;
}}
[data-testid="stRadio"] > div > label {{
  font-family:'DM Sans',sans-serif !important;
  font-size:0.92rem !important; font-weight:500 !important;
  color:{T['text2']} !important;
  padding:8px 28px !important; border-radius:50px !important;
  cursor:pointer !important; transition:all 0.25s ease !important;
  letter-spacing:0 !important; text-transform:none !important;
}}
[data-testid="stRadio"] > div > label:has(input:checked) {{
  background:{T['lavender_deep']} !important;
  color:{T['text_on_accent']} !important;
  box-shadow:0 4px 14px {T['border_mid']} !important;
}}
[data-testid="stRadio"] input[type="radio"] {{ display:none !important; }}

[data-testid="stHorizontalBlock"] > div {{
  background:{T['surface_glass']} !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  border: 1.5px solid {T['border']} !important;
  border-radius:22px !important; padding:0 !important; overflow:hidden !important;
  transition:transform 0.3s cubic-bezier(0.34,1.56,0.64,1), box-shadow 0.3s ease !important;
  box-shadow:{T['shadow_soft']} !important;
}}
[data-testid="stHorizontalBlock"] > div:hover {{
  transform:translateY(-6px) scale(1.02) !important;
  box-shadow:{T['shadow_hover']} !important;
}}

[data-testid="stExpander"] {{
  background:{T['lilac_glass']} !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  border: 1.5px solid {T['lavender_mid']} !important;
  border-radius:18px !important; overflow:hidden !important;
}}
[data-testid="stExpander"] summary {{
  font-family:'DM Sans',sans-serif !important; font-size:0.92rem !important;
  font-weight:600 !important; color:{T['lavender_deep']} !important;
  padding:14px 20px !important; background:transparent !important;
}}
[data-testid="stExpander"] > div > div {{ background:transparent !important; }}

.stButton > button {{
  font-family:'DM Sans',sans-serif !important; font-weight:600 !important;
  font-size:0.82rem !important; border-radius:50px !important;
  padding:0.45rem 1rem !important; width:100% !important;
  border: 2px solid {T['lavender_deep']} !important;
  background:rgba(255,255,255,0.05) !important; color:{T['lavender_deep']} !important;
  transition:all 0.2s ease !important;
}}
.stButton > button:hover {{
  background:{T['lavender_deep']} !important;
  color:{T['text_on_accent']} !important;
  transform:translateY(-2px) !important;
  box-shadow:{T['shadow_soft']} !important;
}}

hr {{ border-color:{T['border_mid']} !important; }}
::-webkit-scrollbar {{ width:5px; }}
::-webkit-scrollbar-track {{ background:{T['surface2']}; }}
::-webkit-scrollbar-thumb {{ background:{T['lavender_mid']}; border-radius:5px; }}

@keyframes moodpulse {{
  0%   {{ box-shadow:0 0 0 0 {T['border_mid']}; }}
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

# song database
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
                    {"name":"Good as Hell",         "artist":"Lizzo",              "film":"Coconut Oil (EP)",        "emoji":"💪","url":"https://www.youtube.com/watch?v=SmbmeOgWsqE"},
                    {"name":"I Gotta Feeling",      "artist":"Black Eyed Peas",   "film":"The E.N.D.",              "emoji":"🍾","url":"https://www.youtube.com/watch?v=uSD4vsh1zDA"},
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
                    {"name":"Fix You",              "artist":"Coldplay",           "film":"X&Y (Album)",             "emoji":"🕯️","url":"https://www.youtube.com/watch?v=k4V3Mo61fJM"},
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
    {"name":"Billie Jean",             "artist":"Michael Jackson",   "film":"Thriller (Album)",         "genre":"Hollywood","emoji":"🕺","url":"https://www.youtube.com/watch?v=Zi_XLOBDo_Y"},
    {"name":"Shape of You",            "artist":"Ed Sheeran",        "film":"Divide (Album)",           "genre":"Hollywood","emoji":"💫","url":"https://www.youtube.com/watch?v=JGwWNGJdvx8"},
    {"name":"Tum Hi Ho",               "artist":"Arijit Singh",      "film":"Aashiqui 2",               "genre":"Bollywood","emoji":"🌟","url":"https://www.youtube.com/watch?v=Umqb9KENgmk"},
    {"name":"One More Time",           "artist":"Daft Punk",         "film":"Discovery (Album)",        "genre":"Hollywood","emoji":"🤖","url":"https://www.youtube.com/watch?v=FGBhQbmPwH8"},
    {"name":"Kal Ho Na Ho",            "artist":"Sonu Nigam",        "film":"Kal Ho Na Ho",             "genre":"Bollywood","emoji":"🌟","url":"https://www.youtube.com/watch?v=bFMJszkMFkI"},
    {"name":"Smells Like Teen Spirit", "artist":"Nirvana",           "film":"Nevermind (Album)",        "genre":"Hollywood","emoji":"⚡","url":"https://www.youtube.com/watch?v=hTWKbfoikeg"},
    {"name":"Gallan Goodiyaan",        "artist":"Shankar-Ehsaan-Loy","film":"Dil Dhadakne Do",          "genre":"Bollywood","emoji":"🎉","url":"https://www.youtube.com/watch?v=9fxfKaTOAV0"},
    {"name":"Rolling in the Deep",     "artist":"Adele",             "film":"21 (Album)",               "genre":"Hollywood","emoji":"🌊","url":"https://www.youtube.com/watch?v=rYEDA3JcQqw"},
    {"name":"Kar Har Maidaan Fateh",   "artist":"Sukhwinder Singh",  "film":"Sanju",                    "genre":"Bollywood","emoji":"⚡","url":"https://www.youtube.com/watch?v=4mONADMBRqA"},
    {"name":"Despacito",               "artist":"Luis Fonsi",        "film":"Vida (Album)",             "genre":"Hollywood","emoji":"🎸","url":"https://www.youtube.com/watch?v=kTJczUoc26U"},
    {"name":"Gerua",                   "artist":"Arijit Singh",      "film":"Dilwale",                  "genre":"Bollywood","emoji":"🌹","url":"https://www.youtube.com/watch?v=AEIVhBS6baE"},
    {"name":"Uptown Funk",             "artist":"Bruno Mars",        "film":"Mark Ronson ft. Bruno",    "genre":"Hollywood","emoji":"🎷","url":"https://www.youtube.com/watch?v=OPf0YbXqDm0"},
]

# toggle dark mode
def toggle_theme():
    st.session_state.dark_mode = not st.session_state.dark_mode

# sidebar config
with st.sidebar:
    c1, c2 = st.columns([3, 1])
    with c1:
        st.markdown(f"""
        <div style="padding:8px 0 16px;">
          <p style="font-family:'Fraunces',serif;font-size:1.6rem;
             color:{T['lavender_deep']};margin:0;line-height:1.1;">Moodify</p>
          <p style="font-family:'Space Mono',monospace;font-size:0.58rem;
             color:{T['text3']};letter-spacing:0.12em;margin:4px 0 0;">
            MUSIC FOR EVERY MOOD · v1.0</p>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("<div style='padding-top:14px'></div>", unsafe_allow_html=True)
        _lbl = "☀️" if st.session_state.dark_mode else "🌙"
        _tip = "Light mode" if st.session_state.dark_mode else "Dark mode"
        
        st.button(_lbl, help=_tip, key="dm", use_container_width=True, on_click=toggle_theme)

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
    for _ml, _md in MOOD_DATA.items():
        st.markdown(
            f'<div style="padding:3px 0;">'
            f'<span style="font-size:0.88rem;color:{T["text"]};">{_ml}</span>'
            f'<span style="font-family:\'Space Mono\',monospace;font-size:0.58rem;'
            f'color:{T["lavender_deep"]};margin-left:8px;font-style:italic;">'
            f'{_md["tagline"]}</span></div>',
            unsafe_allow_html=True,
        )
    st.divider()
    st.caption("Moodify · Let music find your mood 🎼")

# header
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
     color:{T['lavender_mid']};margin-bottom:10px;">
     🎼 ✨ Your personal music companion ✨ 🎼</p>
  <h1 style="font-family:'Fraunces',serif;font-size:3.6rem;font-weight:600;
     color:{T['text']};line-height:1.0;margin-bottom:6px;letter-spacing:-0.02em;">
    <span style="font-style:italic;color:{T['lavender_deep']};">Moodify</span>
  </h1>
  <p style="font-family:'DM Sans',sans-serif;color:{T['text2']};
     font-size:1.0rem;margin:0;font-weight:300;">
    Pick a mood · Choose your genre · Let the music find you 🎵</p>
</div>
""", unsafe_allow_html=True)
st.markdown("<br/>", unsafe_allow_html=True)

# tab navigation
tc1, tc2 = st.columns(2)
with tc1:
    if st.button("🎭  Mood Picks", key="tb1", use_container_width=True):
        st.session_state.active_tab = "moods"
with tc2:
    if st.button("🌍  Global Hits", key="tb2", use_container_width=True):
        st.session_state.active_tab = "global"

_active_col = "1" if st.session_state.active_tab == "moods" else "2"
st.markdown(f"""
<style>
div[data-testid="column"]:nth-child({_active_col}) .stButton > button {{
  background:{T['lavender_deep']} !important;
  color:{T['text_on_accent']} !important;
  border-color:{T['lavender_deep']} !important;
  box-shadow:{T['shadow_soft']} !important;
}}
</style>""", unsafe_allow_html=True)
st.markdown("<br/>", unsafe_allow_html=True)

# card render function
def render_card(col, song, pal, bbg, bfg, prefix, genre_lbl):
    r, g, b, deep = pal["r"], pal["g"], pal["b"], pal["deep"]
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
            background:{deep};box-shadow:0 0 16px rgba({r},{g},{b},0.50);"></div>
          <span style="position:absolute;top:9px;left:10px;
            font-family:'Space Mono',monospace;font-size:0.52rem;
            background:{bbg};color:{bfg};padding:2px 9px;border-radius:20px;
            font-weight:700;letter-spacing:0.05em;
            border:1.5px solid rgba({r},{g},{b},0.25);">{genre_lbl}</span>
          <span style="position:absolute;top:8px;right:10px;
            font-size:1.15rem;opacity:0.9;">{song['emoji']}</span>
        </div>
        <div style="padding:11px 13px 5px;background:transparent;">
          <p style="font-family:'Fraunces',serif;font-size:0.92rem;
             color:{T['text']};margin:0 0 3px;line-height:1.2;
             white-space:nowrap;overflow:hidden;text-overflow:ellipsis;"
             title="{song['name']}">{song['name']}</p>
          <p style="font-family:'DM Sans',sans-serif;font-size:0.72rem;
             color:{T['text2']};margin:0 0 2px;">{song['artist']}</p>
          <p style="font-family:'DM Sans',sans-serif;font-size:0.63rem;
             color:{T['text3']};margin:0 0 10px;font-style:italic;
             white-space:nowrap;overflow:hidden;text-overflow:ellipsis;"
             title="{song['film']}">{song['film']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        _k = f"p{abs(hash(prefix+song['name']))%10**9}"
        
        if st.button("▶  Play", key=_k, use_container_width=True):
            st.session_state.now_playing = {
                **song, "mood_color": deep,
                "mood_r": r, "mood_g": g, "mood_b": b, "genre": genre_lbl,
            }
            st.session_state[f"open_{_k}"] = True
            st.rerun()
        if st.session_state.get(f"open_{_k}"):
            st.session_state[f"open_{_k}"] = False
            st.markdown(
                f'''<a href="{song["url"]}" target="_blank" rel="noopener noreferrer"
                style="display:block;text-align:center;padding:6px 0;
                background:linear-gradient(135deg,{deep},{deep}99);
                color:#fff;border-radius:8px;font-family:DM Sans,sans-serif;
                font-size:0.78rem;font-weight:700;text-decoration:none;
                margin-top:4px;">▶&nbsp; Open on YouTube ↗</a>''',
                unsafe_allow_html=True
            )

# render mood tab
if st.session_state.active_tab == "moods":

    st.markdown(f"""<p style="font-family:'Space Mono',monospace;font-size:0.60rem;
      letter-spacing:0.18em;text-transform:uppercase;color:{T['step_label']};
      margin-bottom:4px;">01 &nbsp;/&nbsp; Choose Your Mood</p>""",
      unsafe_allow_html=True)

    mood_label = st.selectbox("Mood", list(MOOD_DATA.keys()),
                               label_visibility="collapsed")
    mood_data  = MOOD_DATA[mood_label]
    palette    = MOOD_PALETTE[mood_label]

    st.markdown(f"""<p style="font-family:'Space Mono',monospace;font-size:0.60rem;
      letter-spacing:0.18em;text-transform:uppercase;color:{T['step_label']};
      margin:16px 0 6px;">02 &nbsp;/&nbsp; Pick Your Genre</p>""",
      unsafe_allow_html=True)

    genre = st.radio("Genre", ["Bollywood", "Hollywood"],
                     horizontal=True, label_visibility="collapsed")

    songs       = mood_data["songs"][genre]
    top_songs   = songs["top"]
    extra_songs = songs["extra"]
    is_bw       = (genre == "Bollywood")
    bbg = T["badge_bw_bg"] if is_bw else T["badge_hw_bg"]
    bfg = T["badge_bw_fg"] if is_bw else T["badge_hw_fg"]

    st.markdown("<div style='margin:20px 0 10px'></div>", unsafe_allow_html=True)

    r, g, b = palette["r"], palette["g"], palette["b"]
    _emoji = mood_label.split(" ")[0]
    _name  = mood_label.split(" ", 1)[1] if " " in mood_label else mood_label
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,rgba({r},{g},{b},0.15) 0%,
      rgba({r},{g},{b},0.05) 100%);border:1.5px solid rgba({r},{g},{b},0.20);
      border-radius:20px;padding:16px 22px;margin-bottom:18px;
      display:flex;align-items:center;gap:16px;
      backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);">
      <div style="font-size:2.2rem;filter:drop-shadow(0 2px 8px rgba({r},{g},{b},0.4));">
        {_emoji}</div>
      <div>
        <p style="font-family:'Fraunces',serif;font-size:1.35rem;
           color:{T['text']};margin:0;font-style:italic;">{_name}</p>
        <p style="font-family:'DM Sans',sans-serif;font-size:0.82rem;
           color:{T['text2']};margin:0;font-style:italic;font-weight:300;">
          {mood_data['tagline']}</p>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""<p style="font-family:'Space Mono',monospace;font-size:0.60rem;
      letter-spacing:0.18em;text-transform:uppercase;color:{T['step_label']};
      margin-bottom:12px;">03 &nbsp;/&nbsp; Top 3 Tracks</p>""",
      unsafe_allow_html=True)

    cols = st.columns(3)
    for col, song in zip(cols, top_songs):
        render_card(col, song, palette, bbg, bfg, f"top_{mood_label}_{genre}", genre)

    st.markdown("<div style='margin-top:20px'></div>", unsafe_allow_html=True)
    with st.expander(f"🔽  Discover More {genre} Tracks  —  {len(extra_songs)} hidden gems"):
        st.markdown(f"""<p style="font-family:'DM Sans',sans-serif;font-size:0.84rem;
          color:{T['text2']};margin:4px 0 16px;font-style:italic;">
          More vibes to keep the feeling alive ✨</p>""", unsafe_allow_html=True)
        ecols = st.columns(min(len(extra_songs), 4))
        for col, song in zip(ecols, extra_songs):
            render_card(col, song, palette, bbg, bfg, f"ex_{mood_label}_{genre}", genre)

# render global hits tab
else:
    st.markdown(f"""
    <div style="text-align:center;padding:0.5rem 0 1.5rem;">
      <h2 style="font-family:'Fraunces',serif;font-size:2rem;
         color:{T['text']};margin:0 0 6px;font-weight:400;">🌍 Popular Global Hits</h2>
      <p style="font-family:'DM Sans',sans-serif;font-size:0.90rem;
         color:{T['text2']};margin:0;font-style:italic;font-weight:300;">
        A handpicked playlist of timeless Bollywood &amp; Hollywood favourites</p>
    </div>""", unsafe_allow_html=True)

    ACCENTS = ["#9B7ED4","#E06090","#4DBFA0","#E8845A","#3A9BD5",
               "#D4A017","#E06060","#8B6AC4","#D4600A","#4DBFA0","#9B7ED4","#E06090"]

    for i, hit in enumerate(GLOBAL_HITS):
        acc    = ACCENTS[i % len(ACCENTS)]
        is_bw  = hit["genre"] == "Bollywood"
        bb     = T["badge_bw_bg"] if is_bw else T["badge_hw_bg"]
        bf     = T["badge_bw_fg"] if is_bw else T["badge_hw_fg"]
        active = (st.session_state.now_playing or {}).get("name") == hit["name"]
        pill   = (f'&nbsp;<span style="color:{T["lavender_deep"]};'
                  f'font-family:\'Space Mono\',monospace;font-size:0.58rem;">▶ now playing</span>'
                  if active else "")
        bdr    = T["lavender_deep"] if active else T["border"]

        rc, bc = st.columns([5, 1])
        with rc:
            st.markdown(f"""
            <div style="background:{T['surface_glass']};border:1.5px solid {bdr};
              border-left:4px solid {acc};border-radius:14px;padding:12px 18px;
              display:flex;align-items:center;gap:14px;margin-bottom:2px;
              box-shadow:{T['shadow_soft']};
              backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);">
              <span style="font-family:'Space Mono',monospace;font-size:0.64rem;
                color:{T['text3']};min-width:24px;flex-shrink:0;">{str(i+1).zfill(2)}</span>
              <span style="font-size:1.1rem;flex-shrink:0;">{hit['emoji']}</span>
              <div style="flex:1;min-width:0;">
                <p style="font-family:'Fraunces',serif;font-size:0.94rem;
                   color:{T['text']};margin:0;white-space:nowrap;
                   overflow:hidden;text-overflow:ellipsis;">{hit['name']}{pill}</p>
                <p style="font-family:'DM Sans',sans-serif;font-size:0.72rem;
                   color:{T['text2']};margin:0;white-space:nowrap;
                   overflow:hidden;text-overflow:ellipsis;">
                  {hit['artist']} &nbsp;·&nbsp;
                  <span style="color:{T['text3']};font-style:italic;">{hit['film']}</span>
                </p>
              </div>
              <span style="background:{bb};color:{bf};
                font-family:'Space Mono',monospace;font-size:0.56rem;
                font-weight:700;padding:3px 10px;border-radius:20px;
                white-space:nowrap;flex-shrink:0;border:1.5px solid {T['border']};">
                {hit['genre']}</span>
            </div>""", unsafe_allow_html=True)
        with bc:
            _k = f"h{abs(hash(hit['name']))%10**9}"
            if st.button("▶  Play", key=_k, use_container_width=True):
                st.session_state.now_playing = {
                    **hit, "mood_color": acc,
                    "mood_r":155,"mood_g":126,"mood_b":212,
                }
                st.session_state[f"open_{_k}"] = True
                st.rerun()
            if st.session_state.get(f"open_{_k}"):
                st.session_state[f"open_{_k}"] = False
                st.markdown(
                    f'''<a href="{hit["url"]}" target="_blank" rel="noopener noreferrer"
                    style="display:block;text-align:center;padding:5px 0;
                    background:linear-gradient(135deg,#9B7ED4,#7B5EA7);
                    color:#fff;border-radius:8px;font-family:DM Sans,sans-serif;
                    font-size:0.75rem;font-weight:700;text-decoration:none;
                    margin-top:4px;">▶&nbsp; Open on YouTube ↗</a>''',
                    unsafe_allow_html=True
                )
        st.markdown("<div style='margin-bottom:4px'></div>", unsafe_allow_html=True)

# render now playing footer
if st.session_state.now_playing:
    np   = st.session_state.now_playing
    npc  = np.get("mood_color","#9B7ED4")
    nr,ng,nb = np.get("mood_r",155),np.get("mood_g",126),np.get("mood_b",212)
    npg  = np.get("genre","")
    nbb  = T["badge_bw_bg"] if npg=="Bollywood" else T["badge_hw_bg"]
    nbf  = T["badge_bw_fg"] if npg=="Bollywood" else T["badge_hw_fg"]
    st.markdown("<br/>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,rgba({nr},{ng},{nb},0.13),{T['surface_glass']});
      border:1.5px solid rgba({nr},{ng},{nb},0.25);border-radius:20px;
      padding:18px 22px;display:flex;align-items:center;gap:18px;
      box-shadow:0 8px 40px rgba({nr},{ng},{nb},0.12);
      backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);">
      <div style="position:relative;width:14px;height:14px;flex-shrink:0;">
        <div style="position:absolute;inset:0;background:{npc};border-radius:50%;
          animation:moodpulse 1.8s ease-in-out infinite;"></div>
      </div>
      <div style="flex:1;min-width:0;">
        <p style="font-family:'Space Mono',monospace;font-size:0.56rem;
           letter-spacing:0.22em;text-transform:uppercase;color:{npc};margin:0 0 3px;">
          ♫ &nbsp; NOW PLAYING</p>
        <p style="font-family:'Fraunces',serif;font-size:1.1rem;
           color:{T['text']};margin:0 0 3px;font-style:italic;
           white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{np['name']}</p>
        <p style="font-family:'DM Sans',sans-serif;font-size:0.76rem;
           color:{T['text2']};margin:0;">
          {np['artist']} &nbsp;·&nbsp;
          <span style="color:{T['text3']};font-style:italic;">{np.get('film','')}</span>
          &nbsp;&nbsp;
          <span style="background:{nbb};color:{nbf};
            font-family:'Space Mono',monospace;font-size:0.56rem;
            padding:2px 10px;border-radius:20px;font-weight:700;
            border:1.5px solid rgba({nr},{ng},{nb},0.20);">{npg}</span>
        </p>
      </div>
      <a href="{np['url']}" target="_blank" style="
        font-family:'DM Sans',sans-serif;font-size:0.76rem;font-weight:600;
        color:{npc};text-decoration:none;flex-shrink:0;
        border:1.5px solid rgba({nr},{ng},{nb},0.30);
        padding:8px 18px;border-radius:50px;
        background:rgba({nr},{ng},{nb},0.08);">Open ↗</a>
    </div>""", unsafe_allow_html=True)

# footer
st.markdown("<br/><br/>", unsafe_allow_html=True)
st.divider()
st.markdown(f"""
<p style="text-align:center;font-family:'Space Mono',monospace;
   font-size:0.56rem;letter-spacing:0.14em;color:{T['text3']};">
  🎼 &nbsp; MOODIFY &nbsp;·&nbsp; MUSIC FOR EVERY MOOD
  &nbsp;·&nbsp; PYTHON + STREAMLIT &nbsp; 🎵
</p>""", unsafe_allow_html=True)