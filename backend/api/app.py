from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(title="Vertical Studio API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"status": "online", "message": "Vertical Studio API"}

@app.post("/api/documents/analyze")
async def analyze_document(file: UploadFile = File(...)):
    """
    Upload and analyze a document.
    This is a placeholder endpoint that will be implemented with actual document processing.
    """
    try:
        # Just return mock data for now
        return {
            "status": "success",
            "filename": file.filename,
            "analysis": {
                "document_type": "Real Estate Contract",
                "key_dates": [
                    {"label": "Closing Date", "value": "2023-12-15"}
                ],
                "contingencies": [
                    "Financing contingency expires on 2023-11-30",
                    "Inspection contingency expires on 2023-11-15"
                ]
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)), reload=True)