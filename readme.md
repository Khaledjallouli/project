# what this project is about
The main idea is to use machine learning to predict soccer matches.
The secondary idea is to also use machine learning to predict the final result (goals made by each team).
To be able to avoid the hassle of commandline, the web-gui increases usability.


## prerequisites
- install and configure Anaconda
  - start "Anaconda Navigator"
  - start "CMD.exe Prompt" or "Powershell Prompt"
  - conda install python=3.7.7 OR (while on dev) conda update --all
  - cd into/the/projects/directory
  - pip install -r jupyter/requirements.txt


## how to use
- run web-gui:
  - install node and npm
  - cd Web/Frontend
  - npm install
  - npm run serve


## folder structure
- Daily/ contains scrum related files
- data/ contains the data for machine learning
- jupyter/ is where the models are created and evaluated
- model/ is where the models are stored
- Web/ is for ready-to-use software
- Report/ contains the papers which resulted out of this project
- */ the rest is only relevant to students
