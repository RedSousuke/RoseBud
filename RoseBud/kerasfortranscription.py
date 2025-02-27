from deepspeech import audio, text, load_model

deepspeech = load_model(name='polish-model.bin')
files = ['to/test/sample.wav']
transcripts = ['this is a test']

X = audio.get_features(files)
y = text.get_batch_labels(transcripts, deepspeech.alphabet)

y_hat = deepspeech.model.predict_on_batch(X)
sentences = deepspeech.decode(y_hat) # also you could pass custom language model
# or simple:  X, y_hat, sentences = deepspeech(files, full=True)