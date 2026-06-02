def get_response(query):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant for students."},
                {"role": "user", "content": query}
            ]
        )
        return response.choices[0].message.content

    except Exception:
        query = query.lower()

        # ---------------- PROGRAMMING ----------------
        if "python" in query:
            return "Python is a high-level programming language known for its simplicity and readability. It is widely used in web development, data science, AI, and automation."

        elif "java" in query or "oop" in query:
            return "OOP in Java is based on four main concepts: Encapsulation (data hiding), Inheritance (code reuse), Polymorphism (multiple forms), and Abstraction (hiding implementation details)."

        # ---------------- AI / ML ----------------
        elif "machine learning" in query or "ml" in query:
            return "Machine Learning is a subset of Artificial Intelligence where computers learn from data and improve their performance without being explicitly programmed."

        elif "ai" in query:
            return "Artificial Intelligence refers to machines designed to mimic human intelligence, such as learning, reasoning, and problem-solving."

        # ---------------- CAREER ----------------
        elif "data analyst" in query:
            return "To become a Data Analyst, you should learn Python, SQL, Excel, and visualization tools like Power BI or Tableau. Building projects is very important."

        elif "career" in query:
            return "Focus on building strong skills, working on real projects, and applying for internships. Consistency and practice are key."

        # ---------------- INTERVIEW ----------------
        elif "interview" in query:
            return "Prepare by practicing DSA, revising core subjects, and doing mock interviews. Also prepare HR questions like strengths and weaknesses."

        # ---------------- DEFAULT ----------------
        else:
            return "I can help with Programming, AI/ML, Career Guidance, and Interview Preparation. Please ask something related to these topics."