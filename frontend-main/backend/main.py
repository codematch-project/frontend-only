from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from fastapi.middleware.cors import CORSMiddleware


# Create a FastAPI app instance
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Replace with your frontend's origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the input model for the incoming request
class CodeRequest(BaseModel):
    code: str

# Define the output model for the response
class CodeResult(BaseModel):
    link: str
    metadata: Dict[str, str]

# Placeholder function that simulates finding top 10 similar codes
def find_top10(code: str):
    print("Received code:", code)  # Print the received code to verify it's being sent correctly
    """
    This is a placeholder for your actual function.
    Replace this with the real function that finds similar code snippets.
    """
    # Example data to simulate real results
    return [
        {"link": "https://example.com/code1", "metadata": {"language": "Python", "stars": "1500", "similarity": "80%"}},
        {"link": "https://example.com/code2", "metadata": {"language": "JavaScript", "stars": "1200", "similarity": "78%"}},
        # Add up to 10 results or dynamically generate based on your logic
    ]

@app.post("/process_code", response_model=List[CodeResult])
async def process_code(request: CodeRequest):
    code = request.code
    try:
        # Call the find_top10 function with the received code
        similar_codes = find_top10(code)
        return similar_codes  # Directly return the similar_codes list
    
    except Exception as e:
        # Handle any errors and return a 500 response if needed
        raise HTTPException(status_code=500, detail=str(e))

# Run the server if the file is executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
