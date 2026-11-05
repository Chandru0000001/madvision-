# AI Text Summarizer – Testing Report

## 1. Project Information

**Project Name:** AI Text Summarizer

**Programming Language:** Python

**LLM Provider:** Google Gemini API

**Python Library:** Google GenAI SDK

## 2. Testing Objectives

The objective of testing is to verify that the AI Text Summarizer generates meaningful summaries for different types of input.

The application was tested using normal, long, short, technical, repeated, empty and unusual inputs.

## 3. Test Cases

| Test | Input Type         | Expected Result               |
| ---- | ------------------ | ----------------------------- |
| 1    | Normal paragraph   | Generate correct summary      |
| 2    | Long paragraph     | Generate short summary        |
| 3    | One sentence       | Summarize correctly           |
| 4    | Empty input        | Display validation error      |
| 5    | Numbers only       | Handle numerical input        |
| 6    | Technical content  | Identify technical topic      |
| 7    | Repeated sentences | Avoid unnecessary repetition  |
| 8    | Different language | Understand and summarize      |
| 9    | Random characters  | Handle unusual input          |
| 10   | Very long text     | Process text or handle errors |

## 4. Failures Identified

1. Gemini API returned a 503 error due to temporary high demand.
2. Empty input needed validation before sending the API request.
3. Unusual characters may produce meaningless summaries.
4. Very long text may exceed API input limits.

## 5. Improvements Made

1. Changed the LLM provider from OpenAI to Google Gemini.
2. Added input validation to prevent empty requests.
3. Implemented structured JSON output.
4. Added JSON response validation.
5. Added exception handling to manage API errors.
6. Improved the summarization prompt to generate simple and meaningful summaries.

## 6. Conclusion

The AI Text Summarizer was developed using Python and Google Gemini API.

The application accepts user-provided text and generates a short summary along with the main topic.

Different input types were used to evaluate the application's performance and reliability.

Testing helped identify potential failures and improve error handling and response validation.
