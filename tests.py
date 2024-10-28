import pytest
from main import preprocess_text, check_emotions, analyse_sentiment, visualize_emotions
from nltk.corpus import stopwords # stop words are words that have no meaning for the sentence to be analised using NLP
# preprocessing text 
test_text = (
    "Hello! This is a test text, with some punctuations... "
    "It contains multiple sentences. This includes positive words such as 'great', "
    "'fantastic', and 'awesome'. However, it also includes some negative words: "
    "'bad', 'terrible', and 'horrible'. "
    "Additionally, there are some stopwords that should be removed, like 'and', 'the', 'is'. "
    "Overall, the aim is to ensure that the text is cleaned properly, "
    "punctuations are removed, and meaningful words are retained. "
    "This text is for testing the function's ability to preprocess a larger input effectively."
)

expected_cleaned_text = (
    "hello this is a test text with some punctuations it contains multiple sentences "
    "this includes positive words such as great fantastic and awesome however "
    "it also includes some negative words bad terrible and horrible additionally "
    "there are some stopwords that should be removed like and the is overall "
    "the aim is to ensure that the text is cleaned properly punctuations are removed "
    "and meaningful words are retained this text is for testing the functions ability "
    "to preprocess a larger input effectively"
)

test_text_2 = (
    "In today's fast-paced world, we often forget to take a step back and appreciate the "
    "little things. Life is full of ups and downs; sometimes we feel happy, but at other times, "
    "we may feel sad. Words like 'joyful', 'elated', and 'thrilled' capture our positive emotions, "
    "while 'disappointed', 'frustrated', and 'angry' reflect our negative experiences. "
    "It's essential to recognize these feelings. By doing so, we can manage our emotions better. "
    "Additionally, stopwords such as 'in', 'and', 'the', and 'to' should be filtered out. "
    "Ultimately, we want to ensure that the core message of the text remains clear and concise."
)

expected_cleaned_text_2 = (
    "in todays fastpaced world we often forget to take a step back and appreciate the "
    "little things life is full of ups and downs sometimes we feel happy but at other "
    "times we may feel sad words like joyful elated and thrilled capture our positive "
    "emotions while disappointed frustrated and angry reflect our negative experiences "
    "its essential to recognize these feelings by doing so we can manage our emotions better "
    "additionally stopwords such as in and the and to should be filtered out ultimately "
    "we want to ensure that the core message of the text remains clear and concise"
)


def test_preprocess_text(tmp_path):
    temp_file = tmp_path / "test.txt"
    temp_file.write_text(test_text, encoding='utf-8')
    
    # Call the preprocess_text function
    cleaned_text, processed_words = preprocess_text(str(temp_file))
    
    # Test cleaned text
    assert cleaned_text == expected_cleaned_text
    
    # Test processed words
    stop_words = stopwords.words('english')
    for word in processed_words:
        assert word not in stop_words, (
            f"Unexpected stop word found in processed words: '{word}'"
        )

    temp_file.write_text(test_text_2, encoding='utf-8')
    
    # Call the preprocess_text function
    cleaned_text, processed_words = preprocess_text(str(temp_file))
    
    # Test cleaned text
    assert cleaned_text == expected_cleaned_text_2
    
    # Test processed words
    stop_words = stopwords.words('english')
    for word in processed_words:
        assert word not in stop_words, (
            f"Unexpected stop word found in processed words: '{word}'"
        )

def test_check_emotions():
    test_words_list = ["joyless", "optionless", "fidgety"]
    expected_emotions = ["sad", "entitled", "fearful"]
    emotions_list = check_emotions(test_words_list)
    assert emotions_list == expected_emotions, (f" emotions_list: {emotions_list} expected_emotions: {expected_emotions}")
    
    test_words_list_2 = ['laughting','loving','manipulated']
    expected_emotions_2 =['happy','attached','cheated']
    emotions_list_2 = check_emotions(test_words_list_2)
    assert emotions_list_2 == expected_emotions_2, (f" emotions_list: {emotions_list_2} expected_emotions: {expected_emotions_2}")

def test_analyse_sentiment():
    positive_sentiment = analyse_sentiment("I love this product!")
    negative_sentiment = analyse_sentiment("I hate waiting in line.")
    neutral_sentiment = analyse_sentiment("The sky is blue.")

    assert positive_sentiment == "Positive Sentiment"
    assert negative_sentiment == "Negative Sentiment"
    assert neutral_sentiment == "Neutral Sentiment"

def test_visualize_emotions():
    # We can test the visualization function but it produces a plot,
    # so we'll only check if it runs without error here.
    try:
        visualize_emotions("Positive Sentiment", ["happy", "joy", "amazing"])
        visualize_emotions("Negative Sentiment", ["sad", "fearful", "angry"])
        assert True
    except Exception as e:
        pytest.fail(f"visualize_emotions raised an exception: {e}")


pytest.main(["-v", "--tb=line", "-rN", __file__])

