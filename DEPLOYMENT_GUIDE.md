# 🚀 How to Deploy to the Cloud

Since I am an AI assistant running on your machine, I cannot log into your private cloud accounts (like Vercel or Heroku). However, I have made the project **"Cloud Ready"** with the necessary configuration files.

Here is the fastest way to deploy this for free:

## Option 1: Instant Public Demo (No Account Needed)
Use **ngrok** to share your running local app with the world instantly.
1.  Download [ngrok](https://ngrok.com/download).
2.  Open a new terminal.
3.  Run: `ngrok http 8000`
4.  Copy the `https://...` link shown.
5.  **Send that link to anyone.** They can now see your app!

---

## Option 2: Permanent Deployment (Render.com)
This is best for a permanent URL for your resume/portfolio.

1.  **Push code to GitHub**:
    *   Initialize git: `git init`
    *   Add files: `git add .`
    *   Commit: `git commit -m "Initial commit"`
    *   Create a repo on GitHub and push.

2.  **Deploy Backend (Render)**:
    *   Go to [Render.com](https://render.com) > New > Web Service.
    *   Connect your GitHub repo.
    *   **Build Command**: `pip install -r requirements.txt`
    *   **Start Command**: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
    *   Click "Deploy". You will get a backend URL (e.g., `https://fatality-api.onrender.com`).

3.  **Update Frontend**:
    *   Open `frontend/script.js`.
    *   Change `const API_URL = 'http://localhost:8000';` to your new Render URL.

4.  **Deploy Frontend (Vercel/Netlify)**:
    *   Drag and drop the `frontend` folder to [Netlify Drop](https://app.netlify.com/drop).
    *   Done! You have a live website.
