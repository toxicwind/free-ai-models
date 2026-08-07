# 🆓 Free AI Models Tracker

[![Models](https://img.shields.io/badge/Models-21-blue?style=flat-square&logo=openai)](./data/models.json)
[![Updated](https://img.shields.io/badge/Updated-daily-green?style=flat-square&logo=githubactions)](.github/workflows/update.yml)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

> **A community-maintained list of genuinely free AI models** — no credit card, no trial, no hidden costs. Updated automatically every day.

---

## 📋 Table of Contents

- [🚀 Quick Start](#-quick-start)
- [📡 Supported Backends](#-supported-backends)
- [📊 Model Catalog](#-model-catalog)
- [🔧 Grok-Build Integration](#-grok-build-integration)
- [🤝 Contributing](#-contributing)
- [📜 License & Attribution](#-license--attribution)

---

## 🚀 Quick Start

```bash
# Clone this fork
git clone https://github.com/toxicwind/free-ai-models.git
cd free-ai-models

# Regenerate everything from live APIs
node scripts/fetch-models.js

# The generated files:
#   data/models.json              ← current snapshot
#   data/history/YYYY-MM-DD.json  ← daily archive
#   grok_build_config.toml        ← grok-build config with all models
#   README.md                     ← this file (table auto-updated)
```

---

## 📡 Supported Backends

| Backend | Auth | Rate Limit | Models |
|---------|------|------------|--------|
| **OpenRouter** | `OPENROUTER_API_KEY` | 20 RPM (free tier) | 17 |
| **Pollinations AI** | None (keyless) | Unlimited | 4 |

**Total: 21 free models** across 2 backends. No credit card required for any.

---

## 📊 Model Catalog

<!-- TABLE_START -->
> Last updated: **Thu, 06 Aug 2026 23:46:23 UTC** · 21 models tracked

| # | Model | Provider | Context | Modalities | Rate Limit | Source |
|---|-------|----------|---------|------------|------------|--------|
| 1 | **Google: Lyria 3 Pro Preview** | Google | 1M | 💬 text, 🖼️ vision, audio | varies | [link](https://openrouter.ai/google/lyria-3-pro-preview) |
| 2 | **Google: Lyria 3 Clip Preview** | Google | 1M | 💬 text, 🖼️ vision, audio | varies | [link](https://openrouter.ai/google/lyria-3-clip-preview) |
| 3 | **Gemini 2.0 Flash** | Pollinations AI | 1M | 💬 text, 🖼️ vision | unlimited (no auth) | [link](https://pollinations.ai) |
| 4 | **NVIDIA: Nemotron 3 Ultra (free)** | Nvidia | 1M | 💬 text | 40 req/min | [link](https://openrouter.ai/nvidia/nemotron-3-ultra-550b-a55b:free) |
| 5 | **inclusionAI: Ling 3.0 Tiny (free)** | Inclusionai | 262K | 💬 text | varies | [link](https://openrouter.ai/inclusionai/ling-3.0-tiny:free) |
| 6 | **Poolside: Laguna S 2.1 (free)** | Poolside | 262K | 💬 text | varies | [link](https://openrouter.ai/poolside/laguna-s-2.1:free) |
| 7 | **Poolside: Laguna XS 2.1 (free)** | Poolside | 262K | 💬 text | varies | [link](https://openrouter.ai/poolside/laguna-xs-2.1:free) |
| 8 | **Google: Gemma 4 26B A4B  (free)** | Google | 262K | 🖼️ vision, 💬 text, video | varies | [link](https://openrouter.ai/google/gemma-4-26b-a4b-it:free) |
| 9 | **Google: Gemma 4 31B (free)** | Google | 262K | 🖼️ vision, 💬 text, video | varies | [link](https://openrouter.ai/google/gemma-4-31b-it:free) |
| 10 | **NVIDIA: Nemotron 3 Super (free)** | Nvidia | 262K | 💬 text | 40 req/min | [link](https://openrouter.ai/nvidia/nemotron-3-super-120b-a12b:free) |
| 11 | **Cohere: North Mini Code (free)** | Cohere | 256K | 💬 text | varies | [link](https://openrouter.ai/cohere/north-mini-code:free) |
| 12 | **NVIDIA: Nemotron 3 Nano Omni (free)** | Nvidia | 256K | 💬 text, audio, 🖼️ vision, video | 40 req/min | [link](https://openrouter.ai/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free) |
| 13 | **NVIDIA: Nemotron 3 Nano 30B A3B (free)** | Nvidia | 256K | 💬 text | 40 req/min | [link](https://openrouter.ai/nvidia/nemotron-3-nano-30b-a3b:free) |
| 14 | **Free Models Router** | Openrouter | 200K | 💬 text, 🖼️ vision | varies | [link](https://openrouter.ai/openrouter/free) |
| 15 | **OpenAI: gpt-oss-20b (free)** | Openai | 131K | 💬 text | varies | [link](https://openrouter.ai/openai/gpt-oss-20b:free) |
| 16 | **NVIDIA: Nemotron 3.5 Content Safety (free)** | Nvidia | 128K | 💬 text, 🖼️ vision | 40 req/min | [link](https://openrouter.ai/nvidia/nemotron-3.5-content-safety:free) |
| 17 | **NVIDIA: Nemotron Nano 12B 2 VL (free)** | Nvidia | 128K | 🖼️ vision, 💬 text, video | 40 req/min | [link](https://openrouter.ai/nvidia/nemotron-nano-12b-v2-vl:free) |
| 18 | **NVIDIA: Nemotron Nano 9B V2 (free)** | Nvidia | 128K | 💬 text | 40 req/min | [link](https://openrouter.ai/nvidia/nemotron-nano-9b-v2:free) |
| 19 | **Mistral Nemo** | Pollinations AI | 128K | 💬 text | unlimited (no auth) | [link](https://pollinations.ai) |
| 20 | **Mistral Small 3.2** | Pollinations AI | 128K | 💬 text | unlimited (no auth) | [link](https://pollinations.ai) |
| 21 | **GPT-4o** | Pollinations AI | 128K | 💬 text, 🖼️ vision | unlimited (no auth) | [link](https://pollinations.ai) |
<!-- TABLE_END -->

---

## 🔧 Grok-Build Integration

This fork includes **automatic grok-build config generation**.

```bash
# The fetcher auto-generates grok_build_config.toml
node scripts/fetch-models.js

# Use it
cp grok_build_config.toml ~/.config/grok-build/config.toml

# Set your keys
export OPENROUTER_API_KEY=sk-or-...
export MCP_BEARER=your-mcp-token
```

The generated config includes:
- **All 21 free models** with correct `base_url`, `env_key`, `context_window`
- **OpenRouter models** → `base_url = "https://openrouter.ai/api/v1"`
- **Pollinations models** → `base_url = "https://text.pollinations.ai/openai"` (keyless)
- **Auto-detected temperature/top_p** based on provider (Poolside/Cohere get 0.1/0.3)

---

## 🤝 Contributing

1. Fork this repo
2. Add new free providers to `EXTRA_PROVIDERS` in `scripts/fetch-models.js`
3. Run `node scripts/fetch-models.js` to verify
4. Submit a PR

---

## 📜 License & Attribution

This is a **fork** of [ClawLabsAI/free-ai-models](https://github.com/ClawLabsAI/free-ai-models) by **ClawLabs**.

- Original author: **ClawLabs** (https://github.com/ClawLabsAI)
- Fork author: **Pup Trix / toxicwind**
- Added features: grok-build config generation, multi-backend support
- License: MIT (same as original)

> "Free AI for everyone. No gatekeepers."

## Related Repositories

| Repo | Purpose |
|------|---------|
| [my-ai-tools](https://github.com/toxicwind/my-ai-tools) | AI tooling configs |
| [openrouter-free-model](https://github.com/toxicwind/openrouter-free-model) | OpenRouter browser |
| [sniper-super-v3](https://github.com/toxicwind/sniper-super-v3) | Contract hunter |
| [kimi-team-recon](https://github.com/toxicwind/kimi-team-recon) | Infrastructure intel |
