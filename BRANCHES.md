# Branch Structure

## Arborescence
```
main (protected)
├── develop
│   ├── feature/
│   │   ├── perception-system
│   │   ├── memory-architecture
│   │   ├── learning-algorithms
│   │   ├── generation-engine
│   │   └── interaction-layer
│   ├── experiment/
│   │   ├── stage0-teaching
│   │   ├── stage1-vocabulary
│   │   ├── grammar-induction
│   │   └── emotion-modeling
│   ├── refactor/
│   │   ├── memory-optimization
│   │   └── performance-tuning
│   └── bugfix/
│       └── [specific-issue]
└── docs/
    ├── api-documentation
    ├── teaching-manual
    └── research-paper
```

## Branch Purposes

### 🏁 Main Branches
| Branch | Purpose |
|--------|---------|
| **`main`** | Stable releases only. Protected - requires PR reviews. |
| **`develop`** | Integration branch for all features and experiments. |
| **`docs`** | Documentation branches (API, teaching manual, research). |

### 🚀 Feature Branches (from `develop`)
| Branch | Purpose |
|--------|---------|
| `feature/perception-system` | Character processing, segmentation, attention |
| `feature/memory-architecture` | Episodic, semantic, statistical memory systems |
| `feature/learning-algorithms` | Reinforcement, grammar induction, lexical learning |
| `feature/generation-engine` | Response planning, sentence building, lexical choice |
| `feature/interaction-layer` | Teaching sessions, feedback handling, session management |

### 🔬 Experiment Branches (from `develop`)  
| Branch | Purpose |
|--------|---------|
| `experiment/stage0-teaching` | Pre-linguistic phase: character pattern discovery |
| `experiment/stage1-vocabulary` | Word learning: meaning acquisition from context |
| `experiment/grammar-induction` | Grammar rule discovery from examples |
| `experiment/emotion-modeling` | Emotional response generation and recognition |

### 🔧 Refactor Branches (from `develop`)
| Branch | Purpose |
|--------|---------|
| `refactor/memory-optimization` | Improve memory system performance |
| `refactor/performance-tuning` | General performance improvements |

### 🐛 Bugfix Branches (from `develop`)
| Pattern | Purpose |
|---------|---------|
| `bugfix/[specific-issue]` | Fix specific bugs (create from `main` for production bugs) |

### 📚 Documentation Branches (from `main`)
| Branch | Purpose |
|--------|---------|
| `docs/api-documentation` | Module APIs, integration guides, developer docs |
| `docs/teaching-manual` | How to teach AERI at different developmental stages |
| `docs/research-paper` | Academic papers and research documentation |

## Workflow Rules
```bash
# 1. For new features/experiments/refactors: start from develop
git checkout develop
git pull origin develop
git checkout -b feature/perception-system

# 2. For documentation: start from main  
git checkout main
git pull origin main
git checkout -b docs/teaching-manual

# 3. For bug fixes in development code: start from develop
git checkout develop
git pull origin develop
git checkout -b bugfix/memory-leak

# 4. For critical production bug fixes: start from main
git checkout main
git pull origin main
git checkout -b hotfix/critical-issue

# 5. After work: push and create PR
git push origin branch-name
# Then create PR on GitHub
```

## PR Destinations
- `feature/*`, `experiment/*`, `refactor/*`, `bugfix/*` → **`develop`**
- `docs/*`, `develop/*` → **`main`**

## Branch Protection
- **`main`**: Requires PR reviews, status checks, linear history
- **`develop`**: Recommended: status checks, linear history

## Current Status
- **Active**: `main` (v0.1.0 - project structure)
- **To create**: `develop` (from `main`), then feature branches
- **Next up**: `feature/perception-system` (character processing foundation)