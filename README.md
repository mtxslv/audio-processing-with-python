# Olá! 👋👋

Esse repositório contém exemplos de processamentos de áudio com Python. O objetivo é apresentar os conceitos _Transformada de Fourier_ e _Resposta ao Impulso_ de maneira aplicada em um áudio real e em um exemplo fictício.

## 🤔 O que temos aqui? 🤔

Visão geral do repositório:

```shell
.
├── audio-files                                  
│   ├── impulse-responses                      # Efeitos sonoros
│   │   ├── Deep Space.wav 
│   │   ├── Large Long Echo Hall.wav
│   │   ├── Large Wide Echo Hall.wav
│   │   ├── license.txt
│   │   └── St Nicolaes Church.wav
│   ├── results                                # Resultados dos experimentos 
│   │   ├── echoed_filtered_audio.wav
│   │   ├── filtered_audio__936.0__5.wav
│   │   └── sad_sine.wav
│   └── samples                                # Áudios utilizados nos experimentos
│       ├── cup_sound.wav
│       └── mario_and_cup.wav
├── audio-processing-with-python.pptx          # Slides
├── notebooks                                  # Os experimentos 
│   ├── audio_experiments.ipynb
│   ├── end_to_end_processing.ipynb
│   └── toy_example.ipynb
├── poetry.lock
├── pyproject.toml
├── README.md
└── src                                        # Funções utilitárias   
    └── utils.py

```

## 🔬🔭 Sobre os Experimentos 🔬🔭

Dois experimentos estão disponíveis:
- [toy_example.ipynb](./notebooks/toy_example.ipynb): esse arquivo contém a aplicação da transformada de Fourier e do Filtro Rejeita-Banda em um conjunto de senóides-exemplo;
- [end_to_end_processing.ipynb](./notebooks/end_to_end_processing.ipynb): esse arquivo aplica os conceitos desenvolvidos no [toy_example.ipynb](./notebooks/toy_example.ipynb) num áudio real. Também aplica um efeito de eco no resultado obtido;

# 👨‍💻👩‍💻 Como começar 👨‍💻👩‍💻

As dependências desse projeto foi gerenciadas com o gerenciador de pacotes [Poetry](https://python-poetry.org/). Caso esse software esteja instalado, uma vez clonado o repositório, basta executar o comando abaixo para instalar as dependências,:

```shell
poetry install
```

Caso não esteja instalado, pode-se usar o _pip_:

```shell
pip install -r requirements-dev.txt
```

E aí estará tudo pronto para executar os arquivos Jupyter mencionados!

# Hello! 👋👋

This repository contains examples of audio processing with Python. The goal is to present the concepts _Fourier Transform_ and _Impulse Response_ in an applied way in a real audio and in a fictitious example.

## 🤔 What do we have here? 🤔

Repository overview:

``` shell
.
├── audio-files                                  
│   ├── impulse-responses                      # Sound Effects
│   │   ├── Deep Space.wav 
│   │   ├── Large Long Echo Hall.wav
│   │   ├── Large Wide Echo Hall.wav
│   │   ├── license.txt
│   │   └── St Nicolaes Church.wav
│   ├── results                                # Experiments' Results 
│   │   ├── echoed_filtered_audio.wav
│   │   ├── filtered_audio__936.0__5.wav
│   │   └── sad_sine.wav
│   └── samples                                # Experiments' Input Audio Samples 
│       ├── cup_sound.wav
│       └── mario_and_cup.wav
├── audio-processing-with-python.pptx          # Slides
├── notebooks                                  # Experiments 
│   ├── audio_experiments.ipynb
│   ├── end_to_end_processing.ipynb
│   └── toy_example.ipynb
├── poetry.lock
├── pyproject.toml
├── README.md
└── src                                        # Utils   
    └── utils.py



```

## 🔬🔭 About the Experiments 🔬🔭

Two experiments are available:
- [toy_example.ipynb](./notebooks/toy_example.ipynb): this file contains the application of the Fourier transform and the Notch Filter on a set of sinusoids;
- [end_to_end_processing.ipynb](./notebooks/end_to_end_processing.ipynb): this file applies the concepts developed in [toy_example.ipynb](./notebooks/toy_example.ipynb) to real audio. It also applies an echo effect to the result obtained;

# 👨‍💻👩‍💻 How to Get Started 👨‍💻👩‍💻

The dependencies for this project were managed with the [Poetry](https://python-poetry.org/) package manager. If this software is installed, once the repository has been cloned, just run the command below to install the dependencies:

``` shell
poetry install
```

If not installed, you can use _pip_:

``` shell
pip install -r requirements-dev.txt
```

And then you're all set to run the aforementioned Jupyter files!

# 📚 References / Referências 📚

- Visualizando Fourier / _Visualizing Fourier_:
    - https://commons.wikimedia.org/wiki/File:Fourier_synthesis_square_wave_animated.gif
    - https://commons.wikimedia.org/wiki/File:Fourier_series_square_wave_circles_animation.gif
    - https://commons.wikimedia.org/wiki/File:Fourier_series_and_transform.gif

- Experimentos no Chrome Music Lab / _Chrome Music Lab Experiments_:
    - https://musiclab.chromeexperiments.com/

- Noções de Áudio (Digital) / _On (Digital) Audio_
    - https://medium.com/@harmonia.global/digital-audio-the-real-meaning-of-8-bit-music-1be5fc8ab2b1
    - https://source-separation.github.io/tutorial/basics/representations.html
    - http://www.cochlea.eu/en/sound/representation

- Arquivos de Resposta ao Impulso / _Impulse Response Files_
    - https://www.voxengo.com/product/imodeler/
    > Nota: o projeto da Voxengo que disponibilizou os efeitos sonoros foi descontinuado. Alguns destes efeitos se encontram na pasta [./audio-files/impulse-responses/](./audio-files/impulse-responses/) junto ao arquivo de licença.

    > Note: The Voxengo's project which created and distributed the sound effects was discontinued. Some of its files can be found at [./audio-files/impulse-responses/](./audio-files/impulse-responses/), as well as the license file.