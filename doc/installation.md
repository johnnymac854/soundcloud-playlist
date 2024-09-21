# Installation

Follow these steps to set up the SoundCloud Playlist Duplicator on your macOS machine.

## 0. Clone the Repository

Clone the SoundCloud Playlist Duplicator repository to your local machine.

```bash
git clone https://github.com/yourusername/soundcloud_playlist_duplicator.git
cd soundcloud_playlist_duplicator
```

*Replace `yourusername` with your actual GitHub username if applicable.*

## 1. Install pyenv

**pyenv** is a powerful tool for managing multiple Python versions and virtual environments. It allows you to easily switch between different Python versions, ensuring compatibility and ease of development across various projects.

### Install pyenv using Homebrew:

Homebrew is a popular package manager for macOS. If you don't have Homebrew installed, you can install it by following the instructions at [https://brew.sh/](https://brew.sh/).

Once Homebrew is installed, open your Terminal and run:

```bash
brew update
brew install pyenv
brew install pyenv-virtualenv
```

## 2. Configure Your Shell for pyenv and virtualenv

Ref: https://github.com/pyenv/pyenv?tab=readme-ov-file

To enable pyenv in your shell, you need to add its initialization commands to your shell configuration file. Since macOS uses **zsh** by default, you'll modify the `~/.zshrc` file.

### Add pyenv to `~/.zshrc`:

Run the following commands to add these lines to the end of your file:

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
```

**Explanation:**

- `export PYENV_ROOT="$HOME/.pyenv"`: Sets the root directory where pyenv stores its files.
- `[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"`: Adds pyenv's binary directory to your system's `PATH` so you can use pyenv commands.
- `eval "$(pyenv init --path)"`: Initializes pyenv.
- `eval "$(pyenv virtualenv-init -)"`: Initializes pyenv-virtualenv, enabling virtual environment management.

### Apply the Changes:

Reload your shell configuration to apply the changes:

```bash
source ~/.zshrc
```

## 3. Install Python 3.8.14 with pyenv

With pyenv installed and configured, you can now install Python 3.8.14.

### Install Python 3.8.14:

Run the following command to install Python version 3.8.14:

```bash
pyenv install 3.8.14
```

**Note:** The installation process may take a few minutes as pyenv compiles Python from source.

## 4. Create a Virtual Environment with pyenv-virtualenv

**virtualenv** is a tool to create isolated Python environments. Using virtual environments ensures that your project dependencies are managed separately from your system-wide Python packages, preventing version conflicts and maintaining a clean development environment.

With pyenv-virtualenv integrated, you can create virtual environments tied to specific Python versions.

### Create a Virtual Environment Named `soundcloud-playlist`:

```bash
pyenv virtualenv 3.8.14 soundcloud-playlist
```

**Explanation:**

- `3.8.14`: Specifies the Python version for the virtual environment.
- `soundcloud-playlist`: The name of the virtual environment.

## 5. Activate the Virtual Environment

Activate the newly created virtual environment to start using it.

```bash
pyenv activate soundcloud-playlist
```

**Verify Activation:**

Ensure that the virtual environment is active by checking the Python version:

```bash
python --version
```

You should see:

```
Python 3.8.14
```

## 6. Install Dependencies Using pip-compile

To manage dependencies efficiently, this project uses **pip-tools**, which provides the `pip-compile` tool. This tool allows you to maintain a `requirements.in` file with your top-level dependencies and generate a fully pinned `requirements.txt` file.

### Install pip-tools:

```bash
pip install pip-tools
```

### Compile `requirements.txt` from `requirements.in`:

Assuming you have a `requirements.in` file in your project directory that lists your top-level dependencies, run:

```bash
pip-compile requirements.in --no-emit-index-url -o requirements.txt
```

**Explanation:**

- `pip-compile requirements.in`: Generates a `requirements.txt` file with all dependencies and their pinned versions based on the specifications in `requirements.in`.

### Install Dependencies:

Now, install the dependencies listed in the generated `requirements.txt`:

```bash
pip install -r requirements.txt
```

**Note:** This ensures that all packages are installed with the exact versions specified, providing a consistent environment.

---