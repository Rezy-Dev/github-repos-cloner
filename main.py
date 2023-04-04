import tkinter as tk
import git


def clone_repo():
    repo_url = url_input.get()
    local_dir = dir_input.get()

    try:
        git.Repo.clone_from(repo_url, local_dir)
        status_label.config(
            text=f"Repository {repo_url} cloned to {local_dir}", fg="green"
        )
    except git.GitCommandError as e:
        status_label.config(text=str(e), fg="red")


window = tk.Tk()
window.title("GitHub Repository Cloner")
window.geometry("760x600")
window.resizable(False, False)
window.iconbitmap("icon.ico")

window.call("wm", "iconphoto", window._w, tk.PhotoImage(file="icon.png"))

bg_image = tk.PhotoImage(file="background.png")
bg_label = tk.Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

input_frame = tk.Frame(window, bg="#2e2e2e", bd=5)
input_frame.place(relx=0.5, rely=0.35, relwidth=0.9, relheight=0.3, anchor="center")

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

clone_button = tk.Button(
    window,
    text="Clone Repository",
    bg="#2e2e2e",
    fg="white",
    font=("Helvetica", 12),
    command=clone_repo,
)
clone_button.place(relx=0.5, rely=0.7, relwidth=0.3, relheight=0.1, anchor="center")

status_label = tk.Label(
    window, text="", bg="#2e2e2e", fg="white", font=("Helvetica", 12)
)
status_label.place(relx=0.5, rely=0.85, anchor="center")


def on_resize(event):
    bg_image_resized = bg_image.subsample(int(bg_image.width() / event.width))

    bg_label.config(image=bg_image_resized)

    input_frame.place_configure(relwidth=0.9 * event.width / 760)

    font_size = max(int(12 * event.width / 760), 8)

    url_label.config(font=("Helvetica", font_size))
    url_input.config(font=("Helvetica", font_size))

    dir_label.config(font=("Helvetica", font_size))
    dir_input.config(font=("Helvetica", font_size))

    clone_button.config(font=("Helvetica", font_size))

    url_label.place_configure(relx=0.05, rely=0.2, relwidth=0.2 * event.width / 760)
    url_input.place_configure(relx=0.3, rely=0.2, relwidth=0.65 * event.width / 760)

    dir_label.place_configure(relx=0.05, rely=0.6, relwidth=0.2 * event.width / 760)
    dir_input.place_configure(relx=0.3, rely=0.6, relwidth=0.65 * event.width / 760)

    clone_button.place_configure(relx=0.5, rely=0.7, relwidth=0.3 * event.width / 760)

    bg_image = bg_image.subsample(int(bg_image.width() / event.width))

    url_label.place_configure(relwidth=0.2)
    url_input.place_configure(relwidth=0.65)

    dir_label.place_configure(relwidth=0.2)
    dir_input.place_configure(relwidth=0.65)

    clone_button.place_configure(relwidth=0.3)


window.bind("<Configure>", on_resize)

window.mainloop()
