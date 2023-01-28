# youtube-videos

APIs that help in Getting the list and searching YouTube Videos.

## Getting Started

Start by cloning the repository using: git clone https://github.com/akarsh2609/youtube-videos.git followed by cd
youtube-videos.

## Setup the API Keys for calling YouTube APIs

[add your keys here](https://github.com/akarsh2609/youtube-videos/blob/d99fccbfc5961bff9227573a945dc664be15aacd/youtube_videos/youtube_cron.py#L5)

## To run the application

### Install the required dependencies

- pip3 install -r requirements.txt

### Run the migration scripts to create Model

1. python3 manage.py migrate
2. python3 manage.py makemigrations
3. python3 manage.py migrate --run-syncdb

### Add the cron to Django Application to fetch the YouTube data at every 10 seconds.

- python3 manage.py crontab add

### To start the server

- python3 manage.py runserver

## API endpoints

#### 1. `/get/<page-number>`

Fetches the top 25 latest hindi YouTube videos.

URL: /get/:page_number

Request type: GET

#### 2. `/search?<search_string>`

On the basis of search string provided this API returns the video details which contain search string in either title or
description.

URL: /search?search_string

Request type: GET