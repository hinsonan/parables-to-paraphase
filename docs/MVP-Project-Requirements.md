# MVP Requirements: Preacher Audio Transcription API
**Modular FastAPI for Sermon Processing**

## Overview
A FastAPI service with separate endpoints for each processing step: transcribe sermons, translate text, and summarize content.

---

## API Endpoints

### POST `/transcribe`
**Purpose**: Convert sermon audio to English text

**Request**:
```json
{
  "file": "sermon.mp3" (multipart form data)
}
```

**Response**:
```json
{
  "transcript": "Today's sermon focuses on faith and perseverance...",
  "timestamps": [
    {"start": 0.0, "end": 5.2, "text": "Good morning, church family"},
    {"start": 5.2, "end": 12.1, "text": "Today we'll explore Matthew 5:16"}
  ],
  "duration": 3600.5,
  "processing_time": 180.2
}
```

### POST `/translate`
**Purpose**: Translate English text to Spanish

**Request**:
```json
{
  "text": "Today's sermon focuses on faith and perseverance in difficult times.",
  "target_language": "spanish"
}
```

**Response**:
```json
{
  "original_text": "Today's sermon focuses on faith...",
  "translated_text": "El sermón de hoy se centra en la fe y la perseverancia...",
  "target_language": "spanish",
  "processing_time": 2.1
}
```

### POST `/summarize`
**Purpose**: Generate key points summary from sermon text

**Request**:
```json
{
  "text": "Full sermon transcript...",
  "summary_type": "key_points",
  "max_length": 200
}
```

**Response**:
```json
{
  "original_length": 2500,
  "summary": "Key sermon points: 1. Faith sustains us through trials 2. Prayer is essential for spiritual growth 3. Community support strengthens believers",
  "summary_type": "key_points",
  "summary_length": 156,
  "processing_time": 3.4
}
```

### GET `/health`
**Purpose**: Service health check

**Response**:
```json
{
  "status": "healthy",
  "models_loaded": ["whisper", "translator", "summarizer"],
  "uptime": 86400
}
```

---

## Technical Implementation

### Tech Stack
- **API**: FastAPI
- **ML**: PyTorch + Hugging Face Transformers

---

## Functional Requirements

### `/transcribe` Endpoint
- [ ] Accept MP3/WAV files (max 100MB)
- [ ] Support sermon recordings up to 2 hours
- [ ] Generate timestamped transcripts
- [ ] Handle multiple speakers (pastor, congregation responses)
- [ ] Optimize for religious/theological vocabulary

### `/translate` Endpoint
- [ ] Translate English text to Spanish
- [ ] Preserve theological terminology
- [ ] Handle both short phrases and full transcripts
- [ ] Maintain proper punctuation and formatting
- [ ] Support batch translation for efficiency

### `/summarize` Endpoint
- [ ] Generate key sermon points
- [ ] Support different summary types (bullet points, paragraphs)
- [ ] Configurable summary length (50-500 words)
- [ ] Preserve main theological concepts
- [ ] Maintain scripture references

---

## Usage Workflows

### Complete Sermon Processing
```bash
# Step 1: Transcribe audio
curl -X POST "/transcribe" -F "file=@sunday_sermon.mp3"

# Step 2: Summarize transcript
curl -X POST "/summarize" -d '{"text": "transcript_text", "summary_type": "key_points"}'

# Step 3: Translate both transcript and summary
curl -X POST "/translate" -d '{"text": "transcript_text", "target_language": "spanish"}'
curl -X POST "/translate" -d '{"text": "summary_text", "target_language": "spanish"}'
```

### Individual Services
```bash
# Just translation for existing text
curl -X POST "/translate" -d '{"text": "God loves you", "target_language": "spanish"}'

# Just summarization for study notes
curl -X POST "/summarize" -d '{"text": "long_study_notes", "max_length": 100"}'
```

---

## Performance Requirements

- **Transcription**: 1-hour sermon processed in <5 minutes
- **Translation**: 1000 words translated in <10 seconds
- **Summarization**: Summary generated in <20 seconds
- **Concurrent requests**: Support 3-5 simultaneous users
- **Response time**: <2 seconds for non-processing endpoints

---

## Success Criteria

### Quality Metrics
- **Transcription**: >90% accuracy for clear sermon audio
- **Translation**: Theologically appropriate Spanish translations
- **Summarization**: Captures main sermon themes and scripture references

### Usability
- **Modularity**: Each service works independently
- **Flexibility**: Mix and match services as needed
- **Reliability**: Consistent results for weekly sermon processing

---

## Development Timeline

- **Week 1-2**: FastAPI setup + `/transcribe` endpoint
- **Week 3-4**: `/translate` endpoint implementation
- **Week 5-6**: `/summarize` endpoint + integration
- **Week 7-8**: Testing, optimization, documentation
