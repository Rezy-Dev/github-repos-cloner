import tkinter as tk
import git


def clone_repo():
    # Get the repository URL and local directory path from the input fields
    repo_url = url_input.get()
    local_dir = dir_input.get()

    try:
        # Clone the repository to the local directory
        git.Repo.clone_from(repo_url, local_dir)
        status_label.config(
            text=f"Repository {repo_url} cloned to {local_dir}", fg="green"
        )
    except git.GitCommandError as e:
        # Display an error message if the repository cloning failed
        status_label.config(text=str(e), fg="red")


# Create a tkinter window and set its properties
window = tk.Tk()
window.title("GitHub Repository Cloner")
window.geometry("760x600")

# Add a background image to the window
bg_image = tk.PhotoImage(file="background.png")
bg_label = tk.Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Create a frame to hold the input fields and button
input_frame = tk.Frame(window, bg="#2e2e2e", bd=5)
input_frame.place(relx=0.5, rely=0.35, relwidth=0.9, relheight=0.3, anchor="center")

# Create a label and input field for the repository URL
url_label = tk.Label(
    input_frame,
    text="Repository URL:",
    bg="#2e2e2e",
    fg="white",
    font=("Helvetica", 12),
)
url_label.place(relx=0.05, rely=0.2, relwidth=0.2, relheight=0.2)
url_input = tk.Entry(input_frame, bg="white", fg="#2e2e2e", font=("Helvetica", 12))
url_input.place(relx=0.3, rely=0.2, relwidth=0.65, relheight=0.2)

# Create a label and input field for the local directory path
dir_label = tk.Label(
    input_frame,
    text="Local Directory:",
    bg="#2e2e2e",
    fg="white",
    font=("Helvetica", 12),
)
dir_label.place(relx=0.05, rely=0.6, relwidth=0.2, relheight=0.2)
dir_input = tk.Entry(input_frame, bg="white", fg="#2e2e2e", font=("Helvetica", 12))
dir_input.place(relx=0.3, rely=0.6, relwidth=0.65, relheight=0.2)

# Create a button to start the cloning process
clone_button = tk.Button(
    window,
    text="Clone Repository",
    bg="#2e2e2e",
    fg="white",
    font=("Helvetica", 12),
    command=clone_repo,
)
clone_button.place(relx=0.5, rely=0.7, relwidth=0.3, relheight=0.1, anchor="center")

# Create a label to display the cloning status
status_label = tk.Label(
    window, text="", bg="#2e2e2e", fg="white", font=("Helvetica", 12)
)
status_label.place(relx=0.5, rely=0.85, anchor="center")

# Make the input fields and button responsive to window size
def on_resize(event):
    input_frame.place_configure(relwidth=0.9 * event.width / 400)
    url_label.place_configure(relwidth=0.2 * (event.width / 400))
    url_input.place_configure(relwidth=0.65 * (event.width / 400))
    dir_label.place_configure(relwidth=0.2 * (event.width / 400))
    dir_input.place_configure(relwidth=0.65 * (event.width / 400))
    clone_button.place_configure(relwidth=0.3 * (event.width / 400))


window.mainloop()
