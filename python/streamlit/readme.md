# About

Managing Python installs can be a nightmare at times with libraries requiring different python versions. One way to keep everything in neat and consistent package is to use docker. This is a docker forrunnning [streamlit](https://streamlit.io). Streamlit is like low-code for python, it turns data scripts into shareable web apps in minutes. 

## What's in the Dockerfile
TLDR;
- take baseline from python 3.7
- add a user `app` to run the application, as its bad idea to run anything as `root` user.
- install steamlit packages in `requirements.txt` file. You can add anything to the `requirements.txt` file for your own build.


## How to Use
1a. You can pull the image directly from docker hub to run it: 
```
docker run -p 8501:8501 -it pyx7b/streamlit
```
OR

1b. Download files on your local machine and run the following command:
```
docker build -t streamlit .
docker run -p 8501:8501 -it streamlit
```

2. Once inside the container, run the following command:
```
$ streamlit hello
```

3. Open your browser to http://localhost:8501
