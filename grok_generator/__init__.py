"""grok_generator — Generate grok-build config.toml from free-ai-models data."""
import json
import os
from datetime import datetime

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'models.json')

def load_models():
    with open(DATA_PATH) as f:
        return json.load(f)

def generate_model_section(model: dict, idx: int) -> str:
    mid = model.get('id', '')
    name = model.get('name', 'Unknown')
    provider = model.get('provider', 'openrouter')
    ctx = model.get('context_window', 131072)
    out = model.get('max_output', 4096)
    
    # Determine env_key from provider
    env_map = {
        'Nvidia': 'OPENROUTER_API_KEY',
        'Google': 'OPENROUTER_API_KEY',
        'Meta': 'OPENROUTER_API_KEY',
        'OpenAI': 'OPENROUTER_API_KEY',
        'Microsoft': 'OPENROUTER_API_KEY',
        'Mistral': 'MISTRAL_API_KEY',
        'Anthropic': 'OPENROUTER_API_KEY',
        'Cohere': 'OPENROUTER_API_KEY',
        'Qwen': 'OPENROUTER_API_KEY',
        'Pollinations AI': 'POLLINATIONS_API_KEY',
    }
    env_key = env_map.get(provider, 'OPENROUTER_API_KEY')
    
    # Clean model id for section name
    section_name = mid.replace('/', '-').replace(':', '-').replace('.', '-')
    
    lines = [
        f'[model.openrouter-{section_name}]',
        f'model = "{mid}"',
        f'base_url = "https://openrouter.ai/api/v1"',
        f'name = "OpenRouter • {name}"',
        f'description = "{name} — {ctx} context, free tier."',
        f'env_key = "{env_key}"',
        f'api_backend = "chat_completions"',
        f'context_window = {ctx}',
        f'max_completion_tokens = {out}',
        f'temperature = 0.7',
        f'top_p = 0.95',
        f'supports_backend_search = false',
        f'stream_tool_calls = true',
    ]
    return '\n'.join(lines)

def generate_config() -> str:
    data = load_models()
    models = data.get('models', [])
    
    lines = [
        '# Grok Build Config — Generated from free-ai-models',
        f'# Updated: {data.get("updated_at", "unknown")}',
        f'# Total free models: {data.get("total_free_models", 0)}',
        '',
        '[marketplace]',
        'official_marketplace_auto_installed = true',
        'default_skills_installs_purged = true',
        '',
        '[[marketplace.sources]]',
        'name = "xAI Official"',
        'git = "https://github.com/xai-org/plugin-marketplace.git"',
        '',
        '[ui]',
        'max_thoughts_width = 120',
        'yolo = true',
        'compact_mode = true',
        'permission_mode = "always-approve"',
        'cancel_subagents_on_turn_cancel = "always_continue"',
        'remember_tool_approvals = true',
        'auto_interject_on_task_wait = true',
        'hunk_tracker_mode = "off"',
        'combine_queued_prompts = true',
        'fork_secondary_model = "google-gemini"',
        '',
        '[subagents]',
        'enabled = false',
        '',
        '[mcp_servers.mcpproxy]',
        'command = "npx"',
        'args = ["-y", "mcp-remote", "http://127.0.0.1:25109/mcp", "--header", "Authorization: Bearer ${MCP_BEARER}"]',
        'enabled = true',
        'startup_timeout_sec = 30',
        'tool_timeout_sec = 300',
        '',
        '[toolset.bash]',
        'timeout_secs = 600',
        'output_byte_limit = 5000000',
        '',
        '[cli]',
        'installer = "internal"',
        'auto_update = true',
        'show_tips = false',
        '',
        '[plugins]',
        'enabled = ["neon"]',
        '',
        '[agent]',
        'name = "grok-build"',
        '',
        '[models]',
        'default = "openrouter-nemotron-3-ultra-550b-a55b-free"',
        'default_reasoning_effort = "low"',
        '',
        '# ═══════════════════════════════════════════════════════════════════════',
        '# FREE MODELS — Auto-generated from free-ai-models data',
        '# ═══════════════════════════════════════════════════════════════════════',
        '',
    ]
    
    for idx, model in enumerate(models):
        lines.append(generate_model_section(model, idx))
        lines.append('')
    
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_config())
