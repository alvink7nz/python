import time
import random

# Existing functions
def typing_test(rounds=3):
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "A journey of a thousand miles begins with a single step.",
        "To be or not to be, that is the question.",
        "All that glitters is not gold.",
        "In the end, we only regret the chances we didn't take."
    ]

    total_time = 0
    total_words_typed = 0
    mistake_dict = {}  # Dictionary to track mistakes

    
    sentence = random.choice(sentences)

    print(f"\nType the following sentence as quickly and accurately as you can.")
    print("Sentence: ", sentence)
    input("Press Enter when you are ready to start...")

    start_time = time.time()
    user_input = input("\nStart typing here: ")
    end_time = time.time()

    elapsed_time = end_time - start_time
    total_time += elapsed_time

    words_typed = len(user_input.split())
    total_words_typed += words_typed

    typing_speed = round(words_typed / (elapsed_time / 60), 1)  # Round speed to 1 decimal place
    accuracy = calculate_accuracy(sentence, user_input)
    real_speed = typing_speed * accuracy
    real_speed = real_speed / 100

    print("\nTest completed!")
    print(f"Typing Speed: {typing_speed:.0f} WPM")  # Display rounded typing speed
    print(f"Accuracy: {accuracy:.0f}%")
    print(f"Real Speed: {typing_speed:.0f} WPM x {accuracy:.0f}% = {real_speed:.0f} WPM")


def calculate_accuracy(reference, typed):
    reference_words = reference.split()
    typed_words = typed.split()

    correct_words = 0
    for ref_word, typed_word in zip(reference_words, typed_words):
        if ref_word == typed_word:
            correct_words += 1

    return (correct_words / len(reference_words)) * 100


if __name__ == "__main__":
    playing = True
    while playing:
        typing_test()
        playing_letter = input("Again? (y/n)")
        if playing_letter == "y":
            playing = True
        else:
            playing = False
