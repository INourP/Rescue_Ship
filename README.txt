RESCUE SHIP - deployment package for Render

1) Extract this ZIP.
2) Upload the three files (rescue_ship.py, requirements.txt, render.yaml) to a new GitHub repository.
3) On Render, choose New + -> Blueprint, connect the GitHub repository, and deploy.
4) Render will install requirements and start the Flask app with Gunicorn.
5) When deployment finishes, copy the public https://...onrender.com URL and share it.

Note: The free Render instance may sleep when idle and take a little time to wake up.
The app is configured to use Render's PORT environment variable and listen on all interfaces.
