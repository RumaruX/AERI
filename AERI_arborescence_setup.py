#!/usr/bin/env python3
"""
AERI Project Structure Generator
Creates the complete directory and file structure for the AERI project.
"""

import os
from pathlib import Path
import sys

def create_structure(base_path="."):
    """Create the complete AERI project structure."""
    
    # Define the complete structure
    structure = {
        "files": [
            "LICENSE",
            "README.md",
            "CONTRIBUTING.md",
            "CHANGELOG.md",
            ".gitignore",
            "requirements.txt",
            "pyproject.toml",
            "Makefile",
        ],
        "dirs": {
            "docs": {
                "spec": [
                    "architecture.md",
                    "learning_stages.md",
                    "innate_machinery.md",
                    "ethics.md",
                ],
                "api": [],
                "tutorials": [
                    "teaching_protocol.md",
                ],
            },
            "tests": {
                "unit": [
                    "test_perception.py",
                    "test_memory.py",
                    "test_learning.py",
                    "test_generation.py",
                    "test_reasoning.py",
                    "__init__.py",
                ],
                "integration": [
                    "test_interaction_loop.py",
                    "__init__.py",
                ],
                "fixtures": [
                    "sample_logs.json",
                ],
            },
            "data": {
                "raw": {
                    "interactions": {
                        "YYYY-MM-DD": [],
                    },
                },
                "processed": {
                    "vocabularies": [],
                    "grammar_rules": [],
                },
                "logs": [
                    "session_logs.jsonl",
                    "learning_metrics.csv",
                ],
            },
            "config": [
                "default.yaml",
                "development.yaml",
                "staging.yaml",
                "production.yaml",
            ],
            "src": {
                "aeri": [
                    "__init__.py",
                    "core.py",
                    "drives.py",
                ],
                "scripts": [
                    "setup_environment.py",
                    "run_teaching_session.py",
                    "export_learning_data.py",
                    "visualize_progress.py",
                ],
                "cli.py": None,  # This is a file, not a directory
            },
            "experiments": {
                "notebooks": [
                    "01_character_segmentation.ipynb",
                    "02_early_word_learning.ipynb",
                    "03_grammar_induction.ipynb",
                ],
                "protocols": [
                    "protocol_stage0.yaml",
                    "protocol_stage1.yaml",
                ],
                "results": {
                    "logs": [],
                    "figures": [],
                },
            },
            "docker": [
                "Dockerfile",
                "docker-compose.yml",
                "entrypoint.sh",
            ],
        }
    }
    
    # Subdirectories for src/aeri/
    aeri_subdirs = {
        "interaction": [
            "__init__.py",
            "session_manager.py",
            "teacher_interface.py",
            "feedback_handler.py",
        ],
        "perception": [
            "__init__.py",
            "character_stream.py",
            "segmenter.py",
            "pattern_detector.py",
            "attention.py",
        ],
        "memory": {
            "__init__.py": None,
            "memory_orchestrator.py": None,
            "episodic": [
                "__init__.py",
                "experience_buffer.py",
                "recall.py",
            ],
            "semantic": [
                "__init__.py",
                "association_network.py",
                "distributional_memory.py",
                "grounding.py",
            ],
            "statistical": [
                "__init__.py",
                "ngram_store.py",
                "frequency_tracker.py",
            ],
        },
        "learning": {
            "__init__.py": None,
            "learning_orchestrator.py": None,
            "reinforcement": [
                "__init__.py",
                "reward_system.py",
                "policy.py",
            ],
            "grammar_induction": [
                "__init__.py",
                "rule_extractor.py",
                "grammar_optimizer.py",
            ],
            "lexical": [
                "__init__.py",
                "word_discovery.py",
                "meaning_inference.py",
            ],
        },
        "generation": [
            "__init__.py",
            "planner.py",
            "sentence_builder.py",
            "lexical_chooser.py",
            "style_manager.py",
        ],
        "reasoning": [
            "__init__.py",
            "inference_engine.py",
            "goal_manager.py",
            "curiosity_engine.py",
        ],
        "evaluation": [
            "__init__.py",
            "milestone_checker.py",
            "progress_tracker.py",
            "human_feedback_analyzer.py",
        ],
        "utils": [
            "__init__.py",
            "logger.py",
            "serialization.py",
            "helpers.py",
        ],
    }

    def create_dirs_and_files(path, structure, is_file_dict=False):
        """Recursively create directories and files."""
        if isinstance(structure, list):
            # Create files in current directory
            for filename in structure:
                filepath = Path(path) / filename
                filepath.parent.mkdir(parents=True, exist_ok=True)
                if not filepath.exists():
                    filepath.touch()
                    print(f"Created: {filepath}")
                else:
                    print(f"Exists: {filepath}")
        
        elif isinstance(structure, dict):
            for name, content in structure.items():
                new_path = Path(path) / name
                
                if content is None:
                    # This is a file, not a directory
                    new_path.parent.mkdir(parents=True, exist_ok=True)
                    if not new_path.exists():
                        new_path.touch()
                        print(f"Created: {new_path}")
                    else:
                        print(f"Exists: {new_path}")
                else:
                    # This is a directory
                    new_path.mkdir(parents=True, exist_ok=True)
                    print(f"Created: {new_path}/")
                    
                    # Recurse into the directory
                    create_dirs_and_files(new_path, content)

    # Start creating from base path
    base = Path(base_path)
    base.mkdir(exist_ok=True)
    print(f"Creating AERI project structure in: {base.absolute()}")
    print("=" * 60)
    
    # Create root files
    for filename in structure["files"]:
        filepath = base / filename
        if not filepath.exists():
            filepath.touch()
            print(f"Created: {filepath}")
        else:
            print(f"Exists: {filepath}")
    
    # Create directory structure
    create_dirs_and_files(base, structure["dirs"])
    
    # Create src/aeri/ subdirectories
    aeri_path = base / "src" / "aeri"
    create_dirs_and_files(aeri_path, aeri_subdirs)
    
    print("=" * 60)
    print("Structure creation complete!")
    
    # Create minimal .gitignore
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# IDE
.vscode/
.idea/
*.swp
*.swo

