from flask import Flask, request, jsonify

app = Flask(__name__)

# Expanded Dummy Book Data
book_data = {
    "romance": [
        {"title": "Pride and Prejudice", "author": "Jane Austen"},
        {"title": "Me Before You", "author": "Jojo Moyes"},
        {"title": "The Notebook", "author": "Nicholas Sparks"}
    ],
    "thriller": [
        {"title": "Gone Girl", "author": "Gillian Flynn"},
        {"title": "The Girl with the Dragon Tattoo", "author": "Stieg Larsson"},
        {"title": "The Da Vinci Code", "author": "Dan Brown"}
    ],
    "motivational": [
        {"title": "Atomic Habits", "author": "James Clear"},
        {"title": "The Power of Now", "author": "Eckhart Tolle"},
        {"title": "Think and Grow Rich", "author": "Napoleon Hill"}
    ],
    "mystery": [
        {"title": "Murder on the Orient Express", "author": "Agatha Christie"},
        {"title": "The Hound of the Baskervilles", "author": "Arthur Conan Doyle"},
        {"title": "Big Little Lies", "author": "Liane Moriarty"}
    ],
    "horror": [
        {"title": "It", "author": "Stephen King"},
        {"title": "The Haunting of Hill House", "author": "Shirley Jackson"},
        {"title": "Bird Box", "author": "Josh Malerman"}
    ],
    "fantasy": [
        {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling"},
        {"title": "The Hobbit", "author": "J.R.R. Tolkien"},
        {"title": "Percy Jackson & The Olympians", "author": "Rick Riordan"}
    ],
    "science fiction": [
        {"title": "Dune", "author": "Frank Herbert"},
        {"title": "Ender's Game", "author": "Orson Scott Card"},
        {"title": "Ready Player One", "author": "Ernest Cline"}
    ],
    "biography": [
        {"title": "Steve Jobs", "author": "Walter Isaacson"},
        {"title": "Becoming", "author": "Michelle Obama"},
        {"title": "Wings of Fire", "author": "A.P.J. Abdul Kalam"}
    ],
    "historical": [
        {"title": "The Book Thief", "author": "Markus Zusak"},
        {"title": "All the Light We Cannot See", "author": "Anthony Doerr"},
        {"title": "Wolf Hall", "author": "Hilary Mantel"}
    ],
    "comedy": [
        {"title": "Bossypants", "author": "Tina Fey"},
        {"title": "Good Omens", "author": "Neil Gaiman & Terry Pratchett"},
        {"title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams"}
    ],
    "inspiring": [
        {"title": "The Alchemist", "author": "Paulo Coelho"},
        {"title": "Man’s Search for Meaning", "author": "Viktor Frankl"},
        {"title": "Awaken the Giant Within", "author": "Tony Robbins"}
    ],
    "emotional": [
        {"title": "A Thousand Splendid Suns", "author": "Khaled Hosseini"},
        {"title": "The Fault in Our Stars", "author": "John Green"},
        {"title": "The Kite Runner", "author": "Khaled Hosseini"}
    ],
    "funny": [
        {"title": "Diary of a Wimpy Kid", "author": "Jeff Kinney"},
        {"title": "Catch-22", "author": "Joseph Heller"},
        {"title": "Yes Please", "author": "Amy Poehler"}
    ],
    "dark": [
        {"title": "American Psycho", "author": "Bret Easton Ellis"},
        {"title": "1984", "author": "George Orwell"},
        {"title": "The Road", "author": "Cormac McCarthy"}
    ],
    "light-hearted": [
        {"title": "Eleanor Oliphant is Completely Fine", "author": "Gail Honeyman"},
        {"title": "The Rosie Project", "author": "Graeme Simsion"},
        {"title": "Where’d You Go, Bernadette", "author": "Maria Semple"}
    ]
}

@app.route("/recommend", methods=["POST"])
def recommend_books():
    data = request.json
    user_input = data.get("user_input", "").lower()

    # Try exact match
    recommendations = book_data.get(user_input)

    # If not found, try partial match (e.g., "romantic" → "romance")
    if not recommendations:
        for key in book_data:
            if key in user_input:
                recommendations = book_data[key]
                break

    # Fallback
    if not recommendations:
        recommendations = [
            {"title": "Sorry!", "author": "No books found for that category. Try another genre or mood."}
        ]

    return jsonify({"recommendations": recommendations})

if __name__ == "__main__":
    import os
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

