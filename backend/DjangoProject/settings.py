"""
Django settings for DjangoProject project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
import pandas as pd
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-bt579q-94h1%nugm^80wc8*_kc@#gp3w75onc63!eehiwr)boi"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    'ml.apps.MLConfig',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "DjangoProject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates']
        ,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "DjangoProject.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

CORS_ALLOW_ALL_ORIGINS = True

SPOTIFY = {
    'CLIENT_ID': os.getenv('SPOTIFY_CLIENT_ID'),
    'CLIENT_SECRET': os.getenv('SPOTIFY_CLIENT_SECRET'),
    'REDIRECT_URI': os.getenv('SPOTIFY_REDIRECT_URI'),
    'SCOPES': 'playlist-read-private playlist-modify-public',
}

FEATURES = ['popularity',
            'duration_ms',
            'danceability',
            'energy',
            'loudness',
            'speechiness',
            'acousticness',
            'instrumentalness',
            'liveness',
            'valence',
            'tempo']

DF = pd.read_csv("data/songListCleaned.csv")

KV_LABELS = {'high popularity': [42.06213858625163, 100], 'medium popularity': [24.336805205185797, 42.06213858625163], 
             'low popularity': [0, 24.336805205185797], 'high duration_ms': [277791.1256366565, 5237295], 
             'medium duration_ms': [180494.499204635, 277791.1256366565], 'low duration_ms': [8586, 180494.499204635], 
             'high danceability': [0.6382691939772152, 0.985], 'medium danceability': [0.48605865656399494, 0.6382691939772152], 
             'low danceability': [0.0, 0.48605865656399494], 'high energy': [0.7449811392830035, 1.0], 
             'medium energy': [0.5239287468845211, 0.7449811392830035], 'low energy': [0.0, 0.5239287468845211], 
             'high loudness': [-6.2500393083862695, 4.532], 'medium loudness': [-10.748091817015506, -6.2500393083862695], 
             'low loudness': [-49.531, -10.748091817015506], 'high speechiness': [0.13623204572910647, 0.965], 
             'medium speechiness': [0.03864950564260645, 0.13623204572910647], 'low speechiness': [0.0, 0.03864950564260645], 
             'high acousticness': [0.4740026692392782, 0.996], 'medium acousticness': [0.18255796568392224, 0.4740026692392782], 
             'low acousticness': [0.0, 0.18255796568392224], 'high instrumentalness': [0.31290016148271904, 1.0], 
             'medium instrumentalness': [0.03392167416932562, 0.31290016148271904], 'low instrumentalness': [0.0, 0.03392167416932562], 
             'high liveness': [0.30090977169984284, 1.0], 'medium liveness': [0.1330270772625678, 0.30090977169984284], 
             'low liveness': [0.0, 0.1330270772625678], 'high valence': [0.5826921205040139, 0.995], 
             'medium valence': [0.35624952525278547, 0.5826921205040139], 'low valence': [0.0, 0.35624952525278547], 
             'high tempo': [135.03007628967543, 243.372], 'medium tempo': [109.08536385767847, 135.03007628967543], 
             'low tempo': [0.0, 109.08536385767847], 'german': None, 'club': None, 'minimal-techno': None, 
             'hip-hop': None, 'comedy': None, 'chill': None, 'soul': None, 'ska': None, 'punk-rock': None, 
             'bluegrass': None, 'happy': None, 'drum-and-bass': None, 'idm': None, 'alternative': None, 
             'rock': None, 'alt-rock': None, 'emo': None, 'sad': None, 'honky-tonk': None, 'industrial': None, 
             'j-dance': None, 'grindcore': None, 'french': None, 'world-music': None, 'hard-rock': None, 'pagode': None, 
             'forro': None, 'sertanejo': None, 'j-rock': None, 'turkish': None, 'j-pop': None, 'jazz': None, 'indian': None, 
             'children': None, 'power-pop': None, 'blues': None, 'romance': None, 'study': None, 'funk': None, 'metal': None, 
             'afrobeat': None, 'black-metal': None, 'grunge': None, 'opera': None, 'show-tunes': None, 'heavy-metal': None, 
             'k-pop': None, 'progressive-house': None, 'acoustic': None, 'anime': None, 'ambient': None, 'dubstep': None, 
             'iranian': None, 'songwriter': None, 'singer-songwriter': None, 'synth-pop': None, 'chicago-house': None, 
             'detroit-techno': None, 'punk': None, 'kids': None, 'disco': None, 'pop-film': None, 'gospel': None, 'brazil': None, 
             'mandopop': None, 'swedish': None, 'tango': None, 'reggae': None, 'latin': None, 'latino': None, 'reggaeton': None, 
             'piano': None, 'spanish': None, 'salsa': None, 'samba': None, 'electronic': None, 'goth': None, 'dance': None, 
             'malay': None, 'death-metal': None, 'trance': None, 'indie': None, 'indie-pop': None, 'country': None, 
             'hardstyle': None, 'folk': None, 'mpb': None, 'electro': None, 'disney': None, 'rockabilly': None, 'j-idol': None, 
             'hardcore': None, 'british': None, 'psych-rock': None, 'guitar': None, 'dub': None, 'deep-house': None, 'groove': None, 
             'rock-n-roll': None, 'r-n-b': None, 'house': None, 'metalcore': None, 'dancehall': None, 'trip-hop': None, 'party': None, 
             'breakbeat': None, 'sleep': None, 'garage': None, 'techno': None, 'classical': None, 'cantopop': None, 'edm': None, 'pop': None, 'new-age': None}

ZERO_SHOT_LABELS = list(KV_LABELS.keys())
# pip install django-cors-headers