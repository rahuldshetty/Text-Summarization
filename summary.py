from summarizer import Summarizer
model = Summarizer()

def get_summary(body,min_length = 60):
    result = model(body, min_length)
    full = ''.join(result)
    return full