<div align="center">

# PaperViz

<p align="center">
  <strong>A Manim-based Animation Toolkit for Visualizing Research Papers</strong>
</p>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

</div>

## 📖 About The Project

**PaperViz** is a toolkit that transforms complex research papers into engaging visual animations using [Manim Community Edition](https://www.manim.community/). Each paper is broken down into key concepts and visualized through carefully crafted animations, making it easier to understand and share cutting-edge research.

### Why PaperViz?

- 🎬 **Visual Learning**: Transform dense academic papers into intuitive animations
- 🚀 **Easy to Use**: Simple CLI interface with Docker containerization
- 🔄 **Reproducible**: Consistent rendering environment across all platforms
- 📚 **Expandable**: Easy to add new papers and concepts
- 🎨 **Professional**: High-quality animations powered by Manim

---

## 🚀 Getting Started

### Prerequisites

Before using PaperViz, ensure you have the following installed:

- **Docker & Docker Compose**: Required for containerized rendering
- **Git**: For version control
- **Bash**: For running the main script

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/pomelo925/PaperViz.git
   cd PaperViz
   ```

2. Make the run script executable:

   ```bash
   chmod +x run.sh
   ```

3. Build the Docker image (first time only):

   ```bash
   docker compose -f docker/compose.cpu.yml build
   ```

---

## 🎯 Usage

PaperViz provides two ways to render animations:

### Interactive Mode

Simply run the script without arguments to see an interactive menu:

```bash
./run.sh
```

You'll see a menu like this:

```
╔════════════════════════════════════════════════════════════════╗
║                         PaperViz                               ║
║              Manim Animation Toolkit for Papers                ║
╚════════════════════════════════════════════════════════════════╝

Select a paper to visualize:

  [1] PLD: SELF-IMPROVING VISION-LANGUAGE-ACTION MODELS WITH DATA GENERATION VIA RESIDUAL RL
  [2] (Reserved for future paper)
  [3] (Reserved for future paper)

  [0] Exit

Enter paper ID:
```

### Direct Mode

Render a specific paper directly by providing its ID:

```bash
./run.sh 1    # Renders Paper ID 1 (PLD)
```

### Output

Rendered animations are saved to:

```
workspace/media/videos/
```

---

## 📚 Available Papers

| ID | Paper Title | Status | Script |
|----|-------------|--------|--------|
| 1  | **PLD: SELF-IMPROVING VISION-LANGUAGE-ACTION MODELS WITH DATA GENERATION VIA RESIDUAL RL** | ✅ Available | `papers/1_pld/pld_scene.py` |
| 2  | *(Reserved for future paper)* | 🔜 Coming Soon | - |
| 3  | *(Reserved for future paper)* | 🔜 Coming Soon | - |

---

## 📁 Project Structure

```
PaperViz/
├── run.sh                          # Main execution script
├── docker/                         # Docker configuration
│   ├── dockerfile.cpu              # Manim environment Dockerfile
│   └── compose.cpu.yml             # Docker Compose configuration
├── .github/                        # GitHub workflows
│   └── workflows/
│       └── docker.cpu.yml          # CI/CD for Docker image
├── workspace/                      # Main workspace (mounted in container)
│   ├── media/                      # Rendered animation output
│   └── papers/                     # Paper-specific scripts
│       ├── 1_pld/
│       │   ├── pld_scene.py        # Manim scenes for PLD paper
│       │   └── README.md           # Paper-specific documentation
│       ├── 2_xxx/                  # Future papers...
│       └── 3_xxx/
└── README.md                       # This file
```

---

## 🤝 Contributing

We welcome contributions! Here's how to add a new paper:

### Adding a New Paper

1. **Create a new folder** in `workspace/papers/`:

   ```bash
   mkdir -p workspace/papers/[ID]_[paper_name]
   ```

2. **Create the Manim scene file**:

   ```bash
   touch workspace/papers/[ID]_[paper_name]/scene.py
   ```

3. **Write your Manim animations** in the scene file. See `papers/1_pld/pld_scene.py` for examples.

4. **Update `run.sh`** to include your paper:

   ```bash
   # Add to PAPERS array
   PAPERS[2]="YOUR PAPER TITLE"
   
   # Add script path
   PAPER_SCRIPTS[2]="papers/2_yourpaper/scene.py"
   
   # Add scene name
   PAPER_SCENES[2]="YourMainScene"
   ```

5. **Create a README** for your paper:

   ```bash
   touch workspace/papers/[ID]_[paper_name]/README.md
   ```

6. **Test your animation**:

   ```bash
   ./run.sh [ID]
   ```

### Development Workflow

For development and debugging, you can enter the container directly:

```bash
docker compose -f docker/compose.cpu.yml run --rm manim /bin/bash
```

Inside the container, you can run Manim commands manually:

```bash
# Render in low quality for quick preview
manim -ql papers/1_pld/pld_scene.py PLDIntro

# Render in high quality
manim -qh papers/1_pld/pld_scene.py PLDComplete

# Preview specific scene
manim -p papers/1_pld/pld_scene.py PLDWorkflow
```

---

## 🛠️ Technical Details

### Docker Image

The Docker image includes:

- **Base**: Ubuntu 22.04
- **Python**: Python 3 with pip
- **Manim**: Manim Community Edition
- **FFmpeg**: For video rendering
- **LaTeX**: For mathematical typesetting (texlive-full)
- **Scientific Libraries**: NumPy, SciPy, Matplotlib

### Manim Quality Options

- `-ql`: Low quality (854x480, 15fps) - Fast preview
- `-qm`: Medium quality (1280x720, 30fps)
- `-qh`: High quality (1920x1080, 60fps)
- `-qk`: 4K quality (3840x2160, 60fps)

### Flags

- `-p`: Preview after rendering
- `-s`: Save last frame as image
- `-i`: Show file in finder after rendering

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 🙏 Acknowledgments

- [Manim Community Edition](https://www.manim.community/) - The animation engine
- All paper authors whose work we visualize
- Contributors to this project

---

<div align="center">

## Contributors

<a href="https://github.com/pomelo925/PaperViz/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=pomelo925/PaperViz" alt="Contributors" />
</a>

</div>

---

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/pomelo925/PaperViz.svg?style=for-the-badge
[contributors-url]: https://github.com/pomelo925/PaperViz/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/pomelo925/PaperViz.svg?style=for-the-badge
[forks-url]: https://github.com/pomelo925/PaperViz/network/members
[stars-shield]: https://img.shields.io/github/stars/pomelo925/PaperViz.svg?style=for-the-badge
[stars-url]: https://github.com/pomelo925/PaperViz/stargazers
[issues-shield]: https://img.shields.io/github/issues/pomelo925/PaperViz.svg?style=for-the-badge
[issues-url]: https://github.com/pomelo925/PaperViz/issues
[license-shield]: https://img.shields.io/github/license/pomelo925/PaperViz.svg?style=for-the-badge
[license-url]: https://github.com/pomelo925/PaperViz/blob/main/LICENSE
