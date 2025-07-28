# Text-Generation-using-GPT-2

Description:
This project is a Python-based application that leverages OpenAI's GPT-2 language model to generate coherent and creative text continuations from user prompts.
Using the transformers library by Hugging Face, the tool loads the pre-trained gpt2-medium model and allows users to enter a text prompt, upon which the model generates a continuation using probabilistic sampling techniques.

To enhance usability, the project features a clean and responsive Graphical User Interface (GUI) built using tkinter. The GUI includes an input field for the prompt, a button to generate text, and an output area to display the model's response. This provides an intuitive playground for experimenting with generative AI without writing a single line of code.

This tool is useful for creative writing, idea generation, testing GPT-2's behavior, or exploring language models in an educational setting. The project structure separates the AI logic and GUI layer, allowing future extensibility for adding models, saving output, or building web-based interfaces.

Requirements:

Python 3.7 or higher

transformers (Hugging Face Transformers)

torch (PyTorch backend for model execution)

tkinter (for GUI — typically pre-installed with Python)

Internet (only for initial model download)

Features:

Text generation using OpenAI’s GPT-2 (medium) pre-trained model

transformers.pipeline API for clean and high-level model access

Simple GUI using tkinter for seamless user interaction

Temperature and top-p sampling enabled for more creative results

Offline use supported after model download

Ideal for students, hobbyists, and AI/ML enthusiasts exploring NLP
