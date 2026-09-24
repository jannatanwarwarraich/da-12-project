# da-12-project

- In case of multiple GitHub accounts
    - instead of `git clone https://example.com/open-source/library.git`, run:

- open this repo in vs code


2. create virtual env
    - python -m venv env_name
    - activate the env: name\Scripts\activate
    - in case you get a command not recognized error
        - Execute this command in the VS Code PowerShell instance: Set-ExecutionPolicy RemoteSigned --Scope Process
    - install the required libraries: pip install Jupyter ipykernel numpy pandas matplotlib seaborn scikit-learn


3. Data Gathering and Model Training (model.ipynb)
    - select the kernel
    - Load Data and import libraries
    - preprocessing + train test split
    - model training
    - Model evaluation
    - model serialization


4. app.py (streamlit app)
    - import libraries
    - page, title, doc title
    - load model
    - define input fields: st.number_input()
    - make prediction: st.success


5. requirements.txt
    - module__version__
    - don't do pip freeze


6. streamlit community cloud