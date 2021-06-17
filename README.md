# HDP - Heart Disease Prediction

### steps to run the app
1. install pip venv and poetry (this is one time process for your pc)

    on ubuntu
    ```bash
    sudo apt install python3-venv python3-pip
    pip3 install poetry
    ```

    on windows, pip3 and pip3 might be already installed
    ```bash
    pip3 install poetry
    ```

2. create virtual envirnment (this is one time process in your cloned project folder)

    on ubuntu
    ```bash
    python3 -m venv venv/
    ```

    on windows
    ```bash
    python3 -m venv venv/
    venv\Scripts\activate.bat
    ```

3. activate virtual environment (do this ever time you open new terminal/cmd)
    
    on ubuntu
    ```bash
    source venv/bin/activate
    ```

    on windows
    ```bash
    venv\Scripts\activate.bat
    ```

4. install dependancies
   on both windows and ubuntu
   ```bash
   poetry install
   ```

5. run the app
   on both windows and ubuntu
   ```bash
   python3 -m app
   ```
   