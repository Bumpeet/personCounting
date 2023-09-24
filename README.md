# personCounting
This program helps in keeping the track of count of people entering and exiting a location

# instructions to run the script
- If you are using a conda environment, create a new env by running this command `conda create --name track`
- Run these following commands
    - Activate your environment: `conda activate track`
    - Install necessary packages: `pip install -r requirements.txt`
    - Clone this repo: `git clone https://github.com/Bumpeet/personCounting.git`
    - cd to this repo: `cd personCounting`
    - Download the raw footage from this [link](https://storageapi.pushpak.cloud/videos/pc/Main%20Gate%20-%20Luminous.mp4) and place it in the root dir of this repo.
    - Run the script: `python track.py`
    - For changing the parameters: `python track.py --help`
    - For example if you want to change the point1 to (100, 120): `python track.py --point1 100 120`

# Observation
All of the observation made are present in this [document](https://github.com/Bumpeet/personCounting/blob/main/Observations.pdf)
