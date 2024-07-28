from flask import Flask, request, jsonify
import anthropic

app = Flask(__name__)

# Initialize the anthropic client
client = anthropic.Anthropic(
    api_key=""
    )

@app.route('/generate_response', methods=['POST'])
def generate_response():
    if request.method == 'POST':
        # Get user input from the request
        user_input = request.json.get('text')

        # Generate response using anthropic
        message = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=4000,
            temperature=0,
            system="Translate it into hindi.",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": user_input
                        }
                    ]
                }
            ]
        )

        # Extract and return the content from the response
        response_content = message.content[0].text
        return jsonify({'response': response_content})

if __name__ == '_main_':
    app.run(debug=True)
