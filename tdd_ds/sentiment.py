from textblob import TextBlob

def extract_sentiment(text:str) -> float:
    """Extract Sentiment using textblob
    Popularity is within range [-1, 1]

    Args:
        text (str): Input String
    """
    text = TextBlob(text)
    return text.sentiment.polarity

def test_extract_sentiment_positive() -> bool:
    text = "I think today will be a great day"
    sentiment = extract_sentiment(text)
    
    assert sentiment > 0
    
def test_extract_sentiment_negative() -> bool:
    
    text = "Don't touch me again!"
    sentiment = extract_sentiment(text)
    assert sentiment < 0