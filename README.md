# AERI - Artificial Emotional & Reasoning Intelligence

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Pre--Alpha-orange.svg)]()

A developmental AI system that learns language and reasoning from the ground up, like a human child, through natural interaction and experience.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Quick Start](#quick-start)
- [Example Usage](#example-usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

**AERI** (Artificial Emotional & Reasoning Intelligence) is not another fine-tuned language model. It's a fundamentally different approach to artificial intelligence that starts from **zero linguistic knowledge** and learns language, reasoning, and social interaction through developmental learning—much like a human infant grows into a conversational partner.

### Core Philosophy
- **From Scratch Learning**: No pre-trained models, no linguistic databases, no pre-programmed grammar
- **Developmental Approach**: Progresses through stages of linguistic and cognitive development
- **Human-like Acquisition**: Learns through interaction, feedback, and experience
- **Embodied Cognition**: Text-only grounding in distributional semantics and interaction patterns

### Key Differentiators
| Aspect | Traditional AI | AERI |
|--------|---------------|------|
| **Starting Point** | Pre-trained on massive datasets | Zero linguistic knowledge |
| **Learning Method** | Pattern matching in existing data | Constructive learning from interaction |
| **Knowledge Source** | Statistical correlations | Grounded experiences and feedback |
| **Transparency** | Black box neural networks | Explainable developmental stages |

## Features

### **Cognitive Capabilities**
- **Language Acquisition from Zero**: Learns words, grammar, and pragmatics from interaction
- **Developmental Stages**: Progresses through pre-linguistic, lexical, combinatorial, and dialogic stages
- **Memory Systems**: Episodic, semantic, and statistical memory with associative learning
- **Reasoning Engine**: Symbolic and probabilistic inference based on learned knowledge

### **Interactive Learning**
- **Natural Interaction**: Learns through conversation with human teachers
- **Feedback-Driven**: Reinforcement learning from explicit and implicit feedback
- **Curiosity-Driven Exploration**: Intrinsic motivation to learn novel patterns
- **Self-Correction**: Ability to revise incorrect assumptions based on new evidence

### **Technical Infrastructure**
- **Modular Architecture**: Clean separation of perception, memory, learning, and generation
- **Extensible Design**: Plugin system for future capabilities (voice, vision, embodiment)
- **Research-Ready**: Comprehensive logging, evaluation metrics, and experimental protocols
- **Professional Codebase**: Type hints, comprehensive testing, and clear documentation

## Architecture
This document details the complete folder structure of the AERI project, organized by type and alphabetical order.

### Root Structure
```
AERI/
├── config/
├── data/
│ ├── logs/
│ ├── processed/
│ │ ├── grammar_rules/
│ │ └── vocabularies/
│ └── raw/
│ └── interactions/
│ └── YYYY-MM-DD/
├── docker/
├── docs/
│ ├── api/
│ ├── spec/
│ └── tutorials/
├── experiments/
│ ├── notebooks/
│ ├── protocols/
│ └── results/
│ ├── figures/
│ └── logs/
├── src/
│ ├── aeri/
│ │ ├── evaluation/
│ │ ├── generation/
│ │ ├── interaction/
│ │ ├── learning/
│ │ │ ├── grammar_induction/
│ │ │ ├── lexical/
│ │ │ └── reinforcement/
│ │ ├── memory/
│ │ │ ├── episodic/
│ │ │ ├── semantic/
│ │ │ └── statistical/
│ │ ├── perception/
│ │ ├── reasoning/
│ │ └── utils/
│ ├── scripts/
│ └── (cli.py)
└── tests/
├── fixtures/
├── integration/
└── unit/
```

### Structure Explanation

#### **Top-Level Directories (Sorted)**

##### **`config/`** - Configuration Files
Environment-specific settings in YAML format.

##### **`data/`** - Data Management
- `logs/` - System and learning logs
- `processed/` - Learned knowledge and processed data
- `raw/` - Unprocessed interaction data

##### **`docker/`** - Containerization
Docker configuration for deployment.

##### **`docs/`** - Documentation
- `api/` - API documentation (future)
- `spec/` - Design specifications
- `tutorials/` - How-to guides

##### **`experiments/`** - Research & Development
- `notebooks/` - Jupyter notebooks for experimentation
- `protocols/` - Teaching protocols and experiments
- `results/` - Experiment outputs and analysis

##### **`src/`** - Source Code
- `aeri/` - Main Python package
- `scripts/` - Utility scripts
- `cli.py` - Command-line interface (file)

##### **`tests/`** - Testing Suite
- `fixtures/` - Test data
- `integration/` - Integration tests
- `unit/` - Unit tests

#### **`src/aeri/` Subsystem Directories**

##### **Core Cognitive Modules**
- `evaluation/` - Progress tracking and milestone checking
- `generation/` - Response planning and sentence construction
- `interaction/` - Human-AI session management
- `learning/` - All learning algorithms
  - `grammar_induction/` - Grammar pattern learning
  - `lexical/` - Word meaning acquisition
  - `reinforcement/` - Feedback-based learning
- `memory/` - Multiple memory systems
  - `episodic/` - Experience memory
  - `semantic/` - Meaning and association memory
  - `statistical/` - Pattern and frequency memory
- `perception/` - Input processing and pattern detection
- `reasoning/` - Inference, goals, and curiosity
- `utils/` - Shared utilities and helpers

### Design Principles

#### **1. Modular Separation**
Each cognitive function has its own directory, allowing independent development.

#### **2. Data Isolation**
- `data/` separates runtime data from code
- `experiments/` separates research from production code

#### **3. Test Mirroring**
`tests/` structure mirrors `src/` for easy test organization.

#### **4. Documentation First**
`docs/` contains all specifications before implementation.

### Navigation Guidelines

1. **Development**: Work in `src/aeri/[subsystem]/`
2. **Experiments**: Use `experiments/notebooks/`
3. **Configuration**: Modify files in `config/`
4. **Data Analysis**: Check `data/processed/` and `data/logs/`
5. **Testing**: Corresponding tests in `tests/[type]/`

### Adding New Components

When adding new functionality:
1. Identify the appropriate subsystem directory
2. Create new subdirectory if needed
3. Add corresponding test directory in `tests/`
4. Update documentation in `docs/spec/`

---

*This architecture is designed to evolve with AERI's development while maintaining clear organization.*

---

## Quick Start

### Prerequisites
- **Python 3.9** or higher
- **4GB+ RAM** recommended for early learning stages
- **Basic understanding** of developmental AI concepts (optional but helpful)

### Installation Steps

#### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/aeri.git
cd aeri
```

#### 2. Set Up Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
# Upgrade pip
pip install --upgrade pip

# Install AERI in development mode
pip install -e .

# Or install from requirements.txt
pip install -r requirements.txt
```

#### 4. Configure AERI
```bash
# Copy default configuration
cp config/default.yaml config/development.yaml

# Edit configuration if needed
# (See config/default.yaml for all options)
```

#### 5. Verify Installation
```bash
# Run basic tests
pytest tests/unit/test_perception.py -v

# Check AERI version
python -c "import aeri; print(f'AERI version: {aeri.__version__}')"
```

### First Teaching Session

#### Start the Interactive Teacher
```bash
python src/scripts/run_teaching_session.py --stage 0
```

#### Basic Session Commands
During a teaching session, you can use these commands:

- ✓ or + - Positive feedback (AERI did well)

- ✗ or - - Negative feedback (correction needed)

- /help - Show all available commands

- /stats - Show AERI's current learning statistics

- /exit or /quit - End the session

- /save - Save current learning progress

#### Example First Session
```
Starting AERI Teaching Session (Stage 0: Pre-linguistic)
Session ID: 2024-01-15_10-30-00
Type /help for commands

Teacher: hello
AERI:    xjfq
Teacher: ✗
Teacher: hello
AERI:    kptb
Teacher: ✗
Teacher: hello
AERI:    hello
Teacher: ✓
Session saved. Goodbye!
```

## Example Usage

### Stage 0: Pre-linguistic Phase (Days 1-7)
**Goal**: Discover repeating character patterns
```python
from aeri.core import AERI
from aeri.interaction import TeachingSession

# Initialize AERI at Stage 0
aeri = AERI(stage=0)

# Start teaching session
session = TeachingSession(aeri, teacher_id="human_teacher_001")

# Basic interaction loop
for _ in range(10):
    teacher_input = input("You: ")
    response = session.send(teacher_input)
    print(f"AERI: {response}")
    
    # Provide feedback
    feedback = input("Feedback (✓/✗): ")
    session.give_feedback(feedback)
```

### Stage 1: Early Vocabulary (Weeks 2-4)
**Goal**: Learn 50-100 basic words
```python
from aeri.evaluation import ProgressTracker

# Track learning progress
tracker = ProgressTracker()

# Teach common words
teaching_pairs = [
    ("apple", "red fruit"),
    ("happy", "good feeling"),
    ("run", "move fast"),
    ("big", "not small")
]

for word, meaning in teaching_pairs:
    # AERI learns through definition
    aeri.learn_word(word, meaning)
    
    # Check if word was learned
    if aeri.knows_word(word):
        print(f"AERI learned: {word} = {meaning}")

# Get learning statistics
stats = tracker.get_statistics()
print(f"Vocabulary: {stats['vocabulary_size']} words")
print(f"Learning rate: {stats['learning_rate']:.2f} words/day")
```

### Stage 2: Simple Sentences (Months 2-3)
**Goal**: Form basic Subject-Verb-Object sentences
```python
# AERI generates early sentences
sentence = aeri.generate_sentence(
    subject="cat",
    verb="eat",
    object="fish"
)
print(f"AERI says: {sentence}")
# Output: "cat eat fish" (early grammar)

# Interactive correction
# Teacher: "The cat eats fish"
# AERI: "cat eat fish"
# Teacher feedback: "✗"  # Correction for missing 's'
# AERI updates grammar rule for third-person singular
```

### Monitoring Development
```python
from aeri.evaluation import MilestoneChecker

# Check developmental milestones
checker = MilestoneChecker(aeri)

milestones = checker.check_all_milestones()
for milestone, achieved in milestones.items():
    status = "✅" if achieved else "⏳"
    print(f"{status} {milestone}")

# Sample output:
# ✅ First word learned (Day 3)
# ✅ 10-word vocabulary (Week 2)
# ⏳ Two-word combinations (Week 3)
# ⏳ Simple questions (Month 2)
```

### Export Learning Data
```python
from aeri.scripts.export_learning_data import export_session_data

# Export a teaching session
export_session_data(
    session_id="2024-01-15_session_1",
    format="json",  # or "csv", "yaml"
    include_raw_data=True
)

# Export all learned vocabulary
aeri.vocabulary.export("data/processed/vocabularies/current_vocab.json")
```

### Visualization
```bash
# Generate learning progress charts
python src/scripts/visualize_progress.py \\
  --input data/logs/learning_metrics.csv \\
  --output experiments/results/figures/progress_chart.png
```

## Contributing

AERI is an open research project, and we welcome contributions from developers, researchers, linguists, cognitive scientists, and anyone interested in developmental AI.

### Ways to Contribute

#### 1. **Teaching AERI**
- **Become a Teacher**: Interact with AERI and help her learn
- **Document Interactions**: Share interesting learning moments
- **Test Protocols**: Try different teaching methods and report results

#### 2. **Development**
- **Code Contributions**: Implement new features or fix bugs
- **Algorithm Improvements**: Enhance learning or memory systems
- **Performance Optimization**: Make AERI more efficient

#### 3. **Research**
- **Design Experiments**: Create new teaching protocols
- **Analyze Data**: Study learning patterns and behaviors
- **Write Papers**: Document findings and insights

#### 4. **Documentation**
- **Improve Guides**: Make tutorials clearer
- **Add Examples**: Create more usage examples
- **Translate**: Help non-English speakers participate

### Development Workflow

#### Setting Up for Development
```bash
# Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/aeri.git
cd aeri

# Set up development environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install development dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

#### Making Changes
1. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
   
   Branch naming convention:
   - `feature/` for new features
   - `bugfix/` for bug fixes
   - `docs/` for documentation
   - `experiment/` for research experiments

2. **Make Your Changes**
   - Follow the existing code style
   - Add type hints to new functions
   - Write docstrings for public APIs
   - Update documentation if needed

3. **Run Tests**
   ```bash
   # Run all tests
   pytest
   
   # Run specific test file
   pytest tests/unit/test_your_feature.py
   
   # Run with coverage
   pytest --cov=aeri tests/
   ```

4. **Check Code Quality**
   ```bash
   # Format code
   black src/ tests/
   
   # Check linting
   flake8 src/ tests/
   
   # Check types
   mypy src/
   ```

5. **Commit Changes**
   ```bash
   git add .
   git commit -m "Add: brief description of changes"
   
   # Follow conventional commits:
   # feat: new feature
   # fix: bug fix
   # docs: documentation
   # test: tests
   # refactor: code restructuring
   # chore: maintenance
   ```

6. **Submit Pull Request**
   - Push to your fork
   - Create PR to main repository
   - Fill out the PR template
   - Link related issues

### Pull Request Checklist
Before submitting a PR, ensure:

- [ ] Tests pass (`pytest`)
- [ ] Code follows style guide (`black`, `flake8`)
- [ ] Type hints are added (`mypy`)
- [ ] Documentation is updated
- [ ] No breaking changes (unless intentional)
- [ ] Changes are focused and atomic

### Experiment Contribution
For research contributions:
1. Create experiment in `experiments/notebooks/`
2. Document protocol in `experiments/protocols/`
3. Add results to `experiments/results/`
4. Write summary in `docs/spec/` if findings are significant

### Reporting Issues
When reporting issues:
1. Use the issue template
2. Include AERI version and stage
3. Describe expected vs actual behavior
4. Provide reproduction steps
5. Include logs if available

### Learning Resources
To understand AERI's approach:
- Read `docs/spec/innate_machinery.md`
- Study `docs/spec/learning_stages.md`
- Review existing teaching sessions in `data/raw/interactions/`

### Community
- **Discussions**: Use GitHub Discussions for questions
- **Issues**: Bug reports and feature requests
- **Projects**: Check ongoing work in GitHub Projects

### Recognition
Contributors are recognized in:
- `CONTRIBUTORS.md` (planned)
- Release notes
- Project documentation

## License

Copyright © 2026 AERI Development Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

### Full License Text
See the complete license terms in the [LICENSE](LICENSE) file.

### Third-Party Licenses
Any third-party libraries used by AERI maintain their own licenses. See `requirements.txt` and individual package licenses for details.

### Academic Use
For academic research using AERI:
```bibtex
@software{aeri2026,
  title = {AERI: Artificial Emotional & Reasoning Intelligence},
  author = {AERI Development Team},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/yourusername/aeri},
  note = {A developmental AI system learning language from scratch}
}
```

### Data Licensing
- **Interaction Data**: Shared under CC BY-NC 4.0 for research purposes
- **Learned Models**: Released under the same MIT license as code
- **Documentation**: CC BY 4.0 unless otherwise specified

### Contributor License Agreement
By contributing to AERI, you agree that your contributions will be licensed under the same MIT License that covers the project.

### Ethical Use
AERI is intended for:
- Research in developmental AI
- Education about language acquisition
- Ethical AI development

**Not intended for**:
- Malicious or deceptive applications
- Replacement of human interaction in critical contexts
- Creation of synthetic personalities without transparency

See [`docs/spec/ethics.md`](docs/spec/ethics.md) for detailed ethical guidelines.