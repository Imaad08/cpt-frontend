import random

comments = []

def add_comment(meme, comment_text, rating, pin):
    comments.append({"meme": meme, "comment_text": comment_text, "rating": rating, "likes": 0, "pin": pin})

add_comment("Pepe the Frog", "Controversial meme, has evolved into a symbol of various internet subcultures.", 3, str(random.randint(1000, 9999)))
add_comment("Distracted Boyfriend", "Relatable meme, depicts a common situation in a humorous way.", 4, str(random.randint(1000, 9999)))
add_comment("Woman Yelling at a Cat", "Hilarious meme, the contrast between the woman's anger and the cat's nonchalant expression is gold.", 5, str(random.randint(1000, 9999)))
add_comment("Drake Hotline Bling", "Simple yet effective meme, conveys different emotions with the same image.", 4, str(random.randint(1000, 9999)))
add_comment("Confused Nick Young", "Funny meme, captures the moment of confusion perfectly.", 4, str(random.randint(1000, 9999)))
add_comment("Surprised Pikachu", "Cute meme, the expression on Pikachu's face is priceless.", 4, str(random.randint(1000, 9999)))
add_comment("Evil Kermit", "Relatable meme, shows the inner conflict between good and bad impulses.", 3, str(random.randint(1000, 9999)))
add_comment("Hide the Pain Harold", "Classic meme, Harold's smile hides a world of pain.", 4, str(random.randint(1000, 9999)))
add_comment("Arthur Fist", "Great reaction meme, very versatile.", 4, str(random.randint(1000, 9999)))
add_comment("Expanding Brain", "Clever concept, always funny to see the progression.", 5, str(random.randint(1000, 9999)))
add_comment("Is This a Pigeon?", "Classic misunderstanding meme, never gets old.", 4, str(random.randint(1000, 9999)))
add_comment("Mocking SpongeBob", "Simple yet effective, captures sarcasm perfectly.", 5, str(random.randint(1000, 9999)))
add_comment("Trollface", "Overused and outdated, not funny anymore.", 2, str(random.randint(1000, 9999)))
add_comment("Bad Luck Brian", "Was funny at first but now feels forced.", 3, str(random.randint(1000, 9999)))
add_comment("Success Kid", "Used to be funny, now just feels tired.", 2, str(random.randint(1000, 9999)))
add_comment("Forever Alone", "Depressing meme, not enjoyable.", 1, str(random.randint(1000, 9999)))

def edit_comment(meme, new_comment_text, new_rating, pin):
    for comment in comments:
        if comment["meme"] == meme and comment["pin"] == pin:
            comment["comment_text"] = new_comment_text
            comment["rating"] = new_rating
            print(f"\nComment on meme '{meme}' has been updated.\n")
            return
    print("\nEither the comment does not exist or the provided PIN is incorrect.\n")

def like_comment(meme):
    for comment in comments:
        if comment['meme'] == meme:
            comment['likes'] += 1
            print(f"\nComment '{comment['comment_text']}' on meme '{meme}' has been liked. Total likes: {comment['likes']}\n")
            return
    print(f"\nComment on meme '{meme}' not found.\n")

def get_random_comments(num_comments):
    for comment in random.sample(comments, min(num_comments, len(comments))):
        print(f"\nmeme: {comment['meme']}")
        print(f"comment: {comment['comment_text']}")
        print(f"Rating: {comment['rating']} out of 5")
        print(f"Likes: {comment['likes']}\n")

def print_comments_by_rating(desired_rating):
    matching_comments = []
    for comment in comments:
        if comment['rating'] == desired_rating:
            matching_comments.append(comment)
    for comment in matching_comments:
        print(f"\nmeme: {comment['meme']}")
        print(f"comment: {comment['comment_text']}")
        print(f"Rating: {comment['rating']} out of 5")
        print(f"Likes: {comment['likes']}\n")

while True:
    print("1. Add a comment")
    print("2. Edit a comment")
    print("3. Like a comment")
    print("4. Get random comments")
    print("5. Print comments by rating")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        meme = input("Enter the meme name: ")
        comment_text = input("Enter your comment: ")
        rating = int(input("Enter the rating (1-5): "))
        pin = str(random.randint(1000, 9999))
        add_comment(meme, comment_text, rating, pin)
        print("Your comment has been added!\n")
        print(f"Your PIN is: {pin}\n")
    elif choice == "2":
        meme = input("Enter the meme name: ")
        pin = input("Enter your PIN: ")
        new_comment_text = input("Enter the new comment text: ")
        new_rating = int(input("Enter the new rating (1-5): "))
        edit_comment(meme, new_comment_text, new_rating, pin)
    elif choice == "3":
        meme = input("Enter the meme name: ")
        like_comment(meme)
    elif choice == "4":
        num_comments = int(input("Enter the number of random comments you want to see: "))
        get_random_comments(num_comments)
    elif choice == "5":
        desired_rating = int(input("Enter the rating (1-5) of comments you want to filter by: "))
        print_comments_by_rating(desired_rating)
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.\n")