# Jupyter Notebook
.ipynb_checkpoints/

# Data
data/processed/
data/logs/

# Experiments results
experiments/results/

# Environment
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# OS
.DS_Store
Thumbs.db

# Docker
*.log
"""
    
    gitignore_path = base / ".gitignore"
    if gitignore_path.stat().st_size == 0:
        gitignore_path.write_text(gitignore_content)
        print(f"Created default .gitignore")
    
    # Create minimal README
    readme_content = """# AERI - Artificial Emotional & Reasoning Intelligence

A developmental AI that learns language from scratch through human interaction.

## Project Structure

See `docs/spec/` for architecture and design documentation.

## Development

1. Set up environment: `python -m venv venv && source venv/bin/activate`
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `pytest`

## Teaching AERI

See `docs/tutorials/teaching_protocol.md` for guidance on interacting with AERI during early learning stages.
"""
    
    readme_path = base / "README.md"
    if readme_path.stat().st_size == 0:
        readme_path.write_text(readme_content)
        print(f"Created default README.md")
    
    # Create minimal requirements.txt
    requirements_content = """# Core dependencies
python>=3.9

# Development
pytest>=7.0
pytest-cov>=4.0
black>=23.0
flake8>=6.0
mypy>=1.0

# Data handling
numpy>=1.24
pandas>=2.0
pyyaml>=6.0

# Add project-specific dependencies here as needed
"""
    
    requirements_path = base / "requirements.txt"
    if requirements_path.stat().st_size == 0:
        requirements_path.write_text(requirements_content)
        print(f"Created default requirements.txt")
    
    # Create minimal pyproject.toml
    pyproject_content = """[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "aeri"
version = "0.1.0"
description = "Artificial Emotional & Reasoning Intelligence"
authors = [{name = "AERI Team"}]
readme = "README.md"
requires-python = ">=3.9"
classifiers = [
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Science/Research",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
]

[project.optional-dependencies]
dev = ["pytest", "black", "flake8", "mypy"]
notebooks = ["jupyter", "matplotlib", "seaborn"]

[tool.black]
line-length = 88
target-version = ['py39']

[tool.isort]
profile = "black"
"""
    
    pyproject_path = base / "pyproject.toml"
    if pyproject_path.stat().st_size == 0:
        pyproject_path.write_text(pyproject_content)
        print(f"Created default pyproject.toml")

def main():
    """Main entry point."""
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    else:
        base_path = "."
    
    try:
        create_structure(base_path)
        
        print("\n" + "=" * 60)
        print("NEXT STEPS:")
        print("1. Review the created structure")
        print("2. Populate docs/spec/ with design documents")
        print("3. Define innate machinery in docs/spec/innate_machinery.md")
        print("4. Create config/default.yaml with initial settings")
        print("=" * 60)
        
    except Exception as e:
        print(f"Error creating structure: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()