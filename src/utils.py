import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from scipy.io import wavfile
from scipy.fft import fft, fftfreq
from scipy.signal import convolve, fftconvolve

def get_audio(audio_path: Path) -> tuple:
    """
    Get audio data from wav file in auido_path.

    Parameters
    ----------
    audio_path : Path
        Path to wav file.

    Returns
    -------
    data : ndarray
        Audio data.
    sample_rate : int
        Sample rate of audio data. That is, how many samples are taken each second.
    duration : float
        Duration of audio data in seconds.
    """
    sample_rate, data = wavfile.read(str(audio_path))
    duration = data.shape[0]/sample_rate
    return data, sample_rate, duration

def plot_audio_in_time(data:np.array, sample_rate: int, duration: float, plot_title:str = 'Audio File'):
    """
    Plots the audio signal in time.

    Parameters
    ----------
    data : np.array
        The audio signal.
    sample_rate : int
        The sample rate of the audio signal.
    duration : float
        The duration of the audio signal.
    """
    time = np.arange(0, duration, 1/sample_rate)
    plt.plot(time, data, alpha=0.8)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title(plot_title)
    plt.grid(True)
    plt.show()

def normalize_samples(samples: np.ndarray, 
                      bits:int = 16) -> np.ndarray:
    """
    Normalize samples in the range of a given representation.

    Parameters
    ----------
    samples : np.ndarray
        Samples to normalize.
    bits : int, optional
        Number of bits to represent the samples. The default is 16.

    Returns
    -------
    normalized_tone : np.ndarray
        Normalized samples.
    """
    scaler = 2**(bits-1)-1 # subtract 1 because half of the bits representation is positive.
    normalized_tone = np.int16((samples / samples.max()) * scaler)
    return normalized_tone

def get_fft_transform(normalized_samples: np.ndarray,
                      sample_rate: int,
                      duration: float):
    """
    Get the FFT transform of a normalized audio.

    Parameters
    ----------
    normalized_samples : np.ndarray
        The normalized samples of the tone.
    sample_rate : int
        The sample rate of the audio.
    duration : float
        The duration of the audio.

    Returns
    -------
    yf: np.ndarray
        The FFT transform of the audio
    xf: np.ndarray
        The frequency axis.
    """
    N = int(sample_rate * duration) # Number of samples in normalized_tone

    yf = fft(normalized_samples)
    xf = fftfreq(N, 1 / sample_rate)

    return yf, xf

def plot_audio_in_frequency(xf: np.ndarray,
                            yf: np.ndarray,
                            margins: tuple = [-4e3,4e3]):    
    """
    Plot  the FFT of the audio.

    Parameters
    ----------
    xf : np.ndarray
        The frequency axis.
    yf : np.ndarray
        The magnitude of the frequency.
    margin : float
        The margin to be used in the plot. It is applied in both sides (positive and negative). Defaults to 4e3.
    """
    plt.xlim((margins[0],margins[1]))
    plt.grid(True)
    plt.title(f'Fourier/Frequency Domain')
    plt.xlabel(f'Frequency (Hz)')
    plt.ylabel(f'Magnitude')
    plt.plot(xf, np.abs(yf))
    plt.show()