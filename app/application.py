from flask import Flask, render_template, request, session, redirect, url_for
from markupsafe import Markup
import markdown
from dotenv import load_dotenv
from app.components.retriever import create_qa_chain
import os

# Load environment variables
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/", methods=["GET", "POST"])
def index():
    """Main route for chatbot interaction."""
    if "messages" not in session:
        session["messages"] = []

    if request.method == "POST":
        user_input = request.form.get("prompt", "").strip()

        if user_input:
            # Append user message
            session["messages"].append({"role": "user", "content": user_input})
            session.modified = True

            try:
                # Create QA chain and pass conversation history
                qa_chain = create_qa_chain()
                result = qa_chain(user_input, history=session.get("messages", []))

                # Convert Markdown output to HTML
                html_assistant_reply = str(Markup(markdown.markdown(result)))

                # Append assistant message
                session["messages"].append({"role": "assistant", "content": html_assistant_reply})
                session.modified = True

            except Exception as e:
                print(f"Error during QA chain execution: {e}")
                error_msg = "An error occurred while processing your request. Please check the server logs."
                return render_template(
                    "index.html",
                    messages=session.get("messages", []),
                    error=error_msg,
                )

        # Redirect to clear POST form and show updated chat
        return redirect(url_for("index"))

    # Render chat history
    return render_template("index.html", messages=session.get("messages", []))


@app.route("/clear")
def clear():
    """Clears the chat history from the session."""
    session.pop("messages", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
        use_reloader=False,
    )
